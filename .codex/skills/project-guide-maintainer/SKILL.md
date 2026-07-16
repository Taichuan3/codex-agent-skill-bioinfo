---
name: project-guide-maintainer
description: 用于创建、更新或压缩生物信息学项目的轻量 PROJECT_GUIDE.md 项目指导文件。适用于需要把 research-project-planner 和 research-question-brief 的输出整合成可长期读取的研究背景、核心问题、主线、路线、当前进度、结果框架和论文草稿骨架；也适用于用户要求“维护项目指导文件”“更新研究主线”“把当前进展压缩成以后可读的背景”。
---

# Project Guide Maintainer

## 核心问题

如何把项目背景、核心问题、当前结果和下一步压缩成未来 agent 能快速读取的轻量 PROJECT_GUIDE？

## 使用场景

当项目需要一个轻量、长期可读、可作为后续上下文入口的指导文件时使用本 skill。它连接 `research-question-brief` 和 `research-project-planner`：前者保留用户原始想法，后者设计项目路线，本 skill 把二者压缩成项目执行和论文写作都能使用的 `PROJECT_GUIDE.md`。

## 定位

`PROJECT_GUIDE.md` 是 hot context / 当前项目卡片；`PROJECT_PLAN.md` 是 cold append-only log / 审计凭证。GUIDE 负责当前可执行性，PLAN 负责历史完整性。GUIDE 目标 2,000–4,000 中文字符，硬上限 6,000 字符或 120 行；只保存当前事实、关键证据指针、next actions 和风险，不保存流水账。它回答：

- 这个项目研究什么问题。
- 为什么值得研究。
- 当前主线和工作模型是什么。
- 技术路线分成哪几步。
- 每一步做到哪里了。
- 哪些结果可以支撑论文主体框架。
- 哪些 caveat、open question 和下一步最重要。
- 当前项目处于 exploration、confirmation 还是 validation 阶段。
- 五句话 `Known / Unknown / Question / Finding / Advance` 是否已经能说清。
- 哪些 reviewer attack 已经被证据、验证或降级写法处理。

`PROJECT_PLAN.md` 或类似文件只记录操作、运行结果和复盘，不应承担项目背景和论文主线。

## 内容原则

- 尽量短，目标是让 agent 快速理解项目背景和当前进度；用户要求 1–2 页时主动压缩到当前策略和当前执行规则。
- 保留研究主线，不保存流水账。
- 保留关键 claim、证据等级、figure/result skeleton 和 caveat。
- 不塞完整文献综述、长命令记录、大量路径、历史升级解释或每次运行细节。
- 已完成旧路线、详细 checkpoint 和历史产物列表下沉到 `PROJECT_PLAN.md`、README 或 Directory Card；GUIDE 只保留最新稳定策略和下一步决策。
- 未确认的信息标记为 `Assumption`、`Open question` 或 `Needs evidence`。
- 可以作为论文草稿骨架，但不是最终 manuscript。

## 推荐结构

```text
# PROJECT_GUIDE

## One-line summary
## Background
## Central question
## Known / Unknown / Question / Finding / Advance
## Working hypothesis / model
## Current story chain
## Result / figure skeleton
## Evidence package
## Exploration / confirmation / validation status
## Current progress
## Key evidence and caveats
## Reviewer attack list
## Open questions
## Next decisions
## Pointers
```

## 工作流程

1. 读取用户指定材料、已有 `PROJECT_GUIDE.md`、短 `research brief` 或 `project planner` 输出。
2. 抽取最少必要背景、主线、路线和当前进度。
3. 删除流水账式运行记录，把操作细节移交给 `PROJECT_PLAN.md` 或 summary。
4. 如果 GUIDE 过长或用户只要最新策略，重写为 1–2 页 current-state card：项目一句话、最新策略/模型、当前 pipeline、目录/操作规则、当前缺口和下一步；把旧 roadmap、历史版本解释和详细检查清单下沉。
5. 将结果路线组织成可支持论文主体的 result / figure skeleton。
6. 对每个主要 claim 标注证据等级或缺口。
7. 标记当前阶段：exploration、confirmation、validation 或 submission-ready。
8. 输出可直接写入或替换的 `PROJECT_GUIDE.md` 内容。

## 读取规则

后续任务需要项目背景时，优先读取 `PROJECT_GUIDE.md` 的以下短段落：

- `One-line summary`
- `Background`
- `Central question`
- `Known / Unknown / Question / Finding / Advance`
- `Current story chain`
- `Result / figure skeleton`
- `Exploration / confirmation / validation status`
- `Current progress`

只有任务需要复盘操作、找历史命令或确认具体输出时，才读取 `PROJECT_PLAN.md`。

## 输出格式

- `PROJECT_GUIDE.md draft` 或更新后的完整内容
- `保留的信息`
- `删除或下沉到 PROJECT_PLAN.md 的信息`
- `Needs evidence / open questions`
- `Suggested next update`

需要模板时读取 `references/project-guide-template.md`。
