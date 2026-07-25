---
name: controlled-self-improvement
description: 用于把明确长期指令、重复纠正、流程失败、能力漂移、上下文膨胀或跨项目复用模式转化为受治理的 memory、AGENTS.md、Skill、Agent、reference、checklist/eval、配置或 portable package 候选，并管理 review、action-specific approval、验证、发布、安装、监测和回滚；不用于一次性要求、普通 Skill QA 或未经授权的自动自修改。
---

# Controlled Self-Improvement

## 核心问题

如何让 Codex 根据稳定用户习惯持续改进 Agent、Skill、memory 和同步包，同时避免误学、上下文膨胀、隐私泄露和未经审查的自修改？

## 能力边界

- 把 self-improvement 视为受治理的 artifact evolution，不是模型权重训练，也不是“看到问题就自动改所有层”。
- 本 Skill 负责 reusable signal → primary target → candidate → review/approval → source/runtime lifecycle。
- 单个 Skill 的触发、结构、references、metadata 和 eval 质量审计交给 `skill-quality-audit`；其 findings 可作为本 Skill 的证据输入。
- 项目事实和当前 next actions 仍由项目 `AGENTS.md`/`PROJECT_GUIDE.md` 所有；本 Skill 只决定是否及如何沉淀，不替代项目科学判断。

## 授权边界

- 相关的只读检查和聊天内候选可进行；写入 local draft 只限当前已授权范围。
- memory、active Agent/Skill、automation、configuration、runtime target 的每次写入都需要对应授权。
- source edit、commit、push、PR、merge、installation、memory update、automation change 和 rollback 是不同动作；一个动作的批准不能外推到另一个。
- `main` merge、账号授权、凭证处理和不可逆操作始终单独确认。
- proposer 不得成为 public 或高影响变更的唯一 reviewer；无法独立审查时停在明确的 review-needed 状态。

## Workflow

1. 锁定模式：`observe/triage`、`candidate draft`、`approved implementation`、`publish/install` 或 `monitor/rollback`。
2. 捕获 signal type 和证据指针；一次证据只在明确长期指令或高严重度安全失败时足够，否则要求重复证据或 bounded forward test。
3. 判断稳定性、未来价值、重复所有权、scope、privacy 和 context cost；一次性偏好、暂时故障、推测人格或已有更具体 owner 的规则应拒绝或留在项目层。
4. 选择一个 canonical primary target；用 pointer 连接其他层，不复制同一规则到 memory、Agent、Skill 和 GUIDE。
5. 使用 `assets/improvement-candidate.md` 生成一个 coherent candidate 和最小 semantic diff；记录替代目标、冲突、context impact、验证、安装目标与 rollback。
6. 对 source、runtime、project-local rule 和相关历史做 provenance/precedence review；public/high-impact 变更安排独立或用户 review。
7. 在 exact approved scope 内实施 source change；先后状态和可写权限遵循 lifecycle，不把 drafted/reviewed/validated 冒充 approved 或 published。
8. 运行结构、语义、privacy、discovery、behavior 和必要的 parity 检查；记录未运行与覆盖边界。
9. 只有获得对应授权才 publish 或 install；先备份，安装 reviewed source state，并比较 digest/manifest。
10. 监测后续相关使用；出现误触发、冲突、隐私/证据退化、context bloat 或 parity failure 时按授权回滚并验证。

## 候选契约

Every material candidate must contain:

- candidate ID, status, signal type, evidence pointer, and intended scope;
- primary target and why other targets were rejected;
- proposed semantic diff and context-size impact;
- privacy/publication class, conflicts, dependencies, and affected devices/projects;
- validation plan and results;
- authority, branch/commit/PR, installation targets, backup, and rollback procedure;
- owner and next action.

一个 candidate 只表达一个 coherent behavioral change；同一任务发现的无关变化必须拆分。

## 停止条件

- 未授权下一项 write/publish/install/merge/memory/automation 动作时停在 proposal 或当前已批准状态。
- signal 可能短暂、证据不足、与更具体规则冲突或不能安全去标识时，拒绝或等待证据。
- source/runtime drift 或 dirty worktree 使 diff 无法归因时，不覆盖；先建立 provenance 或隔离 worktree。
- 无法定义验证、backup 或 rollback 时，不进入高风险实现/安装。
- 用户撤回偏好或规则已失效时，不让 inactive rule 留在 hot context。

## 按需读取

- 选择 lifecycle 状态、signal threshold、primary target、privacy class、reviewer、validation ladder 或 rollback gate 时，读取 `references/lifecycle-and-governance.md`。
- 需要创建可保存的候选 artifact 时，复制并填写 `assets/improvement-candidate.md`；不要把模板当作背景文档全文复述。

最终回复先给当前 lifecycle 状态和已完成动作，再给 candidate/diff、授权边界、验证、publication/installation 状态、rollback 与下一项用户决定。
