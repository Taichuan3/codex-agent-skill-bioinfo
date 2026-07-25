# Single-cell RNA-seq Execution

## Intake contract

Record:

- raw feature-barcode matrix/reads versus processed-only object;
- donor/sample, library, batch, condition, chemistry and multiplexing;
- feature reference, genome/annotation, barcode/UMI processing and ambient-RNA method;
- intended analysis unit for clustering, annotation, condition testing and composition.

A processed-only object may support bounded exploration, but it is not a reproducible starting point for raw QC or count-based inference when raw counts and preprocessing provenance are absent.

## QC and preprocessing

1. Inspect object layers, sparse shape, feature/cell identifiers and sample metadata before transformation.
2. Evaluate counts/UMIs, detected genes, mitochondrial or assay-relevant metrics by sample; derive thresholds from distributions and protocol context.
3. Assess empty droplets, ambient RNA, doublets, sample identity and known multiplexing failures with method-specific evidence.
4. Record every filter and before/after counts by sample; do not silently remove a weak donor to improve separation.
5. Normalize/select features for the chosen representation while preserving raw counts for compatible downstream models.

## Structure, integration and annotation

1. Establish a transparent unintegrated baseline before complex batch correction.
2. Check whether batch correction preserves biology and mixes only comparable states; over-mixing and under-correction are both failures.
3. Record feature selection, dimensions, neighbors, clustering resolution, seed and software versions.
4. Annotate with multiple evidence types: canonical markers, negative markers, reference mapping and biological context.
5. Flag ambiguous, low-quality or mixed clusters instead of forcing labels; assess stability across reasonable parameters.

## Condition and composition testing

- Treat donor/sample as the replication unit.
- For within-cell-type expression, prefer sample-aware pseudo-bulk or a justified donor-aware model.
- Report aggregation, minimum cell/sample rules, covariates, contrasts and multiple-testing method.
- Test cell-type proportions at sample level with an explicit denominator and compositional caveat.
- Do not use integrated expression values or cell-level independence to inflate evidence.

## Regulon and cross-modality work

- Separate co-expression modules, motif-pruned regulons and activity scores.
- Record motif database/species, background, seed, pruning and stability checks.
- For Multiome, preserve modality-specific QC and define the linkage statistic; correlation across modalities does not prove direct regulation.

## Minimum outputs

- cell/sample manifest and before/after QC counts;
- analysis object with raw-count access or an explicit processed-only limitation;
- reproducible config, environment and random seeds;
- annotation evidence table, sample-aware differential/composition results and source data;
- unresolved batch, label, replicate and validation risks.

Stop and report when sample identity, raw-count provenance, donor replication, pervasive doublets/ambient RNA or confounding prevents the intended inference.
