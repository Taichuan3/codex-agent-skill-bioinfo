---
name: scientific-english-translation
description: 用于将中文科研文本翻译为英文，或将中文草稿转成 Nature/CNS-leaning 但证据边界安全的英文科研表达。适用于摘要、引言、结果、讨论、方法、图注、回复信和标题翻译；不负责中文润色。
---

# Scientific English Translation

## 使用场景

当用户要求“翻译成英文”“中文转英文”“Nature 风格英文”“英文论文表达”时使用本 skill。中文内部润色使用 `chinese-scientific-polishing`。

## 核心原则

- 先保护科学 claim，再追求英文风格。
- 不把相关性写成因果，不把候选机制写成已证明机制。
- 保留项目 profile 中的术语、禁止性表达和证据等级。
- 翻译时保持术语一一对应：同一个中文概念应稳定翻译为同一个英文术语，不要为了英文变化把同一对象翻成多个词。若中文原文中同一概念用了多个说法，应在 `Risk notes` 或 `Terms preserved` 中提示并建议统一。
- `element`、`copy`、`unit`、`locus`、`sequence` 等术语只有在对应不同层级或不同对象时才可并存；否则应选择一个 preferred term 并保持全文一致。
- 翻译按文本部分调整语气：摘要更紧，结果更具体，讨论更有边界。
- 不发明数据、文献、样本数、统计结果或机制。

## 工作流程

1. 判断文本部分：abstract、introduction、results、discussion、methods、figure legend、response。
2. 抽取核心 claim、caveat 和需要稳定翻译的关键术语。
3. 建立或沿用 terminology map，统一同一概念的英文表达。
4. 给出忠实英文版。
5. 如用户需要，再给出更精炼或 Nature-leaning 版本。
6. 标出不建议使用的过强英文词和容易造成歧义的术语替换。

## 输出格式

- `English version`
- `Optional concise version`
- `Risk notes`
- `Terms preserved`
- `Terminology map`

## 风格参考

可参考本地 `nature-polishing` 的 section responsibility 思路，但不要直接照搬 Nature 规则到所有项目。

## 按需读取

需要在忠实翻译、精炼翻译和 Nature-leaning 翻译之间选择时，读取 `references/translation-stance.md`。
需要将中文论文段落翻译成符合高影响期刊 section function 的英文表达，或检查摘要、引言、结果、讨论、方法、图注的英文职责时，读取 `references/high-impact-journal-translation.md`。
