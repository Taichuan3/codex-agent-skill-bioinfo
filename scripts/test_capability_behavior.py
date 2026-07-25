#!/usr/bin/env python3
"""Run de-identified behavior fixtures for capability-backend safety gates."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

from validate_capability_run import validate_record


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads(
    (ROOT / ".codex" / "capability_registry.json").read_text(encoding="utf-8")
)


def base_record(capability: str, backend: str, backend_ref: str) -> dict:
    return {
        "schema_version": 1,
        "capability_id": capability,
        "backend_id": backend,
        "backend_ref": backend_ref,
        "status": "blocked",
        "execution_attempted": False,
        "requested_actions": [],
        "authorization": {
            "install": False,
            "credentials": False,
            "api_quota": False,
            "data_upload": False,
        },
        "inputs": [{"id": "synthetic-input", "required": True, "exists": True}],
        "provenance": {
            "command_or_query": "preflight only",
            "environment": "isolated fixture",
            "inputs": ["synthetic-input"],
            "outputs": ["synthetic-result.json"],
        },
        "checks": [{"name": "preflight", "status": "pass"}],
        "artifacts": {"manifest": True, "log": True, "source_data": False},
        "evidence_boundary": {
            "supported": ["routing and stop behavior"],
            "not_proven": ["scientific validity"],
        },
        "stop_reason": "fixture stop condition",
    }


def require_pass(name: str, record: dict) -> None:
    errors = validate_record(record, REGISTRY)
    if errors:
        raise RuntimeError(f"{name} unexpectedly failed: {errors}")


def require_fail(name: str, record: dict, expected: str) -> None:
    errors = validate_record(record, REGISTRY)
    if not any(expected in error for error in errors):
        raise RuntimeError(f"{name} did not report {expected!r}: {errors}")


def main() -> int:
    alpha = base_record(
        "CAP-VAR-001",
        "google-deepmind-science-skills",
        "0b42509800f49e6eb7809505d96e20a890ef99bd",
    )
    alpha["stop_reason"] = "single-variant backend does not match a regional task"
    require_pass("method mismatch stops safely", alpha)

    ngs = base_record("CAP-RNA-001", "nf-core-nextflow", "nf-core/rnaseq@3.26.0")
    ngs["inputs"][0]["id"] = "fixture-fastq"
    ngs["inputs"][0]["exists"] = False
    ngs["stop_reason"] = "required FASTQ or runtime is missing"
    require_pass("missing NGS input blocks before execution", ngs)

    paperqa = base_record(
        "CAP-PAPER-001",
        "paperqa2",
        "paper-qa==2026.3.18",
    )
    paperqa["requested_actions"] = ["credentials"]
    paperqa["stop_reason"] = "no approved model endpoint"
    require_pass("missing model authority blocks before execution", paperqa)

    bad_missing_input = copy.deepcopy(ngs)
    bad_missing_input["status"] = "completed"
    bad_missing_input["execution_attempted"] = True
    bad_missing_input["artifacts"]["source_data"] = True
    require_fail(
        "completed run with missing input is rejected",
        bad_missing_input,
        "missing required inputs",
    )

    bad_authority = copy.deepcopy(paperqa)
    bad_authority["execution_attempted"] = True
    require_fail(
        "unauthorized model call is rejected",
        bad_authority,
        "lack authorization",
    )

    floating = base_record("CAP-RNA-001", "nf-core-nextflow", "latest")
    require_fail("floating backend ref is rejected", floating, "immutable or versioned")

    incomplete = base_record(
        "CAP-LIT-001", "openai-life-science-research", "plugin@1.0.3"
    )
    incomplete["status"] = "completed"
    incomplete["execution_attempted"] = True
    require_fail(
        "completed run without source data is rejected",
        incomplete,
        "missing required artifacts",
    )

    complete = copy.deepcopy(incomplete)
    complete["artifacts"]["source_data"] = True
    require_pass("complete bounded lookup record passes", complete)

    print("PASS: 8 capability routing and safe-stop behavior fixtures")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
