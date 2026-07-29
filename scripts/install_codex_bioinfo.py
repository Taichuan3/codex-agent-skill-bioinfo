#!/usr/bin/env python3
"""Safely install the portable bioinformatics Codex package.

Default behavior is dry-run. Use --apply only after reviewing the plan.
"""

from __future__ import annotations

import argparse
import filecmp
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS = ROOT / ".codex" / "skills"
SOURCE_AGENTS = ROOT / ".codex" / "agents"
SOURCE_GUIDANCE = ROOT / "templates" / "global-AGENTS.md"
BEGIN = "<!-- BEGIN TAICHUAN BIOINFO AGENT -->"
END = "<!-- END TAICHUAN BIOINFO AGENT -->"


def is_repository_root() -> bool:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"],
        check=False,
        capture_output=True,
        text=True,
    )
    return (
        result.returncode == 0
        and Path(result.stdout.strip()).resolve() == ROOT.resolve()
    )


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
    parser.add_argument(
        "--skills-deployment",
        choices=("auto", "symlink", "copy"),
        default="auto",
        help=(
            "global Skill deployment: auto uses a symlink on POSIX and a managed copy "
            "on Windows"
        ),
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
    if not is_repository_root():
        return "unversioned-archive", False
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
    material_changes = []
    for line in status.stdout.splitlines():
        if line.startswith("?? "):
            untracked_path = line[3:].strip('"')
            if untracked_path == ".codex/candidates/" or untracked_path.startswith(
                ".codex/candidates/"
            ):
                continue
        material_changes.append(line)
    return probe.stdout.strip(), bool(material_changes)


def source_digest() -> str:
    """Hash tracked package files, or all portable files in an archive."""
    digest = hashlib.sha256()
    excluded_parts = {".git", "__pycache__"}
    if is_repository_root():
        tracked = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            check=True,
            capture_output=True,
        )
        paths = [
            ROOT / item.decode("utf-8")
            for item in tracked.stdout.split(b"\0")
            if item
        ]
    else:
        paths = list(ROOT.rglob("*"))
    for path in sorted(paths):
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


def tree_digest(root: Path) -> str:
    """Hash one installed tree so an existing snapshot can be verified."""
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix().encode("utf-8")
        digest.update(relative)
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def make_read_only(root: Path) -> None:
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_file():
            path.chmod(0o555 if path.stat().st_mode & 0o111 else 0o444)
        elif path.is_dir():
            path.chmod(0o555)
    root.chmod(0o555)


def deployment_mode(requested: str) -> str:
    if requested == "auto":
        return "copy" if os.name == "nt" else "symlink"
    return requested


def load_managed_copy(marker: Path, target: Path) -> dict[str, str]:
    if marker.is_symlink() or (marker.exists() and not marker.is_file()):
        raise RuntimeError(f"{marker} is not a regular managed-copy marker")
    if not marker.is_file():
        raise RuntimeError(
            f"{target} is a real directory without {marker.name}; refusing to overwrite "
            "an unmanaged Skill directory"
        )
    try:
        payload = json.loads(marker.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"{marker} is not a valid managed-copy marker") from exc
    required = {
        "schema_version": 1,
        "managed_by": "codex-agent-skill-bioinfo",
        "deployment_mode": "copy",
    }
    for key, expected in required.items():
        if payload.get(key) != expected:
            raise RuntimeError(f"{marker} has an unsupported {key}; refusing to overwrite")
    if any(path.is_symlink() for path in target.rglob("*")):
        raise RuntimeError(
            f"managed Skill copy contains a symlink: {target}; "
            "preserve it and resolve the local changes manually"
        )
    recorded_digest = payload.get("skills_digest")
    if not isinstance(recorded_digest, str) or not recorded_digest.startswith("sha256:"):
        raise RuntimeError(f"{marker} has no valid skills_digest")
    actual_digest = f"sha256:{tree_digest(target)}"
    if actual_digest != recorded_digest:
        raise RuntimeError(
            f"managed Skill copy failed digest verification: {target}; "
            "preserve it and resolve the local changes manually"
        )
    return payload


def remove_path(path: Path) -> None:
    """Remove a file, symlink, or read-only tree during transactional rollback."""
    if path.is_symlink() or path.is_file():
        path.chmod(0o600, follow_symlinks=False)
        path.unlink()
        return
    if not path.exists():
        return
    for child in sorted(path.rglob("*"), reverse=True):
        if child.is_symlink() or child.is_file():
            child.chmod(0o600, follow_symlinks=False)
        elif child.is_dir():
            child.chmod(0o700)
    path.chmod(0o700)
    shutil.rmtree(path)


