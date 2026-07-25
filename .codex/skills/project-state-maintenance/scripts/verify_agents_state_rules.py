#!/usr/bin/env python3
"""Ad-hoc verifier for AGENTS.md project-state / Directory Card rules.

Usage:
  python scripts/verify_agents_state_rules.py [--mode state|combined] /path/to/AGENTS.md

This is not a canonical test suite. State mode checks the hot/cold state-file
contract. Combined mode also checks Directory Card routing.
"""
from __future__ import annotations

from pathlib import Path
import sys


def main() -> int:
    args = sys.argv[1:]
    mode = "combined"
    if len(args) == 3 and args[0] == "--mode":
        mode = args[1]
        args = args[2:]
    if mode not in {"state", "combined"} or len(args) != 1:
        print("usage: verify_agents_state_rules.py [--mode state|combined] /path/to/AGENTS.md")
        return 2
    p = Path(args[0])
    if not p.exists():
        print(f"FAIL - file missing: {p}")
        return 1
    text = p.read_text(encoding="utf-8")
    checks = {
        "AGENTS remains under host context cap": len(text) < 20000,
        "PROJECT_GUIDE hot context rule": "PROJECT_GUIDE.md" in text and "hot" in text.lower(),
        "PROJECT_PLAN cold append-only rule": "PROJECT_PLAN.md" in text and "cold" in text.lower() and "append" in text.lower(),
        "PLAN not read by default": "不读取" in text or "not read" in text.lower(),
        "targeted PLAN reads": any(s in text for s in ["grep", "tail", "log_id", "line range"]),
        "material actions append PLAN": "PROJECT_PLAN.md" in text and ("追加" in text or "append" in text.lower()),
        "durable fact GUIDE updates only": "durable" in text.lower() and "PROJECT_GUIDE.md" in text,
    }
    if mode == "combined":
        checks.update(
            {
                "Directory Cards section": "Directory Cards" in text,
                "do not read all READMEs at startup": "不在 session start 读取所有目录 README"
                in text
                or "Do not read all directory READMEs at startup" in text,
                "README before scanning heavy artifact dirs": "README" in text
                and all(x in text for x in ["data/", "models/", "reports/"]),
                "README is navigation not final truth": "导航" in text
                or "navigation" in text.lower(),
                "nested AGENTS not result catalogs": "子目录 `AGENTS.md`" in text
                or "nested `AGENTS.md`" in text,
            }
        )
    print(f"file={p}")
    print(f"mode={mode}")
    print(f"chars={len(text)} lines={len(text.splitlines())}")
    failed = []
    for name, ok in checks.items():
        print(("PASS" if ok else "FAIL") + " - " + name)
        if not ok:
            failed.append(name)
    if failed:
        print("AD_HOC_VERIFICATION=failed")
        print("FAILED=" + "; ".join(failed))
        return 1
    print("AD_HOC_VERIFICATION=passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
