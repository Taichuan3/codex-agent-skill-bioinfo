# codex-agent-skill-bioinfo

通用生信科研 AGENT 与 skills 包。这个仓库的 GitHub 版本只保留可直接安装/复用的 agent 与 skill 文件；外部审计、润色草稿、迁移讨论和临时复盘默认保留在本地，不进入仓库。

## 内容

- `AGENTS.md` — 通用生信研究 agent 入口和 skill 路由。
- `local_config.yaml` — 本地打包/校验清单。
- `.codex/skills/` — 通用 bioinfo skills；每个 skill 至少包含：
  - `SKILL.md`
  - `agents/openai.yaml`
  - 可选 `references/`

## 使用方式

在新项目中复用时，可以把：

1. `AGENTS.md` 放到项目根目录。
2. `.codex/skills/` 合并到项目的 `.codex/skills/`。
3. 根据任务语义加载相应 skill；不要把所有 skill 同时读入上下文。

## 分支规则

- `main`：稳定、可直接安装/复用版本。
- `Hermes-review`：Hermes 作为最后守门员的审查整合分支。
- 其他 agent/terminal 的分支先合入 `Hermes-review`，通过结构检查和人工/自动审查后，再合并到 `main`。

## 维护原则

- 先优化已有 skill，尤其是 Hermes runtime 中经过多轮使用的 10 个默认 bioinfo skills。
- Runtime skill 的成熟经验要压缩回流到 source；不要整篇覆盖，也不要保留沉积和项目特异细节。
- 新候选 skill 只用于真实能力缺口；不能因为外部 repo 有很多 skill 就盲目新增。
- GitHub 仓库保持轻量：只提交 agent、skills、必要配置和少量安装说明；长审计和工作草稿留在本地。

## 当前状态

- Source skills：29 个。
- Hermes runtime bioinfo skills：10 个本地成熟副本，未在本仓库中直接覆盖。
- 当前候选新增方向包括 database grounding、protein structure/docking、drug discovery/ADMET；是否进入 runtime 需经过实际使用验证。
