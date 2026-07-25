---
name: evidence-gap-finder
description: 用于从已有结果包、论文草稿、figure plan、claim-evidence map、审稿意见或 revision backlog 中识别阻断性与重要证据缺口，并按 claim impact、最小补分析、降级写法、成本和依赖排序；不用于执行分析、开放式找文献、逐条验证 citation 或仅做语言润色。
---

# Evidence Gap Finder

## 核心问题

当前 evidence package 距离目标 claim 还缺什么，最小且最有决策价值的补强路径是什么？

## 能力边界

- 本 Skill 拥有 gap identification、blocking/important/optional triage 和 minimal-fix portfolio。
- 逐句判定现有 claim 是否越界时，以 `claim-evidence-audit` 为主；本 Skill 消费其 findings 并排序补强动作。
- 开放式检索新论文交给 `literature-search-workflow`；核验现有 citation 交给 `citation-verifier`。
- source-data 完整性审计交给 `source-data-audit`；稿件数字/术语/图号一致性使用 `manuscript-consistency-audit`。
- 代码实现、重跑、绘图和湿实验不由本 Skill 执行；输出可验收的 handoff。
- 用户拥有 claim 强度、资源投入和 go/no-go 决策；不得把高成本补强默认为必须执行。

## 证据与优先级边界

- 先锁定目标 deliverable、目标 claim strength、deadline、可用数据和资源限制。
- 每个 gap 必须绑定 claim、figure/table/source data、reviewer risk 或复现要求。
- 区分缺数据、对照、统计、敏感性、外部验证、provenance、复现、citation 和解释过度。
- 缺口可以用补证据、降级写法、移至 Discussion、删除 claim 或明确 limitation 关闭；不把“多做分析”当默认答案。
- 不静默改变样本、阈值、过滤、参考版本、统计定义或环境。

## 工作流程

1. 建立目标 claim–current evidence–intended use 表，记录证据等级与已知 caveat。
2. 识别 claim 能否由当前证据支持，以及缺口属于事实缺失、验证缺失还是叙事越界。
3. 按 P0 blocking、P1 important、P2 useful、P3 optional 分类，并说明 failure mode。
4. 为每项设计最小关闭路径：复用现有输出、补 control/sensitivity/statistics、找外部证据、降级/删除文本或新数据。
5. 估计 cost、dependency、decision value 和验收标准；把高成本或改变研究方向的选项交给用户。
6. 去除重复或不会改变 claim 的分析，形成 1–3 个优先 work packages。
7. 输出执行顺序、stop condition、仍无法关闭的 limitation 和后续 handoff。

## Revision backlog 模式

当用户要求先汇总草稿批注而不改正文时，提取括号批注、审稿意见和口头反馈，按全局问题、Results 小节、figure、Methods/Supplement、术语一致性和执行顺序合并去重。不得直接逐句改稿或把批注当作已验证事实。

## 按需读取

需要统一 P0–P3、成本等级和优先级判定时，读取 `references/gap-priority-rubric.md`。

## 交付契约

优先输出 `Claim | Current evidence | Gap | Failure risk | Minimal fix or downgrade | Cost/dependency | Acceptance criterion | Priority`，并给出 1–3 个 work packages、stop conditions、未解决 limitation 和需要用户决定的高影响选项。
