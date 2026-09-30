---
name: project-state-maintenance
description: 管理 GUIDE hot/PLAN cold 与实质任务收尾，按路径、版本、状态、阻塞或下一步 delta 更新受影响入口。只改 GUIDE→project-guide-maintainer；局部README→project-directory-card-maintenance；布局迁移→research-data-organization。只读/无变化不写。
---
# Project State Maintenance
## 核心问题
如何让 GUIDE 保持当前真值、PLAN 只追加历史且人工找到产物？
## 边界
仅具体项目根维护，父级容器不建状态；AGENTS管稳定边界、GUIDE管hot状态、PLAN管cold历史、README管导航。本 Skill拥有状态生命周期/收尾编排，不必每次加载全部维护Skills。
## 执行契约
1. 明确 initialize/task closeout/material append/targeted history read/state repair/GUIDE update decision；读项目AGENTS，背景必要时才读GUIDE。
2. read-only不写；无delta返回 unchanged及理由，不造空日志，不递归维护维护本身。数据/manifest/QC、分析、图表/claim/稿件、重大失败、工作流/未来决策为material action。
3. 路径/版本、完成或阻塞、限制、下一步、durable科学事实任一变化就评估收尾。只更新受影响的现有索引/入口；GUIDE摘要受影响才局部替换。未知claim/优先级标 Draft/Assumption/Needs confirmation，技术完成与作者接受分开。
4. 主Agent或唯一owner收集worker delta，写前核hash防并发覆盖。GUIDE/PLAN/manifest冲突先给证据和候选修复，不静默以新者为准。
5. PLAN只追加简洁 material record、不逐命令记、不塞原日志/diff/大表/凭据/患者信息/原始数据/不必要机器路径；不为寻找追加锚点读取历史（包括tail），只有audit/history/reconstruction/methods/reviewer-response/retrospective、log_id或冲突时定向查。用实际时钟记录带时区时间，禁止预填或虚构事件时间；改历史需明确修复授权。
6. GUIDE/PLAN耦合写：先备完整GUIDE候选/hash及同change_id prepared，PLAN prepared追加成功才原子替GUIDE，成功再追加committed；prepared失败不改GUIDE，替换失败保留旧GUIDE并尽力aborted，committed失败不回滚已确认GUIDE、报告 reconciliation required并后续核hash补记。不得把prepared报完成。
7. 返回各入口/GUIDE/PLAN的 updated/unchanged/blocked、理由、实际落盘/恢复动作和未决owner。根导航应找到图表/source/producer、不依赖聊天或PLAN；必要导航失败不称完整交付。模式输出与记录预算按下列资源；状态修复给冲突/回滚，定向读报告范围与缺口，初始化报告空字段。

## 按需读取和验证

- 实质写任务收尾或跨会话接手验证时，读取 `references/task-closeout-contract.md`；只核验明确路径、GUIDE 预算和成果登记时运行 `scripts/verify_project_handoff.py --help`，验证器只读且不代替科学审查。
- 初始化状态文件、选择 PLAN 记录预算、生成 entry 或执行 GUIDE/PLAN 耦合写入时，读取 `references/state-file-templates.md`。
- 初始化或修复项目 `AGENTS.md` 的状态规则时，读取 `references/agents-state-files-patch.md`。
- 只编辑状态规则后运行 `scripts/verify_agents_state_rules.py --mode state <AGENTS.md>`；状态与 Directory Card 规则组合后运行 `--mode combined`。它是 focused ad-hoc verifier，不是完整测试套件。

最终回复先给状态维护结果，再给文件、验证边界、剩余风险和下一决策。
