# AGENT 骨架待办清单

本文件是通用生信研究 AGENT 的骨架路线图。它用于记录哪些原则应保留在根 `AGENTS.md`，哪些应下放到 skill、references 或项目 profile。它不承载具体研究背景，也不替代任何 skill。

状态标记：

- `[todo]` 未开始
- `[draft]` 已有草案
- `[migrate-to-skill]` 应下放到 skill
- `[keep-in-agent]` 应保留在根 AGENTS
- `[needs-review]` 需要后续讨论
- `[done]` 已完成当前阶段目标

## 设计原则

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 根 `AGENTS.md` 只定义 agent 定性、通用边界和路由 | 避免根规则过长，占用上下文，降低后续任务可用空间 | 根 `AGENTS.md` 已改为单一统一入口 |
| `[done]` | 任务细节继续下沉到 skill | 不同任务需要不同检查清单，全部写进根 AGENTS 会导致重复加载 | 已新增/更新通用 `.codex/skills/*/SKILL.md` |
| `[draft]` | 每个通用 skill 的 `description` 必须精确 | skill 触发主要依赖 frontmatter，描述不清会误触发或不触发 | 已为通用 skill 补 description；新增 `skill-quality-audit` 用于后续审计 |
| `[done]` | 复杂 skill 用 `references/` 承载细节、例子、rubric 和 QA | 遵循 progressive disclosure，减少默认上下文占用 | 图表、润色、翻译、source data、代码、工具采用、自检和决策 skill 已补 references |
| `[done]` | 不把大量例子、长 checklist、完整 protocol 塞进 `SKILL.md` | `SKILL.md` 应是执行入口，长材料按需读取 | 已将主要细节拆到 references |
| `[draft]` | 参考 Anthropic 官方 skill 规范继续校准目录结构 | 官方仓库强调 skill 是自包含文件夹，不是单个 prompt | 已新增 `skill-quality-audit`，后续逐个审计本地 skill |

## 根 AGENTS 保留项

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 默认用中文沟通 | 符合当前长期协作习惯，提高审阅效率 | 根 `AGENTS.md` |
| `[done]` | 代码、文件名、列名、方法名、数据库名、图中坐标轴和通用术语可保留英文 | 避免技术词翻译导致歧义 | 根 `AGENTS.md` |
| `[done]` | 启动上下文最小化 | 避免每次任务读取过多文件，特别是长项目计划导致上下文浪费 | 根 `AGENTS.md` |
| `[done]` | 默认读取根 `AGENTS.md`、被触发的 skill、轻量 `PROJECT_GUIDE.md` 和用户指定材料 | 保留必要规则与最小研究背景，同时不提前加载长日志 | 根 `AGENTS.md` 已明确先理解需求，再读取最小必要上下文 |
| `[done]` | `PROJECT_PLAN.md` 定位为记录/复盘对象，不作为默认读取对象 | 它适合记录结果，但反复读取会消耗大量上下文 | 根 `AGENTS.md` |
| `[done]` | 保留证据等级和 overclaim 防线 | 科研结论必须由数据支撑，不能由模型常识自动补全 | 根 `AGENTS.md` + `claim-evidence-audit` |
| `[done]` | 保留建设性反对原则 | 当用户方案存在证据、逻辑、复现或图表风险时，agent 应主动指出并给替代方案 | 根 `AGENTS.md` + `research-decision-review` |
| `[done]` | 保留轻量自检入口 | 每次交付前需要做基本一致性检查，但具体检查步骤交给 skill | 根 `AGENTS.md` + `task-self-check` |

## 根 AGENTS 删除或下沉项

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 图表 QA、配色、遮挡、导出格式和 panel 检查 | 图表检查很重要，但不应常驻根上下文 | 已下放到 `publication-plotting`，独立 `figure-qa` 暂缓 |
| `[done]` | 代码任务的输入、输出、环境、source data 详细 checklist | 代码检查与具体任务绑定，应由代码/复现 skill 执行 | 已下放到 `bioinfo-analysis-code` |
| `[done]` | 论文段落通顺性、英文润色、段落逻辑检查 | 写作检查应按任务触发，不应每次默认加载 | 已拆为 `chinese-scientific-polishing`、`scientific-english-translation`、`scientific-english-polishing` |
| `[done]` | source data inventory、Data/Code Availability、FAIR-like 审查细节 | 只有投稿、图表和数据整理任务需要完整加载 | 已下放到 `source-data-audit` |
| `[done]` | 详细默认工作循环 | 当前循环可能导致重复读取长上下文，后续改成轻量入口 + skill 自检 | 已补 `task-self-check` |
| `[done]` | 项目背景、研究主线、专属术语、固定路径、解释边界 | 项目背景和当前进度需要轻量入口，专属边界不属于通用 AGENT | 通用背景与主线下放到 `PROJECT_GUIDE.md`；专属边界放入 project profile |

