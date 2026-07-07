# Report-level reproducibility package pattern

Use when a bioinformatics report is being prepared for an outside reader, TA, reviewer, or collaborator and the user asks for materials to reproduce/check the report.

## Core principle

Do not turn the report Methods into a directory tree. The Methods should explain the analysis logic in paper-style modules; concrete relative paths, file checksums, scripts, and install commands belong in a package `README.md`, `MANIFEST.tsv`, and optional source-data index.

## Recommended package layout

```text
reproducibility_package/<project>_<date>/
  00_environment/
  01_input_sequences/
  02_track_atlas_or_metadata/
  03_model_prediction_or_primary_analysis/
  04_external_validation/
  05_sequence_motif_or_downstream_analysis/
  06_scripts/
  07_report_tables/
  README.md
  MANIFEST.tsv
```

Adapt directory names to the project, but keep them English and reader-facing.

## Include

- Environment files:
  - cross-platform conda environment file as the primary install entry;
  - platform-specific exact export as an audit/lock file;
  - `pip freeze` as an audit record, not the main install route.
- Input manifests and small curated inputs needed to understand the report:
  - BED/interval definitions;
  - sequence-window manifests;
  - report-scale FASTA files if size is reasonable.
- Report-level source data:
  - figure/table source-data TSVs;
  - model/API response manifests and returned metadata needed to trace model outputs;
  - external dataset download/QC metadata;
  - final summary tables and concordance tables;
  - intermediate tables needed for non-obvious claims, especially CTSS/motif/mappability claims.
- Selected scripts that generate report-level tables/figures or key intermediate summaries.
- `README.md` explaining package scope, install path, and what is intentionally excluded.
- `MANIFEST.tsv` with `relative_path`, `size_bytes`, and `sha256` for every packaged file.

## Usually exclude from a portable report package

- Full reference genomes unless explicitly required and size-appropriate.
- Raw FASTQ/BAM/CRAM files and large API caches.
- Temporary logs, failed runs, scratch outputs, and exploratory duplicates.

For excluded raw data, include accession/download manifests and explain how to retrieve originals.

## Verification checklist

Create and run an ad-hoc verification script that checks:

1. Required package directories and key files exist.
2. `README.md` and `MANIFEST.tsv` exist.
3. SHA256 values in `MANIFEST.tsv` match current files.
4. The compressed archive can be opened and contains `README.md` and `MANIFEST.tsv`.
5. Intentionally excluded raw/huge files are not accidentally bundled.
6. Report image links still resolve after Methods/package edits.
7. The project plan/log records the package creation.

Report this as ad-hoc verification, not suite green.
