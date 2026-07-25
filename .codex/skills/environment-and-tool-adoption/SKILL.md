---
name: environment-and-tool-adoption
description: 用于生信任务需要选择、安装、升级、修复或采用 Python/R/CLI 包、成熟软件、容器、官方 protocol、论文代码或外部仓库时，评估来源、license、方法适配、环境影响并做最小验证；不负责新项目环境盘点、日常分析或未经授权的账号/系统变更。
---

# Environment and Tool Adoption

## 核心问题

如何选择并采用最适合任务的外部工具，同时让安装、版本、适配、验证和证据边界可复现？

## 能力边界

- 本 Skill 负责候选工具比较、依赖安装/修复、外部代码采用、版本固定、license/provenance 和 smoke test。
- 新项目或新机器的 cwd、Git、conda、Jupyter 和 local record 核验交给 `project-environment-bootstrap`。
- 本 Skill 不替代领域方法判断：是否采用某算法、阈值或数据库版本仍需结合对应分析 Skill 和用户决策。
- 安装成功不等于科学适用；smoke test 不等于结果有效、性能优越或方法复现完成。

## 权限与安全

- `recommendation-only` 只比较候选和给出命令，不安装或修改环境。
- 安装、升级、移除、写 lock/environment file、修改 shell/global config、容器拉取和源码构建都需要与用户请求相符；账号登录、license 接受和管理员权限单独确认。
- 先核验目标环境和已有版本；不得静默安装到 `base`、system Python/R、错误 kernel 或未指定服务器。
- 不执行 `curl | sh`、未审查的 install script、任意远端代码或含秘密的命令；先检查官方来源、checksum/signature（若提供）、license、依赖与入口。
- 不静默改变样本、过滤、参考版本、数据库、模型权重、随机种子或统计定义。
- 原始数据只读；先用合成或小样本 smoke test，再决定是否扩大运行。

## 工作流程

1. 锁定模式：`recommendation-only`、`install/upgrade`、`adopt/wrap` 或 `repair`。
2. 明确 decision question、目标环境、平台、输入输出、规模、license/引用要求和成功标准。
3. 只读检查已有工具、版本、包管理器、environment/lock file 和项目约束；已有方案满足时避免重复安装。
4. 比较官方成熟工具、论文实现、社区实现和最小本地代码；记录 method fit、维护状态、license、依赖、可移植性和失败模式。
5. 选择最小可复现路径：优先受控环境与固定版本；仅在必要时使用 system package、源码构建或容器。
6. 执行前展示将改变的环境、包和文件；只实施已授权范围，并保留完整命令与来源版本。
7. 先运行 import/version/help 或合成/小样本 smoke test，检查日志、输出 schema/count 和资源占用；高成本运行另行决定。
8. 记录 adopted/direct、wrapped、borrowed 或 rewritten 的边界，以及不能从验证中声称的内容。
9. 交付工具选择、实际变更、验证、provenance、回滚/卸载路径和未解决风险。

## 模式化输出

- `recommendation-only`：给出 decision matrix、推荐理由、可复现命令、风险和 stop point；不得修改环境。
- `install/upgrade`：报告目标环境、实际包/版本/命令、环境文件变化、smoke test 和 rollback。
- `adopt/wrap`：报告来源/license、接口适配、输入输出契约、局部修改、citation 和验证边界。
- `repair`：报告复现的失败、根因证据、最小修复、版本漂移和回归检查。

## 按需读取

比较候选、选择 direct/wrap/borrow/rewrite、评估 license/维护状态或生成 adoption record 时，读取 `references/tool-adoption-rubric.md`。

最终回复先给 adoption decision，再给环境变更、精确命令/版本、验证边界、回滚和下一决策。
