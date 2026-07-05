---
name: citation-verifier
description: 用于核验科研文本中的引用、DOI、PMID、BibTeX、参考文献条目和 claim-to-citation 是否匹配，防止引用幻觉、错误文献、错配 citation 或 unsupported citation。适用于论文写作、投稿前检查、文献表整理和审稿回复。
---

# Citation Verifier

## 使用场景

当任务涉及引用是否真实、引用格式是否正确、某条 citation 是否支持某个 claim、参考文献列表是否一致时使用本 skill。

## 核心原则

- 不凭记忆确认引用真实性。
- 每条引用必须能追踪到 DOI、PMID、URL、BibTeX 或用户提供的文献条目。
- 区分 citation existence、metadata accuracy、claim support 三类问题。
- 引用能支持背景事实，不代表能支持用户项目的新结论。

## 工作流程

1. 抽取待核验 claim 和对应 citation。
2. 检查 citation identity：题目、作者、年份、期刊、DOI/PMID。
3. 判断文献是否真正支持该 claim。
4. 标记错误类型：不存在、metadata 错、引用错配、支持过弱、需要更合适引用。
5. 给出保留、替换、删除或补充引用建议。

## 输出格式

| Claim | Citation | Exists | Metadata | Supports claim | Risk | Action |
|---|---|---|---|---|---|---|

需要详细错误分类时读取 `references/citation-risk-types.md`。
