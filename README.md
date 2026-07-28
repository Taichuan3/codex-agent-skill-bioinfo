# codex-agent-skill-bioinfo

通用生信科研 Codex Agent、Skills 与多设备安装包，面向 MacBook、Home/Lab 电脑和服务器上的 standalone OpenAI Codex CLI/IDE/app。GitHub `main` 只保留供仓库所有者跨设备安装、复用且无机器秘密的生信能力内核；项目私有上下文、运行缓存、原生 Memory、原始数据和结果保留在对应项目或机器上。

## 内容

- `AGENTS.md` — 本 capability package 仓库自己的项目级 Agent；用户运行时的通用方法由 `templates/global-AGENTS.md` 安装到全局。
- `local_config.yaml` — 本地打包/校验清单。
- `.codex/skills/` — 通用 bioinfo skills；每个 skill 至少包含：
  - `SKILL.md`
  - `agents/openai.yaml`
  - `evals/trigger-evals.json`
  - `evals/outcome-evals.json`
  - 可选 `references/`
- `.codex/agents/` — Codex 自定义子 Agent；包含 capability curation、source mapping、实现、复现审查、claim-evidence 审查和发行审查角色。
- `.codex/capability_registry.json` — 把治理型 Skill 映射到可选 plugin、MCP、标准 pipeline 或本地工具的机器可读登记表；它只负责选路，不授权安装、凭据、配额或数据上传。
- `templates/global-AGENTS.md` — 面向所有主机任务的精简全局 guidance；安装时作为受管 block 写入，不把完整 package Agent 复制到每轮上下文。
- `.codex/config.toml.example` — 经当前本机 Codex 验证的多 Agent 配置片段；按机器合并，不覆盖用户现有配置。
- `.agents/skills` — 指向 `.codex/skills` 的 repo-scope 兼容入口，供 standalone OpenAI Codex CLI/IDE/app 自动发现 skills。
- `scripts/install_codex_bioinfo.py` — 默认 dry-run、检查 source revision/digest 且失败时事务回滚的用户级安装器。
- `scripts/validate_package.py` — 全部 38 个 Skills 的结构、metadata、资源路由、eval 平衡、Agent TOML、敏感路径和发现入口校验。
- `scripts/test_release_safety.py` — privacy 拒绝项与安装器 symlink preflight 的隔离回归 fixtures。
- `scripts/validate_capability_run.py` — 对单次后端运行记录执行版本、授权、输入、provenance、artifact 与 evidence-boundary 门控。
- `scripts/test_capability_behavior.py` — 8 个去身份化行为 fixtures，覆盖任务不匹配、输入/运行时缺失、模型未授权、浮动版本和不完整产物的安全停止。
- `docs/MULTI_DEVICE_SYNC.md` — 公共内核、私有项目、机器层和 Memory 晋升边界。
- `docs/SKILL_STANDARDIZATION_2026-07-25.md` — 本轮 37-Skill 统一基线、来源、验证和发布边界。
- `docs/EXTERNAL_SOURCE_PROVENANCE.md` — 从历史审计恢复的 external repository、snapshot、license、能力级吸收和禁止 vendoring 记录。
- `docs/ROUTING_FORWARD_TEST_2026-07-25.tsv` — 可重放的 frontmatter-only 路由请求、expected/observed route 与运行时边界。
- `docs/RESEARCH_LIFECYCLE_SKILL_COVERAGE.md` — 从 Lab workflow audit 压缩出的研究生命周期 × skill 覆盖图，用于 skill-system 审计，不作为普通任务默认上下文。
- `LICENSE` / `NOTICE.md` — package-wide 权限边界及第三方来源处理声明。

## 使用方式

先在 clone 中验证：

```bash
python3 scripts/validate_package.py
python3 scripts/test_release_safety.py
python3 scripts/test_capability_behavior.py
python3 scripts/install_codex_bioinfo.py
```

脚本要求 Python 3.11+（使用标准库 `tomllib`）；若系统 Python 较旧，可在项目的 `bioinfo` conda 环境中运行。

第二条命令只显示计划。确认没有冲突后再执行：

```bash
python3 scripts/install_codex_bioinfo.py --apply
```

安装器会把 `$HOME/.agents/skills` 指向当前 release，使 38 个 Skills 成为不受工作目录限制的用户级全局能力；同时使用 `templates/global-AGENTS.md` 更新全局 `AGENTS.md`，并把自定义 Agent 安装到 `$HOME/.codex/agents/`。遇到非 symlink 的现有 `$HOME/.agents/skills` 时会停止，不静默覆盖。

`--apply` 在 Git checkout 中要求 source 工作树干净，并记录 source revision 与 package digest。安装期间任一步失败都会尝试恢复 Skill symlink、全局 guidance、旧 Skill 和 custom Agents；备份目录保留安装来源和恢复证据。

若当前全局文件已经混入旧 package Agent 或重复规则，可显式压缩为单一受管 block：

```bash
python3 scripts/install_codex_bioinfo.py --apply --replace-global-guidance
```

该模式仍会先备份原文件；后续普通安装可以通过 managed markers 原位更新，不会再次追加重复 block。

若旧版用户 Skills 仍位于 `$HOME/.codex/skills` 并与新 38 个 Skills 重名，可显式备份并退出这些旧目录：

```bash
python3 scripts/install_codex_bioinfo.py --apply \
  --replace-global-guidance \
  --retire-legacy-codex-skills
```

