# Claim-to-figure audit

Use when a manuscript/report has figures or planned panels and the question is whether the claims are supported.

## Audit table

```text
claim_id
claim
figure_or_table
source_data
script_or_pipeline
statistical_test
current_level
risk
limitation
recommended_action
safe_wording
```

## Recommended actions

- `keep`: claim is directly supported.
- `downgrade`: wording is too strong but a weaker version is supported.
- `move_to_discussion`: claim is plausible interpretation/hypothesis, not a result.
- `needs_source_data`: figure/table exists but source-data traceability is missing.
- `needs_analysis`: claim requires additional analysis or validation.
- `remove`: claim is unsupported or misleading.

## Reviewer attack prompts

For each important claim ask:

1. Could a reviewer ask for source data, exact n, denominator, or filtering rule?
2. Could an alternative explanation or confounder explain the result?
3. Does the figure show association while the text implies mechanism or causality?
4. Does the model/docking/annotation/database score exceed its evidence boundary?
5. Is validation independent, or did test/external data leak into preprocessing/model selection?
6. Is the claim generalizing beyond the cohort, assay, species, cell type, sequence region, protein state, or chemical series actually tested?

## Safe output

Always separate:

- Evidence: what was directly observed.
- Interpretation: what the observation suggests.
- Limitation: what it does not prove.
- Next validation: what would upgrade the claim.
