# Cookiecutter Data Science / CCDS layout for bioinfo projects

Use this reference when starting a new project, reorganizing a messy project, or designing a data/result manifest.

## Why adopt it

Cookiecutter Data Science provides a logical, flexible, standardized project structure for doing and sharing data science work. It reduces the common failure mode where raw data, processed data, figures, scripts, notebooks, and final reports become hard to locate or reproduce.

Installed local CLI: `ccds` from `cookiecutter-data-science` via pipx.

## Recommended adapted layout

```text
project-name/
  AGENTS.md
  README.md
  PROJECT_GUIDE.md
  PROJECT_PLAN.md
  PROJECT_CHARTER.md
  Makefile
  pyproject.toml or environment.yml
  configs/
    data/
    model/
    figures/
  data/
    raw/          # immutable raw data; never edit manually
    external/     # third-party downloaded resources
    interim/      # intermediate transformed data
    processed/    # analysis-ready canonical data
  metadata/
    data_sources.tsv
    data_manifest.tsv
    sample_metadata.tsv
    inclusion_exclusion.md
    license_and_usage.md
    provenance_map.md
  references/
    data_dictionaries/
    protocols/
    manuals/
  literature/
    literature_matrix.tsv
    field_map.md
    dataset_map.tsv
    method_map.md
  notebooks/
    exploratory/
    archive/
  src/
    data/
    features/
    genetics/
    structure/
    models/
    visualization/
    paper/
  tests/
    test_data_manifest.py
    test_no_leakage.py
    test_split_integrity.py
  reports/
    qc/
    model/
    figures/
    tables/
    source_data/
  manuscript/
  revision/
  release/
```

## Rules

- `data/raw/` is immutable. Do not edit, normalize, filter, rename in place, or overwrite raw data.
- Every data asset should have source, version/date, license/usage note, checksum when possible, citation, raw path, processed path, and download/build command.
- Exploratory notebooks are allowed, but stable logic should move to `src/` and be callable from Makefile/Snakemake/Nextflow.
- `reports/` contains generated outputs; `reports/source_data/` maps figure/table outputs to scripts and inputs.
- For established manuscript outputs, maintain shallow `priority_tables/`, `priority_figures/`, or manifest views when helpful.

## Minimal manifest fields

```text
asset_id
asset_type
source
version
license
download_command
checksum
raw_path
processed_path
citation
script
command
environment
related_claim
related_figure
notes
```

## When not to force full CCDS

- Tiny one-off checks can use a lightweight subset.
- Existing mature projects should be migrated gradually by adding manifests and shallow entry points first, not by moving every file at once.
- Server/GPU compute projects may keep heavy outputs on server storage; Mac-side repo should still keep manifests, scripts, reports, figures, and paths.
