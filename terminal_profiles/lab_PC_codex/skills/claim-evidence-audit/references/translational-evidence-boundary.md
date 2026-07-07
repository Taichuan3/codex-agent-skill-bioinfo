# Translational Evidence Boundary

用于审查 clinical/translational、variant interpretation、drug repurposing、target validation 和 ADMET/QSAR 文本中的 claim 边界。

## 常见越界

- 把 ClinVar clinical significance 写成当前项目验证。
- 把 Open Targets、PrimeKG、pathway/network association 写成 causal mechanism。
- 把 ClinicalTrials.gov 的 registered/active/recruiting 状态写成疗效证据。
- 把 OpenFDA label/adverse event/reporting signal 写成风险定量结论。
- 把 docking、ADMET、QSAR 或 virtual screening rank 写成 binding affinity、efficacy 或 safety。
- 把 database disease-gene 或 drug-target association 写成 approved indication。

## 审查字段

- Evidence source and date
- Evidence type: curated / submitted / predicted / inferred / experimental / clinical trial / label / observational
- Review or confidence status when available
- Population, tissue, disease subtype or assay context
- Whether the current project generated direct data
- Whether independent validation exists

## 安全写法

- Strong：当前项目直接结果 + source data + 方法可复现，且外部证据一致。
- Moderate：当前结果与多个外部数据库/文献方向一致，但缺少直接功能或临床验证。
- Exploratory：数据库、模型、screen、enrichment、network 或 docking 提示候选方向。
- Speculative：仅有机制想象或弱关联。

默认把 database- or model-only translational statements 限制为 Exploratory；需要写入 Results 时使用 “is consistent with”, “prioritizes”, “suggests a candidate”, “is annotated as”, “has been reported in” 等表述，避免 “demonstrates”, “drives”, “treats”, “is safe/effective”。
