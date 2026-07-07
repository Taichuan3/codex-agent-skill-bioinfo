---
name: pathway-network-analysis
description: 用于 gene list、ranked genes、omics result table 的 pathway enrichment、GSEA、Reactome/GO/KEGG/WikiPathways、network/graph 分析和结果解释边界控制。适用于 pathway/network 结果规划、运行后 QC、图表和 claim 审查；不负责原始 RNA-seq 或 variant calling。
---

# Pathway Network Analysis

## 核心问题

如何把 gene list 或 ranked omics 结果转成可复现、不过度解释的 pathway/network evidence？

## 使用场景

- ORA/GSEA/pathway enrichment、Reactome/GO/KEGG/WikiPathways/MSigDB。
- PPI/network/community/centrality/module 分析。
- 富集气泡图、emapplot、network plot 的解释和 caveat。

## 不适合触发

- 上游 DE/marker/variant 分析：用对应分析 skill。
- 单纯绘图实现：用 `publication-plotting`。
- claim 是否被结果支持：联动 `claim-evidence-audit`。

## 工作流程

1. 锁定输入 universe：gene ID type、species、background、rank metric、filter。
2. 选择方法：ORA、GSEA、module/network、Reactome/GO/KEGG/WikiPathways。
3. QC：ID mapping loss、background mismatch、redundant terms、multiple testing、directionality。
4. 输出：ranked pathway table、leading-edge/core genes、visual plan、safe interpretation。

## 外部语料吸收后的关键门控

- ORA 必须写清 foreground 和 background universe；默认 whole genome 背景常会夸大测序/过滤后 gene list 的富集。
- GSEA/ranked analysis 必须锁定 ranking metric、重复 gene handling、gene-set size bounds、permutation strategy 和 direction。
- Pathway terms 需要去冗余或分组；不要把同一层级的 GO/Reactome 重复 term 当成独立机制证据。
- Network/PPI/STRING/GRN 图要记录 edge source 和 confidence；centrality、hub 或 community 只能作为优先级线索，不是功能证明。
- leading-edge/core genes 是最小可解释单位；结果叙述优先连接到这些 genes 和输入效应方向，而不是只报 pathway 名。

## 输出格式

- Input and universe definition
- Method and database version
- QC warnings
- Pathway/network result table
- Safe wording and caveats


## 按需读取

需要选择工具/证据层级时读取 `references/pathway-network-decision-matrix.md`。
