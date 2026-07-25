# Cohort and Biomarker Evidence Review

## Cohort contract

Record:

- data source, recruitment, setting, dates and inclusion/exclusion;
- unit of analysis, population, exposure/biomarker, comparator and endpoint;
- follow-up, censoring, competing events and missingness;
- derivation/validation split, covariates, model, effect metric and intended use.

Do not silently redefine the cohort, endpoint, cutoff or analysis population after seeing the result.

## Association and survival

1. Verify time origin, event definition, censoring and follow-up distribution.
2. Distinguish univariable, adjusted, subgroup and interaction estimates.
3. Check proportional-hazards or other model assumptions where applicable.
4. Report effect size, uncertainty, event count and missing-data handling, not p-value alone.
5. Separate prognostic association from treatment-effect prediction and causality.

## Biomarker or prediction model

- Define whether the intended use is diagnosis, prognosis, monitoring, prediction or enrichment.
- Preserve assay/platform, preprocessing, cutoff derivation and batch/site effects.
- Evaluate discrimination and calibration; add decision-curve or clinical-utility evidence only when valid for the intended setting.
- Identify leakage, optimistic tuning and whether validation is temporal, geographic, external or only internal.
- Report prevalence and spectrum differences that affect transportability.

## Evidence table

Use one row per cohort/analysis:

`study | population | biomarker/exposure | endpoint | model | effect/performance | uncertainty | validation | bias | applicability | claim_limit`

Patient-level identifiers and unnecessary row-level clinical data must not enter the evidence artifact.
