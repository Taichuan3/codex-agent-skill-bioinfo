#!/usr/bin/env python3
"""Read-only, bounded navigation metadata checks; not scientific validation."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

FIELDS = {"asset_id", "module_id", "scope", "label", "path", "status",
          "source_data", "producer", "command", "environment", "sha256"}
UNKNOWN = {"", "pending", "unknown", "not_assessed", "not_applicable", "n/a"}
STATUSES = {"current", "candidate", "planned", "exploring", "blocked", "failed",
            "accepted", "stopped", "historical", "superseded", "as_of_record",
            "provenance_pending", "unverified_remote", "reference", "referenced",
            "package_record", "archived"}


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def local_path(root: Path, value: str) -> Path | None:
    parsed = urlsplit(value)
    if parsed.scheme in {"https", "http"}:
        return None
    if parsed.scheme or parsed.netloc or "\\" in value:
        raise ValueError("not a portable project-relative path")
    path = Path(unquote(parsed.path))
    if path.is_absolute():
        raise ValueError("absolute path")
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("path escapes project")
    return resolved


def verify(root: Path, guide: str, registry: str, entries: list[str]) -> dict:
    root = root.resolve()
    errors, warnings = [], []
    checked = 0
    guide_stats = {}

    def check_path(value: str, label: str, expected: str = "") -> Path | None:
        nonlocal checked
        try:
            p = local_path(root, value)
            if p is None:
                warnings.append(f"{label}: unverified remote pointer (not fetched)")
                return None
            if not p.exists():
                errors.append(f"{label}: missing {value}")
                return None
            checked += 1
            if expected and expected.lower() not in UNKNOWN:
                if not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
                    errors.append(f"{label}: invalid SHA-256")
                elif not p.is_file() or digest(p) != expected.lower():
                    errors.append(f"{label}: hash mismatch {value}")
            return p
        except (ValueError, OSError) as exc:
            errors.append(f"{label}: {exc}")
            return None

    gp = check_path(guide, "GUIDE")
    if gp is None:
        errors.append("GUIDE must be a local readable file")
    if gp and not gp.is_file():
        errors.append("GUIDE must be a regular file")
    if gp and gp.is_file():
        try:
            content = gp.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"GUIDE read failed: {exc}")
            content = ""
        guide_stats = {"characters": len(content), "lines": len(content.splitlines())}
        if guide_stats["characters"] > 3000 or guide_stats["lines"] > 80:
            warnings.append("GUIDE exceeds compression warning budget; preserve caveats")
        if guide_stats["characters"] > 6000 or guide_stats["lines"] > 120:
            warnings.append("GUIDE exceeds legacy limit; repair or explicit exception required")
    for entry in entries:
        check_path(entry, "entry")
    rp = check_path(registry, "registry")
    if rp is None:
        errors.append("registry must be a local readable file")
    if rp and not rp.is_file():
        errors.append("registry must be a regular file")
    rows = []
    if rp and rp.is_file():
        try:
            with rp.open(encoding="utf-8-sig", newline="") as stream:
                reader = csv.DictReader(stream, delimiter="\t")
                header = reader.fieldnames or []
                missing = FIELDS - set(header)
                if len(header) != len(set(header)):
                    errors.append("registry duplicate headers")
                elif missing:
                    errors.append("registry missing fields: " + ", ".join(sorted(missing)))
                else:
                    rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"registry read failed: {exc}")
    if rp and not rows:
        warnings.append("registry has no validated rows")
    seen, current = set(), set()
    pending = {key: 0 for key in ("source_data", "producer", "command", "environment")}
    for i, row in enumerate(rows, 2):
        if None in row or any(value is None for value in row.values()):
            errors.append(f"row {i}: TSV column count mismatch")
            continue
        for field in ("asset_id", "module_id", "scope", "label", "path", "status"):
            if not row.get(field, "").strip() or row[field].strip().lower() in UNKNOWN:
                errors.append(f"row {i}: required field {field} is empty/unknown")
        label = row.get("asset_id", "")
        if not label or label in seen:
            errors.append(f"row {i}: empty or duplicate asset_id {label}")
        seen.add(label)
        status = row.get("status", "")
        if status not in STATUSES and not status.startswith("x-"):
            errors.append(f"{label}: unknown status; use documented x- extension")
        if row.get("status") == "current":
            key = tuple(row.get(k) for k in ("scope", "module_id", "label"))
            if key in current:
                errors.append(f"{label}: duplicate scoped current role")
            current.add(key)
        if row.get("path", "").lower() in UNKNOWN:
            errors.append(f"{label}: artifact path missing")
        else:
            check_path(row["path"], label, row.get("sha256", ""))
        for key in pending:
            value = row.get(key) or ""
            if value.lower() in UNKNOWN:
                pending[key] += 1
            elif key in {"source_data", "producer"}:
                for pointer in value.split(";"):
                    check_path(pointer.strip(), f"{label}.{key}")
    return {"metadata_valid": not errors, "scientific_validation": "not_performed",
            "guide": guide_stats, "rows": len(rows), "paths_checked": checked,
            "provenance_pending": pending, "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--guide", default="PROJECT_GUIDE.md")
    parser.add_argument("--registry", required=True, help="project-relative TSV")
    parser.add_argument("--entry", action="append", default=[])
    args = parser.parse_args()
    result = verify(args.root, args.guide, args.registry, args.entry)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["metadata_valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
