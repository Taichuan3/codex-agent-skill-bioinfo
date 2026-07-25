#!/usr/bin/env python3
"""Safely install the portable bioinformatics Codex package.

Default behavior is dry-run. Use --apply only after reviewing the plan.
"""

from __future__ import annotations

import argparse
import filecmp
import hashlib
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
        "--retire-legacy-codex-skills",
        action="store_true",
        help=(
            "move user Skill directories from ~/.codex/skills into the installation backup; "
            "preserve ~/.codex/skills/.system and use ~/.agents/skills as the single global source"
        ),
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


def source_state() -> tuple[str, bool]:
    """Return the Git revision and dirty state, or an archive marker."""
    probe = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
        check=False,
        capture_output=True,
        text=True,
    )
    if probe.returncode != 0:
        return "unversioned-archive", False
    status = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=normal"],
        check=True,
        capture_output=True,
        text=True,
    )
    return probe.stdout.strip(), bool(status.stdout.strip())


def source_digest() -> str:
    """Hash the portable package source without Git/runtime cache state."""
    digest = hashlib.sha256()
    excluded_parts = {".git", "__pycache__"}
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or any(part in excluded_parts for part in path.parts)
            or path.suffix == ".pyc"
        ):
            continue
        relative = path.relative_to(ROOT).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    args = parse_args()
    target_home = args.home.expanduser().resolve()
    target_skills = target_home / ".agents" / "skills"
    target_codex = target_home / ".codex"
    legacy_codex_skills = target_codex / "skills"
    target_agents = target_codex / "agents"
    target_guidance = target_codex / "AGENTS.md"

    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_package.py")], check=True)
    revision, source_dirty = source_state()
    digest = source_digest()
    if args.apply and source_dirty:
        raise RuntimeError(
            "source checkout has tracked or untracked changes; commit or use a clean release checkout "
            "before installation"
        )

    if target_codex.exists() and not target_codex.is_dir():
        raise RuntimeError(f"{target_codex} exists and is not a directory")
    if target_agents.is_symlink():
        raise RuntimeError(
            f"{target_agents} is a symlink; preserve its topology and consolidate it manually "
            "before installation"
        )
    if target_agents.exists() and not target_agents.is_dir():
        raise RuntimeError(f"{target_agents} exists and is not a directory")
    if target_guidance.is_symlink():
        raise RuntimeError(
            f"{target_guidance} is a symlink; preserve its topology and consolidate it manually "
            "before installation"
        )
    for source in sorted(SOURCE_AGENTS.glob("*.toml")):
        destination = target_agents / source.name
        if destination.is_symlink():
            raise RuntimeError(
                f"{destination} is a symlink; preserve its topology and consolidate it manually "
                "before installation"
            )

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
    legacy_skill_dirs = (
        sorted(
            child
            for child in legacy_codex_skills.iterdir()
            if child.name != ".system"
            and (child.is_dir() or child.is_symlink())
            and (child / "SKILL.md").is_file()
        )
        if legacy_codex_skills.is_dir()
        else []
    )
    guidance_changed = existing_guidance != new_guidance

    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Source: {ROOT}")
    print(f"Source revision: {revision}{' (dirty; apply blocked)' if source_dirty else ''}")
    print(f"Source digest: sha256:{digest}")
    print(f"Target home: {target_home}")
    print(f"Skills: {skill_action}")
    if not guidance_changed:
        guidance_action = "already current"
    elif args.replace_global_guidance:
        guidance_action = "replace with compact managed block"
    else:
        guidance_action = "update managed block"
    print(f"Global guidance: {guidance_action}")
    if args.retire_legacy_codex_skills:
        print(f"Legacy ~/.codex/skills entries to back up and retire: {len(legacy_skill_dirs)}")
        for path in legacy_skill_dirs:
            print(f"  - {path.name}")
    elif legacy_skill_dirs:
        print(
            "Legacy ~/.codex/skills entries detected but left unchanged: "
            f"{len(legacy_skill_dirs)}; use --retire-legacy-codex-skills after review"
        )
    print(f"Custom Agents to install/update: {len(changed_agents)}")
    for source in changed_agents:
        print(f"  - {source.name}")
    print("Machine config, credentials, SSH, plugins, memory, sessions, and project files are not modified.")

    if not args.apply:
        print("Dry-run only. Re-run with --apply after reviewing this plan.")
        return 0

    retire_legacy = args.retire_legacy_codex_skills and bool(legacy_skill_dirs)
    if not skill_changed and not guidance_changed and not changed_agents and not retire_legacy:
        print("Already current; no files changed.")
        return 0

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup_root = target_codex / "backups" / f"codex-bioinfo-install-{timestamp}"
    backup_root.mkdir(parents=True, mode=0o700)
    atomic_write(
        backup_root / "SOURCE.txt",
        f"revision={revision}\ndigest=sha256:{digest}\nsource={ROOT}\n",
    )

    backup_link = backup_root / "skills.symlink"
    guidance_backup = backup_root / "AGENTS.md"
    legacy_backup = backup_root / "legacy-codex-skills"
    moved_legacy: list[tuple[Path, Path]] = []
    agent_backups: list[tuple[Path, Path | None]] = []
    skill_installed = False
    skill_backup_moved = False
    guidance_installed = False

    try:
        target_skills.parent.mkdir(parents=True, exist_ok=True)
        if skill_changed:
            if target_skills.is_symlink():
                target_skills.rename(backup_link)
                skill_backup_moved = True
            target_skills.symlink_to(SOURCE_SKILLS)
            skill_installed = True

        target_codex.mkdir(parents=True, exist_ok=True)
        if guidance_changed:
            if target_guidance.exists():
                shutil.copy2(target_guidance, guidance_backup)
            atomic_write(target_guidance, new_guidance)
            guidance_installed = True

        if retire_legacy:
            legacy_backup.mkdir()
            for path in legacy_skill_dirs:
                destination = legacy_backup / path.name
                shutil.move(str(path), destination)
                moved_legacy.append((path, destination))

        target_agents.mkdir(parents=True, exist_ok=True)
        for source in changed_agents:
            destination = target_agents / source.name
            backup = backup_root / source.name if destination.exists() else None
            if backup is not None:
                shutil.copy2(destination, backup)
            agent_backups.append((destination, backup))
            atomic_write(destination, source.read_text(encoding="utf-8"))
    except Exception as exc:
        rollback_errors: list[str] = []
        for destination, backup in reversed(agent_backups):
            try:
                if backup is None:
                    if destination.exists():
                        destination.unlink()
                else:
                    shutil.copy2(backup, destination)
            except OSError as rollback_exc:
                rollback_errors.append(f"agent {destination}: {rollback_exc}")
        for original, backup in reversed(moved_legacy):
            try:
                shutil.move(str(backup), original)
            except OSError as rollback_exc:
                rollback_errors.append(f"legacy Skill {original}: {rollback_exc}")
        if guidance_installed:
            try:
                if guidance_backup.exists():
                    shutil.copy2(guidance_backup, target_guidance)
                elif target_guidance.exists():
                    target_guidance.unlink()
            except OSError as rollback_exc:
                rollback_errors.append(f"global guidance: {rollback_exc}")
        if skill_installed or skill_backup_moved:
            try:
                if target_skills.is_symlink():
                    target_skills.unlink()
                if backup_link.exists() or backup_link.is_symlink():
                    backup_link.rename(target_skills)
            except OSError as rollback_exc:
                rollback_errors.append(f"Skill symlink: {rollback_exc}")
        detail = f"; rollback errors: {' | '.join(rollback_errors)}" if rollback_errors else ""
        raise RuntimeError(f"installation failed and rollback was attempted: {exc}{detail}") from exc

    print(f"Applied successfully. Backup: {backup_root}")
    print(f"Installed source: revision={revision} sha256:{digest}")
    print("Restart Codex before checking newly installed Skills and custom Agents.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
