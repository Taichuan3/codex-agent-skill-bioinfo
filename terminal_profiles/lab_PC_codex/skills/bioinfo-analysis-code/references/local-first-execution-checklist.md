# Local-first Execution Checklist

Borrowed lessons from external bioinformatics skill libraries: prefer reproducible local execution, explicit preflight, benchmark-like minimal checks, and no guessing.

## Before running

- Identify raw inputs and confirm they remain read-only.
- Record file counts, sample IDs, genome/reference versions, and expected output shape.
- Check required tools/packages and versions; if adopting an external tool, route through `environment-and-tool-adoption`.
- Decide whether the task is exploratory, stable, or submission-ready.

## During execution

- Save exact commands or notebook cells that generated each stable output.
- Capture stdout/stderr logs for multi-step workflows.
- Use small smoke-test inputs when full data are large or slow.
- Keep parameters in a script/config rather than hidden in chat.

## After execution

- Verify output row/column counts, sample coverage, and key identifiers.
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
