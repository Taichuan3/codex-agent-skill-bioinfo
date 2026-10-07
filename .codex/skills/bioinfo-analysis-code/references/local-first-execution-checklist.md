# Local-first Execution Checklist

Borrowed lessons from external bioinformatics skill libraries: prefer reproducible local execution, explicit preflight, benchmark-like minimal checks, and no guessing.

## Before running

- Identify raw inputs and confirm they remain read-only.
- Record file counts, sample IDs, genome/reference versions, and expected output shape.
- Check required tools/packages and versions; if adopting an external tool, route through `environment-and-tool-adoption`.
- Decide whether the task is exploratory, stable, or submission-ready.

## During execution

- Save exact commands or notebook cells that generated each stable output.
- Capture stdout/stderr logs for multi-step workflows. Record failed or aborted task attempts separately from successful-output provenance: run/task ID, attempt number, exit code or unavailable status, log paths, and retry/successor association. A successful lineage record does not establish that no earlier attempt failed.
- Use small smoke-test inputs when full data are large or slow.
- Keep parameters in a script/config rather than hidden in chat.

## After execution

- Verify output row/column counts, sample coverage, and key identifiers. For aggregated QC reports, compare the expected sample-by-required-module coverage with what was actually parsed; reconcile skipped inputs, warnings and documented exclusions. A generated report or zero exit status alone does not pass acceptance; unresolved missing required coverage remains incomplete.
- Produce a machine-readable table plus a human-readable summary when possible.
- Record caveats, failed alternatives, and whether results are safe for manuscript use.
- If a result becomes figure/source data, make the generating script and source path traceable.


## Stable output bundle

For any result that may be reused, reviewed, or promoted to a figure/report, prefer a small reproducibility bundle:

- `commands.sh` or notebook cell export for exact commands.
- `params.yaml` or equivalent config for filters, thresholds, paths, random seeds and references.
- `manifest.json` or Markdown manifest listing inputs, outputs, row/column expectations and source-data links.
- checksums for stable input/output files when practical.
- `environment.yml`, `requirements.txt`, tool version table, or container tag when dependencies matter.

Do not silently change parameters between smoke test and full run. If parameters change, record the reason and invalidate stale outputs.

## Upstream evidence and version boundary

Reviewed 2026-10-07; mechanism-level clarification, not software adoption:

- [MultiQC mosdepth fix, 6946a9c (2026-10-02)](https://github.com/MultiQC/MultiQC/commit/6946a9c36d7a2f8bb6bc9ca349bed0a6a81ac2d5) shows that malformed/truncated inputs can be skipped with a warning. Verify parsed coverage rather than inferring complete QC from report existence.
- [Nextflow lineage change, f39b2de (2026-10-01)](https://github.com/nextflow-io/nextflow/commit/f39b2dec7bdb559abf0ba55ff0f9468f72632630) excludes failed/aborted attempts from lineage recording on the development line. This is not a claim about an installed stable release. Record the actual executable version and corroborate failure/retry history using available execution logs or trace records; missing attempt metadata stays an explicit gap.

These are independently written validation rules. No upstream code is copied or run, and no pipeline, environment, sample universe or reference version is changed.
