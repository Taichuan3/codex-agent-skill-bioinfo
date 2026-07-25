---
name: skill-quality-audit
description: 用于只读审计或在明确授权范围内修订 Codex Skill：检查触发描述、SKILL.md、references/scripts/assets 路由、agents metadata、evals、安全与科研边界，并做 Skill/Agent library 的 provenance、重复、source/runtime drift 和外部语料吸收评估；不负责批准、发布、安装或自动自修改。
---

# Skill Quality Audit

## 核心问题

如何判断一个 Skill 是否触发准确、上下文高效、可验证、科研安全且能由明确来源维护？

## 能力边界

- 本 Skill 负责质量 findings、优先级、候选 semantic diff、外部吸收建议和授权范围内的 Skill 文件修订。
- `controlled-self-improvement` 负责稳定信号判定、跨层目标路由、action-specific approval、发布、安装、监测与回滚生命周期。
- 单个 Skill 审计不得自动扩展为全库迁移；全库 inventory 不等于复制或公开所有发现的文件。
- canonical source、installed runtime、project-local copy 和 upstream bundle 都是需要 provenance 证明的角色；mtime、路径位置或远端存在不能单独决定权威版本。
- 审计结果不是最终科学批准；内容正确性仍需领域证据和相应 reviewer。

## 权限与完整性

- `read-only audit` 不修改 Skill、manifest、runtime 或 Git。
- 修订只限用户授权的 Skill/文件集合；不得顺带整理全库、安装到 runtime、commit、push、建 PR 或 merge。
- 保留用户和其他 worker 的 dirty changes；无法得到 clean attributable diff 时报告边界，不覆盖来源不明内容。
- 不把凭证、session/memory/cache、机器拓扑、私有路径、原始对话、未发表项目事实或第三方未授权内容写入 portable source。
- 外部 Skill/Agent 只能按 license 与 provenance 做逐机制 keep/merge/split/reference/reject；不得整库复制替代审查。

## 工作流程

1. 锁定模式：`single-skill audit`、`authorized repair`、`library inventory` 或 `external absorption review`。
2. 读取适用 `AGENTS.md`、目标 `SKILL.md` 和直接资源；记录目标范围、source state、dirty files 和验证命令。
3. 检查 hard gates：仅 `name`/`description` frontmatter、核心问题、授权边界、直接资源路由、metadata 结构、危险命令和科研 claim 风险。
4. 评估 trigger precision、neighbor routing、progressive disclosure、task completeness、reproducibility、safety、maintainability 和 eval coverage。
5. 对 source/runtime/project/upstream 副本比较 name、hash、资源集合和 semantic diff；先建立 provenance，再决定 keep/merge。
6. 输出 P0/P1/P2 findings 和最小修订；优先强化现有 Skill，只有明确独立交付物与触发边界时才建议新增。
7. 获得修订授权时，只修改指定文件，保持每个 reference/script/asset 从 `SKILL.md` 直接可发现，并补齐平衡的 trigger/outcome evals。
8. 运行结构解析、validator、JSON/YAML、链接/路径、privacy、diff 和代表性行为检查；区分 pass、not run 和 not covered。
9. 需要发布、安装、跨设备同步或永久规则演化时，交给 `controlled-self-improvement`，不把 QA 结论当作批准。

## 模式化输出

- `single-skill audit`：给出 verdict、P0/P1/P2、trigger 邻居、资源路由、eval 缺口和候选 diff。
- `authorized repair`：报告精确文件、keep/merge/split 决策、验证结果、未覆盖行为和未执行的发布/安装。
- `library inventory`：分开 raw/curated counts，报告 canonical map、drift、upload class、excluded assets 和 dirty-worktree 边界。
- `external absorption review`：报告 strengthen/new candidate/reference/reject、license/provenance、机制级差异和本地 pilot 要求。

## 按需读取

- 需要质量评分、P0/P1/P2 或 verdict 定义时，读取 `references/skill-audit-rubric.md`。
- 需要 package 结构、discovery、source/runtime parity 或发布前检查时，读取 `references/bioinfo-codex-skill-governance.md`。
- 做全库 inventory、canonical 映射、hash/provenance 或 upload classification 时，读取 `references/library-inventory-provenance.md`。
- 从大型外部 corpus 提取机制且控制新增 Skill 数量时，读取 `references/external-corpus-absorption-guardrails.md`。
- 比较单个外部 Skill/Agent 并决定 strengthen/new/reference/reject 时，读取 `references/external-skill-absorption-rubric.md`。

最终回复先给 QA verdict，再给精确文件、证据、验证边界、剩余风险和需要治理授权的下一动作。
