---
name: scientific-english-polishing
description: 用于润色、压缩或重构已有英文标题、摘要、正文、方法、回复信或英文图注，保持术语、数字、caveat 与证据强度。中文或混合文本转英文用 scientific-english-translation，中文输出用 chinese-scientific-polishing；从图和分析信息新写完整 title/panel legend/caption 用 figure-caption。
---

# Scientific English Polishing

## 核心问题

如何在不升级 claim 的前提下，把已有英文科研文本变得更清楚、更精炼、更符合学术表达？

## 路由与边界

- 以来源语言路由：输入已是英文且目标是更清楚、简洁或合适的学术语气时用本 Skill；中文或以中文为主的输入转英文用 `scientific-english-translation`。
- 只改已有英文 caption 的语言时用本 Skill；需要补齐 title、panel、n、统计、编码、source data 或 caveat 时改用或组合 `figure-caption`。
- 中文输出用 `chinese-scientific-polishing`；主要任务是判断 claim 能否成立时先用 `claim-evidence-audit`。
- 不发明数据、文献、机制、novelty 或统计，不静默改变数字、样本、过滤和术语定义。

## 润色契约

- 保留 scientific meaning、evidence level、关键 caveat、样本范围、数据类型和统计限定。
- 不把 association 改为 causation，不把 exploratory、candidate、putative 或 suggestive 改为 demonstrated、established 或 required。
- 一个概念稳定使用一个术语；科学名词不为追求 stylistic variation 而换同义词。
- 先修正段落功能、论证顺序和歧义，再改句式；压缩不得删除改变解释范围的信息。
- Remove machine-local paths, repository/script/raw-table filenames, internal flags or run IDs, raw commands, and unresolved author/editor comments from reader-facing Results, Discussion, and captions. Preserve unresolved scientific questions from those comments as `Risk notes` or explicit author actions, keep reproducibility-critical details in Methods, and retain exact internal provenance in manifests or project records.
- “Nature/CNS 风格”不等于更强措辞；目标期刊 author instructions 优先于通用风格。

## 工作流程

1. 确认文本已是英文，并识别章节、读者、长度、期刊导向和必须保留的术语。
2. 标出核心 claim、证据等级、caveat、数字和术语；疑似事实错误不自行修正。
3. 先处理结构、控制句、指代和术语，再做句子级清晰化与压缩。
4. 对照原文检查意义、数字、术语、claim 强度、section stance 和遗漏。

## 输出格式

- 默认给出可直接替换的 `Polished version`。
- 仅在用户要求时提供 `More concise version` 或替代语气。
- 仅在存在问题时增加 `Risk notes` 或 `Terminology notes`。

## 按需读取

- 局部英文需要检查术语、过强措辞或 section stance 时，读取 `references/style-guardrails.md`。
- 用户明确要求高影响期刊导向或整段 manuscript section 重构时，读取 `references/high-impact-journal-writing.md`；目标期刊规则优先。
