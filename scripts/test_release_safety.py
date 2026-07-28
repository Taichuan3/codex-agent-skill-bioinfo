#!/usr/bin/env python3
"""Run isolated negative fixtures for package privacy and installer preflight."""

from __future__ import annotations

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
        require(runtime.is_symlink(), "fresh install did not create a Skill symlink")
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
            len(list(installed.glob("*/SKILL.md"))) == 38,
            "fresh install did not expose all 38 Skills",
        )

        second = run(command)
        require(
            second.returncode == 0 and "Already current" in second.stdout,
            f"idempotent install was not a no-op: {second.stdout}{second.stderr}",
        )

        installed_skill = installed / "paper-reader" / "SKILL.md"
        installed_before = installed_skill.read_text(encoding="utf-8")
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
            installed_skill.read_text(encoding="utf-8") == installed_before,
            "installed runtime changed after its source checkout was edited",
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
        candidate = source / ".codex" / "candidates" / "tracked-copy" / "NOTE.md"
        candidate.parent.mkdir(parents=True)
        candidate.write_text("tracked candidate\n", encoding="utf-8")
        for command in (
            ["git", "init"],
            ["git", "config", "user.email", "fixture@example.invalid"],
            ["git", "config", "user.name", "Fixture"],
            ["git", "add", "."],
            ["git", "commit", "-m", "fixture with tracked candidate"],
        ):
            setup = run(["git", "-C", str(source), *command[1:]])
            require(
                setup.returncode == 0,
                f"tracked-candidate Git fixture setup failed: {setup.stdout}{setup.stderr}",
            )
        result = run([sys.executable, str(source / "scripts" / "validate_package.py")])
        require(result.returncode != 0, "tracked candidate unexpectedly passed")
        require(
            "only as an untracked local worktree area" in result.stdout,
            "tracked-candidate rejection did not explain the boundary",
        )


def test_transaction_rollback_and_legacy_recovery() -> None:
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
            "fault-injected install did not report rollback",
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


def main() -> int:
    test_privacy_rejections()
    test_history_modes()
    test_guidance_symlink_preflight()
    test_agent_symlink_preflight()
    test_fresh_install_and_idempotence()
    test_dirty_source_refusal()
    test_untracked_local_candidates_do_not_block()
    test_transaction_rollback_and_legacy_recovery()
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
