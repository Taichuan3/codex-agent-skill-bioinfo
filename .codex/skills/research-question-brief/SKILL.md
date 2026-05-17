---
name: research-question-brief
description: 用于把用户口头或零散描述的研究想法转成简短、可维护、可迭代的研究问题 brief。适用于用户想在沟通过程中不断优化一个方向文档，保留主要论点、目标、边界、证据需求和下一步，而不让长记录占用上下文。
---

# Research Question Brief

## 使用场景

当用户提出一个原始想法、研究方向、模糊问题或连续讨论中的项目设想，需要把它整理成短文档时使用本 skill。它不同于 `research-project-planner`：本 skill 维护用户想法的精简方向文档，后者设计完整项目路线。

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
