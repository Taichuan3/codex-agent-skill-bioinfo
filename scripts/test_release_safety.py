#!/usr/bin/env python3
"""Run isolated negative fixtures for package privacy and installer preflight."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def copy_source(destination: Path) -> Path:
    source = destination / "source"
    shutil.copytree(
        ROOT,
        source,
        symlinks=True,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"),
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


def main() -> int:
    test_privacy_rejections()
    test_guidance_symlink_preflight()
    test_agent_symlink_preflight()
    print("PASS: release-safety privacy and symlink-preflight fixtures")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
