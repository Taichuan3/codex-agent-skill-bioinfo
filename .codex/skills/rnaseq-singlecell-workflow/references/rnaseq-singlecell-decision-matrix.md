# RNA-seq / Single-cell Decision Matrix

Use this matrix only after the common input, replicate, reference, and contrast contract is explicit.

| Question | Analysis unit | Typical method class | Required checks | Claim limit |
|---|---|---|---|---|
| Bulk abundance | biological sample | splice-aware alignment plus counting, or transcript-aware quantification | strandedness, annotation, mapping/assignment, composition, replicate structure | expression association |
| Bulk differential expression | biological sample | count-aware GLM or voom-style model | raw counts, full-rank design, contrast, dispersion, multiple testing | design-conditional association |
| Transcript usage / splicing | sample × transcript/event/junction | DTU, event- or junction-based model | read support, event definition, annotation dependence, replicate coverage | isoform/event evidence, not protein function |
| scRNA structure | cell, nested in sample | feature selection, dimension reduction, neighbor graph, clustering | raw counts, QC, doublets, batch, stability | model-dependent cell-state structure |
| scRNA condition effect | sample × cell type/state | pseudo-bulk or donor-aware mixed model | biological replicates, composition, aggregation rule, covariates | condition association within defined state |
| Cell-type proportion | sample | compositional or sample-level model | denominator, sampling depth, replicate count, uncertainty | abundance association |
| Multiome RNA layer | cell, nested in sample | scRNA workflow with cross-modality linkage | modality-specific QC, shared cell identity, batch, linkage definition | cross-modality association |
| Regulon / GRN | cell or sample score | co-expression, motif pruning, activity scoring | species/motif collection, seed, null/background, stability | inferred network/activity, not causal regulation |

## Selection rules

- Prefer a mature, documented workflow when it matches the assay; record versions and config instead of treating a wrapper as evidence.
- Use transformed or normalized matrices for QC and visualization; use model-appropriate counts or sufficient statistics for testing.
- Choose the statistical unit from the experimental replication, not from the largest row count.
- If two methods answer different estimands, preserve both definitions rather than averaging their scores.
