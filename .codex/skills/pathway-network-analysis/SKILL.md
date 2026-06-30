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

## 输出格式

- Input and universe definition
- Method and database version
- QC warnings
- Pathway/network result table
- Safe wording and caveats


## 按需读取

需要选择工具/证据层级时读取 `references/pathway-network-decision-matrix.md`。
