#!/usr/bin/env python3
"""Run isolated negative fixtures for package privacy and installer preflight."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def source_copy_ignore(directory: str, names: list[str]) -> set[str]:
    ignored = set(shutil.ignore_patterns(".git", "__pycache__", "*.pyc")(directory, names))
    if Path(directory).resolve() == (ROOT / ".codex").resolve():
        ignored.add("candidates")
    return ignored


def copy_source(destination: Path) -> Path:
    source = destination / "source"
    shutil.copytree(
        ROOT,
        source,
        symlinks=True,
        ignore=source_copy_ignore,
    )
    return source


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=False, capture_output=True, text=True)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def symlink_fixtures_supported() -> bool:
    return os.name != "nt"


def test_privacy_rejections() -> None:
    fixtures = {
        "memory/MEMORY.md": "native memory fixture\n",
        "state.sqlite": "sqlite fixture\n",
        "logs/runtime.json": '{"fixture": true}\n',
        "metadata/PROJECT_ENVIRONMENT.md": "machine environment fixture\n",
        ".env": "SERVICE_" + "TOKEN=" + "fixturevalue0123456789\n",
        "credentials.json": '{"credential": "fixture"}\n',
        "metadata/server.key": "fixture key material\n",
        "metadata/slack.txt": "xox" + "b-1234567890-abcdefghijklmnop\n",
        "metadata/service.txt": "API_" + "KEY=fixturevalue0123456789\n",
    }
    for relative, content in fixtures.items():
        with tempfile.TemporaryDirectory(prefix="codex-bioinfo-privacy-") as temporary:
            source = copy_source(Path(temporary))
            fixture = source / relative
            fixture.parent.mkdir(parents=True, exist_ok=True)
            fixture.write_text(content, encoding="utf-8")
            result = run([sys.executable, str(source / "scripts" / "validate_package.py")])
            require(result.returncode != 0, f"privacy fixture unexpectedly passed: {relative}")
            require(str(relative) in result.stdout, f"privacy fixture was not reported: {relative}")

    if symlink_fixtures_supported():
        with tempfile.TemporaryDirectory(prefix="codex-bioinfo-private-link-") as temporary:
            source = copy_source(Path(temporary))
            fixture = source / "private-source"
            private_target = Path("/") / "Users" / "fixture-user" / "private-project"
            fixture.symlink_to(private_target)
            result = run([sys.executable, str(source / "scripts" / "validate_package.py")])
            require(result.returncode != 0, "absolute private symlink fixture unexpectedly passed")
            require("private-source" in result.stdout, "absolute private symlink was not reported")


def test_history_modes() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-history-") as temporary:
        source = copy_source(Path(temporary))
        portable = run(
            [sys.executable, str(source / "scripts" / "validate_package.py")]
        )
        require(
            portable.returncode == 0,
            f"history-free portable validation failed: {portable.stdout}{portable.stderr}",
        )
        require(
            "Git history unavailable" in portable.stdout,
            "history-free validation did not report its reduced evidence boundary",
        )
        release = run(
            [
                sys.executable,
                str(source / "scripts" / "validate_package.py"),
                "--require-history",
            ]
        )
        require(
            release.returncode != 0,
            "history-required validation unexpectedly passed without Git history",
        )
        require(
            "--require-history needs" in release.stdout,
            "history-required failure did not explain the missing history",
        )


def test_guidance_symlink_preflight() -> None:
    if not symlink_fixtures_supported():
        return
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-guidance-link-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        codex = home / ".codex"
        codex.mkdir(parents=True)
        backing = root / "global-guidance.md"
        backing.write_text("preserve me\n", encoding="utf-8")
        guidance = codex / "AGENTS.md"
        guidance.symlink_to(backing)

        result = run(
            [
                sys.executable,
                str(source / "scripts" / "install_codex_bioinfo.py"),
                "--home",
                str(home),
                "--apply",
            ]
        )
        require(result.returncode != 0, "guidance symlink fixture unexpectedly passed")
        require(guidance.is_symlink(), "guidance symlink topology changed")
        require(guidance.resolve() == backing.resolve(), "guidance symlink target changed")
        require(backing.read_text(encoding="utf-8") == "preserve me\n", "guidance target changed")
        require(not (home / ".agents" / "skills").exists(), "preflight caused a partial install")


def test_agent_symlink_preflight() -> None:
    if not symlink_fixtures_supported():
        return
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-agent-link-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        agents = home / ".codex" / "agents"
        agents.mkdir(parents=True)
        backing = root / "capability-curator.toml"
        backing.write_text("preserve me\n", encoding="utf-8")
        destination = agents / "capability-curator.toml"
        destination.symlink_to(backing)

        result = run(
            [
                sys.executable,
                str(source / "scripts" / "install_codex_bioinfo.py"),
                "--home",
                str(home),
                "--apply",
            ]
        )
        require(result.returncode != 0, "custom-Agent symlink fixture unexpectedly passed")
        require(destination.is_symlink(), "custom-Agent symlink topology changed")
        require(destination.resolve() == backing.resolve(), "custom-Agent symlink target changed")
        require(backing.read_text(encoding="utf-8") == "preserve me\n", "Agent target changed")
        require(not (home / ".agents" / "skills").exists(), "preflight caused a partial install")


def test_fresh_install_and_idempotence() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-fresh-install-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        command = [
            sys.executable,
            str(source / "scripts" / "install_codex_bioinfo.py"),
            "--home",
            str(home),
            "--apply",
        ]
        first = run(command)
        require(
            first.returncode == 0,
            f"fresh install failed: {first.stdout}{first.stderr}",
        )
        runtime = home / ".agents" / "skills"
        if os.name == "nt":
            require(runtime.is_dir() and not runtime.is_symlink(), "Windows auto install did not create a managed Skill copy")
            marker = home / ".agents" / "codex-bioinfo-skills.json"
            payload = json.loads(marker.read_text(encoding="utf-8"))
            installed = (
                home
                / ".codex"
                / "packages"
                / "codex-agent-skill-bioinfo"
                / payload["release_id"]
                / "skills"
            )
        else:
            require(runtime.is_symlink(), "POSIX auto install did not create a Skill symlink")
            installed = runtime.resolve()
            require(
                installed.is_relative_to((home / ".codex" / "packages").resolve()),
                "runtime Skill link does not point to the managed release store",
            )
            require(
                not installed.is_relative_to(source.resolve()),
                "runtime Skill link still points to the writable source checkout",
            )
        require(
            len(list(runtime.glob("*/SKILL.md"))) == 38,
            "fresh install did not expose all 38 Skills",
        )

        second = run(command)
        require(
            second.returncode == 0 and "Already current" in second.stdout,
            f"idempotent install was not a no-op: {second.stdout}{second.stderr}",
        )

        installed_skill = installed / "paper-reader" / "SKILL.md"
        runtime_skill = runtime / "paper-reader" / "SKILL.md"
        installed_before = installed_skill.read_text(encoding="utf-8")
        runtime_before = runtime_skill.read_text(encoding="utf-8")
        installed_skill.chmod(0o600)
        installed_skill.write_text(installed_before + "\ntampered\n", encoding="utf-8")
        tampered = run(command[:-1])
        require(
            tampered.returncode != 0
            and "failed digest verification" in tampered.stderr,
            "tampered release snapshot was not rejected during preflight",
        )
        installed_skill.write_text(installed_before, encoding="utf-8")
        installed_skill.chmod(0o444)

        source_skill = source / ".codex" / "skills" / "paper-reader" / "SKILL.md"
        source_skill.write_text(
            source_skill.read_text(encoding="utf-8") + "\nsource mutation fixture\n",
            encoding="utf-8",
        )
        require(
            runtime_skill.read_text(encoding="utf-8") == runtime_before,
            "installed runtime changed after its source checkout was edited",
        )


def test_managed_copy_install_and_tamper_refusal() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-managed-copy-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        command = [
            sys.executable,
            str(source / "scripts" / "install_codex_bioinfo.py"),
            "--home",
            str(home),
            "--skills-deployment",
            "copy",
            "--apply",
        ]
        first = run(command)
        require(first.returncode == 0, f"managed-copy install failed: {first.stdout}{first.stderr}")
        runtime = home / ".agents" / "skills"
        marker = home / ".agents" / "codex-bioinfo-skills.json"
        require(runtime.is_dir() and not runtime.is_symlink(), "managed-copy runtime is not a real directory")
        payload = json.loads(marker.read_text(encoding="utf-8"))
        require(payload.get("deployment_mode") == "copy", "managed-copy marker has the wrong mode")
        require(len(list(runtime.glob("*/SKILL.md"))) == 38, "managed-copy runtime does not expose 38 Skills")

        second = run(command)
        require(
            second.returncode == 0 and "Already current" in second.stdout,
            f"managed-copy install was not idempotent: {second.stdout}{second.stderr}",
        )

        runtime_skill = runtime / "paper-reader" / "SKILL.md"
        runtime_skill.chmod(0o600)
        runtime_skill.write_text(
            runtime_skill.read_text(encoding="utf-8") + "\nlocal tamper\n",
            encoding="utf-8",
        )
        tampered = run(command[:-1])
        require(
            tampered.returncode != 0 and "managed Skill copy failed digest verification" in tampered.stderr,
            "tampered managed copy was not rejected",
        )

    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-unmanaged-copy-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        runtime = home / ".agents" / "skills"
        runtime.mkdir(parents=True)
        (runtime / "user-file.txt").write_text("preserve\n", encoding="utf-8")
        result = run(
            [
                sys.executable,
                str(source / "scripts" / "install_codex_bioinfo.py"),
                "--home",
                str(home),
                "--skills-deployment",
                "copy",
                "--apply",
            ]
        )
        require(result.returncode != 0, "unmanaged Skill directory was overwritten")
        require((runtime / "user-file.txt").read_text(encoding="utf-8") == "preserve\n", "unmanaged Skill content changed")


def test_bidirectional_deployment_migration() -> None:
    if not symlink_fixtures_supported():
        return
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-deployment-migration-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        base = [
            sys.executable,
            str(source / "scripts" / "install_codex_bioinfo.py"),
            "--home",
            str(home),
            "--skills-deployment",
        ]
        runtime = home / ".agents" / "skills"
        marker = home / ".agents" / "codex-bioinfo-skills.json"

        linked = run([*base, "symlink", "--apply"])
        require(linked.returncode == 0 and runtime.is_symlink(), "initial symlink deployment failed")
        copied = run([*base, "copy", "--apply"])
        require(copied.returncode == 0, f"symlink-to-copy migration failed: {copied.stdout}{copied.stderr}")
        require(runtime.is_dir() and not runtime.is_symlink(), "symlink-to-copy migration did not create a real directory")
        require(marker.is_file(), "symlink-to-copy migration did not create the managed-copy marker")
        copy_noop = run([*base, "copy", "--apply"])
        require(
            copy_noop.returncode == 0 and "Already current" in copy_noop.stdout,
            "migrated managed copy was not idempotent",
        )

        relinked = run([*base, "symlink", "--apply"])
        require(relinked.returncode == 0, f"copy-to-symlink migration failed: {relinked.stdout}{relinked.stderr}")
        require(runtime.is_symlink(), "copy-to-symlink migration did not restore a symlink")
        require(not marker.exists(), "copy-to-symlink migration left a stale managed-copy marker")
        link_noop = run([*base, "symlink", "--apply"])
        require(
            link_noop.returncode == 0 and "Already current" in link_noop.stdout,
            "migrated symlink deployment was not idempotent",
        )


def test_dirty_source_refusal() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-dirty-source-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        for command in (
            ["git", "init"],
            ["git", "config", "user.email", "fixture@example.invalid"],
            ["git", "config", "user.name", "Fixture"],
            ["git", "add", "."],
            ["git", "commit", "-m", "fixture baseline"],
        ):
            result = run(["git", "-C", str(source), *command[1:]])
            require(
                result.returncode == 0,
                f"dirty-source Git fixture setup failed: {result.stdout}{result.stderr}",
            )
        (source / "untracked-fixture.txt").write_text("dirty\n", encoding="utf-8")
        home = root / "home"
        result = run(
            [
                sys.executable,
                str(source / "scripts" / "install_codex_bioinfo.py"),
                "--home",
                str(home),
                "--apply",
            ]
        )
        require(result.returncode != 0, "dirty source unexpectedly installed")
        require(
            "source checkout has tracked or untracked changes" in result.stderr,
            "dirty-source refusal did not explain the boundary",
        )
        require(
            not (home / ".agents" / "skills").exists(),
            "dirty-source refusal caused a partial install",
        )


def test_untracked_local_candidates_do_not_block() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-local-candidate-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        for command in (
            ["git", "init"],
            ["git", "config", "user.email", "fixture@example.invalid"],
            ["git", "config", "user.name", "Fixture"],
            ["git", "add", "."],
            ["git", "commit", "-m", "fixture baseline"],
        ):
            result = run(["git", "-C", str(source), *command[1:]])
            require(
                result.returncode == 0,
                f"candidate-only Git fixture setup failed: {result.stdout}{result.stderr}",
            )
        candidate = source / ".codex" / "candidates" / "local-only" / "NOTE.md"
        candidate.parent.mkdir(parents=True)
        candidate.write_text("untracked local candidate\n", encoding="utf-8")
        home = root / "home"
        result = run(
            [
                sys.executable,
                str(source / "scripts" / "install_codex_bioinfo.py"),
                "--home",
                str(home),
                "--apply",
            ]
        )
        require(
            result.returncode == 0,
            f"untracked local candidate blocked installation: {result.stdout}{result.stderr}",
        )
        runtime = (home / ".agents" / "skills").resolve()
        require(
            not (runtime / "local-only").exists(),
            "local candidate leaked into the installed Skill snapshot",
        )

    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-archive-candidate-") as temporary:
        source = copy_source(Path(temporary))
        candidate = source / ".codex" / "candidates" / "archive-copy" / "NOTE.md"
        candidate.parent.mkdir(parents=True)
        candidate.write_text("archive candidate\n", encoding="utf-8")
        result = run([sys.executable, str(source / "scripts" / "validate_package.py")])
        require(result.returncode != 0, "candidate-bearing archive unexpectedly passed")
        require(
            "not part of a portable archive" in result.stdout,
            "candidate-bearing archive rejection did not explain the boundary",
        )

    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-tracked-candidate-") as temporary:
        source = copy_source(Path(temporary))
        for command in (
            ["git", "init"],
            ["git", "config", "user.email", "fixture@example.invalid"],
            ["git", "config", "user.name", "Fixture"],
            ["git", "add", "."],
            ["git", "commit", "-m", "fixture baseline"],
        ):
            setup = run(["git", "-C", str(source), *command[1:]])
            require(
                setup.returncode == 0,
                f"tracked-candidate Git fixture setup failed: {setup.stdout}{setup.stderr}",
            )
        baseline = run([sys.executable, str(source / "scripts" / "validate_package.py")])
        require(
            baseline.returncode == 0,
            f"tracked-candidate baseline validation failed: {baseline.stdout}{baseline.stderr}",
        )
        candidate = source / ".codex" / "candidates" / "tracked-copy" / "NOTE.md"
        candidate.parent.mkdir(parents=True)
        candidate.write_text("tracked candidate\n", encoding="utf-8")
        for command in (
            ["git", "add", "--force", ".codex/candidates/tracked-copy/NOTE.md"],
            ["git", "commit", "-m", "fixture with tracked candidate"],
        ):
            setup = run(["git", "-C", str(source), *command[1:]])
            require(
                setup.returncode == 0,
                f"tracked-candidate commit setup failed: {setup.stdout}{setup.stderr}",
            )
        tracked = run(
            [
                "git",
                "-C",
                str(source),
                "ls-files",
                "--",
                ".codex/candidates/tracked-copy/NOTE.md",
            ]
        )
        require(
            tracked.returncode == 0 and tracked.stdout.strip(),
            f"tracked-candidate fixture is not tracked: {tracked.stdout}{tracked.stderr}",
        )
        result = run([sys.executable, str(source / "scripts" / "validate_package.py")])
        require(result.returncode != 0, "tracked candidate unexpectedly passed")
        require(
            "only as an untracked local worktree area" in result.stdout,
            f"tracked-candidate rejection did not explain the boundary: {result.stdout}{result.stderr}",
        )


def test_transaction_rollback_and_legacy_recovery() -> None:
    if not symlink_fixtures_supported():
        return
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-rollback-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        installer = source / "scripts" / "install_codex_bioinfo.py"
        installer_text = installer.read_text(encoding="utf-8")
        marker = "        target_agents.mkdir(parents=True, exist_ok=True)\n"
        require(marker in installer_text, "rollback fault-injection marker is missing")
        installer.write_text(
            installer_text.replace(
                marker,
                '        raise RuntimeError("fixture failure after legacy retirement")\n\n'
                + marker,
                1,
            ),
            encoding="utf-8",
        )

        home = root / "home"
        old_skills = root / "old-skills"
        old_skills.mkdir()
        runtime = home / ".agents" / "skills"
        runtime.parent.mkdir(parents=True)
        runtime.symlink_to(old_skills)
        guidance = home / ".codex" / "AGENTS.md"
        guidance.parent.mkdir(parents=True)
        guidance.write_text("preserve guidance\n", encoding="utf-8")
        legacy = home / ".codex" / "skills" / "legacy-fixture"
        legacy.mkdir(parents=True)
        (legacy / "SKILL.md").write_text("legacy\n", encoding="utf-8")

        result = run(
            [
                sys.executable,
                str(installer),
                "--home",
                str(home),
                "--apply",
                "--retire-legacy-codex-skills",
            ]
        )
        require(result.returncode != 0, "fault-injected install unexpectedly passed")
        require(
            "rollback was attempted" in result.stderr,
            f"fault-injected install did not report rollback: {result.stdout}{result.stderr}",
        )
        require(
            runtime.is_symlink() and runtime.resolve() == old_skills.resolve(),
            "rollback did not restore the previous Skill symlink",
        )
        require(
            guidance.read_text(encoding="utf-8") == "preserve guidance\n",
            "rollback did not restore global guidance",
        )
        require(
            (legacy / "SKILL.md").read_text(encoding="utf-8") == "legacy\n",
            "rollback did not restore the retired legacy Skill",
        )
        package_store = home / ".codex" / "packages" / "codex-agent-skill-bioinfo"
        require(
            not package_store.exists() or not any(package_store.iterdir()),
            "rollback left a partially installed release snapshot",
        )


def test_managed_copy_transaction_rollback() -> None:
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-copy-rollback-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        command = [
            sys.executable,
            str(source / "scripts" / "install_codex_bioinfo.py"),
            "--home",
            str(home),
            "--skills-deployment",
            "copy",
            "--apply",
        ]
        initial = run(command)
        require(initial.returncode == 0, f"copy rollback setup failed: {initial.stdout}{initial.stderr}")
        runtime = home / ".agents" / "skills"
        marker_path = home / ".agents" / "codex-bioinfo-skills.json"
        original_skill = (runtime / "paper-reader" / "SKILL.md").read_text(encoding="utf-8")
        original_marker = marker_path.read_text(encoding="utf-8")
        original_releases = {
            path.name
            for path in (home / ".codex" / "packages" / "codex-agent-skill-bioinfo").iterdir()
        }

        source_skill = source / ".codex" / "skills" / "paper-reader" / "SKILL.md"
        source_skill.write_text(
            source_skill.read_text(encoding="utf-8") + "\ncopy rollback source mutation\n",
            encoding="utf-8",
        )
        installer = source / "scripts" / "install_codex_bioinfo.py"
        installer_text = installer.read_text(encoding="utf-8")
        injection_point = "        target_agents.mkdir(parents=True, exist_ok=True)\n"
        require(injection_point in installer_text, "copy rollback fault-injection marker is missing")
        installer.write_text(
            installer_text.replace(
                injection_point,
                '        raise RuntimeError("fixture failure after managed copy update")\n\n'
                + injection_point,
                1,
            ),
            encoding="utf-8",
        )

        failed = run(command)
        require(failed.returncode != 0, "fault-injected managed-copy update unexpectedly passed")
        require("rollback was attempted" in failed.stderr, "managed-copy rollback was not reported")
        require(
            (runtime / "paper-reader" / "SKILL.md").read_text(encoding="utf-8") == original_skill,
            "managed-copy rollback did not restore the previous Skill tree",
        )
        require(
            marker_path.read_text(encoding="utf-8") == original_marker,
            "managed-copy rollback did not restore the previous marker",
        )
        remaining_releases = {
            path.name
            for path in (home / ".codex" / "packages" / "codex-agent-skill-bioinfo").iterdir()
        }
        require(
            remaining_releases == original_releases,
            "managed-copy rollback left a partial release snapshot",
        )


def test_bidirectional_migration_rollback() -> None:
    if not symlink_fixtures_supported():
        return
    with tempfile.TemporaryDirectory(prefix="codex-bioinfo-migration-rollback-") as temporary:
        root = Path(temporary)
        source = copy_source(root)
        home = root / "home"
        installer = source / "scripts" / "install_codex_bioinfo.py"
        original_installer = installer.read_text(encoding="utf-8")
        injection_point = "        target_agents.mkdir(parents=True, exist_ok=True)\n"
        require(injection_point in original_installer, "migration rollback injection point is missing")
        base = [
            sys.executable,
            str(installer),
            "--home",
            str(home),
            "--skills-deployment",
        ]
        runtime = home / ".agents" / "skills"
        marker = home / ".agents" / "codex-bioinfo-skills.json"

        initial_link = run([*base, "symlink", "--apply"])
        require(initial_link.returncode == 0 and runtime.is_symlink(), "migration rollback symlink setup failed")
        original_link_target = runtime.resolve()
        installer.write_text(
            original_installer.replace(
                injection_point,
                '        raise RuntimeError("fixture failure during symlink-to-copy migration")\n\n'
                + injection_point,
                1,
            ),
            encoding="utf-8",
        )
        copy_failure = run([*base, "copy", "--apply"])
        require(copy_failure.returncode != 0, "fault-injected symlink-to-copy migration unexpectedly passed")
        require(runtime.is_symlink() and runtime.resolve() == original_link_target, "symlink-to-copy rollback did not restore the link")
        require(not marker.exists(), "symlink-to-copy rollback left a managed-copy marker")

        installer.write_text(original_installer, encoding="utf-8")
        copy_setup = run([*base, "copy", "--apply"])
        require(copy_setup.returncode == 0 and marker.is_file(), "migration rollback copy setup failed")
        original_marker = marker.read_text(encoding="utf-8")
        original_runtime = (runtime / "paper-reader" / "SKILL.md").read_text(encoding="utf-8")
        installer.write_text(
            original_installer.replace(
                injection_point,
                '        raise RuntimeError("fixture failure during copy-to-symlink migration")\n\n'
                + injection_point,
                1,
            ),
            encoding="utf-8",
        )
        link_failure = run([*base, "symlink", "--apply"])
        require(link_failure.returncode != 0, "fault-injected copy-to-symlink migration unexpectedly passed")
        require(runtime.is_dir() and not runtime.is_symlink(), "copy-to-symlink rollback did not restore the managed copy")
        require(marker.read_text(encoding="utf-8") == original_marker, "copy-to-symlink rollback did not restore the marker")
        require(
            (runtime / "paper-reader" / "SKILL.md").read_text(encoding="utf-8") == original_runtime,
            "copy-to-symlink rollback did not restore Skill content",
        )


def main() -> int:
    test_privacy_rejections()
    test_history_modes()
    test_guidance_symlink_preflight()
    test_agent_symlink_preflight()
    test_fresh_install_and_idempotence()
    test_managed_copy_install_and_tamper_refusal()
    test_bidirectional_deployment_migration()
    test_dirty_source_refusal()
    test_untracked_local_candidates_do_not_block()
    test_transaction_rollback_and_legacy_recovery()
    test_managed_copy_transaction_rollback()
    test_bidirectional_migration_rollback()
    print(
        "PASS: release-safety privacy, history, preflight, immutable install, "
        "dirty-source, local-candidate exclusion, idempotence, and rollback fixtures"
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
