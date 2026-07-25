#!/usr/bin/env python3
"""Validate one execution-backend run record against the capability registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / ".codex" / "capability_registry.json"
STATUSES = {"planned", "blocked", "validated", "completed", "failed"}
ACTIONS = {"install", "credentials", "api_quota", "data_upload"}
FLOATING_REFS = {"latest", "main", "master", "dev", "head", "current"}


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def capability_backends(capability: dict[str, Any]) -> set[str]:
    routes = [
        *capability.get("preferred_backends", []),
        *capability.get("optional_backends", []),
    ]
    return {route.get("backend") for route in routes if route.get("backend")}


def validate_record(
    record: dict[str, Any], registry: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    if record.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    capability_id = record.get("capability_id")
    capabilities = {
        item.get("id"): item
        for item in registry.get("capabilities", [])
        if isinstance(item, dict)
    }
    capability = capabilities.get(capability_id)
    if capability is None:
        errors.append(f"unknown capability_id: {capability_id}")

    backend_id = record.get("backend_id")
    backends = {
        item.get("id")
        for item in registry.get("backends", [])
        if isinstance(item, dict)
    }
    if backend_id not in backends:
        errors.append(f"unknown backend_id: {backend_id}")
    if capability is not None and backend_id not in capability_backends(capability):
        errors.append(
            f"backend {backend_id} is not routed by capability {capability_id}"
        )

    backend_ref = str(record.get("backend_ref", "")).strip()
    if not backend_ref:
        errors.append("backend_ref is required")
    elif backend_ref.lower() in FLOATING_REFS or backend_ref.lower().endswith(
        ("/latest", "@latest")
    ):
        errors.append(f"backend_ref must be immutable or versioned: {backend_ref}")

    status = record.get("status")
    if status not in STATUSES:
        errors.append(f"invalid status: {status}")

    requested_actions = record.get("requested_actions")
    if not isinstance(requested_actions, list) or any(
        action not in ACTIONS for action in requested_actions
    ):
        errors.append("requested_actions must be a list of registered actions")
        requested_actions = []

    authorization = record.get("authorization")
    if not isinstance(authorization, dict):
        errors.append("authorization must be an object")
        authorization = {}
    for action in ACTIONS:
        if not isinstance(authorization.get(action), bool):
            errors.append(f"authorization.{action} must be boolean")
    unauthorized = [
        action for action in requested_actions if authorization.get(action) is not True
    ]

    execution_attempted = record.get("execution_attempted")
    if not isinstance(execution_attempted, bool):
        errors.append("execution_attempted must be boolean")
    if unauthorized and execution_attempted:
        errors.append(
            "execution_attempted must be false when requested actions lack authorization: "
            + ", ".join(sorted(unauthorized))
        )

    inputs = record.get("inputs")
    if not isinstance(inputs, list) or not inputs:
        errors.append("inputs must be a non-empty list")
        inputs = []
    missing_required = [
        item.get("id", "<unnamed>")
        for item in inputs
        if isinstance(item, dict)
        and item.get("required") is True
        and item.get("exists") is not True
    ]
    if missing_required and status in {"validated", "completed"}:
        errors.append(
            "validated/completed run has missing required inputs: "
            + ", ".join(missing_required)
        )

    provenance = record.get("provenance")
    if not isinstance(provenance, dict):
        errors.append("provenance must be an object")
        provenance = {}
    for field in ("command_or_query", "environment", "inputs", "outputs"):
        if not provenance.get(field):
            errors.append(f"provenance.{field} is required")

    checks = record.get("checks")
    if not isinstance(checks, list) or not checks:
        errors.append("checks must be a non-empty list")
        checks = []
    check_statuses = {
        item.get("status")
        for item in checks
        if isinstance(item, dict) and item.get("name")
    }
    if not check_statuses.issubset({"pass", "fail", "not_run"}):
        errors.append("check status must be pass, fail, or not_run")
    if status in {"validated", "completed"} and check_statuses != {"pass"}:
        errors.append("validated/completed run requires every recorded check to pass")

    artifacts = record.get("artifacts")
    if not isinstance(artifacts, dict):
        errors.append("artifacts must be an object")
        artifacts = {}
    if status == "completed":
        missing_artifacts = [
            name
            for name in ("manifest", "log", "source_data")
            if artifacts.get(name) is not True
        ]
        if missing_artifacts:
            errors.append(
                "completed run is missing required artifacts: "
                + ", ".join(missing_artifacts)
            )

    boundary = record.get("evidence_boundary")
    if not isinstance(boundary, dict):
        errors.append("evidence_boundary must be an object")
        boundary = {}
    for field in ("supported", "not_proven"):
        value = boundary.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"evidence_boundary.{field} must be a non-empty list")

    if status in {"blocked", "failed"}:
        if not str(record.get("stop_reason", "")).strip():
            errors.append(f"{status} record requires stop_reason")
        if status == "blocked" and execution_attempted is not False:
            errors.append("blocked record must not attempt execution")
    if status in {"validated", "completed"} and unauthorized:
        errors.append(
            "validated/completed run cannot retain unauthorized requested actions: "
            + ", ".join(sorted(unauthorized))
        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    args = parser.parse_args()
    try:
        record = load_json(args.record)
        registry = load_json(args.registry)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate_record(record, registry)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(
        f"PASS: {record['capability_id']} -> {record['backend_id']} "
        f"status={record['status']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
