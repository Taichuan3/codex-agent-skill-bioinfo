---
name: drug-discovery-admet-screening
description: 用于药物靶点探索、virtual screening、ADMET/QSAR、drug repurposing、target validation 和小分子筛选策略的候选工作流设计、数据库 grounding、工具选择、结果优先级排序和证据边界控制。适用于药物筛选/ADMET/靶点验证问题；不负责具体 protein docking pose 的结构解释。
---

# Drug Discovery and ADMET Screening

## 核心问题

如何把靶点、化合物、筛选目标、ADMET 风险和证据来源组织成可追踪的早期药物发现筛选计划，而不把预测或数据库关联升级为药效/安全结论？

## 使用场景

当用户讨论或执行以下任务时使用：

- target validation、drug repurposing、Open Targets/ChEMBL/ClinVar/PGx 证据整合。
- virtual screening、compound prioritization、molecular descriptor、QSAR、ADMET 初筛。
- PROTAC/molecular glue/covalent inhibitor 等药物设计想法的早期可行性拆解。
- 需要将 protein/gene evidence、compound evidence、screening metrics 和 caveat 整合成候选表。

不要用于：

- 具体 docking pose 或蛋白互作结构解释：用 `protein-structure-docking`。
- 普通数据库 ID 核验：用 `scientific-database-grounding`。
- 真实临床治疗建议或用药建议；本 skill 仅做科研候选筛选。

## 执行流程

1. 定义 discovery question：target、disease/context、compound space、desired endpoint。
2. Grounding：用 `scientific-database-grounding` 核验 target、compound、bioactivity、literature 和 safety 来源。
3. 选择筛选层级：database prioritization、descriptor/QSAR、ADMET、docking-derived score、pathway/omics support。
4. 建立候选表：每个 candidate 记录 evidence type、metric、source、version/date、uncertainty、next validation。
5. 分级：Strong / Moderate / Exploratory / Speculative；早期 computational screen 通常最多是 Exploratory。
6. 给出 stop/pivot criteria：哪些证据会使候选降级或放弃。

## 解释边界

- ChEMBL/Open Targets/literature association 不是当前项目实验验证。
- ADMET/QSAR 是预测或筛选信号，必须记录 applicability domain 和 uncertainty。
- Virtual screening rank 需要结合物理合理性、数据库活性、化学可行性和反例。
- Clinical/PGx 信息不能转成个人医疗建议。

## 输出格式

- Discovery question
- Target/compound definitions
- Databases and tools used
- Candidate prioritization table
- Evidence level and caveats
- Recommended next validation

## 按需读取

需要选择药筛/ADMET/target-validation 层级时读取 `references/drug-screening-decision-matrix.md`。
