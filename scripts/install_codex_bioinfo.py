#!/usr/bin/env python3
"""Safely install the portable bioinformatics Codex package.

Default behavior is dry-run. Use --apply only after reviewing the plan.
"""

from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS = ROOT / ".codex" / "skills"
SOURCE_AGENTS = ROOT / ".codex" / "agents"
SOURCE_GUIDANCE = ROOT / "templates" / "global-AGENTS.md"
BEGIN = "<!-- BEGIN TAICHUAN BIOINFO AGENT -->"
END = "<!-- END TAICHUAN BIOINFO AGENT -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="apply the displayed installation plan")
    parser.add_argument(
        "--replace-global-guidance",
        action="store_true",
        help="replace the complete global AGENTS.md with the compact managed block",
    )
    parser.add_argument(
        "--home",
        type=Path,
        default=Path.home(),
        help="target home directory; intended for isolated validation fixtures",
    )
    return parser.parse_args()


def managed_guidance(existing: str) -> str:
    source = SOURCE_GUIDANCE.read_text(encoding="utf-8").rstrip()
    block = f"{BEGIN}\n{source}\n{END}"
    begin_count = existing.count(BEGIN)
    end_count = existing.count(END)
    if begin_count != end_count or begin_count > 1:
        raise RuntimeError("global AGENTS.md has mismatched or duplicate managed markers; refusing to edit")
    if begin_count == 1:
        start = existing.index(BEGIN)
        stop = existing.index(END, start) + len(END)
        prefix = existing[:start].rstrip()
        suffix = existing[stop:].strip("\n")
        result = (prefix + "\n\n" if prefix else "") + block
        if suffix:
            result += "\n\n" + suffix
        return result + "\n"
    prefix = existing.rstrip()
    return (prefix + "\n\n" if prefix else "") + block + "\n"


def atomic_write(path: Path, content: str, mode: int = 0o600) -> None:
    temporary = path.with_name(f".{path.name}.codex-bioinfo-tmp")
    temporary.write_text(content, encoding="utf-8")
    os.chmod(temporary, mode)
    os.replace(temporary, path)


def main() -> int:
    args = parse_args()
    target_home = args.home.expanduser().resolve()
    target_skills = target_home / ".agents" / "skills"
    target_codex = target_home / ".codex"
    target_agents = target_codex / "agents"
    target_guidance = target_codex / "AGENTS.md"

    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_package.py")], check=True)

    existing_guidance = target_guidance.read_text(encoding="utf-8") if target_guidance.exists() else ""
    if args.replace_global_guidance:
        source = SOURCE_GUIDANCE.read_text(encoding="utf-8").rstrip()
        new_guidance = f"{BEGIN}\n{source}\n{END}\n"
    else:
        new_guidance = managed_guidance(existing_guidance)

    skill_action: str
    skill_changed = not (
        target_skills.is_symlink() and target_skills.resolve() == SOURCE_SKILLS.resolve()
    )
    if not skill_changed:
        skill_action = "keep existing correct Skill symlink"
    elif target_skills.exists() or target_skills.is_symlink():
        if not target_skills.is_symlink():
            raise RuntimeError(
                f"{target_skills} exists and is not a symlink; consolidate it manually before installation"
            )
        skill_action = f"replace Skill symlink currently pointing to {os.readlink(target_skills)}"
    else:
        skill_action = "create global Skill symlink"

    changed_agents = [
        source
        for source in sorted(SOURCE_AGENTS.glob("*.toml"))
        if not (target_agents / source.name).exists()
        or not filecmp.cmp(source, target_agents / source.name, shallow=False)
    ]
    guidance_changed = existing_guidance != new_guidance

    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Source: {ROOT}")
    print(f"Target home: {target_home}")
    print(f"Skills: {skill_action}")
    if not guidance_changed:
        guidance_action = "already current"
    elif args.replace_global_guidance:
        guidance_action = "replace with compact managed block"
    else:
        guidance_action = "update managed block"
    print(f"Global guidance: {guidance_action}")
    print(f"Custom Agents to install/update: {len(changed_agents)}")
    for source in changed_agents:
        print(f"  - {source.name}")
    print("Machine config, credentials, SSH, plugins, memory, sessions, and project files are not modified.")

    if not args.apply:
        print("Dry-run only. Re-run with --apply after reviewing this plan.")
        return 0

    if not skill_changed and not guidance_changed and not changed_agents:
        print("Already current; no files changed.")
        return 0

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup_root = target_codex / "backups" / f"codex-bioinfo-install-{timestamp}"
    backup_root.mkdir(parents=True, mode=0o700)

    target_skills.parent.mkdir(parents=True, exist_ok=True)
    if skill_changed:
        if target_skills.is_symlink():
            backup_link = backup_root / "skills.symlink"
            target_skills.rename(backup_link)
        target_skills.symlink_to(SOURCE_SKILLS)

    target_codex.mkdir(parents=True, exist_ok=True)
    if guidance_changed:
        if target_guidance.exists():
            shutil.copy2(target_guidance, backup_root / "AGENTS.md")
        atomic_write(target_guidance, new_guidance)

    target_agents.mkdir(parents=True, exist_ok=True)
    for source in changed_agents:
        destination = target_agents / source.name
        if destination.exists():
            shutil.copy2(destination, backup_root / source.name)
        atomic_write(destination, source.read_text(encoding="utf-8"))

    print(f"Applied successfully. Backup: {backup_root}")
    print("Restart Codex before checking newly installed Skills and custom Agents.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