## 需要下放到 Skill 的模块

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 自检模块 | 完成任务后需要检查证据、来源、复现、图表和文字质量，但检查步骤应按任务加载 | 已新增 `task-self-check` |
| `[done]` | 图表 QA 模块 | 需要检查遮挡、配色、排版、导出、source data 和 caption 对齐 | `publication-plotting` + `references/visual-qa.md` |
| `[done]` | 论文润色模块 | 英文和中文写作需要保护证据边界，同时提升可读性 | 已拆成 3 个 writing skills，并补 references |
| `[done]` | 项目指导文件维护模块 | 需要一个比 `PROJECT_PLAN.md` 更短、更适合默认读取的背景和主线入口 | 已新增 `project-guide-maintainer`，用于维护 `PROJECT_GUIDE.md` |
| `[done]` | source data 与复现检查模块 | 论文图表和关键数字必须可追踪 | 已写入 `source-data-audit` |
| `[done]` | 包/软件安装模块 | 任务可能需要 pandas、R 包、绘图包、命令行工具或生信软件；安装不应完全依赖被动 skill 触发 | v1.2 已提升为根 AGENTS 默认原则；复杂安装和 license 风险再调用 `environment-and-tool-adoption` |
| `[done]` | 外部工具借鉴模块 | 避免重复造轮子，优先评估 GitHub、论文代码和成熟工具 | v1.2 已提升为根 AGENTS 默认原则；复杂外部工具采用再调用 `environment-and-tool-adoption` |
| `[done]` | 文献阅读模块 | 需要阅读用户指定论文并抽取 figure-grounded evidence | v1.2 已新增 `paper-reader` |
| `[done]` | 系统文献检索模块 | 项目启动和补证据需要检索式、筛选标准和证据表 | v1.2 已新增 `literature-search-workflow` |
| `[done]` | 引用核验模块 | 防止 DOI/PMID/BibTeX 幻觉和 claim-to-citation 错配 | v1.2 已新增 `citation-verifier` |
| `[done]` | 投稿前预检模块 | 大版本收尾需要跨主文、图表、方法、数据、代码和引用检查 | v1.2 已新增 `submission-readiness-audit` |
| `[done]` | 稿件一致性模块 | 摘要、结果、图注、方法和 source data 的数字与术语需要锁定 | v1.2 已新增 `manuscript-consistency-audit` |
| `[done]` | 真实审稿回复模块 | 真实 reviewer comments 与模拟审稿风险应拆开处理 | v1.2 已新增 `reviewer-response-builder` |
| `[done]` | 证据缺口模块 | 需要从已有结果中找最小补分析集合，而不是无限扩展项目 | v1.2 已新增 `evidence-gap-finder` |
| `[done]` | 验证策略模块 | 探索性发现需要计算验证、外部数据验证、统计敏感性或降级写法 | v1.2 已新增 `validation-strategy-planner` |
| `[done]` | 建设性反对增强模块 | 当前反对原则偏短，未来需要更明确的证据、逻辑、成本和替代方案框架 | 已新增 `research-decision-review` |

