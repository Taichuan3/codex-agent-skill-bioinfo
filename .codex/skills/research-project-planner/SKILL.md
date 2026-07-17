---
name: research-project-planner
description: 用于生物信息学或计算生物学项目启动前，将模糊研究方向转成可执行研究路线：澄清 central question、knowledge gap、hypothesis、evidence package、figure skeleton、技术路线、风险和 stop/pivot criteria。不用于已明确的代码执行、单篇论文阅读或单纯文本润色。
---

# Research Project Planner

## 核心问题

如何把模糊研究方向变成 central question、evidence package、figure skeleton 和可执行路线？

## 使用场景

当用户还没有进入具体分析，而是需要把一个研究方向变成可执行项目时使用本 skill。它的目标是先规划路线，不是直接写代码、画图或写论文。

## 不适合触发

- 用户已经给出明确脚本/表格处理任务时，使用 `bioinfo-analysis-code`。
- 用户指定阅读单篇论文时，使用 `paper-reader`。
- 用户只需要把零散想法压缩成短 brief 时，优先使用 `research-question-brief`。
- 用户只要求润色、翻译或改写文本时，使用对应写作 skill。


## 核心原则

- 从科学问题开始，不从“我会什么分析”开始。
- 先找知识缺口，再设计证据链。
- 把用户的方向压缩成可检验假设、预期主张和 figure skeleton。
- 用重要性、新颖性、可行性、证据路径、风险和产出形态评估方向，而不是凭直觉开题。
- 用 `Known / Unknown / Question / Finding / Advance` 五句话检查故事是否能收敛。
- 区分 `exploration`、`confirmation`、`validation`，避免探索结果直接变成强结论。
- 陌生领域进入复杂建模或调参前，先调查综述/经典论文、可信开源实现、社区实践、成熟 baseline 和专家框架；区分共识、争议与未解问题，不能用单个漂亮结果替代领域定位。
- 只读取用户指定材料和必要 skill，不默认读取长项目记录。
- 用户决定 central question、方法、analysis/figure logic、结果解释、最终 claim 和 go/no-go；agent 负责 source map、备选方案、风险、可执行 contract、实现、测试、provenance 和 sensitivity analysis，并把需要用户确认的 stop/pivot 条件单列。

## 工作流程

0. 若领域或方法不熟悉，先产出最小 `field_map`、`method_map`、evidence/limitation matrix 和 reproduction shortlist，再决定技术路线。
1. 明确 central question：这个项目到底要回答什么生物学或计算问题。
2. 梳理 background / known：领域已知什么，哪些结论较稳。
3. 定义 knowledge gap：机制不清、因果不清、数据缺失、跨队列不一致、方法不足或解释框架不足。
4. 写 hypothesis / expected claim：项目成功后最核心的一句话。
5. 设计 evidence package：需要哪些数据、对照、统计、验证和替代解释排除。
6. 画 figure skeleton：每张主图回答什么问题。
7. 给出 technical route：数据来源、分析模块、工具选择、验证路线和风险节点。
8. 生成 Project Charter 级别的 artifacts：minimum viable analysis、risk register、go/no-go criteria、下一阶段 evidence map questions。
9. 由 agent 起草问题、证据边界、目录/报告备选主线、验收标准和 bounded implementation contract，交由用户确认；不得自动选择模型、figure storyline 或研究方向。
10. 给出待用户确认的 stop / pivot criteria：什么结果继续，什么结果转向，什么结果停止。
11. 建议如何把输出压缩进 `PROJECT_GUIDE.md`，而不是写成长记录。

## 必要输出

优先输出精简 project brief：

- `Central question`
- `Known / background`
- `Knowledge gap`
- `Hypothesis`
- `Expected claim`
- `Topic scorecard`
- `Known / Unknown / Question / Finding / Advance`
- `Evidence package`
- `Figure skeleton`
- `Technical route`
- `Risks and alternatives`
- `Stop / pivot criteria`
- `Project Charter`
- `Minimum viable analysis`
- `Risk register`
- `Go / no-go criteria`
- `Next evidence-map questions`
- `Field/method map and reproduction shortlist`（陌生领域时）
- `Next bounded Codex tasks`

如果用户提供的想法仍然模糊，先输出需要澄清的问题，但不要问太多。优先问会改变技术路线的 3 个问题。

## 可选参考

需要模板时读取 `references/project-brief-template.md`。不要默认把长模板全文加载到回答里。
