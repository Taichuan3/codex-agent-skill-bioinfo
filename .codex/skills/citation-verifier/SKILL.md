---
name: citation-verifier
description: 用于逐条核验科研文本、参考文献表、DOI、PMID、BibTeX 或审稿回复中的 citation identity、题录准确性、可解析性、重复项和 claim-to-citation 支撑范围，并给出保留、修正、替换或删除建议；不用于开放式找文献、精读整篇论文、格式美化或审查无 citation 的项目结果。
---

# Citation Verifier

## 核心问题

如何确认一条 citation 真实、题录正确，并确实支持它旁边的最小 claim？

## 能力边界

- 本 Skill 拥有 citation existence、identifier resolution、metadata accuracy 和 claim-to-citation fit。
- 需要发现一个领域的 paper set 或系统补文献时，改用 `literature-search-workflow`。
- 需要精读指定论文的完整证据链时，改用 `paper-reader`；本 Skill 只读取判断 citation fit 所需的最小原文。
- 只查 gene/variant/protein 等数据库实体时，改用 `scientific-database-grounding`。
- 无 citation 的项目 claim、figure 或 source-data 审查交给 `claim-evidence-audit`。
- 仅调整引用样式、编号或 reference manager 格式不需要本 Skill，除非同时要求真实性或匹配核验。

## 核验边界

- 不凭记忆确认文献；用 DOI/PMID resolver、PubMed/Crossref/Europe PMC、期刊记录或全文交叉核验。
- 分开判定 `identity`、`metadata`、`accessed evidence` 和 `claim support`；metadata 正确不等于支持 claim。
- 摘要只能支持摘要明确陈述的范围；机制、方法参数、数值或 subgroup claim 优先核对全文、figure/table 或 supplement。
- 不能访问必要证据时标记 `unverified` 或 `partially verified`，不得把“未发现”写成“伪造”。
- 区分 primary evidence、review、method paper、database annotation 和 retracted/corrected record。

## 工作流程

1. 抽取最小 claim、citation marker 和 reference entry，建立一一或一对多映射。
2. 解析 DOI、PMID、题名、作者、年份、期刊、volume/pages/article number 和版本。
3. 用权威 metadata source 核验 identity、纠错/撤稿状态、重复项和 identifier 冲突。
4. 定位支持 claim 的原文位置，判断 population/system、condition、endpoint、direction、magnitude 和 evidence type 是否匹配。
5. 按风险分类并记录证据：fabricated/unresolved、metadata error、claim mismatch、scope mismatch、review-vs-primary 或 method-only。
6. 给出 `keep`、`correct metadata`、`narrow wording`、`replace`、`add primary citation`、`remove` 或 `needs full text`。
7. 报告已核验来源、无法访问项和未解决风险；不得自动改写整个 bibliography，除非用户授权。

## 按需读取

需要统一错误代码、风险分类和处置标签时，读取 `references/citation-risk-types.md`。

## 交付契约

优先输出 `Claim | Citation | Identity | Metadata | Evidence inspected | Supports claim | Risk | Action`。每个 `verified` 结论都应有可定位来源；批量任务报告总数、verified/partial/unverified counts、重复项和未检查范围。