## 新增能力待办

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 允许在本地安装任务所需包或软件 | 实际分析经常依赖缺失包；agent 应能主动安装并记录环境变化，而不是等用户指定 skill | v1.2 根 AGENTS 默认原则 + `environment-and-tool-adoption` 专项评估 |
| `[done]` | 安装前优先判断是否已有环境、包管理器或项目约束 | 避免污染环境、重复安装或破坏项目可复现性 | `environment-and-tool-adoption` |
| `[done]` | 使用成熟 GitHub 工具、论文代码或官方 protocol 前先做来源审查 | 避免直接运行不可信代码，也避免自己重写已有成熟工具 | v1.2 根 AGENTS 默认原则 + `environment-and-tool-adoption` |
| `[done]` | 对外部工具记录版本、来源、license、输入输出和适配改动 | 方便复现、引用和后续维护 | `environment-and-tool-adoption` + `source-data-audit` / `bioinfo-analysis-code` |
| `[done]` | 对“论文里已有方法”和“本地重写实现”做取舍 | 成熟工具优先，但需要能解释为什么不用或为什么改写 | `research-decision-review` + `environment-and-tool-adoption/references/tool-adoption-rubric.md` |

## 下一步收缩根 AGENTS.md

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 将根 `AGENTS.md` 压缩为短入口 | 当前根文件仍包含较多执行细节 | 已按 Anthropic skill 思路二次瘦身，根 AGENT 只保留身份、硬约束、证据规则和 skill 路由 |
| `[done]` | 删除默认读取 `PROJECT_PLAN.md` 的规则 | `PROJECT_PLAN.md` 应记录结果，不应每次消耗上下文 | 根 `AGENTS.md` 已明确不默认读取 |
| `[done]` | 保留最小上下文规则：用户指定文件、触发 skill、必要项目 profile | 降低上下文占用，避免任务后期频繁压缩 | 根 `AGENTS.md` |
| `[done]` | 把数据处理和图表细节移到 skill | 这些规则只在相关任务触发时需要 | 细节已下沉到 `bioinfo-analysis-code` / `publication-plotting` / `source-data-audit` |
| `[done]` | 把输出更新规则改成“建议记录项” | 避免每次自动读取和重写长项目计划 | 根 `AGENTS.md` 只保留是否建议写入长期记录 |
| `[done]` | 将默认工作循环压缩为轻量检查 | 只保留识别任务、选 skill、找证据、交付前自检 | 根 `AGENTS.md` + `task-self-check` |

## 后续参考来源

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[draft]` | Anthropic 官方 `skills` 仓库 | 参考 skill 最小结构、template 和 progressive disclosure 思路 | `agent_skill_review/github_repos/anthropics__skills` |
| `[draft]` | `Yuan1z0825/nature-skills` | 参考 Nature 写作、图表、引用、数据可用性、审稿回复的 workflow 结构 | `agent_skill_review/github_repos/Yuan1z0825__nature-skills` |
| `[draft]` | `Boom5426/Nature-Paper-Skills` | 参考 `paper-workflow`、`submission-audit`、`figure-planner` 等论文流程分层 | `agent_skill_review/github_repos/Boom5426__Nature-Paper-Skills` |
| `[draft]` | `K-Dense-AI/scientific-agent-skills` | 参考生信工具型 skill 和科学数据库 skill 的边界写法 | `agent_skill_review/github_repos/K-Dense-AI__scientific-agent-skills` |
| `[draft]` | `aipoch/medical-research-skills` | 参考医学研究任务拆分和 `skill-auditor` 质量门控 | `agent_skill_review/github_repos/aipoch__medical-research-skills` |
| `[draft]` | `wshobson/agents` | 参考插件化、能力包、agent/skill/command 分层组织 | `agent_skill_review/github_repos/wshobson__agents` |

## 当前不做

| 状态 | 事项 | 原因 | 下一步落点 |
|---|---|---|---|
| `[done]` | 不维护两个子 AGENT | 最终只保留一个根 AGENT，论文、数据、绘图、代码都由 skill 承载 | 当前仅要求通用根 `AGENTS.md`；项目 profile 按具体项目可选 |
| `[done]` | 不安装第三方 skill 到 `.codex/skills` | 需要先审查来源、触发描述、脚本和安全风险 | 已 clone 到 `agent_skill_review/github_repos/`，未直接安装 |
| `[done]` | 不把 Nature 规则写入根 AGENTS | Nature 是 venue/profile，不是所有科研任务的默认规则 | Nature 只作为本地 skill 设计参考 |
| `[done]` | 不把具体研究背景写进通用 AGENT | 具体项目应该放入 `PROJECT_GUIDE.md` 或 project profile | 通用 AGENT 不承载任何具体项目背景 |
