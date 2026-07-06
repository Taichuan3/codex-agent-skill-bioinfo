# Evidence map matrix

Use this when a literature task should support a research decision rather than just summarize papers.

## Minimum columns

```text
paper_id
PMID_or_DOI_or_arXiv
year
claim
evidence
dataset
method
limitation
reusable_resources
relevance_to_project
action
notes
```

## Action vocabulary

- `follow`: core evidence or method to build on.
- `reproduce`: worth reproducing or benchmarking.
- `avoid`: method/claim is weak, biased, or not relevant.
- `cite_only`: useful background but not direct evidence.
- `data_source`: contains reusable dataset/structure/model/code.
- `method_reference`: method or protocol worth adapting.

## Synthesis sections

- Consensus: what multiple strong papers agree on.
- Controversy: conflicts, inconsistent datasets, or method-dependent conclusions.
- Method gap: missing or weak analytical methods.
- Data gap: missing cohort/tissue/assay/structure/validation.
- Reusable resources: datasets, code, models, structures, supplementary tables.
- Possible contribution: where this project could add a defensible result.
- Go/no-go: whether evidence justifies the next stage.

## Claim discipline

Do not upgrade literature association into causality. State what each paper does not prove, especially for genetics, structural mechanism, ML performance, docking/ADMET, and clinical translation.
