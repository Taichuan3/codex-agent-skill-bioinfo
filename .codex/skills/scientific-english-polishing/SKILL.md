---
name: scientific-english-polishing
description: 用于已有英文科研文本的润色、压缩、段落重构、Nature/CNS-leaning academic style 和学术语气检查；必须保护证据边界，不能升级科学 claim。中文到英文翻译优先使用 scientific-english-translation，中文内部润色优先使用 chinese-scientific-polishing。
---

# Scientific English Polishing

## 使用场景

当用户提供已有英文文本并要求英文润色、Nature/CNS-leaning style、摘要压缩、标题优化、response letter 改写或 figure legend 英文打磨时使用本 skill。

## 核心原则

- 先确认 claim 的证据等级，再改英文。
- 不为了语言更强而把 association 写成 causation。
- 不把 exploratory、candidate、putative、suggestive 结果写成 demonstrated、established、required。
- 保留项目 profile 中定义的术语和禁止性表达。
- 保持 scientific terminology 一致性。同一概念、对象或结构层级必须使用同一英文术语；不要为了 stylistic variation 把同一对象在相邻句中改写为不同名词，例如未定义差异时不要在 `element`、`copy`、`unit`、`locus`、`sequence` 之间来回切换。
- 只有在不同术语代表不同层级或不同对象时才并用，并应在文本中明确边界。
- 能压缩就压缩，但不能删除关键 caveat、样本范围、数据类型和统计限定。
- 润色完成后先自检再输出。风险说明、术语说明和替代表达只在确有必要时给出，避免把无问题文本附加过多说明。

## 工作流程

1. 读取根 `AGENTS.md`、当前项目 profile 和用户给定文本。
2. 标出文本中的核心 claim、证据等级和必须保留的 caveat。
3. 建立或保留 terminology map，检查同一概念是否被多个英文词替换、代词是否指代不清。
4. 先修正结构、术语歧义和过强 claim，再进行句子层面润色。
5. 对高风险表达给出替代表述，而不是直接强化。
6. 交付前自检：检查 claim 是否升级、terminology 是否稳定、section stance 是否正确、caveat 是否保留、英文是否引入新歧义。
7. 如发现证据不足或表达风险，明确说明不建议使用的英文表达。

## 输出格式

根据任务输出：

- `Polished version`：可直接替换的英文。
- `More concise version`：可选；仅在用户要求压缩或原文明显冗长时提供。
- `Risk notes`：可选；仅在存在过度解释、证据不足或 section stance 风险时提供。
- `Terms preserved`：可选；仅在项目 profile 或用户文本中有必须保留的术语时提供。
- `Terminology notes`：可选；仅在发现术语不一致、已做术语统一或仍有歧义时提供。

## 按需读取

需要检查英文过强措辞、section stance、style guardrails 或 Nature/CNS-leaning academic style 时，读取 `references/style-guardrails.md`。
需要按高影响期刊作者指南检查英文 manuscript section function、title/abstract/results/discussion/methods/figure legend 写作职责时，读取 `references/high-impact-journal-writing.md`。
