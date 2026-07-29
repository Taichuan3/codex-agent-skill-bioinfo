---
name: task-self-check
description: 用于任何生物信息学研究任务交付前的轻量自检，检查证据是否支撑 claim、文件是否可追踪、代码是否可复现、图表是否可读、文字是否越界，以及是否需要记录建议更新项。适用于用户要求“检查一下”“自检”“交付前 QA”“看看有没有问题”，或任务完成前需要统一质量门控的场景。
---

# Task Self Check

## 核心问题

如何在交付前做轻量质量门控，确认没有证据、复现、图表、路径或文字越界问题？

## 使用场景

当一个写作、分析、绘图、数据整理或项目规划任务即将交付时使用本 skill。它不是替代具体任务 skill，而是最后的轻量质量门控。

## 核心原则

- 自检要短，不重新读取大量上下文。
- 优先检查当前交付物和用户指定文件。
- 不用自检发明新结论。
- 如果发现问题，给出最小可修复建议。
- 复杂投稿级审计再交给更专门的 skill。

## 快速检查

按任务类型选择相关项：

- `Claim`：关键结论是否有证据来源，证据等级是否合适。
- `Writing`：段落是否服务章节功能，是否过度堆数据，是否越界。
- `Code`：输入、输出、命令、环境、参数是否清楚。
- `Figure`：是否有遮挡，字号是否可读，PNG/SVG 是否一致，source data 是否可追踪。
- `Data`：关键表格和最新文件是否容易找到，manifest 是否指向当前有效版本。
- `Tool`：外部工具或包是否记录版本、来源、license 和适配改动。
- `Phase`：当前交付物属于 exploration、confirmation、validation 还是 submission-ready，表述强度是否匹配。

## 输出格式

```text
Self-check
- Pass:
- Needs fix:
- Evidence risk:
- Reproducibility risk:
- Suggested record:
```

For this user's long-running research/project-organization tasks, the final chat output after self-check must be self-contained and Chinese by default. Include: actual work completed, changed files/dirs, key findings or comparison results, verification status and boundary, remaining risks, and next decision. Do not make temporary verification scripts or raw tool logs the main content, and do not require the user to open audit files just to understand the conclusion.

需要更细的检查表时读取 `references/self-check-rubric.md`。
