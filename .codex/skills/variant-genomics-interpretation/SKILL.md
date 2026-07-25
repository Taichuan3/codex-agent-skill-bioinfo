---
name: variant-genomics-interpretation
description: 解释或审查 variant 与 statistical-genetics 证据，包括 VCF/BCF callset QC、build/REF/ALT/HGVS 标准化、功能注释、population frequency、ClinVar、GWAS、fine-mapping、QTL/colocalization、rare-variant、PRS 和 MR 结果。用于需要解决 allele/build/population/LD 冲突并形成可追踪证据表的科研任务；不负责 variant-calling 执行、临床诊断、个人风险或治疗建议。
---

# Variant and Genomics Interpretation

## 核心问题

如何把 variant identity、callset 质量、数据库注释与统计遗传证据连接成可审计解释，同时避免把预测、关联或共享信号写成致病性、因果或临床结论？

## 能力边界

- 负责已有 variant/callset、locus 或 statistical-genetics 结果的科研解释与 QC 审查。
- 不默认重跑 variant calling、joint genotyping 或硬过滤；实现型调用流程转交 `bioinfo-analysis-code` 或相应项目 workflow。
- 简单、单源 ID 查询转交 `scientific-database-grounding`；跨来源解释仍由本 Skill 负责。
- trial、cohort、biomarker、PGx 或临床行动证据转交 `clinical-bioinformatics-evidence`。
- 不输出个人诊断、风险告知、筛查、用药或生育建议；不得把数据库标签直接应用到个人。

## 首要门控

解释前明确最可能改变结论的 1–3 项：

1. genome build、coordinate、REF/ALT、strand、normalization 和 transcript；
2. callset/sample QC、analysis population、ancestry、phenotype 与 effect allele；
3. 证据类别、数据版本/日期、LD reference、模型假设与目标 claim。

关键 identity 未解析时停止跨库合并；不得用 rsID 或 HGVS 单独替代规范化 allele identity。

## 工作流

1. 锁定模式：`variant record`、`callset QC review`、`locus/statistical evidence`、`conflict resolution` 或 `research evidence table`。
2. 读取项目 `AGENTS.md`、variant manifest/header、样本/phenotype 表、reference 与产生结果的 config；原始 VCF/BCF 只读。
3. 规范化实体：build、chr:pos、REF/ALT、variant type、strand、transcript/HGVS 和 multi-allelic representation。
4. 核验上游 QC：sample identity、sex、contamination、missingness、depth、filter、normalization 和 population structure。
5. 按证据类型读取合适资源并保留 source、release/query date、population、metric、allele direction 与 review status。
6. 显式检查 build mismatch、allele flip、palindromic ambiguity、LD proxy、transcript difference、population mismatch 与 predicted/curated 冲突。
7. 形成 evidence table；把 observation、model-dependent inference、limitation 和 unresolved conflict 分列。
8. 给出可证伪的下一项验证，不用综合分数掩盖来源差异。

## 分支路由

- 单 variant、VCF record、HGVS、ClinVar/gnomAD/VEP 或 callset QC：读取 `references/variant-record-interpretation.md`。
- GWAS、fine-mapping、QTL/colocalization、rare-variant、PRS 或 MR：读取 `references/statistical-genetics-interpretation.md`。
- 需要比较来源、字段与 claim 上限：读取 `references/variant-genomics-evidence-matrix.md`。

## 执行后端

- 实际 lookup 读取 `../../capability_registry.json` 的 `CAP-VAR-001`，按证据类型选择 ClinVar、gnomAD、Ensembl、GWAS/QTL 或 locus-to-gene leaf Skill；不要让聚合器替代 allele/build normalization。
- 只有用户授权 variant-calling 执行且输入、reference、样本设计和运行环境齐全时，才转交 NGS calling backend；本 Skill 保留解释与证据表所有权。
- registry 不授权安装、凭据或临床使用。记录 backend/version、query/callset provenance、resolved allele、空/失败状态和 downstream handoff。

## 证据边界

- 计算 consequence、conservation、motif 或 regulatory overlap 是 context/prediction，不单独证明功能或致病性。
- population frequency 受 ancestry、coverage、filters 与 ascertainment 影响；“rare”不等于 pathogenic。
- GWAS association 不等于 causal variant/gene；fine-mapping credible set 依赖 LD、model 与 variant coverage。
- colocalization 支持模型假设下的共享信号，不自动识别 causal variant、gene、direction 或 mechanism。
- MR 依赖 relevance、independence、exclusion restriction 等假设；敏感性分析不能证明所有假设成立。
- PRS 是特定训练、LD、ancestry、phenotype 与 calibration 条件下的模型输出，不得转为个人风险建议。
- ClinVar assertion 必须保留 condition、review status、submitter/conflict 和 evaluation date；它不是个人诊断。

## 交付

先给实体与主要证据结论，再给 build/allele 定义、QC、来源与版本、evidence table、冲突、claim 上限、下一项验证及临床安全边界。不得自称最终 variant classification 或临床审批。
