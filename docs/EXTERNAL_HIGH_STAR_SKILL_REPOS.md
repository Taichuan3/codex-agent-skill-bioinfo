# External High-Star Skill / Agent Repository Candidates

> 分支：`Hermes-review`。用途：记录适合 Hermes / Codex / bioinfo agent 体系吸收、审计、去重和迁移的外部高质量 skill / agent 项目。此文件只是候选清单，不代表已迁移或已认可全部内容。

## 使用原则

- 先下载/审计/学习，不直接整包导入。
- GitHub 源仓库与 license 必须记录。
- 重点吸收：trigger 设计、router 分层、references/static 结构、QA checklist、科研证据边界、可复用脚本。
- 谨慎吸收：过度宽泛的 trigger、平台私有 API、自动生成低质内容、过度 Nature/CNS 化、会导致上下文膨胀的大型技能包。
- 与用户现有 bioinfo skill 体系冲突时，优先保留用户现有逻辑，只吸收能提高 precision、reproducibility、evidence boundary 或运行效率的部分。

## 优先级定义

- **P0**：立刻审计，和用户背景/当前 Hermes 运行效率高度相关。
- **P1**：适合第二轮审计，可能部分吸收。
- **P2**：作为生态参考或索引，不直接迁移。

## P0：用户背景强相关 / 第一批审计

| Repo | URL | Stars 快照 | SKILL.md 数量 | 方向 | 初步用途 |
|---|---|---:|---:|---|---|
| nature-skills | https://github.com/Yuan1z0825/nature-skills | ~24.4k | 14 | Nature 风格科研写作、绘图、审稿、文献 | 吸收 router/manifest/static/references 架构和科研表达 QA |
| science-skills | https://github.com/google-deepmind/science-skills | ~2.1k | 37 | AlphaGenome、AFDB、UniProt、ChEMBL 等科学数据库 grounding | 补强 genetics / variant / structure / drug database grounding |
| scientific-agent-skills | https://github.com/K-Dense-AI/scientific-agent-skills | ~29.6k | 149 | biology / chemistry / medicine / drug discovery | 科学 agent 总库，按主题采样 |
| ClawBio | https://github.com/ClawBio/ClawBio | ~1.0k | 92 | bioinformatics-native, local-first, reproducible | 学习可复现生信 workflow 和 local-first 设计 |
| bioSkills | https://github.com/GPTomics/bioSkills | ~961 | 553 | 广泛生信任务 | 用作缺口词典和任务覆盖参考，强去重后采样 |
| BioNeMo Agent Toolkit | https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit | ~200 | 65 | protein folding, docking, generative chemistry, genomics | 补强 protein/docking/drug discovery 方向 |
| protein-design-skills | https://github.com/adaptyvbio/protein-design-skills | ~143 | 24 | protein/binder design | 专项吸收 binder design/AlphaFold/BindCraft workflow |
| AtomisticSkills | https://github.com/learningmatter-mit/AtomisticSkills | ~124 | 127 | atomistic chemistry, docking, molecular workflow | 药物设计/化学计算候选，谨慎采样 |

## P1：提高 Hermes / Codex 工作效率

| Repo | URL | Stars 快照 | SKILL.md 数量 | 初步用途 |
|---|---|---:|---:|---|
| superpowers | https://github.com/obra/superpowers | ~241k | 14 | agentic workflow / planning / parallel agents 方法论 |
| agent-skills | https://github.com/addyosmani/agent-skills | ~68k | 24 | 生产级工程质量、测试、CI/CD、API 设计 |
| mattpocock/skills | https://github.com/mattpocock/skills | ~150k | 36 | 工程师实践、重构、QA |
| ECC | https://github.com/affaan-m/ECC | ~223k | 887 | agent harness / skills / memory / security，大而全，需谨慎审计 |
| Agent-Skills-for-Context-Engineering | https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering | ~16.8k | 21 | 上下文工程、多 agent 架构 |

## P2：官方生态与索引参考

| Repo | URL | Stars 快照 | 初步用途 |
|---|---|---:|---|
| anthropics/skills | https://github.com/anthropics/skills | ~156k | 官方 skill 规范参考 |
| openai/skills | https://github.com/openai/skills | ~23k | Codex skill 结构参考，注意 deprecated 状态 |
| google/skills | https://github.com/google/skills | ~14k | Google 官方工具/产品 skill 结构 |
| huggingface/skills | https://github.com/huggingface/skills | ~10.7k | HF Hub / model / dataset 工作流 |
| NVIDIA/skills | https://github.com/NVIDIA/skills | ~2k | NVIDIA 官方 AI agent skills，可能与 GPU/加速计算有关 |
| agentskills/agentskills | https://github.com/agentskills/agentskills | ~21k | Agent Skills 标准/spec 参考 |
| VoltAgent/awesome-agent-skills | https://github.com/VoltAgent/awesome-agent-skills | ~26k | 索引型目录，不直接迁移 |

## 审计输出格式

每个 repo 的审计报告应包含：

1. repo 元信息：URL、commit、license、stars、更新日期。
2. skill inventory：SKILL.md 数量、目录结构、support files。
3. 高价值模块：值得吸收的 trigger、流程、模板、references、脚本。
4. 与现有 bioinfo skills 的重叠：保留、合并、改写或跳过。
5. 迁移建议：core / on-demand / reference only / reject。
6. 风险：license、平台耦合、过度触发、上下文膨胀、证据边界。
7. 下一步：是否创建具体 migration branch 或只保留为参考。

## 当前策略

- 第一批优先审计 P0 中前 4 个：`nature-skills`、`science-skills`、`scientific-agent-skills`、`ClawBio`。
- 暂不向 `~/.hermes/skills/bioinfo/` 复制外部 skill。
- 暂不 merge 到 `main`。
- 成熟后才进入默认 Hermes skill 仓库。
