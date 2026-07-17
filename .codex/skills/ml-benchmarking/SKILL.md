---
name: ml-benchmarking
description: 用于生物信息学或 AI for biomedicine 的机器学习 benchmark 设计与审查：task contract、baseline、split protocol、leakage checks、negative controls、ablation、external validation、model card 和可交给 Codex 的实现任务。不用于普通脚本执行或泛泛模型介绍。
metadata:
  hermes:
    tags: [bioinformatics, machine-learning, benchmarking, validation, leakage, model-card]
    related_skills: [bioinfo-analysis-code, validation-strategy-planner, research-data-organization, claim-evidence-audit]
---

# ML Benchmarking

## 核心问题

如何把一个生物医学机器学习想法变成可复现、可比较、无明显 leakage、能支撑安全 claim 的 benchmark？

## 使用场景

当用户要设计、审查或实现机器学习 benchmark 时使用本 skill，例如：

- clinical/genetic risk prediction
- variant/pathogenicity prediction
- protein/ligand/property prediction
- binding affinity / docking score surrogate model
- multi-modal genetics + structure + omics + clinical model
- representation learning 或 generative model evaluation
- 比较多个模型、baseline、ablation 或 external validation

## 不适合触发

- 只需要写普通 Python/R 脚本、处理表格或跑命令时，使用 `bioinfo-analysis-code`。
- 只需要给探索性结果设计验证策略且不涉及 ML benchmark 时，使用 `validation-strategy-planner`。
- 只需要整理数据目录、manifest 或 source data 时，使用 `research-data-organization`。
- 不要为一个没有明确 task、target、split 和 metric 的问题直接推荐复杂模型。

## 原则

- 先 task contract，再模型。
- 先 baseline，再复杂模型。
- split protocol 必须模拟真实应用场景。
- preprocessing、feature selection、normalization、model selection 和 hyperparameter tuning 不得使用 test/external validation 信息。
- performance claim 必须绑定 dataset、split、metric、confidence/uncertainty 和 validation context。
- 生物学/医学解释必须区分 evidence、interpretation、limitation、speculation。
- Agent 提供 benchmark 备选、leakage 风险分析、bounded implementation、测试、provenance 和 sensitivity analysis；用户决定 task、split、metric、模型选择、解释和最终 claim。

## Workflow

1. 定义 task contract：task type、input unit、target、prediction horizon/label source、intended use、forbidden claim。
2. 定义 dataset/provenance：data sources、versions、license、sample inclusion/exclusion、duplicates/homology/scaffold/batch risk。
3. 定义 split protocol：patient-level、family-level、gene/protein-family-level、scaffold split、time split、batch-aware split 或 external cohort。
4. 定义 metrics：primary metric、secondary metrics、calibration、uncertainty、subgroup/error analysis。
5. 建立 baseline：最简单可信模型或规则，不允许直接跳到复杂模型。
6. 设计 leakage checks：preprocessing fit scope、duplicate leakage、homology/scaffold leakage、label leakage、batch/confounder leakage。
7. 设计 negative controls：label shuffle、feature shuffle、decoy/scaffold control、known easy/hard subsets、null background。
8. 设计 ablation：data modality、feature group、architecture component、training data size、preprocessing choices。
9. 设计 robustness/external validation：独立 cohort、orthogonal assay、OOD split、temporal validation、known benchmark comparison。
10. 生成 Codex task contract：只交给 Codex 实现 Dataset/DataModule、split script、baseline runner、evaluation table、tests 和 figure scripts。
11. 产出 model card 和 claim boundary。

## Required artifacts

```text
models/task_definition.md
models/baseline_plan.md
models/split_protocol.md
models/leakage_checklist.md
models/negative_controls.md
models/ablation_plan.md
models/validation_protocol.md
models/model_card.md
reports/model/metrics.tsv
reports/model/calibration_report.md
reports/model/robustness_report.md
reports/model/error_analysis.md
```

## Codex-suitable tasks

- 实现 Dataset/DataModule 和 data loaders。
- 写 split 脚本与 leakage tests。
- 写 baseline train/evaluate runner。
- 写 model comparison table 和 plotting scripts。
- 写 ablation runner。
- 将 notebook 逻辑抽成 `src/` 和 `tests/`。

Codex prompt 必须包含：输入路径、输出路径、schema、split 规则、禁止读取 test fold 的步骤、测试命令和 done definition。

## Output format

- `Task contract`
- `Data/provenance risks`
- `Split protocol`
- `Baseline`
- `Metrics`
- `Leakage checklist`
- `Negative controls`
- `Ablation plan`
- `External validation`
- `Codex implementation tasks`
- `Claim boundary / model card notes`

## Verification

输出合格标准：

- task、target、unit、split、metric 明确；
- 至少一个 baseline；
- leakage checklist 覆盖 preprocessing / feature selection / duplicates / homology or scaffold / batch / label source；
- 有 negative control 和 ablation；
- 有 external validation 或明确说明暂不可行；
- claim 不把 benchmark metric 写成临床、生物学或药物发现最终证明。

需要模板时读取 `references/ml-benchmark-contract.md`。
