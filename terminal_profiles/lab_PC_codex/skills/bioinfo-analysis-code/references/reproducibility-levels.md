# Code Reproducibility Levels

## Exploratory

Use for early tests.

- Script/notebook can be rough.
- Record input, command and output.
- Do not over-document every line.
- Mark unstable parameters.
- Record negative results and failed checks when they may affect future decisions.
- Do not phrase exploratory outputs as final manuscript claims.

## Stable

Use when results may enter figures or manuscript drafts.

- Script has clear input/output arguments.
- Key parameters are explicit.
- Environment and package versions are recorded.
- Output path is stable.
- Script and output paths use workflow stage numbering when the analysis has multiple steps.
- Caveats are written down.
- Parameters, sample set, feature set and statistical plan are fixed before confirmation runs.
- If machine learning is involved, train/test/validation separation and leakage prevention are documented.

## Submission-ready

Use before sharing code or submitting.

- README or method note explains how to rerun.
- Dependencies are pinned where feasible.
- Scripts are named by workflow order or task.
- Main scripts, logs, tables, figures and source data can be traced by stage ID.
- Comments explain non-obvious logic.
- Main figures/tables can be regenerated.
- Random seeds, references and database versions are recorded.
- Main analysis has a documented path from raw/processed data to source data and figures.
- Notebook-only final results are converted into scripts or explicitly justified.

## Analysis phases

| Phase | Goal | Required guardrail |
|---|---|---|
| Exploration | Find patterns and candidate hypotheses | Mark parameters as provisional and record failed/negative attempts worth remembering |
| Confirmation | Test the central hypothesis | Lock parameters, sample set, background set, statistics and expected outputs before rerunning |
| Validation | Test robustness beyond the original discovery context | Use independent data, orthogonal methods, negative controls, sensitivity analyses or justified claim downgrade |

## Machine-learning leakage checks

When scripts include prediction, classification, clustering used for downstream inference, or model selection:

- Split train/test/validation before feature selection where applicable.
- Avoid using test labels during normalization, batch correction, feature filtering or threshold tuning.
- Record random seeds, folds, leakage-sensitive preprocessing and final held-out performance.
- Report effect size and biological interpretation, not only accuracy or p value.
