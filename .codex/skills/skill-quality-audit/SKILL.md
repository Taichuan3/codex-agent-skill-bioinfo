---
name: skill-quality-audit
description: 用于审查本地 Codex/Agent skill 的质量、触发描述、结构完整性、上下文占用、references 拆分、安全风险、科研诚信边界和可维护性。适用于用户要求“检查这个 skill”“优化 skill”“这个 skill 是否太长/会误触发”“按 Anthropic/AIPOCH 思路审计 skill”等场景。
---

# Skill Quality Audit

## 核心问题

如何判断一个 skill 是否触发精准、上下文高效、任务闭环、可维护，并给出修改方案？

## 使用场景

当需要审查或改进本地 skill 时使用本 skill。它借鉴 Anthropic 的 skill 最小结构和 progressive disclosure 思路，以及 AIPOCH skill-auditor 的质量门控，但本地化为轻量、中文、科研优先版本。

## Hard gates

先检查：

- `SKILL.md` 是否存在。
- frontmatter 是否有 `name` 和 `description`。
- `description` 是否清楚说明何时触发，避免过宽或过窄。
- 是否能用一句话回答“这个 skill 解决的核心问题是什么”。
- 是否包含会直接执行不可信用户字符串的脚本或危险命令。
- 是否要求默认读取大量无关文件。
- 是否可能诱导模型编造数据、文献、机制或过强 claim。

## 评分维度

- Trigger precision
- Context efficiency
- Progressive disclosure
- Task completeness
- Research integrity
- Reproducibility
- Safety and dependency handling
- Maintainability

## 输出格式

- Verdict
- Core question
- Hard-gate issues
- Strengths
- P0 fixes
- P1 improvements
- P2 polish
- Suggested description
- Suggested reference split
- Absorption action: strengthen existing / new candidate skill / reference only / reject

需要细化评分时读取 `references/skill-audit-rubric.md`。
需要审计外部 skill/agent 并决定是否吸收时，读取 `references/external-skill-absorption-rubric.md`。
