---
name: scientific-english-polishing
description: 英文润色模块：润色、压缩或重构已有英文科研文本，去除套话和机械表达，保护数字、术语、限定与证据强度。中文转英文用 scientific-english-translation，中文修改用 chinese-scientific-polishing，指定桥本风格用 hashimoto-scientific-writing；从图和分析信息起草完整图注用 figure-caption。
---

# 英文润色

## 核心问题

如何在不升级 claim 的前提下，把已有英文科研文本变得更清楚、更精炼、更符合学术表达？

## 路由与边界

- 以来源语言路由：输入已是英文且目标是更清楚、简洁或合适的学术语气时用本 Skill；中文或以中文为主的输入转英文用 `scientific-english-translation`。
- 只改已有英文 caption 的语言时用本 Skill；需要补齐 title、panel、n、统计、编码、source data 或 caveat 时改用或组合 `figure-caption`。
- 中文输出用 `chinese-scientific-polishing`；主要任务是判断 claim 能否成立时先用 `claim-evidence-audit`。
- `hashimoto-scientific-writing` 是独立风格模块，仅在用户指定时联用；本 Skill 不默认模仿 Hashimoto。整条四模块流水线不是每次必须全部执行的清单。
- 不发明数据、文献、机制、novelty 或统计，不静默改变数字、样本、过滤和术语定义。

## 润色契约

- 保留 scientific meaning、evidence level、关键 caveat、样本范围、数据类型和统计限定。
- 不把 association 改为 causation，不把 exploratory、candidate、putative 或 suggestive 改为 demonstrated、established 或 required。
- 一个概念稳定使用一个术语；科学名词不为追求 stylistic variation 而换同义词。
- 先修正段落功能、论证顺序和歧义，再改句式；压缩不得删除改变解释范围的信息。
- Remove machine-local paths, repository/script/raw-table filenames, internal flags or run IDs, raw commands, and unresolved author/editor comments from reader-facing Results, Discussion, and captions. Preserve unresolved scientific questions from those comments as `Risk notes` or explicit author actions, keep reproducibility-critical details in Methods, and retain exact internal provenance in manifests or project records.
- “Nature/CNS 风格”不等于更强措辞；目标期刊 author instructions 优先于通用风格。
- 默认采用本地 Nature-informed 写作机制，并在末轮进行科研约束下的自然表达检查；不模仿原句，不强制增删标题，不替代科学审查。
- 输入充分时交付请求范围内的完整连续正文，而非只给建议或提纲；已经成熟的句段可以不改。局部修改不得牵动未授权章节。

## 工作流程

1. 确认文本已是英文，并识别章节、读者、长度、期刊导向和必须保留的术语。
2. 标出核心 claim、证据等级、caveat、数字和术语；疑似事实错误不自行修正。
3. 先处理结构、控制句、指代和术语，再做句子级清晰化与压缩。
4. 在完整改稿上检查空泛意义、无依据对比、重复结尾、机械排比和聊天痕迹；改的是无效表达，不是科学术语或必要限定。
5. 对照原文检查意义、数字、术语、claim 强度、section stance 和遗漏。遇到数值冲突或无法判定的科学歧义，完成不受影响部分并列出待核实项，不擅自选值。

## 输出格式

- 默认给出可直接替换的 `Polished version`。
- 仅在用户要求时提供 `More concise version` 或替代语气。
- 仅在存在问题时增加 `Risk notes` 或 `Terminology notes`。
- 不承诺发表、接收或通过 AI 检测；说明是否核查了数据，语言自检不等于科学验证。文件修改按用户指定路径/版本交付，必要状态收尾归 `project-state-maintenance`，不因润色重建项目管理。

## 按需读取

- 英文科研段落/章节润色默认读取 `references/integrated-writing-profile.md`；仅拼写、单词或纯格式修正无需加载。用户明确风格优先，已有英文与中译英共享本文件，不重复维护两套风格。
- 实质英文润色的末轮读取 `references/research-humanizer.md`；用户只要拼写/格式修正时不扩大编辑范围。
- 局部英文需要检查术语、过强措辞或 section stance 时，读取 `references/style-guardrails.md`。
- 用户明确要求高影响期刊导向或整段 manuscript section 重构时，读取 `references/high-impact-journal-writing.md`；目标期刊规则优先。