该选项把 `$HOME/.codex/skills` 下直接包含 `SKILL.md` 的用户 Skill 移入本次安装备份，保留 Codex 自带的 `.system`，并以 `$HOME/.agents/skills` 作为唯一 portable 全局 Skill source。

运行时只采用两层 Agent：全局 `$HOME/.codex/AGENTS.md` 与具体项目根 `AGENTS.md`。仅用于容纳多个项目的父目录不放 `AGENTS.md`、`PROJECT_GUIDE.md` 或 `PROJECT_PLAN.md`。具体项目必须在项目 Agent 中声明目录、数据边界、运行命令、环境、data/results/figures/source-data/manifest 入口和项目逻辑；项目专用 Skill 随私有项目仓库同步，不复制进公共全局内核。

## Standalone Codex CLI

- 从仓库根目录启动 `codex` 或 `codex exec` 时，Codex 会读取根 `AGENTS.md`。
- Codex 的 repo-scope Skill 自动发现路径是 `.agents/skills`；本仓库用 `.agents/skills -> ../.codex/skills` 保持一个 canonical source。
- `agents/openai.yaml` 是 Codex/OpenAI 产品侧 UI 元数据和默认提示，不替代 `SKILL.md`；触发判断仍以 `SKILL.md` frontmatter 的 `name` 和 `description` 为准。
- `.codex/agents/*.toml` 是真正的 Codex 自定义子 Agent 定义，不等同于 Skill 内的 `agents/openai.yaml`。

## 分支规则

- `main`：由 MacBook 维护的 owner-canonical，供 Home/Lab standalone Codex 直接安装和同步。
- `agent/<topic>`：其他终端、高风险实验或需要隔离审查时使用的短生命周期候选分支。
- 旧机器分支只作为历史输入，不再作为可直接安装的完整镜像。

MacBook Codex 可以把已完成 provenance、隐私、行为和 release review 的成熟变更直接发布到 `main`，但仍需用户明确批准。其他终端的变化先作为候选输入，不得整机覆盖 canonical。

## 许可边界

本仓库目前公开用于来源审阅和仓库所有者的多设备同步，但尚未授予开源复用许可；以根 `LICENSE` 为准。第三方工具、标准和知识来源仍受各自许可证或使用条款约束，仓库不因引用其名称而重新授权其内容。若未来希望允许外部人员复制、修改或分发，应由仓库所有者另行选择并提交明确的开源许可证。

此外，`docs/EXTERNAL_SOURCE_PROVENANCE.md`、`docs/EXTERNAL_FILE_LINEAGE.tsv`、`docs/EXTERNAL_EXPRESSION_REVIEW_2026-07-25.tsv` 与 `THIRD_PARTY_NOTICES.md` 保存历史来源、处置和保守归因。仓库所有者已授权当前版本作为自己跨设备安装使用的 canonical `main`；这不等于开放复用、第三方再分发或 license-cleared public release。历史 K-Dense 精确 snapshot 仍不可重新获取，因此不创建 stable release/tag，也不向外部授予根 `LICENSE` 之外的权利。

## 维护原则

- 先优化已有 Skill，尤其是跨项目实际使用后形成的成熟 bioinfo 机制。
- Runtime skill 的成熟经验要压缩回流到 source；不要整篇覆盖旧 source 后保留项目特异沉积，也不要用旧 source 覆盖 runtime 中已验证的新机制。
- 新候选 skill 只用于真实能力缺口；不能因为外部 repo 或某台机器有很多 skill 就盲目新增。
- 用户长期指令、重复纠正、流程失败和能力漂移通过 `controlled-self-improvement` 进入候选 → diff → 验证 → PR → 安装 → 监测/回滚闭环；curator 和定期 guardian 默认只读。
- GitHub 仓库保持轻量：只提交 Agent、Skills、必要配置和少量安装说明；长审计和工作草稿留在本地。
- 金融投资、旅行、个人账本和其他非生信工作流不进入本仓库。
- 运行时 Agent 只保留全局与具体项目两层；项目容器父目录不得成为隐式工作区。
- 项目级 Agent 必须保留：每个具体科研项目的 `AGENTS.md` 管理该项目的操作逻辑，通用包只提供基础规则和默认数据布局。

## 当前状态

- Source skills：38 个。
- Codex custom agents：6 个。
- 38 个 Skills 已统一为双字段 frontmatter、按需 references、三字段 UI metadata、20 条平衡 trigger eval 和至少 5 条 outcome case；当前共有 760 条 trigger 与 207 条 outcome 定义。
- Package validator 检查 eval 的 schema、数量、平衡、路由所有者和冲突；另有 8 个 capability safe-stop fixtures，但它们不替代真实模型 trigger/outcome forward test 或科研结果验证。
- 六个高频科研 owner Skill 已通过 capability registry 连接可选执行后端；registry 中的 `tool-bound` 只表示完成选路契约，不能写成安装、集成测试或科研验证已完成。
- Runtime 成熟经验按逐项 keep/merge 审查后回流 source；项目沉积、机器路径和重复 reference 不进入 canonical。
- 根 `AGENTS.md` 只保留认知/决策归属、证据、数据安全、项目状态和分支守门内核；细节由对应 skill/reference 承担。
- RNA-seq/single-cell、variant/genomics、pathway/network、clinical/translational、protein docking、drug screening、database grounding 已作为成熟领域 skill 保留。
