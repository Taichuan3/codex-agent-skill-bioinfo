---
name: project-state-maintenance
description: 用于项目状态系统规则与日志：初始化或修复 PROJECT_GUIDE hot / PROJECT_PLAN cold append-only 角色、记录 material action、定向读取历史并判定是否更新 GUIDE；不写 GUIDE 的具体研究内容，不维护目录 README 或迁移项目布局。
---

# Project State Maintenance

## 核心问题

如何让 hot `PROJECT_GUIDE.md` 保持当前真值，同时用 cold append-only `PROJECT_PLAN.md` 保存可定向检索的历史 provenance？

## 能力边界

```text
AGENTS.md          稳定行为与项目边界
PROJECT_GUIDE.md  hot current state，按需读取
PROJECT_PLAN.md   cold append-only log，默认只写不读
*/README.md       局部目录导航
```

- 本 Skill 负责两个状态文件的生命周期、读写边界、material-action 记录和 GUIDE 更新判定。
- 只创建、替换或压缩 GUIDE 内容时，组合或改用 `project-guide-maintainer`。
- 只维护局部 artifact 目录 README 时，改用 `project-directory-card-maintenance`。
- 项目级布局、manifest 或物理迁移交给 `research-data-organization`。

## 权限与安全

- 只在具体项目根维护状态文件；不得在仅用于容纳多个项目的父目录创建它们。
- `PROJECT_PLAN.md` 默认 append-only；除非用户明确要求修复损坏记录，否则不重写、重排或删除历史条目。
- 正常任务不得全文读取 PLAN；仅在 audit/history/reconstruction/methods/reviewer response/retrospective、指定 `log_id` 或状态冲突时用 `rg`、`tail` 或行范围定向读取。
- read-only 任务不创建或更新状态文件。
- 不写入原始日志、长命令输出、完整 diff/表格、凭证、患者可识别信息、原始数据内容或未必要暴露的机器路径。
- 用户未确认的研究问题、claim、解释和优先级不得升级为 GUIDE 当前事实；标记为 `Draft`、`Assumption` 或 `Needs confirmation`。

## 工作流程

1. 锁定模式：`initialize`、`material append`、`targeted history read`、`state repair` 或 `GUIDE update decision`。
2. 读取项目 `AGENTS.md`；只有任务依赖项目背景、当前结果或下一步时才读取 GUIDE。
3. 判断是否发生 material action：数据/manifest/QC、模型或结构分析、重要图表/claim/稿件、重大失败、工作流规则或未来决策发生实质变化。
4. 若是 material action，在不全文读取 PLAN 的前提下追加一条结构化记录；不要记录每条 shell 命令。
5. 判断 durable fact 是否改变：它是否影响下一决策、paper claim/figure、数据/模型/结构协议或默认项目知识，并且是否有 artifact/run/config/log 证据。
6. “满足至少两个 durable 条件”只是默认启发式；用户明确确认且有证据的单一关键事实也可更新 GUIDE。内容编辑交给 `project-guide-maintainer`，耦合写入按下述两阶段协议执行。
7. 若 GUIDE 与 PLAN、manifest 或 artifact 冲突，报告证据差异并停在候选修复；不得静默选择“最新”版本。
8. 交付时报告 PLAN 追加状态、GUIDE 更新状态、定向读取范围、精确文件和未决风险。

## GUIDE/PLAN 两阶段写入

1. 先准备完整 GUIDE 候选和 PLAN `prepared` 记录，共用一个 `change_id`，记录目标 GUIDE 摘要或 hash；此时不改 GUIDE。
2. PLAN `prepared` 追加成功后，才原子替换 GUIDE；成功后再追加同一 `change_id` 的 `committed` 记录。
3. `prepared` 追加失败：不写 GUIDE。GUIDE 替换失败：保持旧 GUIDE，并尽力追加 `aborted`。最终 `committed` 追加失败：不回滚已确认 GUIDE，报告 `reconciliation required`，下一次先核验 GUIDE hash 再补记。
4. 任一部分失败都必须报告实际落盘状态和恢复动作；不得把 `prepared` 冒充已完成更新，也不得重写既有 PLAN 历史。

## 模式化输出

- `initialize`：创建最小 PLAN header，并协调 `project-guide-maintainer` 生成 GUIDE；报告项目根和未填写字段。
- `material append`：输出一条 MINI、STANDARD 或 DECISION/MILESTONE 记录及追加位置，不读取完整 PLAN。
- `targeted history read`：报告查询词或 `log_id`、读取范围、找到的证据与缺口，不把局部记录冒充完整历史。
- `state repair`：给出冲突表、保留/修复建议和回滚路径；重写历史需要单独授权。
- `GUIDE update decision`：说明 durable 条件、证据指针、是否调用 GUIDE 维护，以及不更新的理由。

## 按需读取和验证

- 初始化状态文件、选择 PLAN 记录预算、生成 entry 或执行 GUIDE/PLAN 耦合写入时，读取 `references/state-file-templates.md`。
- 初始化或修复项目 `AGENTS.md` 的状态规则时，读取 `references/agents-state-files-patch.md`。
- 只编辑状态规则后运行 `scripts/verify_agents_state_rules.py --mode state <AGENTS.md>`；状态与 Directory Card 规则组合后运行 `--mode combined`。它是 focused ad-hoc verifier，不是完整测试套件。

最终回复先给状态维护结果，再给文件、验证边界、剩余风险和下一决策。
