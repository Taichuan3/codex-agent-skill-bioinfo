---
name: paper-reader
description: 用于精读用户指定的一篇或固定少量科研论文、PDF、全文网页、markdown、补充材料或指定图表，提取研究设计、figure/table 证据链、claim 边界、方法参数、可复用资源和局限；不用于开放式找文献、数据库实体查询、参考文献表核验或稿件全局审计。
---

# Paper Reader

## 核心问题

如何从指定论文中提取可定位、可复核且不超出原文的证据？

## 能力边界

- 本 Skill 拥有固定 paper set 的全文阅读、结构化理解和 figure/table grounding。
- 需要发现或筛选新 paper set 时，改用 `literature-search-workflow`。
- 只核验 DOI/PMID、题录或 claim-to-citation 匹配时，改用 `citation-verifier`。
- 只查数据库实体记录时，改用 `scientific-database-grounding`。
- 跨稿件检查 claim 强度或内部一致性时，分别改用 `claim-evidence-audit` 或 `manuscript-consistency-audit`。
- 不把单篇论文结论自动迁移为用户项目事实，也不代替方法复现或独立验证。

## 输入与访问边界

- 优先读取用户提供的 PDF/全文/补充材料或明确指定的链接、DOI、PMID。
- 只有 metadata/abstract 时，清楚标记 `metadata-only` 或 `abstract-only`；不得补写未见的实验细节、图表结果或局限。
- PDF/OCR/网页抽取不完整时记录缺页、不可读 figure、supplement 缺失和访问限制。
- 引用原文时保持短摘录并定位到 page、section、figure、table 或 supplement；其余内容用忠实释义。

## 工作流程

1. 核验 paper identity、版本和可用材料，区分 preprint、accepted manuscript 与 version of record。
2. 提取 central question、study system、design、sample/data、comparison、endpoint 和主要假设。
3. 建立 claim–evidence 表：作者 claim、支持的 figure/table、数据、分析、结果和 caveat。
4. 对关键 figure/table 检查 panel、axis/legend、sample size、control、statistical definition 和 supplement 依赖。
5. 提取可复用方法、参数、software/version、data/code accession，以及复现所缺信息。
6. 区分作者解释、数据直接支持、读者推断和未验证机制；指出外推范围。
7. 输出与用户问题相关的 take-home、局限和 follow-up，不做无关全文翻译。

## 按需读取

需要逐图精读、panel-to-claim 映射或 figure/table 证据表时，读取 `references/figure-grounding-template.md`。

## 交付契约

至少交付 paper identity、access scope、research question、design/data/methods、main claims with evidence locations、limitations 和 follow-up questions。若用户要求比较固定少量论文，使用同一字段逐篇提取后再比较，避免把跨论文解释写成任一作者的结论。
