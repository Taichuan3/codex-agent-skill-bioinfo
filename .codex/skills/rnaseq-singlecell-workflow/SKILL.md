---
name: rnaseq-singlecell-workflow
description: 用于 RNA-seq、single-cell RNA-seq、pseudo-bulk、marker/contrast、QC、批次整合和 splicing/isoform 初步分析的工作流规划、工具选择、结果检查和证据边界控制。适用于 bulk RNA-seq、scRNA-seq、Multiome RNA 层、marker table、DE/DTU/splicing 任务；不负责通用绘图或文献综述。
---

# Rnaseq Singlecell Workflow

## 核心问题

如何把 RNA-seq / single-cell 数据从输入定义、QC、差异/marker 分析到结果解释组织成可复现且证据边界清楚的工作流？

## 使用场景

- bulk RNA-seq differential expression、pseudo-bulk、marker/contrast 表格解释。
- scRNA-seq QC、doublet/batch/integration、cluster annotation、marker validation。
- alternative splicing、isoform switching、long-read RNA-seq 的方法选择和 caveat。
- 从外部 skill 生态吸收 nf-core/rnaseq、nf-core/scrnaseq、Scanpy/Seurat、FRASER/OUTRIDER、rMATS/LeafCutter/MAJIQ 等工作流思路。

## 不适合触发

- 单纯写脚本或表格整理：用 `bioinfo-analysis-code`。
- 论文图生成：用 `publication-plotting`。
- 结果 claim 是否越界：联动 `claim-evidence-audit`。

## 工作流程

1. 锁定输入：FASTQ/BAM/count matrix/h5ad、物种、reference、annotation、样本表、batch 和 contrast。
2. 定义 analysis level：gene、transcript、junction、cell、cluster、pseudo-bulk 或 region/gene-set。
3. 选择工具：优先成熟标准流程；记录版本、参数和过滤标准。
4. QC：library size、mapping/feature counts、mitochondrial/ribosomal、doublet、batch、replicate consistency、marker sanity checks。
5. 输出：结果表、QC 图、source data、解释等级和下一步验证。

## 输出格式

- Task type and input definition
- Recommended workflow/tools
- QC and filtering contract
- Expected outputs and source data
- Evidence level and caveats
- Next validation / reviewer risk


## 按需读取

需要选择工具/证据层级时读取 `references/rnaseq-singlecell-decision-matrix.md`。
