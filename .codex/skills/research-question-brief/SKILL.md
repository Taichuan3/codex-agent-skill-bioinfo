---
name: research-question-brief
description: 将口头、零散或多轮讨论中的生物信息学研究想法压缩为一页以内的 research question brief，明确 working question、意义、必要证据、约束、假设、开放问题和下一项方向决策；用于尚未进入完整项目规划的早期问题澄清，不用于技术路线、验证矩阵、决策取舍审查、文献检索或执行。
---

# Research Question Brief

## 核心问题

把用户真正想研究的问题压缩成可确认、可继续规划且不虚构结论的短方向契约。

## 边界

- 本 Skill 只澄清研究对象、问题边界、价值、证据需求和下一项方向决策，不选择完整方法、数据管线、figure skeleton、里程碑或 go/no-go 标准。
- 需要完整项目路线时转交 `research-project-planner`；已有方案需要 continue/pivot/stop 或工具取舍时转交 `research-decision-review`。
- 针对既有 claim 设计验证层级时转交 `validation-strategy-planner`；系统检索证据时转交 `literature-search-workflow`。
- 将已确认内容写入当前项目状态时转交 `project-guide-maintainer`；具体分析、代码、绘图或写作使用相应执行 Skill。
- 不把未确认信息写成事实；统一标记 `Assumption` 或 `Open question`。不把 brief 扩写成综述、项目日志或 prompt 执行计划。

## 工作流程

1. 抽取对象、现象、比较、范围、期望贡献和显式约束；保留用户原意。
2. 将宽泛主题改写为一个主 working question；必要时给出最多两个候选表述，不替用户选方向。
3. 区分已知输入、暂定假设和缺失信息；只问最多三个会改变研究边界或后续路线的问题。
4. 说明支持或否定该问题需要的证据类别，不提前承诺具体方法或结果。
5. 输出并迭代一页以内的 brief；更新时替换旧表述，不追加讨论流水账。

## 输出契约

- `One-line idea`
- `Current working question`
- `Why it matters`
- `Possible hypothesis`（可选，必须标明暂定）
- `Evidence needed`
- `Current constraints`
- `Assumptions and open questions`
- `Next decision`

需要可直接填写或落盘的一页结构时读取 `references/research-question-brief-template.md`；不需要模板时不要加载它。

最终说明哪些内容来自用户、哪些仍待确认，以及下一步应继续问题澄清还是转入项目规划。
