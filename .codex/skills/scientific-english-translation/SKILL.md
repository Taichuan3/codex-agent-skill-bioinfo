---
name: scientific-english-translation
description: 用于把中文或以中文为主的科研文本忠实翻译为英文，适用于摘要、正文、方法、回复信、标题和既有图注，并保护术语、数字、章节职责与证据强度。已有英文文本的语言改写用 scientific-english-polishing，中文输出用 chinese-scientific-polishing；需要从图和分析信息起草完整 figure title/panel legend/caption 时用 figure-caption。
---

# Scientific English Translation

## 核心问题

如何把中文科研草稿翻译成证据边界安全、可投稿语气的英文表达？

## 路由与边界

- 以来源语言和目标语言路由：中文或中英混合输入、目标为英文时用本 Skill；已有英文的清晰度和风格修改用 `scientific-english-polishing`。
- 只翻译现成中文图注时用本 Skill；需要决定 caption 应包含哪些 panel、n、统计、编码、source data 或 caveat 时改用或组合 `figure-caption`。
- 只需要中文改写时用 `chinese-scientific-polishing`；主要任务是验证 claim 时先用 `claim-evidence-audit`。
- 不发明数据、文献、样本数、统计、机制或术语定义，不静默纠正疑似错误数字。

## 翻译契约

- 先忠实保留 scientific meaning、evidence boundary、数字、限定词和章节职责，再改善英文流畅度。
- 不把相关性翻译成因果，不把 candidate、putative 或 exploratory 结果翻译成 demonstrated、established 或 mechanistic conclusion。
- 一个中文概念稳定映射为一个英文术语；原文术语不一致时选择最保守映射并标记歧义。
- Results 保持观察性，Discussion 可解释但保留限制，Methods 不压缩掉复现信息。
- “Nature/高影响期刊风格”只改变选择、结构与简洁度，不授权新增 novelty 或增强 claim。

## 工作流程

1. 确认英文目标、章节、读者、期刊导向、长度和必须保留的术语。
2. 提取 claim、直接证据、caveat、数字和术语映射；遇到歧义先保守处理并标记。
3. 先完成忠实英文版，再按用户要求压缩或调整期刊语气。
4. 逐项回对原文，检查遗漏、增译、数字、术语、claim 强度和 section function。

## 输出格式

- 默认给出可直接使用的 `English version`。
- 仅在用户要求时给出 `Concise` 或 journal-leaning variant。
- 仅在存在歧义或证据风险时增加 `Risk notes`；复杂术语才给 `Terminology map`。

## 按需读取

- 需要选择 faithful、concise 或 journal-leaning stance，或原文术语不稳定时，读取 `references/translation-stance.md`。
- 用户明确要求高影响期刊导向或需要维护 manuscript section function 时，读取 `references/high-impact-journal-translation.md`；目标期刊规则优先。
