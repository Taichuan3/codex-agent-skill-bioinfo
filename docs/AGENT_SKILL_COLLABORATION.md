# Agent / Skill 多终端协作规则草案

> 状态：草案。用于让 Hermes、Codex、ChatGPT Pro、其他终端 agent 在多个终端/机器之间持续优化 bioinfo agent 与 skills。默认不自动合并、不自动覆盖本地 Hermes runtime skills。

## 1. 总原则

- **GitHub 仓库是唯一 source of truth**：`Taichuan3/codex-agent-skill-bioinfo`。
- **本地 Hermes runtime skills 只是运行副本**：`~/.hermes/skills/bioinfo/` 不作为主库。
- **多 agent 像多人协作**：每个终端/agent 使用独立 branch，提交后通过 PR 或审查队列合并。
- **先审查，再迁移**：外部 skill、其他终端的修改、本地 runtime 改动都先进入审查报告或同步分支，不直接污染主分支。
- **小批量合并**：一次 PR 只处理一个主题或一组强相关 skills。

## 2. Agent 角色分工

| 角色 | 默认职责 | 不应默认做的事 |
|---|---|---|
| Hermes | 主控、审查、去重、迁移决策、定期同步报告 | 未审查自动合并所有分支 |
| Codex | 大规模编辑、格式统一、脚本/测试/批量重构 | 改动多个无关 skill 后直接推 main |
| ChatGPT Pro browser | 慢速深度架构、从零设计、外部视角综合 | 日常小修小补、直接改 runtime skills |
| 其他终端 agent | 专项检索、候选清单、局部实验 | 越权覆盖主库规则 |

## 3. Branch 命名

推荐格式：

```text
<agent>/<type>/<short-topic>
```

示例：

```text
hermes/audit/external-skill-candidates
hermes/sync/local-runtime-skills-2026-06-30
codex/refactor/skill-frontmatter-boundaries
codex/migrate/evidence-gap-finder
chatgpt/architecture/bioinfo-skill-pack-v2
manual/hotfix/citation-verifier-trigger
```

`type` 建议：

- `audit`：只读审查、清单、报告
- `sync`：同步本地/其他终端改动
- `migrate`：迁移某个 skill 或一小组 skill
- `refactor`：结构调整、去重、拆 references
- `docs`：协作规则、说明文档
- `hotfix`：紧急修正

## 4. 每两天同步流程草案

推荐先采用 **半自动以下** 的安全流程：

1. 拉取主分支：
   ```bash
   git fetch origin --prune
   git checkout main
   git pull --ff-only origin main
   ```
2. 收集本地候选改动：
   - Git 仓库内改动：`git status --short`
   - Hermes runtime bioinfo skills：比较 `~/.hermes/skills/bioinfo/` 与仓库 `.codex/skills/`
   - 本地新增 agent/skill 草稿：只记录清单，不自动复制
3. 生成同步报告：
   ```text
   docs/sync-reports/YYYY-MM-DD-agent-skill-sync.md
   ```
4. 如果存在可提交改动，创建同步分支：
   ```bash
   git checkout -b hermes/sync/local-runtime-skills-YYYY-MM-DD
   ```
5. 只 staging 明确允许的文件：
   - `AGENTS.md`
   - `.codex/skills/**/SKILL.md`
   - `.codex/skills/**/references/**`
   - `docs/**`
   - `scripts/**`
6. 禁止 staging：
   - 原始数据、大型中间结果
   - API keys、tokens、cookies、浏览器缓存
   - 个人隐私文件
   - `PROJECT_ENVIRONMENT.md` 等本地私有环境文件
7. 提交并推送同步分支，默认创建 PR 或保留为候选分支。
8. Hermes 审查后再决定是否 squash merge 到 main。
9. 合并后，各终端从 main 更新。
10. 只有通过审查的稳定 skills 才同步到 `~/.hermes/skills/bioinfo/`。

## 5. PR / 合并标准

每个 PR 至少说明：

- 改动来源：哪个终端/agent/外部 repo/人工编辑
- 改动范围：涉及哪些 skills / docs / scripts
- 为什么需要：解决什么触发、复现、表达或效率问题
- 重叠检查：与现有哪些 skills 重复，如何处理
- 风险：是否可能过度触发、上下文膨胀、证据边界变弱
- 验证：至少跑过结构检查或人工审查

合并前检查：

```bash
git status --short
git diff --stat origin/main...HEAD
git diff --check origin/main...HEAD
find .codex/skills -name SKILL.md | sort | wc -l
```

## 6. 外部 skill 吸收规则

外部 repo 只能进入候选清单或改写后的新 skill，不能直接整包导入。

必须记录：

- source URL
- commit / release
- license
- 原始 skill 名称
- 吸收方式：引用 / 摘要 / 改写 / 灵感来源
- 与现有 skill 的重叠
- 是否适合 Hermes runtime

优先吸收：

- trigger 设计
- router / manifest / references 分层
- QA checklist
- evidence / citation / source-data guardrails
- 可复用脚本或模板

谨慎吸收：

- 过度 Nature/CNS 化表达
- 大而全但不精确的触发词
- 绑定特定平台或私有 API 的流程
- 自动生成、质量不稳定的 skill

## 7. 常见错误

1. **多个终端同时改 main**：导致覆盖和难以追溯。解决：一律 branch + PR。
2. **runtime skills 与 GitHub 主库脱节**：解决：runtime 只从 main 或明确 commit 同步。
3. **全量导入外部 skill**：导致误触发和上下文膨胀。解决：候选池 -> 去重 -> 小批量迁移。
4. **自动合并低质量改动**：解决：定时任务默认只报告或开 PR，不自动 merge。
5. **提交私密或大型文件**：解决：同步脚本做 allowlist + size check。
6. **不同 agent 风格冲突**：解决：Hermes 作为最终审查层，统一触发边界和证据规则。
7. **缺少来源记录**：解决：每次外部吸收必须写 source metadata。

## 8. 推荐自动化分级

| 等级 | 行为 | 适用阶段 |
|---|---|---|
| 安全档 | 只生成报告，不 push | 初期建立规则 |
| 半自动 | 推送 sync branch / draft PR，不 merge | 稳定后日常使用 |
| 高自动 | 自动审查通过后 merge + 本地同步 | 需要完整测试和回滚后再启用 |

当前建议：先使用 **安全档或半自动**，不要一开始自动合并。
