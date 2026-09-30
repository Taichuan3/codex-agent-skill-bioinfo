#!/usr/bin/env python3
"""Isolated regression fixtures; never read user projects."""
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("handoff", ROOT / ".codex/skills/project-state-maintenance/scripts/verify_project_handoff.py")
handoff = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(handoff)


class HandoffChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "PROJECT_GUIDE.md").write_text("# Current\nCaveat: exploratory, not author accepted.\n")
        (self.root / "figure.svg").write_text("<svg/>")
        (self.root / "README.md").write_text("See current.tsv")
        self.row = {k: "pending" for k in handoff.FIELDS}
        self.row.update(asset_id="a", module_id="sequence-comparison", scope="exploration",
                        label="distance", path="figure.svg", status="candidate",
                        sha256=handoff.digest(self.root / "figure.svg"))

    def run_check(self, rows=None):
        with (self.root / "current.tsv").open("w", newline="") as stream:
            writer = csv.DictWriter(stream, sorted(handoff.FIELDS), delimiter="\t")
            writer.writeheader()
            writer.writerows(rows if rows is not None else [self.row])
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        result = handoff.verify(self.root, "PROJECT_GUIDE.md", "current.tsv", ["README.md"])
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})
        return result

    def test_early_project_without_result(self):
        r = self.run_check()
        self.assertTrue(r["metadata_valid"])
        self.assertEqual(r["scientific_validation"], "not_performed")
        self.assertEqual(r["provenance_pending"]["producer"], 1)

    def test_missing_current_path(self):
        self.row["path"] = "missing.svg"
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_hash_drift(self):
        self.row["sha256"] = "0" * 64
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_duplicate_current(self):
        self.row["status"] = "current"
        other = dict(self.row, asset_id="b")
        self.assertFalse(self.run_check([self.row, other])["metadata_valid"])

    def test_distinct_scopes_allowed(self):
        self.row["status"] = "current"
        other = dict(self.row, asset_id="b", scope="submission")
        self.assertTrue(self.run_check([self.row, other])["metadata_valid"])

    def test_remote_not_fetched(self):
        self.row.update(path="https://example.invalid/plot.png", status="unverified_remote", sha256="pending")
        r = self.run_check()
        self.assertTrue(r["metadata_valid"])
        self.assertTrue(r["warnings"])

    def test_escape_rejected(self):
        self.row["path"] = "../outside"
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_source_gap_detected(self):
        self.row["source_data"] = "missing.tsv"
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_budget_warns_without_trimming(self):
        (self.root / "PROJECT_GUIDE.md").write_text("x" * 7000)
        r = self.run_check()
        self.assertEqual(r["guide"]["characters"], 7000)
        self.assertEqual(len(r["warnings"]), 2)

    def test_directory_not_guide(self):
        self.run_check()
        r = handoff.verify(self.root, ".", "current.tsv", [])
        self.assertFalse(r["metadata_valid"])

    def test_directory_not_registry(self):
        r = handoff.verify(self.root, "PROJECT_GUIDE.md", ".", [])
        self.assertFalse(r["metadata_valid"])

    def test_empty_current_identity(self):
        self.row.update(module_id="", scope="", label="", status="current")
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_malformed_tsv_is_reported(self):
        (self.root / "current.tsv").write_text("\t".join(sorted(handoff.FIELDS)) + "\nshort\n")
        r = handoff.verify(self.root, "PROJECT_GUIDE.md", "current.tsv", [])
        self.assertFalse(r["metadata_valid"])
        self.assertTrue(any("column count" in e for e in r["errors"]))

    def test_non_utf8_is_reported(self):
        (self.root / "current.tsv").write_bytes(b"\xff\xfeinvalid")
        r = handoff.verify(self.root, "PROJECT_GUIDE.md", "current.tsv", [])
        self.assertFalse(r["metadata_valid"])

    def test_duplicate_header_is_reported(self):
        (self.root / "current.tsv").write_text("\t".join(sorted(handoff.FIELDS) + ["path"]) + "\n")
        r = handoff.verify(self.root, "PROJECT_GUIDE.md", "current.tsv", [])
        self.assertFalse(r["metadata_valid"])

    def test_unknown_status_is_not_current(self):
        self.row["status"] = "currrent"
        self.assertFalse(self.run_check()["metadata_valid"])

    def test_empty_early_registry_is_disclosed(self):
        r = self.run_check([])
        self.assertTrue(r["metadata_valid"])
        self.assertEqual(r["rows"], 0)
        self.assertTrue(r["warnings"])


if __name__ == "__main__":
    unittest.main()
