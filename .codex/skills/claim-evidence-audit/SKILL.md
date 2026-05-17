---
name: claim-evidence-audit
description: 用于在论文写作、结果段、摘要、讨论、图注、figure interpretation、审稿回复或投稿前检查中审查生物信息学 claim 是否有足够证据、是否过度解释、是否映射到 figure/table/source data/caveat，并给出降级或补强建议。不用于普通代码执行或一般项目管理任务，除非用户明确询问某个科学说法是否成立。
---

# Claim Evidence Audit

## 使用场景

当任务涉及论文文本、结果解释、图注、figure-to-claim、审稿回复、投稿前检查，或用户明确要求检查“这个说法是否成立”“是否 overclaim”“结果段是否安全”“图能否支持结论”“审稿人会不会质疑证据”时使用本 skill。

不要因为任务中出现了数据、图或结果就自动触发本 skill。普通脚本执行、文件整理、绘图实现和环境安装应优先使用对应执行 skill；只有需要判断科学 claim 与证据是否匹配时才使用本 skill。

## 证据等级

- **Strong**：有当前项目直接输出，且有 table、figure、script、source data 或已发表论文支撑。
- **Moderate**：多个分析模块结果一致，或 prior publication 与当前分析共同支持。
- **Exploratory**：基于早期分析、有限参数检查、局部复核、manual review 未完成或统计背景仍需确认。
- **Speculative**：尚无直接验证的功能、机制或因果假说。

## 审查流程

1. 抽取每个 claim，拆成最小可验证单元。
2. 为每个 claim 找到对应 evidence、figure/table、source data、script 或 citation。
3. 判断证据等级和主要 caveat。
4. 标记过强动词、因果词、机制词、泛化范围和样本范围问题。
5. 给出推荐写法：保留、降级、移动到 Discussion、补分析后再写或删除。

## 输出格式

优先输出表格：

| Claim | Evidence | Level | Risk | Recommended wording |
|---|---|---|---|---|

如果材料不足，先列出缺失证据，不要凭记忆补全。
