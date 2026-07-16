---
name: skill-quality-audit
description: 用于审查和治理本地 Codex/Agent skill library：单个 skill 的触发描述、结构、上下文、references、安全与科研边界，以及全机 skill/agent 盘点、canonical/runtime/project/upstream 去重、provenance、隐私和 Git 分支归属。适用于“检查/优化 skill”“整理所有 skill/agent”“判断哪个版本是权威来源”“按项目或类型上传 review 分支”等场景。
---

# Skill Quality Audit

## 核心问题

如何判断一个 skill 是否触发精准、上下文高效、任务闭环、可维护，并给出修改方案？

## 使用场景

当需要审查或改进本地 skill 时使用本 skill。它借鉴 Anthropic 的 skill 最小结构和 progressive disclosure 思路，以及 AIPOCH skill-auditor 的质量门控，但本地化为轻量、中文、科研优先版本。

## Runtime/source guardrail

When auditing this user's Codex/Hermes bioinfo skill system, treat the local runtime skill as the newest user-iterated source unless the user explicitly says otherwise. Do not overwrite runtime `SKILL.md` bodies with older GitHub source bodies. Correct optimization flow:

1. Read the runtime skill first and identify mature reusable behavior, sediment, duplication, and project-specific residue.
2. Mine external skill corpora to strengthen existing local skills before creating new candidates.
3. Backport only stable, compressed mechanisms to the installable source repo (`AGENTS.md`, `local_config.yaml`, `.codex/skills`), keeping long audits local.
4. For standalone Codex compatibility, ensure global or repo-level discovery exposes the same skills via `.agents/skills` / `~/.agents/skills`, and keep `~/.codex/AGENTS.md` aligned with the bioinfo agent rules.
5. Verify both runtime and source counts/metadata after edits; use ad-hoc verification when no canonical validator exists.

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

## Bioinfo Codex/Hermes skill-system audits

When auditing this user's bioinfo skill library, read `references/bioinfo-codex-skill-governance.md` for the runtime-first, external-corpus, Codex discovery, and lightweight-repo rules learned from prior maintenance mistakes.

## Library-wide inventory and publishing

When the user asks to organize all local skills/agents or publish them by project/type, do a provenance-aware catalog rather than bulk-copying every discovered file:

1. Separate raw discovery counts from curated active counts.
2. Classify canonical source, runtime mirror, project-specific asset, bundled/upstream content, cache/archive, and personal local-only material.
3. Record home-relative path, hash, provenance, Git ownership, and upload policy in a machine-readable manifest; never export credentials, sessions, memories, raw data, or private self-model content.
4. Map each reusable asset to its real canonical repo; reference bundled/third-party sources instead of vendoring them.
5. For source/runtime drift, perform semantic comparison before promotion; do not let an older GitHub body overwrite user-tested runtime behavior.
6. Push only to the authorized review/working branch and verify visibility, commit, and clean worktree. Never update `main` without explicit permission.

Read `references/library-inventory-provenance.md` for the two-pass inventory, privacy classes, dirty-worktree strategy, manifest fields, and verification checklist.

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

当任务涉及从大型外部 skill 语料库吸收内容、判断是否新增 skill、或维护 bioinfo runtime/source skill 体系时，读取 `references/external-corpus-absorption-guardrails.md`。
需要审计外部 skill/agent 并决定是否吸收时，读取 `references/external-skill-absorption-rubric.md`。
