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
- 能压缩就压缩，但不能删除关键 caveat、样本范围、数据类型和统计限定。

## 工作流程

1. 读取根 `AGENTS.md`、当前项目 profile 和用户给定文本。
2. 标出文本中的核心 claim、证据等级和必须保留的 caveat。
3. 先修正结构和过强 claim，再进行句子层面润色。
4. 对高风险表达给出替代表述，而不是直接强化。
5. 如发现证据不足，明确说明不建议使用的英文表达。

## 输出格式

根据任务输出：

- `Polished version`：可直接替换的英文。
- `More concise version`：需要压缩时提供。
- `Risk notes`：列出可能过度解释的词或句子。
- `Terms preserved`：列出按项目 profile 保留的术语。

## 按需读取

需要检查英文过强措辞、section stance、style guardrails 或 Nature/CNS-leaning academic style 时，读取 `references/style-guardrails.md`。