def main() -> int:
    args = parse_args()
    target_home = args.home.expanduser().resolve()
    target_skills = target_home / ".agents" / "skills"
    skills_marker = target_home / ".agents" / "codex-bioinfo-skills.json"
    target_codex = target_home / ".codex"
    legacy_codex_skills = target_codex / "skills"
    target_agents = target_codex / "agents"
    target_guidance = target_codex / "AGENTS.md"

    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_package.py")], check=True)
    revision, source_dirty = source_state()
    digest = source_digest()
    skills_digest = tree_digest(SOURCE_SKILLS)
    selected_deployment = deployment_mode(args.skills_deployment)
    if args.apply and source_dirty:
        raise RuntimeError(
            "source checkout has tracked or untracked changes; commit or use a clean release checkout "
            "before installation"
        )
    release_id = f"{revision[:12]}-{digest[:12]}"
    release_root = (
        target_codex
        / "packages"
        / "codex-agent-skill-bioinfo"
        / release_id
    )
    installed_skills = release_root / "skills"
    if release_root.exists():
        if not installed_skills.is_dir():
            raise RuntimeError(f"existing release snapshot is incomplete: {release_root}")
        installed_digest = tree_digest(installed_skills)
        if installed_digest != skills_digest:
            raise RuntimeError(
                f"existing release snapshot failed digest verification: {release_root}"
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
    marker_changed = skills_marker.exists() or skills_marker.is_symlink()
    if skills_marker.is_symlink() or (skills_marker.exists() and not skills_marker.is_file()):
        raise RuntimeError(f"{skills_marker} is not a regular file")
    if target_skills.is_symlink():
        if skills_marker.exists():
            try:
                marker_payload = json.loads(skills_marker.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError) as exc:
                raise RuntimeError(f"{skills_marker} is not a valid managed-copy marker") from exc
            if (
                marker_payload.get("schema_version") != 1
                or marker_payload.get("managed_by") != "codex-agent-skill-bioinfo"
            ):
                raise RuntimeError(
                    f"{skills_marker} is not owned by this installer; refusing to overwrite"
                )
        correct_link = target_skills.resolve() == installed_skills.resolve()
        skill_changed = selected_deployment != "symlink" or not correct_link
        marker_changed = selected_deployment == "copy" or marker_changed
        if not skill_changed:
            skill_action = "keep existing correct Skill symlink"
        elif selected_deployment == "copy":
            skill_action = (
                f"replace Skill symlink currently pointing to {os.readlink(target_skills)} "
                "with a managed copy"
            )
        else:
            skill_action = f"replace Skill symlink currently pointing to {os.readlink(target_skills)}"
    elif target_skills.exists():
        if not target_skills.is_dir():
            raise RuntimeError(f"{target_skills} exists and is not a directory or symlink")
        managed = load_managed_copy(skills_marker, target_skills)
        current_release = managed.get("release_id") == release_id
        current_digest = managed.get("skills_digest") == f"sha256:{skills_digest}"
        skill_changed = selected_deployment != "copy" or not (current_release and current_digest)
        marker_changed = selected_deployment != "copy" or not (current_release and current_digest)
        if not skill_changed:
            skill_action = "keep existing verified managed Skill copy"
        elif selected_deployment == "symlink":
            skill_action = "replace verified managed Skill copy with a symlink"
        else:
            skill_action = "update verified managed Skill copy"
    else:
        if skills_marker.exists():
            raise RuntimeError(
                f"{skills_marker} exists but {target_skills} is missing; "
                "resolve the incomplete managed copy manually"
            )
        skill_changed = True
        marker_changed = selected_deployment == "copy"
        skill_action = (
            "create managed global Skill copy"
            if selected_deployment == "copy"
            else "create global Skill symlink"
        )

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
    print(f"Installed Skill snapshot: {installed_skills}")
    print(f"Target home: {target_home}")
    print(f"Skill deployment: {selected_deployment}")
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
    if (
        not skill_changed
        and not marker_changed
        and not guidance_changed
        and not changed_agents
        and not retire_legacy
    ):
        print("Already current; no files changed.")
        return 0

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup_root = target_codex / "backups" / f"codex-bioinfo-install-{timestamp}"
    backup_root.mkdir(parents=True, mode=0o700)
    atomic_write(
        backup_root / "SOURCE.txt",
        f"revision={revision}\ndigest=sha256:{digest}\nsource={ROOT}\n",
    )

    backup_skills = backup_root / "skills.previous"
    marker_backup = backup_root / "codex-bioinfo-skills.json"
    guidance_backup = backup_root / "AGENTS.md"
    legacy_backup = backup_root / "legacy-codex-skills"
    moved_legacy: list[tuple[Path, Path]] = []
    agent_backups: list[tuple[Path, Path | None]] = []
    skill_installed = False
    skill_backup_moved = False
    skill_backup_was_directory = False
    marker_backup_copied = False
    marker_installed = False
    guidance_installed = False
    release_created = False
    staging: Path | None = None

    try:
        if not release_root.exists():
            release_root.parent.mkdir(parents=True, exist_ok=True)
            staging = Path(
                tempfile.mkdtemp(
                    prefix=f".{release_root.name}.staging-",
                    dir=release_root.parent,
                )
            )
            shutil.copytree(SOURCE_SKILLS, staging / "skills")
            atomic_write(
                staging / "SOURCE.txt",
                f"revision={revision}\npackage_digest=sha256:{digest}\n"
                f"skills_digest=sha256:{skills_digest}\n",
                mode=0o444,
            )
            try:
                os.replace(staging, release_root)
            except OSError:
                if (
                    not installed_skills.is_dir()
                    or tree_digest(installed_skills) != skills_digest
                ):
                    raise
                shutil.rmtree(staging)
                staging = None
            else:
                release_created = True
                staging = None
                make_read_only(release_root)

        target_skills.parent.mkdir(parents=True, exist_ok=True)
        if skill_changed:
            if target_skills.exists() or target_skills.is_symlink():
                if target_skills.is_dir() and not target_skills.is_symlink():
                    previous_root_mode = target_skills.stat().st_mode & 0o777
                    target_skills.chmod(0o700)
                    try:
                        target_skills.rename(backup_skills)
                    except OSError:
                        target_skills.chmod(previous_root_mode)
                        raise
                    skill_backup_was_directory = True
                else:
                    target_skills.rename(backup_skills)
                skill_backup_moved = True
            if selected_deployment == "symlink":
                target_skills.symlink_to(installed_skills, target_is_directory=True)
            else:
                shutil.copytree(installed_skills, target_skills)
            skill_installed = True
        if marker_changed:
            if skills_marker.exists():
                shutil.copy2(skills_marker, marker_backup)
                marker_backup_copied = True
            if selected_deployment == "copy":
                marker_payload = {
                    "schema_version": 1,
                    "managed_by": "codex-agent-skill-bioinfo",
                    "deployment_mode": "copy",
                    "release_id": release_id,
                    "source_revision": revision,
                    "package_digest": f"sha256:{digest}",
                    "skills_digest": f"sha256:{skills_digest}",
                }
                atomic_write(
                    skills_marker,
                    json.dumps(marker_payload, indent=2, sort_keys=True) + "\n",
                )
            elif skills_marker.exists():
                skills_marker.unlink()
            marker_installed = True

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
        if marker_installed or marker_backup_copied:
            try:
                if skills_marker.exists() or skills_marker.is_symlink():
                    remove_path(skills_marker)
                if marker_backup.exists():
                    shutil.copy2(marker_backup, skills_marker)
            except OSError as rollback_exc:
                rollback_errors.append(f"Skill deployment marker: {rollback_exc}")
        if skill_installed or skill_backup_moved:
            try:
                if target_skills.exists() or target_skills.is_symlink():
                    remove_path(target_skills)
                if backup_skills.exists() or backup_skills.is_symlink():
                    backup_skills.rename(target_skills)
                    if skill_backup_was_directory:
                        make_read_only(target_skills)
            except OSError as rollback_exc:
                rollback_errors.append(f"Skill deployment: {rollback_exc}")
        if release_created:
            try:
                remove_path(release_root)
            except OSError as rollback_exc:
                rollback_errors.append(f"release snapshot {release_root}: {rollback_exc}")
        if staging is not None and staging.exists():
            try:
                shutil.rmtree(staging)
            except OSError as rollback_exc:
                rollback_errors.append(f"release staging {staging}: {rollback_exc}")
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
