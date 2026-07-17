# Repeat-rich external-validation claim audit

Use this reference when a claim compares a model prediction with public or project-processed signals in a repeat-rich or mappability-sensitive interval.

## Separate the compared objects

Do not treat a matching assay or tissue label as proof that two signal tracks are the same object. Audit three layers separately:

- `A — model prediction`: the model-returned profile for the specified sequence and output definition.
- `B — official processed target`: the processed track or target object identified by the model metadata.
- `C — project observed signal`: signal reconstructed or summarized by the current project from raw or retained processed data.

Report `A vs B`, `B vs C`, and `A vs C` separately when the objects exist. Concordance is not accuracy unless a metric and reference truth were defined in advance.

## Required checks

1. **Provenance**: resource, sample/library/run identifiers, access date, file integrity, processing state and retained source-data path.
2. **Metadata consistency**: compare biologically explicit sample, condition and treatment fields. Record label conflicts rather than choosing silently.
3. **Coordinates**: reference assembly, coordinate convention, strand handling, liftover/remapping and interval definition.
4. **Signal definition**: raw counts, normalized coverage, enrichment, peak calls or endpoint counts; record transformations and resolution.
5. **Mapping sensitivity**: primary/secondary handling, MAPQ, duplicates, strict versus relaxed or multi-mapping views. Never merge sensitivity layers silently.
6. **Controls**: matched input/control, negative control or background definition when the assay requires one.
7. **Traceability**: every figure or table points to the source data, generating script, parameters and display transform.

## Absence and disagreement

- “No signal” is valid only for a named signal object, interval, threshold and resolution. Sparse calls hidden by aggregation require wording such as “weak/sparse at the tested resolution,” not “absent.”
- Signal confined to relaxed or low-mappability views is exploratory and cannot establish a biological difference.
- Matched-source disagreement narrows possible explanations but does not by itself prove model failure, filtering loss or a biological mechanism.
- If raw data are unavailable, do not claim robustness to alternative mapping, filtering or processing choices that were not rerun.

## Safe outcomes

| Audit result | Safe interpretation |
|---|---|
| Matched source, comparable signal object and localized agreement | Moderate proxy support or profile concordance |
| Agreement only after relaxed mapping or in low-mappability sequence | Exploratory, mappability-sensitive support |
| Official target and project reprocessing disagree | Processing/reference discrepancy requiring follow-up |
| Negative summary without raw data or exact-resolution checks | Insufficient for an absence claim |

Database, model and public-signal evidence remain proxy evidence unless orthogonal experimental validation supports the biological or causal claim.
