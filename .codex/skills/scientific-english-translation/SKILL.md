---
name: scientific-english-translation
description: 英文翻译模块：按用户要求把已确认或本次明确交付翻译的中文/中文为主科研文本忠实译为英文，保护术语、数字、章节职责和证据强度。已有英文润色用 scientific-english-polishing，中文修改用 chinese-scientific-polishing；中文确认本身不触发翻译，完整图注起草用 figure-caption。
---

# 英文翻译

## 核心问题

如何把中文科研草稿翻译成证据边界安全、可投稿语气的英文表达？

## 路由与边界

- 以来源语言和目标语言路由：中文或中英混合输入、目标为英文时用本 Skill；已有英文的清晰度和风格修改用 `scientific-english-polishing`。
- 通常在作者确认中文后进入本模块；用户本次明确说“翻译以下中文”已给出当前文本的翻译授权，不必反复索取中文确认。仅说“中文没问题了”不自动翻译；若用户明确标记仍待确认且不得翻译，继续停在中文阶段。
- 只翻译现成中文图注时用本 Skill；需要决定 caption 应包含哪些 panel、n、统计、编码、source data 或 caveat 时改用或组合 `figure-caption`。
- 只需要中文改写时用 `chinese-scientific-polishing`；主要任务是验证 claim 时先用 `claim-evidence-audit`。
- 不发明数据、文献、样本数、统计、机制或术语定义，不静默纠正疑似错误数字。

## 翻译契约

- 先忠实保留 scientific meaning、evidence boundary、数字、限定词和章节职责，再改善英文流畅度。
- 不把相关性翻译成因果，不把 candidate、putative 或 exploratory 结果翻译成 demonstrated、established 或 mechanistic conclusion。
- 一个中文概念稳定映射为一个英文术语；原文术语不一致时选择最保守映射并标记歧义。
- Results 保持观察性，Discussion 可解释但保留限制，Methods 不压缩掉复现信息。
- “Nature/高影响期刊风格”只改变选择、结构与简洁度，不授权新增 novelty 或增强 claim。
- 使用独立的 Nature-informed 英文表达原则，不默认调用 Hashimoto；忠实翻译优先，明确要求直译时不强制重排结构。单独的英文润色是后续可选模块，不能借润色改写已确认的研究判断。
- 保留源文信息与结构，除非用户要求压缩或重构；可调整英语语法、语序和衔接，但不得删去实际结果、负结果、范围或不确定性。源文的过强结论与数据冲突时标记并给出有据的保守建议，不静默替作者更改结论。

## 工作流程

1. 从本次请求确认英文目标与翻译范围，沿用已有中文版本、章节、读者、长度和术语约定；充分信息下直接翻译，不强制新增审批步骤。
2. 提取 claim、直接证据、caveat、数字和术语映射；遇到歧义先保守处理并标记。
3. 先完成忠实英文版，再按用户要求压缩或调整期刊语气。
4. 逐项回对原文，检查遗漏、增译、数字、术语、claim 强度和 section function。
5. 记录影响翻译的歧义、数值冲突或缺句；完成不受影响部分，不靠检索原论文或猜测补回被打乱/劣译而丢失的信息，除非用户另授权核验。

## 输出格式

- 默认给出可直接使用的 `English version`。
- 仅在用户要求时给出 `Concise` 或 journal-leaning variant。
- 仅在存在歧义或证据风险时增加 `Risk notes`；复杂术语才给 `Terminology map`。
- 交付请求范围内的完整英文正文，不只给术语表或提纲。语言 QA 不代表发表级科学验证；文件修改按用户指定版本交付，必要状态收尾归 `project-state-maintenance`。

## 按需读取

- 实质科研段落/章节的英文输出读取 `../scientific-english-polishing/references/integrated-writing-profile.md`，共享风格而不复制；纯单词翻译不加载。中文输出与已有英文改写仍按上述边界路由。

- 需要选择 faithful、concise 或 journal-leaning stance，或原文术语不稳定时，读取 `references/translation-stance.md`。
- 用户明确要求高影响期刊导向或需要维护 manuscript section function 时，读取 `references/high-impact-journal-translation.md`；目标期刊规则优先。
