# ML benchmark contract

按任务只使用需要的模板。所有 `planned`、`not assessed` 和污染状态必须显式保留，不得用空白或高指标掩盖。

## Task contract

```yaml
task_type: classification | regression | survival | ranking | generation | representation_learning
prediction_unit: patient | sample | variant | gene | protein | ligand | protein_ligand_pair | cell | sequence_region
inputs: []
target: ""
label_source: ""
prediction_horizon: ""
intended_use: ""
decision_context: ""
forbidden_claims: []
primary_metric: ""
secondary_metrics: []
success_criterion: ""
```

## Dataset and split contract

```yaml
dataset:
  sources: []
  versions: []
  license_or_access: ""
  inclusion_exclusion: ""
  immutable_manifest: ""
  duplicate_or_relatedness_policy: ""
  pretraining_overlap_check: ""
split:
  type: patient | family | group | gene | protein_family | homology | scaffold | site | batch | temporal | external_cohort
  rationale: ""
  train_ids: ""
  validation_ids: ""
  test_ids: ""
  external_ids: ""
  stratification: ""
  random_seeds: []
  test_access_policy: locked_until_final
```

选择 split 时回答：未来预测对象与训练对象在哪个维度真正不同？若实际部署跨患者、家系、site、时间、protein family 或 chemical scaffold，随机行级 split 通常不是充分主验证。

## Baseline and comparison contract

| model_id | role | eligible data | preprocessing | tuning budget | folds/seeds | selection rule |
|---|---|---|---|---|---|---|
| null | trivial baseline | | | none | | fixed |
| simple | classical/rule baseline | | | | | |
| candidate | proposed method | | | | | |

在比较前固定：

- 所有候选使用相同的 eligible samples、fold IDs 和 metric implementation。
- preprocessing、feature selection 和 learned transforms 在每个 training fold 内 fit。
- tuning budget 与 early-stopping 信息等价；若不等价，明确标记。
- 报告 paired differences、confidence interval 或跨 folds/seeds 的分布，而非只报最佳点估计。
- 公开论文或 leaderboard 数字只有在数据版本、split、metric 和 exclusions 可比时才作为直接 baseline。

## Leakage audit

- [ ] normalization/imputation/feature learning 只在 training fold fit
- [ ] feature selection、threshold selection 和 calibration 不读取 test/external labels
- [ ] hyperparameter/model selection 只使用 training/validation information
- [ ] duplicates、technical replicates、related patients 或 repeated measures 不跨不允许的 split
- [ ] homologous sequences、protein families 或 chemical scaffolds 按 intended use 分组
- [ ] site、batch、time、source 和 acquisition artifacts 未成为 outcome proxy
- [ ] label definition、post-outcome variables 和 missingness 未泄漏未来信息
- [ ] pretrained models/features 检查 benchmark contamination 或记录未知状态
- [ ] test/external set 未被反复查看、筛模型、选阈值或改 pipeline
- [ ] split IDs 与 test-access events 可审计

发现 test reuse 时记录：

```yaml
test_status: untouched | accessed_once_final | reused_or_contaminated | unknown
access_events: []
consequence: ""
repair: new_locked_test | external_validation | claim_downgrade | other
```

## Controls, ablations, and robustness

```yaml
negative_controls:
  - label_shuffle
  - feature_shuffle_or_random_features
  - null_or_decoy_background
ablations:
  - modality_or_feature_group_removal
  - architecture_component_removal
  - training_data_size_curve
robustness:
  - repeated_seeds
  - parameter_or_preprocessing_sensitivity
  - subgroup_error_analysis
  - ood_or_temporal_challenge
external_validation:
  status: completed | planned | infeasible | not_assessed
  dataset_or_assay: ""
  independence_from_model_selection: ""
```

按领域选择 controls，不机械填满。每个 control 说明它排除的替代解释、预期失败模式与判定标准。

## Reproducibility record

```yaml
code_revision: ""
input_manifest_and_hash: ""
split_ids_and_hash: ""
environment_lock: ""
random_seeds: []
hardware_and_nondeterminism: ""
train_command: ""
evaluate_command: ""
artifact_paths:
  metrics: ""
  predictions: ""
  calibration: ""
  errors: ""
  model: ""
artifact_hashes: {}
```

最小可追踪 artifacts：

```text
models/task_definition.md
models/dataset_manifest.tsv
models/split_protocol.md
models/baseline_plan.md
models/leakage_checklist.md
models/comparison_plan.md
models/controls_and_ablations.md
models/validation_protocol.md
models/model_card.md
reports/model/metrics.tsv
reports/model/predictions.tsv
reports/model/calibration_report.md
reports/model/error_analysis.md
reports/model/robustness_report.md
```

路径服从项目 `AGENTS.md`；不要为迁就模板静默迁移成熟项目。

## Model card and claim boundary

至少记录：

- model/data summary、intended use 和 unsupported use
- training/evaluation data、exclusions、split 和 test-access status
- metric definitions、confidence intervals、calibration 与 threshold policy
- subgroup/error analysis、robustness、external validity 和 failure modes
- code/data/split/environment provenance 与 reproduction commands
- supported performance statement、unsupported biological/clinical claims 和 remaining validation

安全句式：

> 在 `[dataset/version]` 的 `[split]` 下，模型对 `[prediction unit/target]` 的 `[metric]` 为 `[estimate, uncertainty]`；结果支持该评估条件下的预测性能，不单独证明生物学机制、临床效用或外部泛化。
