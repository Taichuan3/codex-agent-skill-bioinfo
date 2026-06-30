---
name: variant-genomics-interpretation
description: 用于 variant/genomics 任务中的 VCF/BCF、GWAS、QTL、ClinVar/gnomAD/dbSNP、colocalization、PRS 或 rare-variant 结果解释、数据库 grounding、QC 和证据边界控制。不用于临床诊断或个人医疗建议。
---

# Variant Genomics Interpretation

## 核心问题

如何把 variant/genomics 结果从坐标、等位基因、频率、功能注释和遗传证据组织成可追踪、不过度解释的证据表？

## 使用场景

- VCF/BCF variant annotation、ClinVar/dbSNP/gnomAD/Ensembl VEP 结果解释。
- GWAS/QTL/colocalization/MR/PRS/rare variant 分析的证据边界和 QC。
- 需要和 `scientific-database-grounding` 联动核验 build、allele、transcript 和 population frequency。

## 不适合触发

- 纯数据库 ID 查询：用 `scientific-database-grounding`。
- 通用代码执行：用 `bioinfo-analysis-code`。
- 临床诊断或个人医疗建议：拒绝或降级为科研信息整理。

## 工作流程

1. 锁定 genome build、coordinate、REF/ALT、strand、transcript/isoform、population/background。
2. 判断证据类型：annotation、frequency、association、colocalization、causal inference、clinical assertion、functional validation。
3. 检查冲突：build mismatch、allele flip、LD proxy、isoform difference、population mismatch、curated vs predicted。
4. 输出 evidence table：variant/entity、source、metric、support level、caveat、next validation。

## 输出格式

- Entity and build/allele definition
- Databases/tools consulted
- QC/conflict checks
- Evidence table
- Claim boundary and next validation


## 按需读取

需要选择工具/证据层级时读取 `references/variant-genomics-evidence-matrix.md`。
