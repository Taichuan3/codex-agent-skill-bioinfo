---
name: project-guide-maintainer
description: 用于创建、压缩或按任务delta更新 PROJECT_GUIDE 的当前摘要、状态、证据入口、关键限制和 next decisions；替换过期状态而非追加历史，详细结果按模块下沉；状态收尾编排、PLAN与目录卡分别交给专项Skill。
---

# Project Guide Maintainer

## 核心问题

如何把经确认的项目背景、当前结果、证据边界和下一决策压缩成未来 Agent 能快速读取的轻量 GUIDE？

## 能力边界

- 本 Skill 只维护 `PROJECT_GUIDE.md` 的 current-state 内容，不管理 PLAN 生命周期。
- 初始化 GUIDE+PLAN、追加 material-action 日志、定向查历史或修复两者关系时，组合或改用 `project-state-maintenance`。
- 局部目录导航使用 `project-directory-card-maintenance`；项目级布局和迁移使用 `research-data-organization`。
- GUIDE 可作为论文叙事骨架，但不是最终 manuscript，也不是操作日志、完整综述或 artifact inventory。

## 事实与证据边界

- 科学解释、方法取舍、claims 和研究优先级须保留作者确认状态；可核验的文件路径、实际完成/失败和阻塞可按证据维护，不把技术完成升级为科学接受。
- Agent 新提出的解释或优先级必须标记 `Draft`、`Assumption`、`Open question` 或 `Needs evidence`。
- 区分 evidence、interpretation、limitation 和 speculation；不得因压缩或润色提高 claim 强度。
- 每个主要 finding/claim 保留短证据指针、证据等级、caveat 和状态；详细表格、日志、命令和历史下沉到 artifact、PLAN 或 Directory Card。
- 不把凭证、患者可识别信息、原始数据内容、长机器路径列表或未必要公开的项目事实复制进公共模板。

## 工作流程

1. 锁定模式：`create`、`durable update`、`compress/replace` 或 `draft proposal`。
2. 读取项目 `AGENTS.md`、现有 GUIDE 和用户指定的最小证据；需要历史时让 `project-state-maintenance` 定向读取 PLAN。
3. 区分 confirmed fact、working model、open question、current evidence、caveat、risk 和 next decision。
4. 保留理解当前项目与下一步所需的信息；按 delta 局部更新并保留其他模块当前事实。chronology 留在 PLAN，详细结果留模块页/成果索引；下沉前后核对关键限制与证据入口，不直接截断超长内容。
5. 按稳定研究问题/工作模块连接 evidence pointer；仅在论文主线成熟后再映射 result/figure skeleton，不给新项目预设 Result。未验证观察保持 candidate/exploratory 状态。
6. 更新时替换过期 current-state 表述，不在 GUIDE 尾部持续追加版本历史。
7. 检查预算、内部一致性、claim 强度、指针有效性和用户确认状态。
8. GUIDE 写入属于 material action；把完整候选交给 `project-state-maintenance`，由其执行 `prepared → 原子替换 GUIDE → committed` 两阶段协议。部分失败时报告实际落盘状态，不自行改写 PLAN 历史。

## 内容与预算契约

- 默认目标 1,000–2,000 字符；超过 3,000 字符或 80 行触发压缩告警，项目可说明例外。既有 6,000 字符或 120 行为安全上限，超过时先报告并规划保真压缩，绝不自动删去科学限制。
- Main findings 最多 5–7 项；Next decisions 最多 3 项；Risks 最多 5 项。
- 默认只用五块：目标、当前状态、关键限制/作者接受状态、最多三项下一步、稳定入口；一句话目标可含 central question/current story，不机械增加标题。
- 项目需要时再加入 working model、result/figure skeleton、reviewer risks 或 evidence package；不要机械填满所有模板段落。
- 超出预算时优先删除重复背景、chronology 和过期路线，并用 `log_id`、manifest、报告或 Directory Card 指针替代。

## 模式化输出

- `create`：给出可直接写入的 GUIDE、未确认字段和证据缺口。
- `durable update`：列出替换的 current facts、证据指针、保留的 caveat 和需要追加的 PLAN 记录。
- `compress/replace`：报告保留、删除、下沉和仍需用户确认的内容，并提供压缩后的完整 GUIDE。
- `draft proposal`：不得把建议写成当前事实；清楚标记等待用户确认的段落。

需要完整结构和字段示例时读取 `references/project-guide-template.md`。最终回复说明更新结果、精确路径、证据边界、PLAN 同步状态和下一决策。
