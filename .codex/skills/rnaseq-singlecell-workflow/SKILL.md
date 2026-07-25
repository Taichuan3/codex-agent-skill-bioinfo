---
name: rnaseq-singlecell-workflow
description: 规划、执行或审查 bulk RNA-seq 与 single-cell RNA-seq 工作流，包括 FASTQ/BAM/count matrix/h5ad 输入、QC、定量、差异表达、pseudo-bulk、cluster/marker、batch/integration、splicing/isoform 和 regulon 结果。用于需要锁定样本设计、reference、过滤、工具参数、可复现产物与表达证据边界的 RNA 分析；不用于通用代码、绘图、variant 解释或临床证据审查。
---

# RNA-seq and Single-cell Workflow

## 核心问题

如何把 bulk RNA-seq 或 scRNA-seq 从输入与实验设计推进到可复现结果，同时避免把技术结构、marker 或差异信号升级为机制与因果结论？

## 能力边界

- 负责 RNA 工作流的设计、受控执行、QC、结果表和方法审查；只读请求不得修改数据或运行分析。
- 原始 FASTQ/BAM、原始 counts 和原始 cell matrix 只读；派生产物写入项目约定目录。
- 不替用户静默选择样本、contrast、reference/annotation、QC 阈值、batch covariate 或统计定义。
- 通用脚本工程交给 `bioinfo-analysis-code`；成图交给 `publication-plotting`；claim 强度专项审计交给 `claim-evidence-audit`。
- variant/genomics 证据转交 `variant-genomics-interpretation`；clinical/trial/cohort 证据转交 `clinical-bioinformatics-evidence`。

## 首要门控

执行前明确最可能改变路线的 1–3 项：

1. 输入层级、原始数据可用性及其 provenance；
2. biological replicate、sample identity、batch、condition 和 contrast；
3. 物种、genome build、annotation、library chemistry、strandedness 或 assay 类型。

任一关键项未知时，标记 `Assumption` 或 `Open question`；不得用工具默认值掩盖。

## 工作流

1. 锁定模式：`plan`、`execute`、`QC/review`、`result interpretation` 或 `repair`。
2. 读取项目 `AGENTS.md`、样本表、输入 schema 和已有 workflow/config；扫描大型数据目录前先读 Directory Card。
3. 写 analysis contract：analysis unit、replicate、design、contrast、reference、输入/输出、过滤、版本和 stop condition。
4. 先在 1–2 个代表样本或小矩阵上检查 schema、日志、输出数量和磁盘，再扩展大任务。
5. 执行对应分支并保留 command/config、software/reference provenance、QC 和排除理由。
6. 在统计前检查 identity、replicate consistency、depth/complexity、outlier、batch 与模型可辨识性。
7. 输出分析就绪矩阵、QC、结果表、source data、方法定义和 caveat；不要只交付图片或工具日志。
8. 区分 evidence、interpretation、limitation 和 speculation，并列出 reviewer risk 与下一项验证。

## 分支规则

- bulk RNA-seq、count matrix、DE、DTU 或 junction/splicing：读取 `references/bulk-rnaseq-execution.md`。
- scRNA-seq、pseudo-bulk、annotation、integration 或 Multiome RNA 层：读取 `references/single-cell-rnaseq-execution.md`。
- 需要在工具类别、analysis unit 或证据层级间选择：读取 `references/rnaseq-singlecell-decision-matrix.md`。
- 同一任务同时包含 bulk 与 scRNA 时，分别执行两个分支，再用共同的 sample/reference/provenance 字段衔接；不要把 cell 当作独立 biological replicate。

## 执行后端

- 实际执行前读取 `../../capability_registry.json` 的 `CAP-RNA-001`：先用已安装 NGS plugin 做 assay routing、runtime/reference preflight 和小 fixture；需要 FASTQ-to-matrix 生产流程时再采用固定 release 的 nf-core/Nextflow。
- preflight 或 registry 不是安装授权。必须先审查 install plan、executor/container、reference 体积、license、磁盘和服务器策略；失败时停在 plan/review，不改用未记录环境。
- 运行记录至少包含 backend/pipeline release、profile/executor、sample sheet、reference、command/config、成功/失败计数、QC 和输出 manifest。

## 证据边界

- 差异表达支持给定设计下的表达关联，不单独证明通路激活、调控方向、疾病机制或治疗效应。
- cluster 和 marker 依赖预处理、表示空间、分辨率与 annotation reference；不得把聚类标签当作天然真值。
- 条件比较优先使用 sample-aware pseudo-bulk 或明确处理 donor 重复测量的模型；大量 cell 不能补偿 biological replicate 不足。
- integrated/latent 表示主要用于结构与批次校正，不默认作为基因层差异检验输入。
- 3' tag scRNA-seq 通常不足以支持强 isoform/splicing claim；junction、coverage 与 event definition 必须可追踪。
- regulon activity、motif enrichment 和 co-expression 不等于 TF expression、直接结合或因果调控。

## 交付

先报告推荐或实际完成的工作流，再给输入与设计、精确产物、QC/过滤、版本与命令、验证边界、未解决风险和需用户决定的下一步。不得自称完成最终科学审批。
