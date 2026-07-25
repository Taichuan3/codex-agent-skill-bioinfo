---
name: project-directory-card-maintenance
description: 用于审计、创建或更新重要 artifact 目录的短 README Directory Card，维护文件状态、producer、读取顺序和 manifest 指针；不用于项目迁移、GUIDE/PLAN 或普通 README。
---

# Project Directory Card Maintenance

## 核心问题

如何用选择性的短 README 提供可信、按需读取且不复制完整 inventory 的局部 artifact 导航？

## 能力边界

- Directory Card 只描述已验证的当前布局；它不是科学真值、项目 GUIDE、历史日志、manifest 或行为规则。
- 本 Skill 可创建或更新局部 README，但不得移动、重命名、删除、归档或重新分类整个项目。
- 项目级 artifact 盘点、manifest/latest/priority 入口或迁移交给 `research-data-organization`。
- GUIDE/PLAN 生命周期交给 `project-state-maintenance`；GUIDE 内容编辑交给 `project-guide-maintainer`。
- 普通仓库介绍、安装教程或非 artifact README 不使用本 Skill。

## 权限与证据

- read-only 请求只报告候选 card 内容，不创建文件。
- 写卡片前从 manifest/registry、producer、consumer、报告链接或用户确认状态核验 current/candidate/deprecated；不得只凭文件名或日期判断。
- README 与结构化记录冲突时，以可验证证据为准，报告冲突后再更新 card。
- 不把完整文件列表、全量指标/样本/变异/候选分子表、原始日志、凭证或患者可识别信息复制进 README。
- 不为每个 run、临时图、cache 或快速变化的 interim 目录创建 card。

## 工作流程

1. 锁定模式：`read-only proposal`、`create`、`durable update` 或 `stale-card repair`。
2. 读取项目 `AGENTS.md`、目标目录现有 README 和最近的 manifest/registry；限制扫描范围，不默认打开全部文件。
3. 判断目录是否值得维护 card：会复用/引用/共享、版本难辨、支持独立 claim、需要特定读取顺序或重建入口。
4. 核验当前重要 artifact、状态、producer、consumer、source-data/manifest 指针和 reproduction command。
5. 写最小导航：purpose、current important files、read first、reproduce/update、ignore/deprecated、last updated。
6. 用链接或 manifest 指针替代长表；状态不确定时写 `candidate`、`provenance_pending` 或 `not assessed`。
7. 若核验暴露项目级路径问题，停在 navigation/migration handoff，不执行物理整理。
8. Card 写入属于 material action：调用 `project-state-maintenance` 追加 PLAN；只有项目真值或下一决策改变时才更新 GUIDE。
9. 交付时报告精确 README 路径、验证来源、未扫描范围、状态冲突和后续 handoff。

## 长度与内容契约

- 普通 card 目标 800–1,500 字符，硬上限约 2,000。
- 复杂 data/model/structure card 可到 2,500 字符，硬上限约 3,000。
- `reports/figures/README.md` 可为 1–2 页，硬上限约 4,000。
- 优先使用短表、relative path、manifest/registry、script/command 和明确状态；不要写背景长文。

## 模式化输出

- `read-only proposal`：给出候选 card、证据和不确定项，不创建文件。
- `create`：报告新 README、current artifact 证据、读取顺序和 reproduction 入口。
- `durable update`：列出状态变化、替换关系、证据来源和 PLAN 同步。
- `stale-card repair`：列出旧指针、真实 consumer/producer、修复内容和仍未解决的冲突。

## 按需读取

- 需要具体 card 结构或 data/model/figure 示例时，读取 `references/directory-card-templates.md`。
- 初始化或修复项目 `AGENTS.md` 的 Directory Card 规则时，读取 `references/agents-directory-cards-patch.md`，并运行 `project-state-maintenance` verifier 的 `--mode combined` 检查组合规则。
- 版本化 artifact 家族难以导航时，读取 `references/versioned-research-artifact-layout.md`；如需移动路径，转交 `research-data-organization`。

最终回复先给导航成果，再给文件、证据、PLAN/GUIDE 同步状态、剩余风险和下一决策。
