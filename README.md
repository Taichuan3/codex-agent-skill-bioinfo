# codex-agent-skill-bioinfo

通用生信科研 Codex Agent、Skills 与多设备安装包，面向 MacBook、Home/Lab 电脑和服务器上的 standalone OpenAI Codex CLI/IDE/app。GitHub `main` 只保留可安装、可复用、无机器秘密的生信能力内核；项目私有上下文、运行缓存、原生 Memory、原始数据和结果保留在对应项目或机器上。

## 内容

- `AGENTS.md` — 通用生信研究 agent 入口、上下文预算、项目状态规则和 skill 路由。
- `local_config.yaml` — 本地打包/校验清单。
- `.codex/skills/` — 通用 bioinfo skills；每个 skill 至少包含：
  - `SKILL.md`
  - `agents/openai.yaml`
  - 可选 `references/`
- `.codex/agents/` — Codex 自定义子 Agent；包含 source mapping、实现、复现审查、claim-evidence 审查和发行审查角色。
- `.codex/config.toml.example` — 推荐的多 Agent 配置片段；按机器合并，不覆盖用户现有配置。
- `.agents/skills` — 指向 `.codex/skills` 的 repo-scope 兼容入口，供 standalone OpenAI Codex CLI/IDE/app 自动发现 skills。
- `scripts/install_codex_bioinfo.py` — 默认 dry-run 的用户级安装器。
- `scripts/validate_package.py` — package 结构、Agent TOML、敏感路径和发现入口校验。
- `docs/MULTI_DEVICE_SYNC.md` — 公共内核、私有项目、机器层和 Memory 晋升边界。
- `docs/RESEARCH_LIFECYCLE_SKILL_COVERAGE.md` — 从 Lab workflow audit 压缩出的研究生命周期 × skill 覆盖图，用于 skill-system 审计，不作为普通任务默认上下文。

## 使用方式

先在 clone 中验证：

```bash
python3 scripts/validate_package.py
python3 scripts/install_codex_bioinfo.py
```

脚本要求 Python 3.11+（使用标准库 `tomllib`）；若系统 Python 较旧，可在项目的 `bioinfo` conda 环境中运行。

第二条命令只显示计划。确认没有冲突后再执行：

```bash
python3 scripts/install_codex_bioinfo.py --apply
```

安装器会把 `$HOME/.agents/skills` 指向当前 release，更新全局 `AGENTS.md` 中的受管 bioinfo block，并把自定义 Agent 安装到 `$HOME/.codex/agents/`。遇到非 symlink 的现有 Skill 目录时会停止，不静默覆盖。

具体项目仍需保留自己的项目级 `AGENTS.md`：项目目录、数据边界、运行命令、环境、禁止修改路径和项目逻辑不能由通用包替代。项目专用 Skill 应随私有项目仓库同步，不复制进公共全局内核。

## Standalone Codex CLI

- 从仓库根目录启动 `codex` 或 `codex exec` 时，Codex 会读取根 `AGENTS.md`。
- Codex 的 repo-scope Skill 自动发现路径是 `.agents/skills`；本仓库用 `.agents/skills -> ../.codex/skills` 保持一个 canonical source。
- `agents/openai.yaml` 是 Codex/OpenAI 产品侧 UI 元数据和默认提示，不替代 `SKILL.md`；触发判断仍以 `SKILL.md` frontmatter 的 `name` 和 `description` 为准。
- `.codex/agents/*.toml` 是真正的 Codex 自定义子 Agent 定义，不等同于 Skill 内的 `agents/openai.yaml`。

## 分支规则

- `main`：稳定、可直接安装到 Home/Lab standalone Codex 的版本。
- `agent/<topic>`：短生命周期的候选整理/审查分支，通过 draft PR 汇总变更。
- 旧机器分支只作为历史输入，不再作为可直接安装的完整镜像。

MacBook Codex 可以周期性整理各终端的候选变化，但必须逐项审查来源、适用范围、隐私、license 和复现性。只有通过验证并获得用户明确批准后，才允许合并或更新 `main`。

## 维护原则

- 先优化已有 Skill，尤其是跨项目实际使用后形成的成熟 bioinfo 机制。
- Runtime skill 的成熟经验要压缩回流到 source；不要整篇覆盖旧 source 后保留项目特异沉积，也不要用旧 source 覆盖 runtime 中已验证的新机制。
- 新候选 skill 只用于真实能力缺口；不能因为外部 repo 或某台机器有很多 skill 就盲目新增。
- GitHub 仓库保持轻量：只提交 Agent、Skills、必要配置和少量安装说明；长审计和工作草稿留在本地。
- 金融投资、旅行、个人账本和其他非生信工作流不进入本仓库。
- 项目级 agent 文件必须保留：每个具体科研项目的 `AGENTS.md` 管理该项目的操作逻辑，通用包只提供基础规则。

## 当前状态

- Source skills：36 个。
- Codex custom agents：5 个。
- Runtime 成熟经验按逐项 keep/merge 审查后回流 source；项目沉积、机器路径和重复 reference 不进入 canonical。
- 根 `AGENTS.md` 只保留认知/决策归属、证据、数据安全、项目状态和分支守门内核；细节由对应 skill/reference 承担。
- RNA-seq/single-cell、variant/genomics、pathway/network、clinical/translational、protein docking、drug screening、database grounding 已作为成熟领域 skill 保留。
