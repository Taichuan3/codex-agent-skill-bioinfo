---
name: research-project-planner
description: 用于新项目启动或重大重规划：把已有基本边界的生物信息学方向设计成 central question、knowledge gap、hypothesis、evidence package、figure skeleton、技术模块、风险、里程碑和 stop/pivot criteria；不负责早期一页问题澄清、既有方案取舍、单个 claim 验证、具体执行或 GUIDE 状态维护。
---

# Research Project Planner

## 核心问题

如何把已具基本边界的研究方向变成可检验、可分阶段、可停止或转向的项目路线？

## 边界与归属

- 从科学问题与知识缺口开始，不从可用工具清单开始；用户拥有 central question、方法、figure logic、最终 claim 和 go/no-go 决策。
- 零散想法尚不能形成 bounded question 时，先用 `research-question-brief`；已有路线需要比较 continue/pivot/stop 或工具取舍时，用 `research-decision-review`。
- 单个 claim 的分层验证选项交给 `validation-strategy-planner`；本 Skill 只在项目级定义需要何种验证证据及其阶段位置。
- 规划完成后写入当前 GUIDE 交给 `project-guide-maintainer`；明确代码、分析或绘图任务交给相应执行 Skill。
- 单篇论文阅读用 `paper-reader`，系统证据地图用 `literature-search-workflow`。不把计划写成已执行结果。

## 工作流程

1. 读取 research brief、项目规则、用户指定证据和必要的当前 GUIDE；不默认读取完整历史或大型 artifact 目录。
2. 明确 central question、已知背景、knowledge gap、范围和预期贡献；若关键边界缺失，只问最多三个会改变路线的问题。
3. 写 tentative hypothesis 与 expected claim，同时列出竞争解释和 claim 降级条件。
4. 设计 evidence package：数据、对照、统计、外部或实验验证、可复现性和主要排除项；区分 exploration、confirmation、validation。
5. 用 `Known / Unknown / Question / Finding / Advance` 检查逻辑收敛，并让每张主图对应一个问题与证据门槛。
6. 规划 minimum viable analysis、后续模块、依赖、里程碑、risk register 和 bounded implementation tasks；不执行这些任务。
7. 对陌生领域先建立最小 field/method map：权威综述、成熟 baseline、可信实现、共识/争议、复现候选和适用限制。
8. 为关键节点定义可观测的 continue、pivot 和 stop 条件，标明哪些需要用户决定。
9. 输出完整但精简的 project brief，并给出可压缩进 GUIDE 的 seed；不要直接接管 GUIDE 生命周期。

## 输出契约

- Central question、known/background、knowledge gap、scope
- Tentative hypothesis、expected claim、alternative explanations
- Topic scorecard 与 `Known / Unknown / Question / Finding / Advance`
- Evidence package 与 phase labels
- Figure skeleton（每图的问题、输入和证据门槛）
- Technical modules、minimum viable analysis、dependencies 和 milestones
- Risk register、alternatives、stop/pivot/go-no-go criteria
- Field/method map（仅陌生领域）与 next bounded tasks
- User decisions required 与 `PROJECT_GUIDE` seed

需要完整字段或可落盘 project brief 时读取 `references/project-brief-template.md`；只需路线摘要时不要加载模板。
