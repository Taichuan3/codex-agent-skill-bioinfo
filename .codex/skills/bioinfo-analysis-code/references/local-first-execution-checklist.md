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
