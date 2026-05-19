# Code Reproducibility Levels

## Exploratory

Use for early tests.

- Script/notebook can be rough.
- Record input, command and output.
- Do not over-document every line.
- Mark unstable parameters.

## Stable

Use when results may enter figures or manuscript drafts.

- Script has clear input/output arguments.
- Key parameters are explicit.
- Environment and package versions are recorded.
- Output path is stable.
- Script and output paths use workflow stage numbering when the analysis has multiple steps.
- Caveats are written down.

## Submission-ready

Use before sharing code or submitting.

- README or method note explains how to rerun.
- Dependencies are pinned where feasible.
- Scripts are named by workflow order or task.
- Main scripts, logs, tables, figures and source data can be traced by stage ID.
- Comments explain non-obvious logic.
- Main figures/tables can be regenerated.
- Random seeds, references and database versions are recorded.
