# ML benchmark contract template

Use this as the minimal input/output contract before implementing a benchmark.

## task_definition.md

```yaml
task_type: classification | regression | survival | ranking | generation | representation_learning
input_unit: patient | sample | variant | gene | protein | ligand | protein_ligand_pair | cell | sequence_region
target: ""
label_source: ""
intended_use: ""
forbidden_claims:
  - ""
primary_metric: ""
secondary_metrics: []
calibration_or_uncertainty: ""
```

## split_protocol.md

```yaml
split_type: patient_level | family_level | gene_level | protein_family_level | scaffold | time | batch_aware | external_cohort
split_rationale: "why this matches intended use"
train: ""
validation: ""
test: ""
external_validation: ""
stratification: ""
random_seed: ""
leakage_controls:
  preprocessing_fit_scope: train_only
  feature_selection_scope: train_only
  hyperparameter_tuning_scope: validation_only
  duplicate_handling: ""
  homology_or_scaffold_handling: ""
  batch_or_site_handling: ""
```

## leakage_checklist.md

- [ ] preprocessing fit only on train fold
- [ ] normalization/statistics fit only on train fold
- [ ] feature selection fit only on train fold
- [ ] duplicates across splits removed or grouped
- [ ] homologous proteins / related patients / chemical scaffolds grouped as needed
- [ ] batch/site/time/source confounding checked
- [ ] label source does not encode outcome proxy leakage
- [ ] test/external validation not used for model selection

## negative_controls.md

- label shuffle
- feature shuffle or random features
- decoy molecules/sequences/scaffolds if relevant
- easy/hard subgroup checks
- null/background comparison

## model_card.md sections

- model and data summary
- intended use
- training data and exclusions
- split protocol
- metrics and confidence intervals
- calibration/uncertainty
- subgroup/error analysis
- robustness/external validation
- known limitations
- unsupported claims
- reproducibility commands
