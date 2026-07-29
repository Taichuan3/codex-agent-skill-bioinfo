---
name: paper-reader
description: 用于阅读用户指定的科研论文、PDF、全文 markdown 或网页论文，并输出中文结构化阅读笔记、关键证据、figure grounding、可借鉴方法和局限。不用于开放式文献检索；需要查找新文献时使用 literature-search-workflow。
---

# Paper Reader

## 核心问题

如何从一篇指定论文中提取可验证证据、figure grounding、方法启发和局限，而不是泛泛总结？

## 使用场景

当用户指定一篇或少量论文，希望理解其研究问题、方法、证据、图表和可借鉴点时使用本 skill。目标是帮用户读懂论文，而不是替作者扩展未证明结论。

## 核心原则

- 只基于用户提供或明确指定的论文内容。
- 区分作者结论、数据支持、解释假设和读者可借鉴方法。
- figure/table 必须对应到支持的 claim。
- 不把单篇论文结论自动泛化到用户项目。
- 长论文优先压缩为可维护摘要，不全文翻译。

## 工作流程

1. 确认输入：PDF、全文、DOI、链接、用户摘录或图表。
2. 提取 paper identity：题目、作者、年份、期刊、研究对象、数据类型。
3. 识别 central question、main claim 和 study design。
4. 按 figure/table 提取证据链：每张图回答什么、用了什么数据、支持什么 claim。
5. 总结可借鉴方法、可复用工具、关键参数、局限和潜在偏差。
6. 标记与用户项目可能相关但需要独立验证的点。

## 输出格式

优先输出：

- `One-sentence take-home`
- `Research question`
- `Data and methods`
- `Main claims and evidence`
- `Figure grounding`
- `Reusable ideas for our project`
- `Limitations / caveats`
- `Follow-up questions`

需要精读图表时，读取 `references/figure-grounding-template.md`。
