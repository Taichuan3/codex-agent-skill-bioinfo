---
name: pathway-network-analysis
description: 用于 gene list、ranked genes 或 omics result table 的 pathway enrichment/GSEA、通路数据库、PPI/graph/module 分析、QC 和证据受限解释；不用于上游差异分析、通用代码实现、绘图-only 或 claim-only 审查。
---

# Pathway Network Analysis

## 核心问题

如何把 gene list 或 ranked omics 结果转成可复现、不过度解释的 pathway/network evidence？

## 边界与组合

- 本 Skill 为 pathway/network 问题定义、方法备选、分析执行、结果 QC 和谨慎解释提供技术支持；用户确认研究问题、方法选择和最终解释。
- 上游 DE、marker、variant calling 或 feature selection 用相应分析 Skill；不得从不清楚的 gene list 反推其生成过程。
- 已确认方法后，若主要交付是可复用脚本、workflow 或通用表格处理，组合 `bioinfo-analysis-code`；本 Skill负责 universe、方法记录和解释边界，不替代用户的科学判断。
- 只生成/美化 enrichment plot 或 network figure 时用 `publication-plotting`；只审查 claim 支持度时用 `claim-evidence-audit`。
- 数据库检索与版本证据可组合 `scientific-database-grounding`，但数据库关联不等于实验验证。

## 工作流程

1. 锁定研究比较、species、gene ID、foreground/background 或完整 ranked list、rank metric、重复 ID 处理、过滤来源和输入效应方向。
2. 依据问题选择 ORA、GSEA/ranked test、pathway activity、PPI/graph、community/module 或 regulon 方法；记录数据库、版本/访问日期和基因集大小限制。
3. 先做 ID mapping 和 universe QC。报告输入数、成功映射数、丢失/重复数；background 必须代表实际可被选中的基因。
4. 运行分析并保存参数、随机种子、multiple-testing correction、完整结果表和必要的 leading-edge/core genes；不得只保存 top terms 图片。
5. 对 term 冗余、基因集重叠、方向、degree bias、edge confidence、node filtering 和稳定性做与方法相称的检查。
6. 将 pathway 名称连接回输入基因、效应方向和 leading edge；将 centrality/community/module 视为优先级或假设生成，除非有独立实验支持。
7. 交付 input/universe contract、方法/数据库版本、映射和 QC、完整与精简结果、可视化建议、安全措辞、limitation 和下一项验证。

## 关键门控

- ORA 不默认用 whole genome；若背景未知，先停在假设或敏感性分析。
- GSEA 明确 rank metric 方向、ties/duplicates、gene-set size、permutation 和空值构造。
- 去冗余或分组不得把多个高度重叠 term 冒充独立机制证据。
- Network 记录 edge source、directionality/weight、confidence、layout seed 与 node/edge filter；hub 不等于功能必需基因。
- Pathway enrichment、inferred activity 和 network topology 通常属于探索性到中等证据，不单独证明机制、因果或治疗价值。

## 按需资源

选择 ORA/GSEA、数据库、network/regulon 方法、关键检查与解释边界时，读取 [pathway-network-decision-matrix.md](references/pathway-network-decision-matrix.md)。

最终回复先给 pathway/network 结果和安全解释，再列输入 universe、方法版本、映射/QC、输出文件、复现入口、局限和未解决风险。
