# Claim-to-figure system

Use this reference when figures are being organized for a manuscript, preprint, thesis chapter, report, or submission package.

## Principle

Do not start from “what plots do we have?” Start from “what claims are safe, necessary, and supported?” Each figure panel must serve a claim; each claim must have evidence, source data, a script, a statistical context, and a limitation.

## Core artifacts

```text
paper/CLAIM_TABLE.md
paper/FIGURE_PLAN.md
paper/RESULTS_NARRATIVE.md
paper/FIGURE_LEGENDS.md
reports/figures/figure_source_mapping.tsv
reports/source_data/
```

## CLAIM_TABLE.md columns

```text
claim_id
claim
evidence
figure_panel
source_data
script
statistical_test
limitation
status
reviewer_risk
next_action
```

Status vocabulary: `draft`, `validated`, `needs_source_data`, `needs_analysis`, `downgrade`, `reject`.

## FIGURE_PLAN.md fields

For each figure:

- main claim;
- panels and panel roles;
- input/source-data tables;
- generating script and rerun command;
- statistics, n, denominator, random seed, database version when relevant;
- what each panel can and cannot support;
- whether it belongs in main text, supplement, or internal/PPT inspection only;
- reviewer attack points and planned response.

## Reviewer attack matrix

```text
attack_id
claim_id
likely_reviewer_question
weak_point
current_evidence
minimum_fix
cost
priority
response_strategy
```

## Done definition

- Every main-text claim maps to at least one figure/table/source-data item.
- Every main figure panel has a script or saved rendering session.
- Caption describes data universe, axes, encodings, denominators, and statistics without overinterpreting.
- Claims and captions separate evidence, interpretation, limitation, and speculation.
- Unsupported or weak claims are downgraded, moved to Discussion, or removed.
