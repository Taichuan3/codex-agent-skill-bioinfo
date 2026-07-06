# codex-agent-skill-bioinfo

通用生信科研 Codex/Hermes agent 与 skills 包。GitHub 版本只保留可直接安装/复用的 agent、skills、兼容入口、少量 profile snapshot 和必要说明；外部审计、迁移草稿、运行缓存、原始数据和项目结果默认保留本地。

## 内容

- `AGENTS.md` — 通用生信研究 agent 入口、上下文预算、项目状态规则和 skill 路由。
- `local_config.yaml` — 本地打包/校验清单。
- `.codex/skills/` — 通用 bioinfo skills；每个 skill 至少包含：
  - `SKILL.md`
  - `agents/openai.yaml`
  - 可选 `references/`
- `.agents/skills` — 指向 `.codex/skills` 的 repo-scope 兼容入口，供 standalone OpenAI Codex CLI/IDE/app 自动发现 skills。
- `terminal_profiles/` — Home/Lab/Codex machine-level agent snapshot 的审计输入；只保留 agent/profile 说明，不作为默认运行规则。

## 使用方式

在新项目中复用时：

1. 把 `AGENTS.md` 放到项目根目录作为通用起点。
2. 保留或新增该项目自己的项目级 `AGENTS.md` 内容：项目目录、数据边界、运行命令、禁止修改路径、项目状态文件和 Codex 操作逻辑仍应由项目 agent 管理。
3. 合并 `.codex/skills/` 到项目 `.codex/skills/`，或安装到用户级 skills 目录。
4. 若直接使用 standalone OpenAI Codex CLI/IDE/app，在项目根目录创建 `.agents/skills` 指向 `.codex/skills`，或把 skills 安装到 `$HOME/.agents/skills`。
5. 根据任务语义加载相应 skill；不要把所有 skill 同时读入上下文。

## Standalone Codex CLI

- 从仓库根目录启动 `codex` 或 `codex exec` 时，Codex 会读取根 `AGENTS.md`。
- Codex 的 repo-scope skill 自动发现路径是 `.agents/skills`；本仓库用 `.agents/skills -> ../.codex/skills` 保持与 Hermes source layout 兼容。
- `agents/openai.yaml` 是 Codex/OpenAI 产品侧 UI 元数据和默认提示，不替代 `SKILL.md`；触发判断仍以 `SKILL.md` frontmatter 的 `name` 和 `description` 为准。

## 分支规则

- `main`：稳定、可直接安装/复用版本。
- `Hermes-review`：Hermes 作为最后守门员的审查整合分支。
- `home_PC_codex` / `lab_PC_codex`：机器或终端上传的输入分支，用于比较和吸收，不直接视为稳定版。

Hermes 定期检查其他 agent/terminal 推送的分支，把可用改动整合到 `Hermes-review`，通过结构检查和人工/自动审查后，再合并到 `main`。

## 维护原则

- 先优化已有 skill，尤其是 Hermes runtime 中经过多轮使用的本地 bioinfo skills。
- Runtime skill 的成熟经验要压缩回流到 source；不要整篇覆盖旧 source 后保留项目特异沉积，也不要用旧 source 覆盖 runtime 中已验证的新机制。
- 新候选 skill 只用于真实能力缺口；不能因为外部 repo 或某台机器有很多 skill 就盲目新增。
- GitHub 仓库保持轻量：只提交 agent、skills、必要配置和少量安装说明；长审计和工作草稿留在本地。
- 项目级 agent 文件必须保留：每个具体科研项目的 `AGENTS.md` 管理该项目的操作逻辑，通用包只提供基础规则。

## 当前状态

- Source skills：36 个。
- 新增/回写 runtime 成熟能力：`ml-benchmarking`、`project-state-maintenance`、`project-directory-card-maintenance`。
- 已吸收 Home/Lab 分支中稳定的 agent/profile 信息；Lab 机器的 profile agent snapshot 保留在 `terminal_profiles/lab_PC_codex/` 作为审计输入。
- RNA-seq/single-cell、variant/genomics、pathway/network、clinical/translational、protein docking、drug screening、database grounding 已作为成熟领域 skill 保留。
