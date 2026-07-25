# Numbered Output Layout

Use this reference when organizing outputs from multi-step bioinformatics workflows.

## Principle

Results should reveal the analysis order. A reader should be able to tell which step produced a table, figure or log without opening multiple nested folders.

## Stage numbering

Example for RNA-seq:

```text
01_raw_inventory
02_qc_filtering
03_normalization
04_differential_expression
05_enrichment
06_visualization
07_source_data
```

Example directory:

```text
05_results/
  latest_manifest.tsv
  01_raw_inventory/
  02_qc_filtering/
  03_normalization/
  04_differential_expression/
  05_enrichment/
  06_visualization/
  07_source_data/
  priority_tables/
  priority_figures/
  archive/
```

## File naming

Use stage prefixes for important files:

```text
02_sample_qc_summary.tsv
03_normalized_counts.tsv
04_differential_expression.tsv
05_gsea_results.tsv
06_pca_plot.svg
07_fig2_source_data.tsv
```

## Manifest additions

Add or preserve these fields when possible:

```text
stage_id
stage_name
file_path
file_type
status
latest
related_claim
related_figure
source_input
script
command
environment
updated_at
notes
```

## Priority views

`priority_tables/` and `priority_figures/` are shallow entry points for files the user often needs. They can be copies or symlinks depending on project policy.

Do not bury confirmed manuscript tables under deeply nested temporary folders.

## Overwrite versus archive

- Read-only audits never create, update, move, or overwrite files.
- Corrected derived files may overwrite old wrong files only after the user authorizes that write and the analysis definition is unchanged.
- Different parameters, different biological interpretations or alternative branches should be archived or named as branches.
- Manifest must point to the current valid version.
