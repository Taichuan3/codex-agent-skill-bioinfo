#!/usr/bin/env python3
"""Validate the portable bioinformatics Codex package without dependencies."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".codex" / "skills"
AGENTS = ROOT / ".codex" / "agents"
AGENT_ROUTING_EVALS = AGENTS / "evals" / "agent-routing-evals.json"
AGENT_ROUTING_FORWARD_TEST = ROOT / "docs" / "AGENT_ROUTING_FORWARD_TEST_2026-07-28.tsv"
AGENT_ROUTING_FORWARD_PROTOCOL = ROOT / "docs" / "AGENT_ROUTING_FORWARD_PROTOCOL_2026-07-28.md"
MANIFEST = ROOT / "local_config.yaml"
CAPABILITY_REGISTRY = ROOT / ".codex" / "capability_registry.json"
CAPABILITY_RUN_VALIDATOR = ROOT / "scripts" / "validate_capability_run.py"
CAPABILITY_BEHAVIOR_TESTS = ROOT / "scripts" / "test_capability_behavior.py"
GLOBAL_GUIDANCE = ROOT / "templates" / "global-AGENTS.md"
ROUTING_FORWARD_TEST = ROOT / "docs" / "ROUTING_FORWARD_TEST_2026-07-25.tsv"
ROUTING_MIXED_BASELINE = ROOT / "docs" / "ROUTING_MIXED_BLIND_BASELINE_2026-07-28.tsv"
ROUTING_MIXED_BLIND_TEST = ROOT / "docs" / "ROUTING_MIXED_BLIND_TEST_2026-07-28.tsv"
ROUTING_MIXED_PROTOCOL = ROOT / "docs" / "ROUTING_MIXED_BLIND_PROTOCOL_2026-07-28.md"
EXTERNAL_LINEAGE = ROOT / "docs" / "EXTERNAL_FILE_LINEAGE.tsv"
POST_BASELINE_LINEAGE = ROOT / "docs" / "EXTERNAL_FILE_LINEAGE_POST_BASELINE.tsv"
EXPRESSION_REVIEW = ROOT / "docs" / "EXTERNAL_EXPRESSION_REVIEW_2026-07-25.tsv"
THIRD_PARTY_NOTICES = ROOT / "THIRD_PARTY_NOTICES.md"
ABSORPTION_COMMITS = ("a2f35f4", "e4ee03a", "e649474", "875cb4a")
EXPECTED_LINEAGE_PATH_HASH = "81d474ae12dd073bbe6e22f0e61a35f4ec0833caa4a23e898b92d589539f4a4f"

errors: list[str] = []
warnings: list[str] = []
REQUIRE_HISTORY = False
for argument in sys.argv[1:]:
    if argument == "--require-history":
        REQUIRE_HISTORY = True
    else:
        errors.append(f"unknown validator argument: {argument}")


def fail(message: str) -> None:
    errors.append(message)


def git_repository_root() -> Path | None:
    if shutil.which("git") is None:
        return None
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    resolved = Path(result.stdout.strip()).resolve()
    return resolved if resolved == ROOT.resolve() else None


REPOSITORY_ROOT = git_repository_root()


def expected_count(key: str) -> int | None:
    match = re.search(rf"(?m)^\s*{re.escape(key)}:\s*(\d+)\s*$", MANIFEST.read_text())
    return int(match.group(1)) if match else None


skill_dirs = sorted(path.parent for path in SKILLS.glob("*/SKILL.md"))
known_skill_names = {path.name for path in skill_dirs}
skill_names: set[str] = set()
trigger_query_owners: dict[str, str] = {}
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
    elif len(description_match.group(1).strip()) > 300:
        fail(f"{skill_file.relative_to(ROOT)}: description exceeds the 300-character trigger budget")
    if "## 核心问题" not in text:
        fail(f"{skill_file.relative_to(ROOT)}: missing ## 核心问题")
    if len(text) > 6000 or len(text.splitlines()) > 120:
        fail(f"{skill_file.relative_to(ROOT)}: exceeds the 6000-character or 120-line body budget")
    frontmatter_keys = set(re.findall(r"(?m)^([A-Za-z][A-Za-z0-9_-]*):", frontmatter))
    if frontmatter_keys != {"name", "description"}:
        fail(f"{skill_file.relative_to(ROOT)}: frontmatter must contain only name and description")
    metadata_file = skill_dir / "agents" / "openai.yaml"
    if not metadata_file.is_file():
        fail(f"{skill_dir.relative_to(ROOT)}: missing agents/openai.yaml")
    else:
        metadata_text = metadata_file.read_text(encoding="utf-8")
        metadata_match = re.fullmatch(
            r'interface:\n'
            r'  display_name: "([^"\n]+)"\n'
            r'  short_description: "([^"\n]+)"\n'
            r'  default_prompt: "([^"\n]+)"\n?',
            metadata_text,
        )
        if not metadata_match:
            fail(
                f"{metadata_file.relative_to(ROOT)}: must contain only quoted "
                "interface display_name, short_description, and default_prompt"
            )
        elif not 25 <= len(metadata_match.group(2)) <= 64:
            fail(f"{metadata_file.relative_to(ROOT)}: short_description must be 25-64 characters")
        if f"${skill_dir.name}" not in metadata_text:
            fail(f"{metadata_file.relative_to(ROOT)}: default_prompt must mention ${skill_dir.name}")
    for resource_dir_name in ("references", "scripts", "assets"):
        resource_dir = skill_dir / resource_dir_name
        for resource_file in sorted(resource_dir.glob("*")):
            if resource_file.is_file() and resource_file.name not in text:
                fail(f"{skill_file.relative_to(ROOT)}: does not route to {resource_file.name}")
    for portable_file in skill_dir.rglob("*"):
        if not portable_file.is_file() or portable_file.suffix.lower() not in {
            ".json",
            ".md",
            ".py",
            ".yaml",
            ".yml",
        }:
            continue
        portable_text = portable_file.read_text(encoding="utf-8", errors="replace")
        if re.search(r"\bHermes\b", portable_text, flags=re.IGNORECASE):
            fail(f"{portable_file.relative_to(ROOT)}: standardized Skill contains Hermes residue")
    eval_dir = skill_dir / "evals"
    eval_files = sorted(eval_dir.glob("*.json"))
    if not eval_dir.exists():
        fail(f"{skill_dir.relative_to(ROOT)}: standardized Skill is missing evals/")
    if eval_dir.exists():
        expected_eval_names = {"trigger-evals.json", "outcome-evals.json"}
        actual_eval_names = {path.name for path in eval_files}
        if actual_eval_names != expected_eval_names:
            fail(
                f"{eval_dir.relative_to(ROOT)}: eval files must be exactly "
                "trigger-evals.json and outcome-evals.json"
            )
    for eval_file in eval_files:
        try:
            eval_data = json.loads(eval_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"{eval_file.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        if eval_data.get("schema_version") != 1:
            fail(f"{eval_file.relative_to(ROOT)}: schema_version must be 1")
        if eval_data.get("skill_name") != skill_dir.name:
            fail(f"{eval_file.relative_to(ROOT)}: skill_name does not match directory")
        cases = eval_data.get("cases")
        if not isinstance(cases, list) or not cases:
            fail(f"{eval_file.relative_to(ROOT)}: cases must be a non-empty list")
            continue
        if eval_file.name == "trigger-evals.json" and len(cases) != 20:
            fail(f"{eval_file.relative_to(ROOT)}: standardized trigger eval needs exactly 20 cases")
        if eval_file.name == "outcome-evals.json" and len(cases) < 5:
            fail(f"{eval_file.relative_to(ROOT)}: standardized outcome eval needs at least 5 cases")
        case_ids: set[str] = set()
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                fail(f"{eval_file.relative_to(ROOT)}: case {index} must be an object")
                continue
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id.strip():
                fail(f"{eval_file.relative_to(ROOT)}: case {index} is missing id")
            elif case_id in case_ids:
                fail(f"{eval_file.relative_to(ROOT)}: duplicate case id {case_id}")
            else:
                case_ids.add(case_id)
            if eval_file.name == "trigger-evals.json":
                for key in ("query", "expected_primary_skill", "rationale"):
                    if not isinstance(case.get(key), str) or not case[key].strip():
                        fail(f"{eval_file.relative_to(ROOT)}: {case_id or index} is missing {key}")
                if not isinstance(case.get("should_trigger"), bool):
                    fail(f"{eval_file.relative_to(ROOT)}: {case_id or index} should_trigger must be boolean")
                if case.get("split") not in {"train", "validation"}:
                    fail(f"{eval_file.relative_to(ROOT)}: {case_id or index} split must be train or validation")
                expected_primary = case.get("expected_primary_skill")
                if expected_primary != "none" and expected_primary not in known_skill_names:
                    fail(
                        f"{eval_file.relative_to(ROOT)}: {case_id or index} "
                        f"references unknown Skill {expected_primary}"
                    )
                if case.get("should_trigger") is True and expected_primary != skill_dir.name:
                    fail(
                        f"{eval_file.relative_to(ROOT)}: {case_id or index} positive case "
                        f"must route primarily to {skill_dir.name}"
                    )
                if case.get("should_trigger") is False and expected_primary == skill_dir.name:
                    fail(
                        f"{eval_file.relative_to(ROOT)}: {case_id or index} negative case "
                        f"cannot route primarily to {skill_dir.name}"
                    )
                query = case.get("query")
                if isinstance(query, str) and isinstance(expected_primary, str):
                    prior_owner = trigger_query_owners.get(query)
                    if prior_owner is not None and prior_owner != expected_primary:
                        fail(
                            f"{eval_file.relative_to(ROOT)}: {case_id or index} duplicates a query "
                            f"with conflicting primary routes {prior_owner} and {expected_primary}"
                        )
                    trigger_query_owners[query] = expected_primary
            elif eval_file.name == "outcome-evals.json":
                for key in ("mode", "task"):
                    if not isinstance(case.get(key), str) or not case[key].strip():
                        fail(f"{eval_file.relative_to(ROOT)}: {case_id or index} is missing {key}")
                for key in ("must_include", "must_not"):
                    value = case.get(key)
                    if not isinstance(value, list) or not value or not all(
                        isinstance(item, str) and item.strip() for item in value
                    ):
                        fail(f"{eval_file.relative_to(ROOT)}: {case_id or index} {key} must be non-empty strings")
        if eval_file.name == "trigger-evals.json":
            trigger_values = {case.get("should_trigger") for case in cases if isinstance(case, dict)}
            splits = {case.get("split") for case in cases if isinstance(case, dict)}
            positives = sum(case.get("should_trigger") is True for case in cases if isinstance(case, dict))
            train_cases = sum(case.get("split") == "train" for case in cases if isinstance(case, dict))
            train_positives = sum(
                case.get("split") == "train" and case.get("should_trigger") is True
                for case in cases
                if isinstance(case, dict)
            )
            validation_positives = sum(
                case.get("split") == "validation" and case.get("should_trigger") is True
                for case in cases
                if isinstance(case, dict)
            )
            if trigger_values != {True, False}:
                fail(f"{eval_file.relative_to(ROOT)}: trigger eval needs positive and negative cases")
            if splits != {"train", "validation"}:
                fail(f"{eval_file.relative_to(ROOT)}: trigger eval needs train and validation splits")
            if positives != 10:
                fail(f"{eval_file.relative_to(ROOT)}: trigger eval needs exactly 10 positive cases")
            if train_cases != 10:
                fail(f"{eval_file.relative_to(ROOT)}: trigger eval needs exactly 10 train cases")
            if train_positives != 5 or validation_positives != 5:
                fail(
                    f"{eval_file.relative_to(ROOT)}: each split needs exactly "
                    "5 positive and 5 negative trigger cases"
                )

expected_skills = expected_count("expected_skill_count")
if expected_skills is None:
    fail("local_config.yaml: expected_skill_count is missing")
elif len(skill_dirs) != expected_skills:
    fail(f"Skill count is {len(skill_dirs)}, expected {expected_skills}")

manifest_text = MANIFEST.read_text(encoding="utf-8")
skills_block_match = re.search(r"(?ms)^skills:\n(.*?)^custom_agents:", manifest_text)
if not skills_block_match:
    fail("local_config.yaml: skills list is missing")
else:
    manifest_skill_names = re.findall(r"(?m)^  - ([a-z0-9-]+)$", skills_block_match.group(1))
    if len(manifest_skill_names) != len(set(manifest_skill_names)):
        fail("local_config.yaml: skills list contains duplicates")
    if set(manifest_skill_names) != known_skill_names:
        missing = sorted(known_skill_names - set(manifest_skill_names))
        extra = sorted(set(manifest_skill_names) - known_skill_names)
        fail(f"local_config.yaml: skills list mismatch; missing={missing}, extra={extra}")

if "capability_registry: .codex/capability_registry.json" not in manifest_text:
    fail("local_config.yaml: capability_registry entrypoint is missing")
for entrypoint, expected_path in (
    ("capability_run_validator", "scripts/validate_capability_run.py"),
    ("capability_behavior_fixtures", "scripts/test_capability_behavior.py"),
):
    if f"{entrypoint}: {expected_path}" not in manifest_text:
        fail(f"local_config.yaml: {entrypoint} entrypoint is missing")
for required_script in (CAPABILITY_RUN_VALIDATOR, CAPABILITY_BEHAVIOR_TESTS):
    if not required_script.is_file():
        fail(f"{required_script.relative_to(ROOT)} is missing")

registered_owner_skills = {
    "scientific-database-grounding",
    "rnaseq-singlecell-workflow",
    "variant-genomics-interpretation",
    "literature-search-workflow",
    "paper-reader",
    "protein-structure-docking",
}
if not CAPABILITY_REGISTRY.is_file():
    fail(".codex/capability_registry.json is missing")
else:
    try:
        capability_registry = json.loads(CAPABILITY_REGISTRY.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f".codex/capability_registry.json is invalid JSON: {exc}")
        capability_registry = {}
    if capability_registry.get("schema_version") != 1:
        fail(".codex/capability_registry.json: schema_version must be 1")
    maturity_levels = capability_registry.get("maturity_levels")
    expected_maturity_levels = {
        "spec-only",
        "tool-bound",
        "fixture-tested",
        "integration-tested",
        "research-piloted",
        "production",
    }
    if not isinstance(maturity_levels, list) or set(maturity_levels) != expected_maturity_levels:
        fail(".codex/capability_registry.json: maturity_levels do not match the package contract")
    operating_rules = capability_registry.get("operating_rules")
    if not isinstance(operating_rules, dict) or set(operating_rules) != {
        "selection",
        "authority",
        "provenance",
        "fallback",
        "promotion",
        "rollback",
    }:
        fail(".codex/capability_registry.json: operating_rules are incomplete")
    backends = capability_registry.get("backends")
    backend_ids: set[str] = set()
    if not isinstance(backends, list) or not backends:
        fail(".codex/capability_registry.json: backends must be a non-empty list")
        backends = []
    for backend in backends:
        if not isinstance(backend, dict):
            fail(".codex/capability_registry.json: every backend must be an object")
            continue
        backend_id = backend.get("id")
        if not isinstance(backend_id, str) or not backend_id:
            fail(".codex/capability_registry.json: backend is missing id")
            continue
        if backend_id in backend_ids:
            fail(f".codex/capability_registry.json: duplicate backend id {backend_id}")
        backend_ids.add(backend_id)
        for field in (
            "kind",
            "source",
            "license",
            "network",
            "adoption",
            "validation",
        ):
            if not isinstance(backend.get(field), str) or not backend[field].strip():
                fail(f".codex/capability_registry.json: backend {backend_id} is missing {field}")
        credentials = backend.get("credentials")
        if not isinstance(credentials, list) or not all(
            isinstance(item, str) and item.strip() for item in credentials
        ):
            fail(f".codex/capability_registry.json: backend {backend_id} credentials must be strings")
    capabilities = capability_registry.get("capabilities")
    capability_ids: set[str] = set()
    owner_skills: set[str] = set()
    expected_registered = expected_count("expected_registered_execution_capabilities")
    if not isinstance(capabilities, list):
        fail(".codex/capability_registry.json: capabilities must be a list")
        capabilities = []
    elif expected_registered is None:
        fail("local_config.yaml: expected_registered_execution_capabilities is missing")
    elif len(capabilities) != expected_registered:
        fail(
            ".codex/capability_registry.json: capability count is "
            f"{len(capabilities)}, expected {expected_registered}"
        )
    for capability in capabilities:
        if not isinstance(capability, dict):
            fail(".codex/capability_registry.json: every capability must be an object")
            continue
        capability_id = capability.get("id")
        owner = capability.get("owner_skill")
        if not isinstance(capability_id, str) or not capability_id:
            fail(".codex/capability_registry.json: capability is missing id")
            continue
        if capability_id in capability_ids:
            fail(f".codex/capability_registry.json: duplicate capability id {capability_id}")
        capability_ids.add(capability_id)
        if owner not in known_skill_names:
            fail(
                f".codex/capability_registry.json: capability {capability_id} "
                f"references unknown owner Skill {owner}"
            )
            continue
        if owner in owner_skills:
            fail(f".codex/capability_registry.json: duplicate owner Skill {owner}")
        owner_skills.add(owner)
        if capability.get("maturity") not in expected_maturity_levels:
            fail(f".codex/capability_registry.json: capability {capability_id} has invalid maturity")
        for field in ("deliverable",):
            if not isinstance(capability.get(field), str) or not capability[field].strip():
                fail(f".codex/capability_registry.json: capability {capability_id} is missing {field}")
        stop_conditions = capability.get("stop_conditions")
        if not isinstance(stop_conditions, list) or not stop_conditions:
            fail(f".codex/capability_registry.json: capability {capability_id} needs stop_conditions")
        for route_field in ("preferred_backends", "optional_backends"):
            routes = capability.get(route_field, [])
            if not isinstance(routes, list):
                fail(
                    f".codex/capability_registry.json: capability {capability_id} "
                    f"{route_field} must be a list"
                )
                continue
            for route in routes:
                if not isinstance(route, dict) or route.get("backend") not in backend_ids:
                    fail(
                        f".codex/capability_registry.json: capability {capability_id} "
                        f"has an unknown {route_field} backend"
                    )
        owner_skill_text = (SKILLS / owner / "SKILL.md").read_text(encoding="utf-8")
        if "../../capability_registry.json" not in owner_skill_text or capability_id not in owner_skill_text:
            fail(
                f"{(SKILLS / owner / 'SKILL.md').relative_to(ROOT)}: "
                f"does not route directly to registry capability {capability_id}"
            )
    if owner_skills != registered_owner_skills:
        fail(
            ".codex/capability_registry.json: owner Skill set mismatch; "
            f"missing={sorted(registered_owner_skills - owner_skills)}, "
            f"extra={sorted(owner_skills - registered_owner_skills)}"
        )

if not ROUTING_FORWARD_TEST.is_file():
    fail("routing forward-test record is missing")
else:
    with ROUTING_FORWARD_TEST.open(encoding="utf-8", newline="") as handle:
        routing_rows = list(csv.DictReader(handle, delimiter="\t"))
    required_routing_fields = {
        "case_id",
        "group",
        "query",
        "expected",
        "observed",
        "runtime",
        "date",
        "pass",
    }
    if not routing_rows or set(routing_rows[0]) != required_routing_fields:
        fail("routing forward-test record has an invalid header")
    if expected_skills is not None and len(routing_rows) != expected_skills:
        fail(
            f"routing forward-test record has {len(routing_rows)} rows, "
            f"expected {expected_skills}"
        )
    routing_ids = [row.get("case_id", "") for row in routing_rows]
    if len(routing_ids) != len(set(routing_ids)):
        fail("routing forward-test record contains duplicate case IDs")
    for row in routing_rows:
        case_id = row.get("case_id", "unknown")
        if row.get("expected") not in known_skill_names:
            fail(f"routing forward-test {case_id}: expected route is not a source Skill")
        if row.get("observed") not in known_skill_names:
            fail(f"routing forward-test {case_id}: observed route is not a source Skill")
        if row.get("pass") not in {"true", "false"}:
            fail(f"routing forward-test {case_id}: pass must be true or false")
        if (row.get("expected") == row.get("observed")) != (row.get("pass") == "true"):
            fail(f"routing forward-test {case_id}: pass does not match expected/observed")

if not ROUTING_MIXED_BASELINE.is_file():
    fail("docs/ROUTING_MIXED_BLIND_BASELINE_2026-07-28.tsv is missing")
else:
    with ROUTING_MIXED_BASELINE.open(encoding="utf-8", newline="") as handle:
        baseline_routing_rows = list(csv.DictReader(handle, delimiter="\t"))
    expected_baseline_fields = {
        "case_id",
        "query",
        "original_expected",
        "observed_a",
        "observed_b",
        "agreement",
        "a_match",
        "b_match",
    }
    if not baseline_routing_rows or set(baseline_routing_rows[0]) != expected_baseline_fields:
        fail("mixed blind routing baseline has an invalid header")
    if len(baseline_routing_rows) != 38:
        fail("mixed blind routing baseline must contain exactly 38 cases")
    baseline_ids = [row.get("case_id", "") for row in baseline_routing_rows]
    if len(baseline_ids) != len(set(baseline_ids)):
        fail("mixed blind routing baseline contains duplicate case IDs")
    baseline_a_matches = 0
    baseline_b_matches = 0
    baseline_agreements = 0
    stable_baseline_mismatches = 0
    for row in baseline_routing_rows:
        case_id = row.get("case_id", "unknown")
        if not all(row.get(field, "").strip() for field in expected_baseline_fields):
            fail(f"mixed blind routing baseline {case_id}: field is missing")
        agreement = row.get("observed_a") == row.get("observed_b")
        a_match = row.get("observed_a") == row.get("original_expected")
        b_match = row.get("observed_b") == row.get("original_expected")
        baseline_a_matches += int(a_match)
        baseline_b_matches += int(b_match)
        baseline_agreements += int(agreement)
        stable_baseline_mismatches += int(agreement and not a_match)
        for field, actual in (
            ("agreement", agreement),
            ("a_match", a_match),
            ("b_match", b_match),
        ):
            if row.get(field) != str(actual).lower():
                fail(f"mixed blind routing baseline {case_id}: {field} is inconsistent")
    if (
        baseline_a_matches,
        baseline_b_matches,
        baseline_agreements,
        stable_baseline_mismatches,
    ) != (21, 20, 34, 14):
        fail(
            "mixed blind routing baseline metrics must preserve raw "
            "21/38, 20/38, 34/38 agreement and 14 stable mismatches"
        )

if not ROUTING_MIXED_BLIND_TEST.is_file():
    fail("docs/ROUTING_MIXED_BLIND_TEST_2026-07-28.tsv is missing")
else:
    with ROUTING_MIXED_BLIND_TEST.open(encoding="utf-8", newline="") as handle:
        mixed_routing_rows = list(csv.DictReader(handle, delimiter="\t"))
    expected_mixed_fields = {
        "case_id",
        "query",
        "expected",
        "observed_a",
        "observed_b",
        "agreement",
        "a_match",
        "b_match",
        "adjudication",
    }
    if not mixed_routing_rows or set(mixed_routing_rows[0]) != expected_mixed_fields:
        fail("mixed blind routing record has an invalid header")
    if len(mixed_routing_rows) != 38:
        fail("mixed blind routing record must contain exactly 38 cases")
    mixed_ids = [row.get("case_id", "") for row in mixed_routing_rows]
    if len(mixed_ids) != len(set(mixed_ids)):
        fail("mixed blind routing record contains duplicate case IDs")
    allowed_routes = known_skill_names | {"none"}
    for row in mixed_routing_rows:
        case_id = row.get("case_id", "unknown")
        if not row.get("query", "").strip() or not row.get("adjudication", "").strip():
            fail(f"mixed blind routing {case_id}: query/adjudication is missing")
        for field in ("expected", "observed_a", "observed_b"):
            if row.get(field) not in allowed_routes:
                fail(f"mixed blind routing {case_id}: invalid {field} route")
        agreement = row.get("observed_a") == row.get("observed_b")
        a_match = row.get("observed_a") == row.get("expected")
        b_match = row.get("observed_b") == row.get("expected")
        for field, actual in (
            ("agreement", agreement),
            ("a_match", a_match),
            ("b_match", b_match),
        ):
            if row.get(field) != str(actual).lower():
                fail(f"mixed blind routing {case_id}: {field} does not match routes")
    mixed_a_matches = sum(row.get("a_match") == "true" for row in mixed_routing_rows)
    mixed_b_matches = sum(row.get("b_match") == "true" for row in mixed_routing_rows)
    mixed_agreements = sum(row.get("agreement") == "true" for row in mixed_routing_rows)
    if (mixed_a_matches, mixed_b_matches, mixed_agreements) != (36, 38, 36):
        fail("post-fix mixed blind routing metrics must remain 36/38, 38/38, agreement 36/38")

if not ROUTING_MIXED_PROTOCOL.is_file():
    fail("docs/ROUTING_MIXED_BLIND_PROTOCOL_2026-07-28.md is missing")
else:
    routing_protocol_text = ROUTING_MIXED_PROTOCOL.read_text(encoding="utf-8")
    for required_text in (
        "32b5e2e41a48964d8cdad08b1293d6a54f644606",
        "21/38",
        "20/38",
        "14",
        "36/38",
        "38/38",
        "B28",
    ):
        if required_text not in routing_protocol_text:
            fail(f"mixed blind routing protocol is missing provenance: {required_text}")

agent_files = sorted(AGENTS.glob("*.toml"))
agent_names: set[str] = set()
agent_modes: dict[str, str] = {}
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
        if data.get("sandbox_mode") in {"read-only", "workspace-write"}:
            agent_modes[name] = data["sandbox_mode"]
    if data.get("sandbox_mode") not in {"read-only", "workspace-write"}:
        fail(f"{agent_file.relative_to(ROOT)}: sandbox_mode must be read-only or workspace-write")

expected_agents = expected_count("expected_custom_agent_count")
if expected_agents is None:
    fail("local_config.yaml: expected_custom_agent_count is missing")
elif len(agent_files) != expected_agents:
    fail(f"custom Agent count is {len(agent_files)}, expected {expected_agents}")

if not AGENT_ROUTING_EVALS.is_file():
    fail(".codex/agents/evals/agent-routing-evals.json is missing")
else:
    try:
        agent_eval_data = json.loads(AGENT_ROUTING_EVALS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f".codex/agents/evals/agent-routing-evals.json is invalid JSON: {exc}")
        agent_eval_data = {}
    if agent_eval_data.get("schema_version") != 1:
        fail("Agent routing eval schema_version must be 1")
    agent_cases = agent_eval_data.get("cases")
    if not isinstance(agent_cases, list) or len(agent_cases) != 18:
        fail("Agent routing evals must contain exactly 18 cases")
        agent_cases = []
    agent_case_ids: set[str] = set()
    positive_agent_counts = {name: 0 for name in agent_names}
    for index, case in enumerate(agent_cases):
        if not isinstance(case, dict):
            fail(f"Agent routing eval case {index} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            fail(f"Agent routing eval case {index} is missing id")
        elif case_id in agent_case_ids:
            fail(f"Agent routing eval contains duplicate id: {case_id}")
        else:
            agent_case_ids.add(case_id)
        for field in ("query", "expected_agent", "expected_sandbox_mode", "rationale"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                fail(f"Agent routing eval {case_id or index} is missing {field}")
        expected_agent = case.get("expected_agent")
        should_delegate = case.get("should_delegate")
        if not isinstance(should_delegate, bool):
            fail(f"Agent routing eval {case_id or index}: should_delegate must be boolean")
        if should_delegate:
            if expected_agent not in agent_names:
                fail(f"Agent routing eval {case_id or index}: unknown expected Agent")
            else:
                positive_agent_counts[expected_agent] += 1
                if case.get("expected_sandbox_mode") != agent_modes.get(expected_agent):
                    fail(
                        f"Agent routing eval {case_id or index}: sandbox mode does not "
                        "match the Agent definition"
                    )
        elif (
            expected_agent != "none"
            or case.get("expected_sandbox_mode") != "none"
        ):
            fail(
                f"Agent routing eval {case_id or index}: non-delegated case must use none"
            )
    for agent_name, count in positive_agent_counts.items():
        if count < 2:
            fail(f"Agent routing evals need at least two positive cases for {agent_name}")

if not AGENT_ROUTING_FORWARD_TEST.is_file():
    fail("docs/AGENT_ROUTING_FORWARD_TEST_2026-07-28.tsv is missing")
else:
    with AGENT_ROUTING_FORWARD_TEST.open(encoding="utf-8", newline="") as handle:
        agent_forward_rows = list(csv.DictReader(handle, delimiter="\t"))
    expected_agent_forward_fields = {
        "case_id",
        "query",
        "expected",
        "observed_a",
        "observed_b",
        "agreement",
        "a_match",
        "b_match",
    }
    if not agent_forward_rows or set(agent_forward_rows[0]) != expected_agent_forward_fields:
        fail("custom Agent routing forward-test has an invalid header")
    if len(agent_forward_rows) != 18:
        fail("custom Agent routing forward-test must contain exactly 18 cases")
    forward_by_id = {row.get("case_id", ""): row for row in agent_forward_rows}
    if len(forward_by_id) != len(agent_forward_rows):
        fail("custom Agent routing forward-test contains duplicate case IDs")
    eval_by_id = {
        case.get("id"): case for case in agent_cases if isinstance(case, dict)
    }
    if set(forward_by_id) != set(eval_by_id):
        fail("custom Agent routing forward-test IDs do not match the static eval set")
    for case_id, row in forward_by_id.items():
        static_case = eval_by_id[case_id]
        static_expected = static_case.get("expected_agent")
        if row.get("query") != static_case.get("query") or row.get("expected") != static_expected:
            fail(f"custom Agent routing forward-test {case_id}: query/expected drift")
        for field in ("observed_a", "observed_b"):
            if row.get(field) not in agent_names | {"none"}:
                fail(f"custom Agent routing forward-test {case_id}: invalid {field}")
        agreement = row.get("observed_a") == row.get("observed_b")
        a_match = row.get("observed_a") == row.get("expected")
        b_match = row.get("observed_b") == row.get("expected")
        for field, actual in (
            ("agreement", agreement),
            ("a_match", a_match),
            ("b_match", b_match),
        ):
            if row.get(field) != str(actual).lower():
                fail(f"custom Agent routing forward-test {case_id}: {field} is inconsistent")
    if not all(
        row.get("agreement") == row.get("a_match") == row.get("b_match") == "true"
        for row in agent_forward_rows
    ):
        fail("custom Agent routing forward-test must preserve the reviewed 18/18 result")

if not AGENT_ROUTING_FORWARD_PROTOCOL.is_file():
    fail("docs/AGENT_ROUTING_FORWARD_PROTOCOL_2026-07-28.md is missing")
else:
    agent_forward_protocol = AGENT_ROUTING_FORWARD_PROTOCOL.read_text(encoding="utf-8")
    for required_text in ("18/18", "workspace-write", "read-only", "`none`", "not exposed"):
        if required_text not in agent_forward_protocol:
            fail(f"custom Agent routing protocol is missing provenance: {required_text}")

curator = AGENTS / "capability-curator.toml"
if not curator.is_file():
    fail(".codex/agents/capability-curator.toml is missing")
else:
    with curator.open("rb") as handle:
        curator_data = tomllib.load(handle)
    if curator_data.get("sandbox_mode") != "read-only":
        fail("capability-curator must be read-only")

self_improvement = SKILLS / "controlled-self-improvement"
for required in (
    self_improvement / "SKILL.md",
    self_improvement / "agents" / "openai.yaml",
    self_improvement / "references" / "lifecycle-and-governance.md",
    self_improvement / "assets" / "improvement-candidate.md",
):
    if not required.is_file():
        fail(f"{required.relative_to(ROOT)} is missing")

if not GLOBAL_GUIDANCE.is_file():
    fail("templates/global-AGENTS.md is missing")
else:
    guidance_text = GLOBAL_GUIDANCE.read_text(encoding="utf-8")
    if len(guidance_text) > 6000:
        fail("templates/global-AGENTS.md exceeds the 6000-character context budget")
    if guidance_text.count("## Controlled self-improvement") != 1:
        fail("templates/global-AGENTS.md must contain one Controlled self-improvement section")
    controlled_section = guidance_text.split("## Controlled self-improvement", 1)[1].split("## ", 1)[0]
    controlled_rules = [line for line in controlled_section.splitlines() if line.startswith("- ")]
    if len(controlled_rules) != 5:
        fail("Controlled self-improvement section must contain exactly five rules")
    for required_text in (
        "Agent 只采用两层",
        "~/.agents/skills",
        "data/raw",
        "reports/figures/",
        "reports/source_data/",
        "research-data-organization",
    ):
        if required_text not in guidance_text:
            fail(f"templates/global-AGENTS.md is missing required global layout rule: {required_text}")

installer_text = (ROOT / "scripts" / "install_codex_bioinfo.py").read_text(encoding="utf-8")
if "--retire-legacy-codex-skills" not in installer_text:
    fail("installer is missing the explicit legacy ~/.codex/skills retirement option")

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
    r"(?:(?:/" + r"Users|/home)/[A-Za-z0-9._-]+(?:/|\b)|"
    + r"[A-Za-z]:\\Users\\[A-Za-z0-9._-]+(?:\\|\b)|Extreme "
    + r"SSD)"
)
secret_pattern = re.compile(
    "(?:github"
    + r"_pat_[A-Za-z0-9_]{20,}|gh"
    + r"[pousr]_[A-Za-z0-9]{20,}|sk-"
    + r"(?:proj-)?[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|"
    + r"xox[baprs]-[A-Za-z0-9-]{10,}|glpat-[A-Za-z0-9_-]{16,}|"
    + r"hf_[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|"
    + r"BEGIN [A-Z ]*PRIVATE KEY)"
)
generic_secret_assignment = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|service[_-]?token|"
    r"client[_-]?secret|password|secret)\b\s*[:=]\s*['\"]?"
    r"[A-Za-z0-9_./+=-]{16,}"
)
blocked_data_suffixes = {
    ".bam",
    ".bai",
    ".bcf",
    ".cram",
    ".fast5",
    ".fastq",
    ".fq",
    ".h5ad",
    ".loom",
    ".pdb",
    ".rds",
    ".sam",
    ".sdf",
    ".vcf",
}
blocked_runtime_parts = {
    "cache",
    "caches",
    "log",
    "logs",
    "memory",
    "memories",
    "session",
    "sessions",
}
blocked_runtime_suffixes = {".db", ".db3", ".log", ".sqlite", ".sqlite3"}
blocked_runtime_filenames = {
    "auth.json",
    "history.jsonl",
    "project_environment.md",
    "project_environment.local.md",
}
blocked_secret_filenames = {
    "credentials.json",
    "secrets.json",
    "secrets.yaml",
    "secrets.yml",
}
blocked_secret_suffixes = {".key", ".pem", ".p12", ".pfx"}
max_public_file_bytes = 5 * 1024 * 1024
local_candidate_root = ROOT / ".codex" / "candidates"
ignore_local_candidates = False
if local_candidate_root.exists():
    tracked_candidates = subprocess.run(
        ["git", "ls-files", "--", ".codex/candidates"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if (
        REPOSITORY_ROOT is not None
        and tracked_candidates.returncode == 0
        and not tracked_candidates.stdout.strip()
    ):
        ignore_local_candidates = True
    else:
        fail(
            ".codex/candidates may exist only as an untracked local worktree area; "
            "it is not part of a portable archive or release"
        )
for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    relative = path.relative_to(ROOT)
    if ignore_local_candidates and relative.parts[:2] == (".codex", "candidates"):
        continue
    if path.is_symlink():
        link_target = os.readlink(path)
        if relative != Path(".agents/skills") or link_target != "../.codex/skills":
            fail(f"{relative}: unexpected symlink target is not allowed in the portable package")
        continue
    if not path.is_file():
        continue
    if path.suffix.lower() in blocked_data_suffixes:
        fail(f"{relative}: raw/research data file type is not allowed in the portable package")
    if any(part.lower() in blocked_runtime_parts for part in relative.parts):
        fail(f"{relative}: native memory/session/cache/log path is not allowed in the portable package")
    if path.suffix.lower() in blocked_runtime_suffixes:
        fail(f"{relative}: runtime database/log file type is not allowed in the portable package")
    if path.name.lower() in blocked_runtime_filenames:
        fail(f"{relative}: machine-local runtime/environment record is not allowed in the portable package")
    lower_name = path.name.lower()
    if (
        lower_name == ".env"
        or lower_name.startswith(".env.")
        or lower_name in blocked_secret_filenames
        or path.suffix.lower() in blocked_secret_suffixes
    ):
        fail(f"{relative}: credential-bearing filename or file type is not allowed")
    size = path.stat().st_size
    if size > max_public_file_bytes:
        fail(f"{relative}: file exceeds the 5 MiB portable-package limit")
        continue
    content = path.read_bytes()
    if b"\0" in content:
        continue
    text = content.decode("utf-8", errors="replace")
    if private_path.search(text):
        fail(f"{relative}: contains a private machine path")
    if secret_pattern.search(text):
        fail(f"{relative}: contains a high-risk secret pattern")
    if generic_secret_assignment.search(text):
        fail(f"{relative}: contains a generic secret assignment")

root_agent_text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
if "Hermes" in root_agent_text:
    fail("AGENTS.md still contains a Hermes runtime dependency")
if "controlled-self-improvement" not in root_agent_text:
    fail("AGENTS.md does not route governed capability evolution to controlled-self-improvement")

license_file = ROOT / "LICENSE"
notice_file = ROOT / "NOTICE.md"
if not license_file.is_file():
    fail("LICENSE is missing")
elif "No permission is granted" not in license_file.read_text(encoding="utf-8"):
    fail("LICENSE must state the package-wide permission boundary")
if not notice_file.is_file():
    fail("NOTICE.md is missing")
else:
    notice_text = notice_file.read_text(encoding="utf-8")
    if "third-party" not in notice_text.lower():
        fail("NOTICE.md must state third-party provenance handling")
    if "Historical provenance: RECONSTRUCTED; OWNER-SYNC MAIN AUTHORIZED" not in notice_text:
        fail("NOTICE.md must preserve reconstructed provenance and owner-sync main scope")
    if "owner-authorized canonical `main`" not in notice_text:
        fail("NOTICE.md must distinguish owner installation from external reuse")
if "release_status: stable_owner_sync_not_open_source_reuse" not in manifest_text:
    fail("local_config.yaml must preserve the owner-sync and no-open-reuse boundary")
external_provenance = ROOT / "docs" / "EXTERNAL_SOURCE_PROVENANCE.md"
if not external_provenance.is_file():
    fail("docs/EXTERNAL_SOURCE_PROVENANCE.md is missing")
else:
    provenance_text = external_provenance.read_text(encoding="utf-8")
    for required_text in (
        "ClawBio/ClawBio",
        "GPTomics/bioSkills",
        "google-deepmind/science-skills",
        "Future-House/robin",
        "CC-BY-4.0",
        "no executable wrapper copied",
    ):
        if required_text not in provenance_text:
            fail(f"external provenance record is missing: {required_text}")

lineage_rows: list[dict[str, str]] = []
required_lineage_fields = {
    "target_path",
    "local_commits",
    "current_state",
    "source_id",
    "upstream_ref",
    "upstream_path",
    "decision",
    "derivation",
    "vendored",
    "license",
    "obligation",
    "review_evidence",
}
if not EXTERNAL_LINEAGE.is_file():
    fail("docs/EXTERNAL_FILE_LINEAGE.tsv is missing")
else:
    with EXTERNAL_LINEAGE.open(encoding="utf-8", newline="") as handle:
        lineage_rows = list(csv.DictReader(handle, delimiter="\t"))
    if not lineage_rows or set(lineage_rows[0]) != required_lineage_fields:
        fail("external file lineage has an invalid header")
    targets = [row.get("target_path", "") for row in lineage_rows]
    if len(lineage_rows) != 62 or len(targets) != len(set(targets)):
        fail("external file lineage must contain exactly 62 unique historical target paths")
    target_digest = hashlib.sha256(
        ("\n".join(sorted(targets)) + "\n").encode("utf-8")
    ).hexdigest()
    if target_digest != EXPECTED_LINEAGE_PATH_HASH:
        fail("external file lineage target-path set does not match the reviewed historical set")
    for row in lineage_rows:
        target = row.get("target_path", "")
        state = row.get("current_state")
        for field in required_lineage_fields:
            if not row.get(field, "").strip():
                fail(f"external file lineage {target or 'unknown'}: missing {field}")
        if state not in {"current", "tombstone"}:
            fail(f"external file lineage {target}: current_state must be current or tombstone")
        target_exists = (ROOT / target).exists()
        if state == "current" and not target_exists:
            fail(f"external file lineage {target}: current path is missing")
        if state == "tombstone" and target_exists:
            fail(f"external file lineage {target}: tombstone path still exists")
        if row.get("vendored") != "no":
            fail(f"external file lineage {target}: vendored content is not allowed")
        if row.get("license") == "unknown" and row.get("decision") not in {
            "reference-only",
            "reject",
        }:
            fail(f"external file lineage {target}: unknown-license material cannot be absorbed")
        material = row.get("source_id") not in {
            "project-owned",
            "historical-audit-corpus",
        }
        if material:
            source_ids = set(row.get("source_id", "").split(";"))
            refs = row.get("upstream_ref", "").split(";")
            if not refs or any(
                re.fullmatch(r"[a-z0-9-]+=[0-9a-f]{40}", item) is None
                for item in refs
            ):
                fail(f"external file lineage {target}: material refs must use source=full-40-char-SHA")
            ref_keys = {item.split("=", 1)[0] for item in refs if "=" in item}
            paths = row.get("upstream_path", "").split(";")
            if not paths or any(
                re.fullmatch(r"[a-z0-9-]+=[^\t;]+", item) is None
                for item in paths
            ):
                fail(f"external file lineage {target}: upstream paths must use source=path")
            path_keys = {item.split("=", 1)[0] for item in paths if "=" in item}
            if ref_keys != source_ids or path_keys != source_ids:
                fail(
                    f"external file lineage {target}: source, ref and path keys must cover "
                    "the same source IDs"
                )
            if row.get("upstream_path") == "n/a" or row.get("license") in {"n/a", "unknown"}:
                fail(f"external file lineage {target}: material source/path/license is incomplete")
            if "THIRD_PARTY_NOTICES.md" not in row.get("obligation", ""):
                fail(f"external file lineage {target}: material row lacks notice handling")
        if any(
            marker in row.get("derivation", "").lower()
            for marker in ("adapted", "verbatim", "copied code")
        ) and "THIRD_PARTY_NOTICES.md" not in row.get("obligation", ""):
            fail(f"external file lineage {target}: adapted/verbatim/code row lacks notice handling")
        if "bionemo" in row.get("source_id", ""):
            if "CC-BY-4.0" not in row.get("license", ""):
                fail(f"external file lineage {target}: BioNeMo content license must be CC-BY-4.0")
            if "THIRD_PARTY_NOTICES.md" not in row.get("obligation", ""):
                fail(f"external file lineage {target}: BioNeMo attribution/change notice is missing")

    if REPOSITORY_ROOT is not None:
        historical_targets: set[str] = set()
        history_complete = True
        for commit in ABSORPTION_COMMITS:
            result = subprocess.run(
                [
                    "git",
                    "diff-tree",
                    "--no-commit-id",
                    "--name-only",
                    "-r",
                    commit,
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            if result.returncode != 0:
                history_complete = False
                message = f"cannot inspect historical absorption commit {commit}"
                if REQUIRE_HISTORY:
                    fail(message)
                else:
                    warnings.append(
                        message
                        + "; frozen 62-row lineage path hash remains the portable check"
                    )
                continue
            historical_targets.update(line for line in result.stdout.splitlines() if line)
        if history_complete and historical_targets != set(targets):
            missing = sorted(historical_targets - set(targets))
            extra = sorted(set(targets) - historical_targets)
            fail(f"external lineage/history mismatch; missing={missing}, extra={extra}")
    elif REQUIRE_HISTORY:
        fail("--require-history needs a Git worktree with the reviewed absorption commits")
    else:
        warnings.append(
            "Git history unavailable; frozen 62-row lineage path hash remains the portable check"
        )

post_baseline_rows: list[dict[str, str]] = []
expected_post_baseline_targets = {
    path.relative_to(ROOT).as_posix()
    for path in (SKILLS / "research-discovery-orchestration").rglob("*")
    if path.is_file()
}
if not POST_BASELINE_LINEAGE.is_file():
    fail("docs/EXTERNAL_FILE_LINEAGE_POST_BASELINE.tsv is missing")
else:
    with POST_BASELINE_LINEAGE.open(encoding="utf-8", newline="") as handle:
        post_baseline_rows = list(csv.DictReader(handle, delimiter="\t"))
    if not post_baseline_rows or set(post_baseline_rows[0]) != required_lineage_fields:
        fail("post-baseline external file lineage has an invalid header")
    post_targets = [row.get("target_path", "") for row in post_baseline_rows]
    if len(post_targets) != len(set(post_targets)):
        fail("post-baseline external file lineage has duplicate target paths")
    if set(post_targets) != expected_post_baseline_targets:
        missing = sorted(expected_post_baseline_targets - set(post_targets))
        extra = sorted(set(post_targets) - expected_post_baseline_targets)
        fail(
            "post-baseline external lineage does not cover the complete active "
            f"research-discovery-orchestration Skill; missing={missing}, extra={extra}"
        )
    for row in post_baseline_rows:
        target = row.get("target_path", "")
        for field in required_lineage_fields:
            if not row.get(field, "").strip():
                fail(f"post-baseline external lineage {target or 'unknown'}: missing {field}")
        if row.get("current_state") != "current" or not (ROOT / target).is_file():
            fail(f"post-baseline external lineage {target}: active file is missing")
        if row.get("vendored") != "no":
            fail(f"post-baseline external lineage {target}: vendored content is not allowed")
        if row.get("source_id") == "robin":
            if (
                row.get("upstream_ref")
                != "robin=4a5cce310f3bc7663a67117db88af43b84733ffe"
            ):
                fail(f"post-baseline external lineage {target}: Robin ref must be pinned")
            if not row.get("upstream_path", "").startswith("robin="):
                fail(f"post-baseline external lineage {target}: Robin path is missing")
            if row.get("license") != "Apache-2.0":
                fail(f"post-baseline external lineage {target}: Robin license is incorrect")
            if "THIRD_PARTY_NOTICES.md" not in row.get("obligation", ""):
                fail(f"post-baseline external lineage {target}: notice handling is missing")
        elif row.get("source_id") != "project-owned":
            fail(f"post-baseline external lineage {target}: unsupported source_id")

if not EXPRESSION_REVIEW.is_file():
    fail("docs/EXTERNAL_EXPRESSION_REVIEW_2026-07-25.tsv is missing")
else:
    with EXPRESSION_REVIEW.open(encoding="utf-8", newline="") as handle:
        expression_rows = list(csv.DictReader(handle, delimiter="\t"))
    required_expression_fields = {
        "local_path",
        "source_id",
        "upstream_ref",
        "upstream_path",
        "method",
        "shared_40_char_shingles",
        "shared_lines_ge_35",
        "result",
    }
    if not expression_rows or set(expression_rows[0]) != required_expression_fields:
        fail("external expression review has an invalid header")
    if len(expression_rows) != 19:
        fail("external expression review must preserve the 19 retrieved comparison pairs")
    expression_local_paths = {row.get("local_path", "") for row in expression_rows}
    if len(expression_local_paths) != 8:
        fail("external expression review must cover eight unique current Skill bodies")
    for row in expression_rows:
        if not (ROOT / row.get("local_path", "")).is_file():
            fail(f"expression review local path is missing: {row.get('local_path')}")
        if re.fullmatch(r"[0-9a-f]{40}", row.get("upstream_ref", "")) is None:
            fail(f"expression review ref is not a full SHA: {row.get('upstream_ref')}")
        if (
            row.get("shared_40_char_shingles") != "0"
            or row.get("shared_lines_ge_35") != "0"
            or row.get("result") != "pass"
        ):
            fail(f"expression review pair is not a zero-match pass: {row.get('upstream_path')}")

if not THIRD_PARTY_NOTICES.is_file():
    fail("THIRD_PARTY_NOTICES.md is missing")
else:
    third_party_text = THIRD_PARTY_NOTICES.read_text(encoding="utf-8")
    for required_text in (
        "NVIDIA CORPORATION & AFFILIATES",
        "CC-BY-4.0",
        "Apache-2.0",
        "historical short ref `0807ddb`",
        "reference-only and never a copy source",
        "Future-House/robin",
        "4a5cce310f3bc7663a67117db88af43b84733ffe",
    ):
        if required_text not in third_party_text:
            fail(f"third-party notices are missing: {required_text}")

if external_provenance.is_file():
    provenance_text = external_provenance.read_text(encoding="utf-8")
    full_shas = {
        "fbb0910761ab12a9a403060d04248e155b862437",
        "c8d403984b1f35c14861b0064d24695f82d44904",
        "33557e0f1faf0f281d255940de58935c61b2143b",
        "54fc67cd87b240f98ffc3223268c77c5eae6e028",
        "59dd63374314baa2fb1f9864f190775bd7466647",
        "ca695e1b89ea48613291c88bd8c73e71af2025c7",
        "af29cdd0201fd9158f140adcda24bc8b2506d246",
        "aba7c4e9695c363e65cb59effe926c7f1d1abe3d",
        "896224c4b1879920ab573417e68fd51d2ccc9072",
        "175cee7c25b5d98d919369f53427c646cdd86d93",
        "4a5cce310f3bc7663a67117db88af43b84733ffe",
    }
    for full_sha in full_shas:
        if full_sha not in provenance_text:
            fail(f"external provenance record is missing full SHA: {full_sha}")
    for required_text in (
        "historical short ref `0807ddb`",
        "Reference-only because the exact audited object cannot be revalidated",
        "Skill/docs/content CC-BY-4.0; code Apache-2.0",
        "Five initially unavailable path guesses were corrected",
        "repository owner's explicit authorization of",
        "canonical `main`",
        "`nature-skills` is reference-only",
    ):
        if required_text not in provenance_text:
            fail(f"external provenance exception/boundary is missing: {required_text}")

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
    "static eval schemas, discovery link, manifest counts, and privacy gates validated"
)
