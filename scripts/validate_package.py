#!/usr/bin/env python3
"""Validate the portable bioinformatics Codex package without dependencies."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".codex" / "skills"
AGENTS = ROOT / ".codex" / "agents"
MANIFEST = ROOT / "local_config.yaml"

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def expected_count(key: str) -> int | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(\d+)\s*$", MANIFEST.read_text())
    return int(match.group(1)) if match else None


skill_dirs = sorted(path.parent for path in SKILLS.glob("*/SKILL.md"))
skill_names: set[str] = set()
for skill_dir in skill_dirs:
    skill_file = skill_dir / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{skill_file.relative_to(ROOT)}: missing YAML frontmatter")
        continue
    parts = text.split("---", 2)
    if len(parts) < 3:
        fail(f"{skill_file.relative_to(ROOT)}: unclosed YAML frontmatter")
        continue
    frontmatter = parts[1]
    name_match = re.search(r"(?m)^name:\s*['\"]?([^'\"\n]+)", frontmatter)
    description_match = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    if not name_match:
        fail(f"{skill_file.relative_to(ROOT)}: missing name")
    else:
        name = name_match.group(1).strip()
        if name in skill_names:
            fail(f"duplicate Skill name: {name}")
        skill_names.add(name)
        if name != skill_dir.name:
            fail(f"{skill_file.relative_to(ROOT)}: name does not match directory")
    if not description_match:
        fail(f"{skill_file.relative_to(ROOT)}: missing description")
    if "## 核心问题" not in text:
        fail(f"{skill_file.relative_to(ROOT)}: missing ## 核心问题")
    if not (skill_dir / "agents" / "openai.yaml").is_file():
        fail(f"{skill_dir.relative_to(ROOT)}: missing agents/openai.yaml")

expected_skills = expected_count("expected_skill_count")
if expected_skills is None:
    fail("local_config.yaml: expected_skill_count is missing")
elif len(skill_dirs) != expected_skills:
    fail(f"Skill count is {len(skill_dirs)}, expected {expected_skills}")

agent_files = sorted(AGENTS.glob("*.toml"))
agent_names: set[str] = set()
for agent_file in agent_files:
    try:
        with agent_file.open("rb") as handle:
            data = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        fail(f"{agent_file.relative_to(ROOT)}: invalid TOML: {exc}")
        continue
    for key in ("name", "description", "developer_instructions"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            fail(f"{agent_file.relative_to(ROOT)}: missing non-empty {key}")
    name = data.get("name")
    if isinstance(name, str):
        if name in agent_names:
            fail(f"duplicate custom Agent name: {name}")
        agent_names.add(name)
    if data.get("sandbox_mode") not in {"read-only", "workspace-write"}:
        fail(f"{agent_file.relative_to(ROOT)}: sandbox_mode must be read-only or workspace-write")

expected_agents = expected_count("expected_custom_agent_count")
if expected_agents is None:
    fail("local_config.yaml: expected_custom_agent_count is missing")
elif len(agent_files) != expected_agents:
    fail(f"custom Agent count is {len(agent_files)}, expected {expected_agents}")

skill_link = ROOT / ".agents" / "skills"
if not skill_link.is_symlink():
    fail(".agents/skills must be a symlink")
elif skill_link.resolve() != SKILLS.resolve():
    fail(".agents/skills does not resolve to .codex/skills")

for forbidden in (
    "terminal_profiles",
    "PROJECT_ENVIRONMENT.md",
    "PROJECT_ENVIRONMENT.local.md",
    "auth.json",
):
    forbidden_path = ROOT / forbidden
    has_content = forbidden_path.exists() and (
        not forbidden_path.is_dir()
        or any(item.is_file() or item.is_symlink() for item in forbidden_path.rglob("*"))
    )
    if has_content:
        fail(f"forbidden package path exists: {forbidden}")

private_path = re.compile(
    r"(?:/Users/(?:" + "yaji" + r"ehu)|/home/(?:" + "huya" + r"jie)|Extreme " + "SSD)"
)
secret_pattern = re.compile(
    "(?:github" + r"_pat_[A-Za-z0-9_]{20,}|sk-" + r"proj-[A-Za-z0-9_-]{20,}|BEGIN [A-Z ]*PRIVATE KEY)"
)
scannable_suffixes = {".md", ".yaml", ".yml", ".toml", ".py", ".sh", ".txt"}
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in scannable_suffixes:
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if private_path.search(text):
        fail(f"{path.relative_to(ROOT)}: contains a private machine path")
    if secret_pattern.search(text):
        fail(f"{path.relative_to(ROOT)}: contains a high-risk secret pattern")

if "Hermes" in (ROOT / "AGENTS.md").read_text(encoding="utf-8"):
    fail("AGENTS.md still contains a Hermes runtime dependency")

if warnings:
    for warning in warnings:
        print(f"WARNING: {warning}")
if errors:
    for error in errors:
        print(f"ERROR: {error}")
    print(f"FAIL: {len(errors)} validation error(s)")
    sys.exit(1)

print(
    "PASS: "
    f"{len(skill_dirs)} Skills, {len(agent_files)} custom Agents, "
    "discovery link, manifest counts, and privacy gates validated"
)
