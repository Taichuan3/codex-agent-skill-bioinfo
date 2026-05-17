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
- 翻译按文本部分调整语气：摘要更紧，结果更具体，讨论更有边界。
- 不发明数据、文献、样本数、统计结果或机制。

## 工作流程

1. 判断文本部分：abstract、introduction、results、discussion、methods、figure legend、response。
2. 抽取核心 claim 和 caveat。
3. 给出忠实英文版。
4. 如用户需要，再给出更精炼或 Nature-leaning 版本。
5. 标出不建议使用的过强英文词。

## 输出格式

- `English version`
- `Optional concise version`
- `Risk notes`
- `Terms preserved`

## 风格参考

可参考本地 `nature-polishing` 的 section responsibility 思路，但不要直接照搬 Nature 规则到所有项目。

## 按需读取

需要在忠实翻译、精炼翻译和 Nature-leaning 翻译之间选择时，读取 `references/translation-stance.md`。
