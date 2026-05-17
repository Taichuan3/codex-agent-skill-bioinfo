# v1.2 参考候选清单

本文件记录后续可选择性扩展的参考来源和候选能力。v1.2 已将 P1 文献/引用、P1 投稿/审稿和 P2 研究设计中的部分候选提升为本地通用 skill；生信专项 skill pack 仍保留为未来候选。

## 候选能力优先级

### P1：文献与引用

| 候选 skill | 价值 | 本地化方向 | 参考来源 |
|---|---|---|---|
| `paper-reader` | 把论文 PDF/全文转为带 figure grounding 的中文阅读材料 | 已在 v1.2 新增 | Nature reader 类 skill、Scientific Agent Skills 文献工具 |
| `literature-search-workflow` | 项目启动和补证据时系统检索文献 | 已在 v1.2 新增 | Nature academic search、K-Dense database/search skills |
| `citation-verifier` | 防止引用幻觉、DOI 错误和 unsupported citation | 已在 v1.2 新增 | Nature citation、Nature Paper citation verifier |

### P1：投稿与审稿

| 候选 skill | 价值 | 本地化方向 | 参考来源 |
|---|---|---|---|
| `submission-readiness-audit` | 投稿前检查主文、图、方法、数据和代码是否一致 | 已在 v1.2 新增 | Nature Paper submission audit、AIPOCH reporting guideline 思路 |
| `manuscript-consistency-audit` | 检查摘要、结果、图注、方法和 source data 的数字一致性 | 已在 v1.2 新增 | AIPOCH consistency checker、Nature Paper manuscript optimizer |
| `reviewer-response-builder` | 返修时把审稿意见转成 response table 和补分析优先级 | 已在 v1.2 新增 | Nature response、AIPOCH author response builder |

### P2：研究设计

| 候选 skill | 价值 | 本地化方向 | 参考来源 |
|---|---|---|---|
| `evidence-gap-finder` | 从已有结果中找出缺失证据和过弱 claim | 已在 v1.2 新增 | AIPOCH claim strength / gap 思路 |
| `validation-strategy-planner` | 为 exploratory 结果设计验证路线 | 已在 v1.2 新增 | AIPOCH protocol design、K-Dense scientific workflows |

### P3：生信专项 skill pack

| 候选方向 | 价值 | 本地化方向 | 参考来源 |
|---|---|---|---|
| RNA-seq | 常见表达矩阵、差异分析、富集和图表 | 只在出现真实 RNA-seq 任务时加入 | K-Dense / AIPOCH data analysis skills |
| single-cell | Scanpy/Seurat、annotation、marker、trajectory | 需要强依赖版本和输入对象规范 | K-Dense Scanpy/anndata/cellxgene 类 skills |
| ATAC-seq / ChIP-seq | peak、motif、coverage、QC 和可视化 | 需明确 genome build、blacklist、peak caller | K-Dense deeptools 等专项 skills |
| GSEA / pathway | 富集分析、背景基因集、结果解释 | 防止把富集写成机制结论 | Scientific Agent Skills pathway/ontology 方向 |
| variant / GWAS | variant annotation、locus interpretation、PRS/GWAS | 需严格处理人群结构、版本和统计阈值 | K-Dense genomics / clinical precision medicine 方向 |

## 已 clone 本地仓库可借鉴点

| 本地仓库 | 可借鉴点 | 不直接采用的原因 |
|---|---|---|
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/anthropics__skills` | 短 `SKILL.md`、精确 description、复杂材料放 `references/`、完整目录作为分发单元 | 平台是 Claude 示例，需要按 Codex 校验和本地科研规则适配 |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/Yuan1z0825__nature-skills` | 论文阅读、学术检索、引用核验、数据可用性、审稿回复、Nature 风格写作链路 | 偏 Nature/CNS 期刊场景，需转成通用生信科研，不引入项目专属图表 skill |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/Boom5426__Nature-Paper-Skills` | paper workflow、bootstrap、figure planner、citation verifier、submission audit、rebuttal response | 强 journal-first，不适合作为根 AGENT；适合拆成候选投稿/引用 skill |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/K-Dense-AI__scientific-agent-skills` | 生信/科学工具专项 skill pack、数据库和 Python 包参考、安装安全提醒 | 覆盖面很大，直接安装会增加误触发和维护成本 |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/aipoch__medical-research-skills` | 医学研究工作流分类、MedSkillAudit、claim strength、consistency、response builder | 医学临床色彩较强，需要抽取通用科研结构 |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/InternScience__Awesome-Scientific-Skills` | 科研 skill 分类、来源分层、Phase 1/2/3 渐进式建设方式 | 当前更像索引，不是可直接迁移的本地 skill |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/VoltAgent__awesome-agent-skills` | 大型 skill registry 的分类和质量标准入口 | 大量非科研技能，适合作为发现来源，不适合作为默认上下文 |
| `/Users/yajiehu/bioinfo/agent_skill_review/github_repos/wshobson__agents` | 插件粒度控制、渐进披露、多 agent/workflow 分层、质量评估框架 | 偏软件工程与 Claude 插件生态，不能直接迁入科研 AGENT |

## 外部高星/高关注候选来源

以下为本轮网络检索记录，仅作为后续 v1.2 候选来源。是否克隆和纳入审阅需用户后续指定。

| 仓库 | 候选价值 | 后续建议 |
|---|---|---|
| [openai/skills](https://github.com/openai/skills) | Codex skill 官方目录，可参考安装、元数据和标准结构 | P1：后续优先 clone 或拉取特定官方示例 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | Web quality / engineering skill 组织方式，可借鉴质量门控和 review 结构 | P3：仅借鉴结构，不作为科研内容来源 |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | 大规模跨 agent skill 索引，可用于发现 paper/search/citation 类技能 | P3：先筛选，不整库导入 |
| [callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills) | 结构清晰的团队技能包，含 Codex/Claude marketplace 元数据 | P3：借鉴分发和 metadata 组织 |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 大型 Claude/Codex 兼容 skill 索引，分类较全 | P3：只作搜索入口 |
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | OpenClaw skill 大型目录，可查找 academic search、paper retrieval 等方向 | P3：注意供应链和质量风险 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code 生态索引，包含 agents、hooks、commands 和 skills | P3：适合参考生态，不直接迁移 |

## 本轮提取出的设计原则

- 根 `AGENTS.md` 只做短入口，不承载候选功能。
- skill 的 `description` 必须同时说明“做什么”和“什么时候用”。
- 复杂示例、模板和 checklist 放入 `references/`，由 skill 按需读取。
- 大型 skill registry 只能作为发现来源，不能整库导入到当前项目。
- 涉及外部代码、脚本、安装命令的 skill 必须先审查 license、来源、版本和安全风险。
- 科研 skill 必须优先保护证据边界，不能把写作质量优化变成 claim 升级。
