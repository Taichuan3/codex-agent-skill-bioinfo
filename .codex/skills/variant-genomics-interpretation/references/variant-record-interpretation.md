# Variant Record Interpretation

## Identity contract

For each allele, retain:

- reference build and contig naming;
- 1-based VCF coordinate with REF/ALT;
- normalization status, representation of indels and split multi-allelic records;
- strand where a non-VCF source uses it;
- transcript accession/version and HGVS expression when relevant.

Resolve reference mismatches before liftover or cross-database joins. After liftover, revalidate REF against the target reference; a mapped coordinate alone is insufficient.

## Callset fitness review

1. Inspect header, provenance, sample roster, caller/filter fields and reference.
2. Review genotype/sample missingness, depth/quality distributions, contamination, sex/identity concordance and relatedness where relevant.
3. Check site filters, normalization, multi-allelic handling and region-specific technical limitations.
4. Confirm the QC population and thresholds match the downstream question.
5. Report excluded samples/sites and reasons without changing the callset during interpretation.

Missing or failed QC limits every downstream annotation; do not compensate with more database fields.

## Cross-source interpretation

- Match normalized alleles, not rsID alone.
- For population frequency, record ancestry, AC/AN, homozygote count when relevant, coverage/filters and release.
- For consequence, record transcript choice, ontology term and whether the value is curated, rule-based or predicted.
- For clinical assertions, record condition, significance, review status, conflicts, submitter context and evaluation date.
- For regulatory annotations, record cell/tissue context, assay, interval definition and reference build.

## Conflict report

Use one row per source and include:

`normalized_variant | source_release | condition_or_population | observation | review_or_model | support | conflict | limitation`

Do not adjudicate a clinical classification unless the user has explicitly scoped a standards-based classification process with appropriate expert review. This Skill may map evidence but cannot supply final clinical sign-out.
