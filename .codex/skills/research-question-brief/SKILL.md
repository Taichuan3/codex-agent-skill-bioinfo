---
name: research-question-brief
description: 用于把用户口头、零散或多轮讨论中的研究想法压缩成简短 research question brief，保留 one-line idea、working question、why it matters、evidence needed、constraints 和 next decision。不用于完整技术路线设计、文献检索或项目执行。
---

# Research Question Brief

## 核心问题

如何把零散想法压缩成一个短 research question brief，保留为什么重要和下一步决策？

## 使用场景

当用户提出一个原始想法、研究方向、模糊问题或连续讨论中的项目设想，需要把它整理成短文档时使用本 skill。它不同于 `research-project-planner`：本 skill 维护用户想法的精简方向文档，后者设计完整项目路线。

## 不适合触发

- 需要完整项目路线、figure skeleton 或技术路线时，使用 `research-project-planner`。
- 需要系统文献检索时，使用 `literature-search-workflow`。
- 已进入具体分析、绘图或写作任务时，使用对应执行 skill。


## 核心原则

- brief 要短，只保留指导后续执行的主线。
- 记录用户真实意图，不替用户发明结论。
- 可以在多轮沟通中迭代，但每次都压缩旧信息。
- 不存放长背景、详细文献笔记、完整结果和大量路径。
- 未确认的信息标记为 `Assumption` 或 `Open question`。

## 推荐结构

- `One-line idea`
- `Current working question`
- `Why it matters`
- `Possible hypothesis`
- `Evidence needed`
- `Current constraints`
- `Open questions`
- `Next decision`

## 工作流程

1. 从用户描述中抽取核心想法和研究对象。
2. 把模糊表达改写成可执行问题。
3. 标出不确定点和需要用户确认的关键选择。
4. 输出一个不超过 1 页的 brief。
5. 如果用户继续讨论，更新 brief 时优先合并和压缩，不追加流水账。

## 输出规则

输出必须可作为后续任务方向指导，但不能替代证据、项目计划或论文正文。

需要模板时读取 `references/research-question-brief-template.md`。
