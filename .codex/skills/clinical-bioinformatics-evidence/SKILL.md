---
name: clinical-bioinformatics-evidence
description: 用于临床/转化相关生物信息学证据整理，包括 clinical trial、pharmacogenomics、disease association、patient/cohort table、survival/biomarker 结果的科研证据分层和安全边界控制。不提供诊断、治疗或个人医疗建议。
---

# Clinical Bioinformatics Evidence

## 核心问题

如何把临床/转化相关生信证据整理成科研用途的 evidence map，同时避免诊断或治疗建议越界？

## 使用场景

- clinical trial / disease association / biomarker / survival / pharmacogenomics 信息整理。
- 转化方向 target/variant/gene/drug 证据表。
- 审稿或报告中需要区分科研证据、临床关联和医疗建议。

## 不适合触发

- 个人医疗建议、诊断、治疗方案：必须拒绝或转为一般科研信息。
- 药筛/ADMET 工作流：用 `drug-discovery-admet-screening`。
- variant 坐标和数据库核验：用 `variant-genomics-interpretation` 或 `scientific-database-grounding`。

## 工作流程

1. 定义对象：gene/variant/drug/disease/cohort/trial/endpoint。
2. 区分证据：clinical assertion、trial record、biomarker association、survival model、PGx annotation、literature hypothesis。
3. 记录来源、版本/日期、样本/人群、endpoint、effect metric 和限制。
4. 输出科研 evidence map，不写个人化建议。

## 输出格式

- Clinical/translational question
- Sources and dates
- Evidence map
- Safety boundary
- Research next step


## 按需读取

需要选择工具/证据层级时读取 `references/clinical-evidence-boundary.md`。
