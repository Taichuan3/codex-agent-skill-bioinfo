# Statistical-genetics Interpretation

## Shared contract

Record phenotype definition, cohort, ancestry, sample size, covariates, effect allele, genome build, QC, imputation/variant coverage, software/model and multiple-testing rule. Harmonize alleles before comparing effects.

## GWAS and fine-mapping

1. Verify effect/non-effect alleles, units, direction, genomic control and population structure handling.
2. Separate discovery, replication and external evidence.
3. For fine-mapping, record locus window, variant set, LD source, priors, number-of-causal-variant assumptions and credible-set coverage.
4. Treat the credible set as model-dependent candidates, not a ranked proof of causality.

## QTL and colocalization

- Match tissue/cell state, phenotype transformation, alleles and ancestry.
- Distinguish LD overlap, conditional independence, fine-mapped overlap and formal colocalization.
- Record datasets, sample overlap, LD, priors, number-of-signal handling and posterior definitions.
- A shared signal does not by itself establish mediation, target gene, direction or mechanism.

## Rare variants

- Preserve qualifying-variant mask, consequence definition, frequency source/threshold, ancestry and genotype QC.
- Distinguish burden, variance-component and combined tests.
- Check whether one allele or subgroup dominates the aggregate signal.
- A gene-level association does not classify every included variant.

## PRS

- Record training GWAS, target population, LD reference, feature selection, scaling and calibration.
- Evaluate discrimination, calibration and uncertainty in a relevant external population.
- Report ancestry/phenotype transfer limits; do not convert a research PRS into personal risk or action.

## Mendelian randomization

- Define exposure, outcome, instruments, harmonization and sample overlap.
- Review instrument strength, directionality, heterogeneity, horizontal pleiotropy and alternate pathways.
- Use sensitivity analyses as diagnostics, not proof that assumptions hold.
- State causal language only at the strength warranted by design, assumptions and convergent evidence.

## Output

Use one row per analysis:

`question | population | allele_or_unit | model | estimate | uncertainty | QC | assumptions | support_level | limitation | next_test`
