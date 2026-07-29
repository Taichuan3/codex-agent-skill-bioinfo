---
name: environment-and-tool-adoption
description: 用于在生物信息学任务中安装缺失的 Python/R/命令行包，评估并采用 GitHub 工具、论文代码、官方 protocol 或成熟软件，避免重复造轮子，同时记录版本、来源、license、环境和适配改动。
---

# Environment and Tool Adoption

## 核心问题

如何在需要外部工具或依赖时，选择成熟方案、记录来源版本 license，并避免不可复现或不可信安装？

## 使用场景

当任务需要缺失依赖、包安装、R 绘图包、Python 包、生信软件、GitHub 工具、论文代码或官方 protocol 时使用本 skill。

## 核心原则

- 优先使用成熟工具和已有论文代码，不重复造轮子。
- 安装前先检查当前环境、包管理器、项目约束和已有替代方案。
- 不直接运行不可信脚本；先审查来源、license、依赖和输入输出。
- 记录工具版本、安装命令、来源链接、license、适配改动和运行环境。
- 对探索阶段和发表整理阶段使用不同严格度。

## 安装流程

1. 检查当前环境和已有包。
2. 判断安装方式：`mamba/conda`、`pip`、`R install.packages`、`BiocManager`、`brew`、源码或容器。
3. 优先选择可复现方式，例如环境文件、版本号或 lock file。
4. 安装后运行最小验证命令。
5. 记录安装命令和版本。

## 外部工具采用流程

1. 找到候选工具或论文代码。
2. 审查维护状态、stars/issues、license、文档、输入输出、依赖和引用方式。
3. 判断是否直接使用、局部借鉴、重写最小实现或放弃。
4. 若采用，写明适配边界和不能声称的内容。
5. 把工具来源和版本写入方法或复现记录。

## 输出格式

- `Need`
- `Existing environment check`
- `Recommended tool/package`
- `Install or adoption command`
- `Verification`
- `Version/source/license`
- `Reproducibility notes`

## 按需读取

需要判断外部工具是直接使用、包装适配、只借鉴思路还是本地重写时，读取 `references/tool-adoption-rubric.md`。
