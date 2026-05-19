# Workflow Numbering and Pipeline Layout

Use this reference when a bioinformatics task has multiple processing steps, such as RNA-seq, single-cell, ATAC-seq, variant analysis, enrichment analysis, or repeated plotting workflows.

## Goal

Three months later, the user should be able to regenerate the main tables and figures by reading the README and running the ordered scripts or workflow entrypoint.

## Numbering rules

- Use `00_` for setup, configuration, metadata checks, project initialization or helper scripts.
- Use `01_`, `02_`, `03_` for analysis stages in execution order.
- Keep the same stage ID across script, output directory, log file and key result files.
- Do not reorder existing stable step IDs casually. If a new step is inserted, prefer `02b_` or add a clear migration note rather than silently renaming everything.
- Use descriptive names after the number: `02_qc_filtering.R`, not `02_script.R`.

## Minimum script layout

```text
03_code/
  00_setup/
    00_check_environment.sh
  01_preprocessing/
    01_import_metadata.py
    02_filter_samples.py
  02_qc/
    01_qc_summary.R
  03_analysis/
    01_differential_expression.R
  04_visualization/
    01_make_main_figures.R
```

For smaller projects:

```text
scripts/
  00_check_environment.sh
  01_import_data.py
  02_qc_filtering.R
  03_analysis.R
  04_make_figures.R
```

## Output layout

```text
05_results/
  01_preprocessing/
    tables/
    logs/
  02_qc/
    tables/
    figures/
    logs/
  03_analysis/
    tables/
    logs/
  04_visualization/
    figures/
    source_data/
```

Key files should include the stage ID when useful:

```text
05_results/02_qc/tables/02_sample_qc_summary.tsv
05_results/03_analysis/tables/03_differential_expression.tsv
05_results/04_visualization/figures/04_volcano_plot.svg
```

## Notebook policy

- Exploration notebooks may be named `00_explore_<topic>.ipynb`.
- Stable notebook outputs must be converted into scripts or documented as fixed analysis notebooks.
- Do not leave final results only inside notebooks.
- If a notebook is retained, record its kernel, environment, input files and exported outputs.

## Pipeline tiers

### Minimum

Numbered scripts, clear inputs/outputs, recorded commands and version-controlled code.

### Stable

Conda/mamba/renv environment, README commands, logs, `run_all.sh`, manifest of key outputs.

### Advanced

Snakemake, Nextflow, nf-core style, containers, execution trace, semantic versions, CI tests when feasible.

## Command logging

For each step, record:

```text
step_id
script
input
output
command
environment
parameters
date
caveat
```
