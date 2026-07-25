---
name: task-self-check
description: 对即将交付的具体生物信息学产物做轻量最终 QA，按可见材料检查 claim 支撑、复现信息、文件与 source-data 追踪、图表可读性、阶段标签和交付完整性，并报告 Pass/Needs fix/Not checked；用于“交付前自检/最后检查”而非深度科学审计、方案取舍、验证设计、代码实现或稿件全面一致性审查。
---

# Task Self Check

## 核心问题

如何用最小范围确认一个具体交付物是否可安全交付，并诚实标记未检查项？

## 边界

- 本 Skill 是任务完成后的轻量门控，不替代生成交付物的主 Skill，也不扩大范围重新分析数据。
- 高影响方案是否值得采用交给 `research-decision-review`；为具体 claim 设计验证交给 `validation-strategy-planner`。
- claim-to-evidence 深审用 `claim-evidence-audit`，引文核验用 `citation-verifier`，整篇稿件一致性用 `manuscript-consistency-audit`。
- 只检查当前交付物、直接依赖和用户指定证据；看不到的项目写 `Not checked`，不得猜测为 Pass。
- 发现问题时给出最小修复和严重度；除非用户已授权修复，否则停在 QA 报告。

## 工作流程

1. 明确交付物、预期用途、当前阶段和验收标准；选择相关检查维度，不机械跑全表。
2. 检查交付物及其直接指针，记录实际可见证据；不为自检扫描完整项目或冷历史。
3. 先识别 hard stop，再按 High/Medium/Low 分级；将缺少输入与失败区分。
4. 对每个问题给出最小修复、责任文件或下一检查；不得借 QA 发明新 claim。
5. 输出是否可交付：`Ready`、`Ready with caveats` 或 `Not ready`，并说明验证边界。

## 检查维度

按任务类型选择：

- `Claim`：关键结论是否有证据来源，证据等级是否合适。
- `Writing`：段落是否服务章节功能，是否过度堆数据，是否越界。
- `Code`：输入、输出、命令、环境、参数是否清楚。
- `Figure`：是否有遮挡，字号是否可读，PNG/SVG 是否一致，source data 是否可追踪。
- `Data`：关键表格和最新文件是否容易找到，manifest 是否指向当前有效版本。
- `Tool`：外部工具或包是否记录版本、来源、license 和适配改动。
- `Phase`：当前交付物属于 exploration、confirmation、validation 还是 submission-ready，表述强度是否匹配。
- `Delivery`：实际完成内容、变更文件、验证、边界、剩余风险和下一决策是否自包含。

## 输出契约

- Scope and stage
- Ready / Ready with caveats / Not ready
- Pass、Needs fix 和 Not checked
- Evidence/reproducibility risks with severity
- Minimal fixes and suggested durable record
- Validation boundary

长期研究或项目组织任务的最终回复默认中文且自包含：概括实际完成、变更文件、关键发现、验证状态与边界、剩余风险和下一决策；不以临时脚本或原始日志代替结论。

需要 hard-stop、严重度、phase-aware checks 或最小报告表时读取 `references/self-check-rubric.md`；单一格式检查不必加载。
