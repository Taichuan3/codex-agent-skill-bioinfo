---
name: controlled-self-improvement
description: 将用户明确的长期指令、重复纠正、流程失败、能力漂移或跨项目可复用经验转化为受控的 Codex memory、AGENTS.md、Skill、Agent、reference、checklist、配置或同步候选。适用于用户说“以后都这样”“记住这个偏好”“写进 Agent/Skill”“同步到其他设备”，或需要执行候选、diff、验证、PR、安装、监测、回滚闭环时；不用于一次性任务要求或未经授权的自动自修改。
---

# Controlled Self-Improvement

## 核心问题

如何让 Codex 根据稳定用户习惯持续改进 Agent、Skill、memory 和同步包，同时避免误学、上下文膨胀、隐私泄露和未经审查的自修改？

## Operating rule

Treat self-improvement as governed artifact evolution, not model-weight training. Detect candidates proactively, but do not silently make permanent changes.

Use this authority boundary:

- Read-only inspection and candidate drafting are allowed when relevant.
- Writing a local draft is allowed only within the current task scope.
- Updating active global guidance, memory, Skills, Agents, automation, or configuration requires explicit user authority.
- Commit, push, PR, installation, and rollback require the authority appropriate to each action.
- Updating or merging `main` always requires explicit user approval.

## Workflow

1. **Observe**
   - Capture an explicit long-term instruction, repeated correction, material failure, capability drift, or reusable cross-project pattern.
   - Preserve evidence pointers; do not copy raw private conversation or sensitive project content into a public candidate.

2. **Triage**
   - Decide whether the signal is stable, repeated, scope-changing, and future-useful.
   - Reject one-off preferences, transient environment failures, speculative personality inferences, and rules already covered by a more specific artifact.
   - Route the candidate to one primary target:
     - stable personal preference → memory;
     - all-task host rule → global `AGENTS.md`;
     - project boundary/fact → project `AGENTS.md` or `PROJECT_GUIDE.md`;
     - repeatable multi-step workflow → Skill/reference;
     - independent responsibility boundary → custom Agent;
     - quality gate → checklist/eval;
     - machine-only value → local config/template;
     - cross-device reusable source → reviewed Git branch/PR.

3. **Draft**
   - Copy `assets/improvement-candidate.md` or emit the same fields in chat.
   - Produce the smallest semantic diff. Prefer strengthening or compressing an existing artifact over adding a new one.
   - State context-size impact, privacy class, conflicts, installation targets, and rollback plan.

4. **Review**
   - Compare source, active runtime, project-local rules, and relevant history.
   - Check trigger precision, duplicate rules, scope precedence, provenance, secrets, private paths, unpublished facts, and license constraints.
   - Do not let the proposer be the only reviewer for public or high-impact changes.

5. **Validate**
   - Run structural validation plus the smallest behavioral or discovery check that can falsify the change.
   - Record exact commands, inputs, outputs, limitations, and before/after counts or hashes when useful.
   - A passing linter is evidence, not approval or proof of behavioral improvement.

6. **Publish and install**
   - After explicit authority, commit to an intake/review branch and open or update a draft PR.
   - Keep credentials, native memory/session/cache, machine paths, raw data, financial/personal content, and private project facts out of public Git.
   - Install only the reviewed source state; record source commit, runtime target, backup, and parity check.

7. **Monitor and rollback**
   - Observe at least one relevant future use when practical.
   - Roll back when the change mis-triggers, conflicts, expands context without value, weakens safety/evidence boundaries, or fails installation parity.
   - Preserve the rejected or rolled-back candidate record with the reason; do not keep inactive rules in hot context.

Read `references/lifecycle-and-governance.md` when selecting status transitions, privacy class, evidence threshold, reviewer requirements, or rollback gates.

## Candidate output

Every material candidate must contain:

- candidate ID, status, signal type, evidence pointer, and intended scope;
- primary target and why other targets were rejected;
- proposed semantic diff and context-size impact;
- privacy/publication class, conflicts, dependencies, and affected devices/projects;
- validation plan and results;
- authority, branch/commit/PR, installation targets, backup, and rollback procedure;
- owner and next action.

Use one candidate for one coherent behavioral change. Split unrelated changes even if discovered in the same task.

## Stop conditions

Stop at proposal-only when:

- the user has not authorized the required write, publish, install, or merge action;
- the signal may be temporary or conflicts with a more specific project rule;
- evidence is insufficient to distinguish stable preference from one-off correction;
- the candidate contains private or unpublished material that cannot be safely generalized;
- runtime/source drift or a dirty worktree prevents an attributable diff;
- validation or rollback cannot be defined.

Report the blocker and the smallest next decision. Do not interpret “self-improve” as permission to modify every available surface.
