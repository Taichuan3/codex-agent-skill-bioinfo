---
name: chinese-scientific-polishing
description: 用于把已有或目标输出为中文的科研文本做语言润色、压缩和段落结构优化，适用于摘要、引言、结果、讨论、方法、报告和审稿回复。中文转英文用 scientific-english-translation，已有英文润色用 scientific-english-polishing；完整图题、panel legend 或 caption 的起草与内容完整性审查用 figure-caption，仅润色既有中文图注时才用本 Skill。
---

# Chinese Scientific Polishing

## 核心问题

如何在不改变证据强度的前提下，让中文科研文本更清楚、更顺、更像给真实读者看的研究叙事？

## 路由与边界

- 以目标语言和主要交付物路由：中文语言/结构修改用本 Skill；中文或混合草稿转英文用 `scientific-english-translation`；已有英文文本改写用 `scientific-english-polishing`。
- 只润色已有中文图注时用本 Skill；需要补齐 figure title、panel 顺序说明、统计、n、编码、source data 或 caveat 时改用或组合 `figure-caption`。
- 若主要任务是判断 claim 是否由数据支持，先用 `claim-evidence-audit`；本 Skill 不替代证据审查。
- 不发明数据、文献、统计、机制或新结论，不静默改变数字、样本范围、过滤或术语定义。

## 证据与写作契约

- 区分 evidence、interpretation、limitation 和 speculation；不得把相关性、候选机制或探索性结果升级为因果、机制或确定结论。
- 保留关键 caveat、数据类型、样本范围和统计限定；无法确认的内容标记为待核实，不替作者补全。
- 一个概念稳定使用一个术语；只有层级或对象确实不同才并用近义术语，并先定义区别。
- 按章节职责控制语气和数据密度：Results 陈述观察，Discussion 解释意义与边界，Methods 优先可复现性。
- 若草稿明确提示缺图、缺数据或 claim 未闭合，先列 revision backlog 或 claim-to-figure 缺口，不把待证实内容润色成定稿。

## 工作流程

1. 确认目标是中文输出，并识别章节、读者、长度、语气和必须保留的术语。
2. 标出核心 claim、直接证据、限定词和不可改动的数字；证据缺口先暂停成稿化。
3. 先修正段落功能、控制句、证据顺序和术语歧义，再做句子级润色。
4. 压缩不服务主线的重复与数字，但保留改变解释范围的限定。
5. 对照原文检查意义、数字、术语、claim 强度和章节职责；只报告确实存在的风险。

## 输出格式

- 默认给出可直接替换的 `润色版`。
- 发生实质结构、术语或 claim 调整时，简列 `主要修改点`。
- 仅在存在问题时增加 `待核实/风险`；不要为无风险短文本附加空模板。

## 按需读取

- 章节职责或小节结构不清时，读取 `references/section-responsibilities.md`。
- 需要系统检查结构、数据密度、术语和过强措辞时，读取 `references/polishing-checklist.md`。
- 用户明确要求高影响期刊导向或整段 manuscript 结构时，读取 `references/high-impact-journal-writing.md`；目标期刊规则优先。
- 外部读者报告需要去除内部编辑痕迹，或用户同时要求交付包时，读取 `references/external-report-polishing-and-bundling.md`；文本润色本身不授权创建或打包文件。
