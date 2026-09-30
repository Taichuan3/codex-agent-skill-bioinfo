#!/usr/bin/env python3
"""Check real installed capability references with source unavailable.

Runs only in temporary homes. Explicit copy mode exercises the Windows layout
on POSIX too; it is not a substitute for a native Windows test.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from test_release_safety import copy_source, require


def run_fixture(mode: str) -> None:
    with tempfile.TemporaryDirectory(prefix='codex-installed-refs-') as temporary:
        root = Path(temporary).resolve()
        source = copy_source(root)
        home = root / 'home'
        command = [sys.executable, str(source / 'scripts/install_codex_bioinfo.py'),
                   '--home', str(home), '--skills-deployment', mode, '--apply']
        install = subprocess.run(command, capture_output=True, text=True)
        require(install.returncode == 0, install.stdout + install.stderr)
        runtime = home / '.agents/skills'
        # Relocate the entire source, not just its registry. No source fallback
        # or import can accidentally satisfy the installed references below.
        hidden_source = root / 'source-unavailable'
        source.rename(hidden_source)
        checked = 0
        registries = set()
        for skill in sorted(runtime.glob('*/SKILL.md')):
            text = skill.read_text(encoding='utf-8')
            for relative in re.findall(r'`([^`\n]*capability_registry\.json)`', text):
                registry = (skill.parent / relative).resolve()
                require(registry.is_file(), f'{mode}: missing {skill.parent.name} -> {relative}')
                require(registry.is_relative_to(home), f'{mode}: reference escapes installation')
                payload = json.loads(registry.read_text(encoding='utf-8'))
                ids = set(re.findall(r'`(CAP-[A-Z]+-\d+)`', text))
                matches = [c for c in payload['capabilities']
                           if c['owner_skill'] == skill.parent.name and c['id'] in ids]
                require(len(matches) == 1, f'{mode}: owner/CAP-ID mismatch: {skill.parent.name}')
                registries.add(registry)
                checked += 1
        require(checked == 6, f'{mode}: expected six owner references, got {checked}')
        require(len(registries) == 1, f'{mode}: references do not share one installed registry')
        hidden_source.rename(source)
        second = subprocess.run(command, capture_output=True, text=True)
        require(second.returncode == 0 and 'Already current' in second.stdout,
                f'{mode}: install is not idempotent: {second.stdout}{second.stderr}')
        registry = next(iter(registries))
        original = registry.read_bytes()
        registry.chmod(0o600)
        registry.write_bytes(original + b'\n')
        tampered = subprocess.run(command[:-1], capture_output=True, text=True)
        require(tampered.returncode != 0 and 'digest verification' in tampered.stderr,
                f'{mode}: registry tamper not rejected: {tampered.stdout}{tampered.stderr}')
        registry.write_bytes(original)
        registry.chmod(0o444)
        # Fail after a new registry/tree has been deployed; the old registry,
        # deployment topology, copy marker and release store must be restored.
        package_store = home / '.codex/packages/codex-agent-skill-bioinfo'
        old_releases = {p.name for p in package_store.iterdir()}
        old_runtime_target = runtime.resolve()
        marker = home / '.agents/codex-bioinfo-skills.json'
        old_marker = marker.read_bytes() if marker.exists() else None
        source_registry = source / '.codex/skills/capability_registry.json'
        source_registry.write_bytes(source_registry.read_bytes() + b'\n')
        installer = source / 'scripts/install_codex_bioinfo.py'
        installer_text = installer.read_text(encoding='utf-8')
        injection = '        target_agents.mkdir(parents=True, exist_ok=True)\n'
        require(injection in installer_text, 'fault injection point is missing')
        installer.write_text(installer_text.replace(injection,
            '        raise RuntimeError("registry rollback fixture")\n' + injection, 1), encoding='utf-8')
        failed = subprocess.run(command, capture_output=True, text=True)
        require(failed.returncode != 0 and 'rollback was attempted' in failed.stderr,
                f'{mode}: expected transactional failure: {failed.stdout}{failed.stderr}')
        require((runtime / 'capability_registry.json').read_bytes() == original,
                f'{mode}: old registry was not restored')
        require(runtime.resolve() == old_runtime_target and runtime.is_symlink() == (mode == 'symlink'),
                f'{mode}: old deployment topology was not restored')
        require((marker.read_bytes() if marker.exists() else None) == old_marker,
                f'{mode}: old deployment marker was not restored')
        require({p.name for p in package_store.iterdir()} == old_releases,
                f'{mode}: rollback left a new release snapshot')
        print(f'PASS: {mode}: six references; no source; CAP-IDs; no-op; tamper refusal; registry rollback')


if __name__ == '__main__':
    modes = ['copy'] if os.name == 'nt' else ['symlink', 'copy']
    for deployment in modes:
        run_fixture(deployment)
