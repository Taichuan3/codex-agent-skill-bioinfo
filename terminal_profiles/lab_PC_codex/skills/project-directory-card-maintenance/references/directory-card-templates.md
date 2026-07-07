# Directory Card templates

## Generic Directory Card

```markdown
# Directory Card: <relative/path>

## Purpose
<One sentence: what this directory contains and why it exists.>

## Current important files
| path | status | meaning | produced by |
|---|---|---|---|
| <file> | current / candidate / deprecated | <what it is> | <script/notebook/command> |

## Read first
- Start with: <file/manifest/script>
- For exact file metadata, use: <manifest.tsv / registry.tsv>
- For history, search: `PROJECT_PLAN.md` by `<log_id / keyword>` only if needed.

## Reproduce / update
Command: `<make command or python script>`

## Ignore / deprecated
- Ignore: `<pattern>` because <reason>.
- Deprecated: `<file>` replaced by `<file>` on <date>.

## Notes for Hermes/Codex
- Do not inspect all files unless the task requires it.
- Prefer the current files listed above.

## Last updated
YYYY-MM-DD - <reason>
```

## data/processed/README.md

```markdown
# Directory Card: data/processed

## Purpose
Canonical analysis-ready datasets. These are the datasets that downstream QC, modeling, figures, and manuscript claims should use.

## Current canonical datasets
| dataset | status | samples | features | source | produced by |
|---|---:|---:|---:|---|---|
| <dataset.parquet> | current | <n> | <p> | <raw/external> | `make data` / `<script>` |

## Data rules
- Do not manually edit files in this directory.
- Any new canonical dataset must be reproducible from `data/raw` and code.
- Update `metadata/data_manifest.tsv` when adding/replacing datasets.
- If a dataset is for modeling, record split strategy and leakage checks.

## Read first
- `metadata/data_manifest.tsv`
- `metadata/sample_metadata.tsv`
- This README

## Reproduce / update
Command: `make data && make qc`

## Deprecated / ignore
- `<old_dataset>` replaced by `<new_dataset>` on YYYY-MM-DD.

## Last updated
YYYY-MM-DD - <reason>
```

## models/README.md

```markdown
# Directory Card: models

## Purpose
Trained models, model summaries, predictions, and model selection records.

## Current model status
| model/run | status | task | split | primary metric | artifact | produced by |
|---|---|---|---|---:|---|---|
| baseline_v1 | baseline | <classification/regression/survival> | <split> | <metric> | <path> | <command> |
| model_v2 | current_best | <task> | <split> | <metric> | <path> | <command> |

## Current interpretation
- Best model:
- Baseline comparison:
- External validation:
- Known limitations:

## Read first
- `models/model_registry.tsv`
- `reports/model_eval/README.md` if present
- Configs under `configs/model/`

## Reproduce / update
Command: `make train && make evaluate`

## Rules
- No model claim without baseline.
- No performance claim without split protocol and leakage check.
- Record code commit and data version for each candidate model.

## Last updated
YYYY-MM-DD - <reason>
```

## reports/figures/README.md

```markdown
# Directory Card: reports/figures

## Purpose
Publication-oriented figures and figure candidates. Use this file to map figure panels to scientific claims and generation scripts.

## Figure-to-claim map
| figure/panel | status | claim | evidence | script | stats/source |
|---|---|---|---|---|---|
| Fig1A | candidate | <claim> | <evidence> | `src/visualization/fig1a.py` | <test/data> |
| Fig2B | final | <claim> | <evidence> | `src/visualization/fig2b.py` | <test/data> |

## Current figure set
- Main figure candidates:
- Supplementary candidates:
- Deprecated figures:

## Read first
- `reports/figures/figure_manifest.tsv`
- `CLAIM_TABLE.md` if present
- This README before opening individual images

## Reproduce / update
Command: `make figures`

## Visual standards
- Use consistent panel labels.
- Keep source scripts and figure files linked.
- Do not treat exploratory plots as final figures unless marked `candidate` or `final`.

## Last updated
YYYY-MM-DD - <reason>
```
