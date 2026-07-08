---
name: project-state-maintenance
description: 用于维护研究项目的 PROJECT_GUIDE hot context 与 PROJECT_PLAN cold append-only log，处理初始化、追加、压缩、修复和读取边界。
metadata:
  hermes:
    tags: [bioinformatics, project-state, project-guide, project-plan, provenance, context-budget]
    related_skills: [project-guide-maintainer, research-data-organization, bioinfo-agent-workflow]
---

# Project State Maintenance

## Purpose

Maintain two local project state files for research repos:

- `PROJECT_GUIDE.md` = hot project context, current project card, short source of current truth.
- `PROJECT_PLAN.md` = cold append-only project log, audit/provenance/electronic-lab-notebook style record.

Use this skill when initializing, repairing, reading, appending, compressing, or updating project state files; also when the user says “state maintenance”, “项目状态文件”, “PROJECT_PLAN”, “PROJECT_GUIDE”, “项目日志”, “项目卡片”, or asks to make project records easier for future Hermes/Codex sessions.

Full source standard is stored at `/Users/yajiehu/.hermes/references/Taichuan_Hermes_Project_State_File_Standards.md`.

## Core distinction

```text
AGENTS.md          behavior/routing rules, short and stable
PROJECT_GUIDE.md  hot current context, read for project tasks
PROJECT_PLAN.md   cold append-only log, write by default after material actions, do not read by default
```

Do not let `PROJECT_GUIDE.md` become a second log. Do not let `PROJECT_PLAN.md` enter normal context.

## Startup policy

For project tasks:

1. Read `AGENTS.md` if loaded or inspect project rules when needed.
2. Decide whether the task depends on project background/current state.
3. If yes, read `PROJECT_GUIDE.md`.
4. Do **not** read `PROJECT_PLAN.md` by default.
5. Read `PROJECT_PLAN.md` only by targeted grep/tail/log_id/line range when the user asks for audit/history/reconstruction/methods/reviewer response/retrospective, when `PROJECT_GUIDE.md` points to a needed `log_id`, or when project state is inconsistent.

## End-of-task policy

Before finalizing a material project task:

1. Decide whether the turn produced a material project action.
2. If yes, append a concise structured entry to `PROJECT_PLAN.md` **without reading the full file**.
3. Decide whether a durable project fact changed.
4. If yes, read and update `PROJECT_GUIDE.md` by replacement/compression, not endless append.
5. For workflow/style corrections, also perform self-improvement routing: decide whether the correction belongs in USER/memory, global `AGENTS.md`, project `AGENTS.md`, a class-level skill, checklist/eval, or a prompt contract. Do not store long procedures in memory.
6. In final reply, report `PROJECT_PLAN.md` append status and `PROJECT_GUIDE.md` update status.

Material actions include: data download/transform/QC, manifest/checksum changes, model training/evaluation/ablation/validation, structure modeling/docking/MD, important figure/claim/manuscript changes, major failures, rejected hypotheses, project-level constraints, workflow rule changes, user corrections that affect future behavior, or decisions that affect future analysis.

Non-material actions include: generic Q&A, read-only inspection with no decision, trivial formatting/spelling, or temporary debug output already saved elsewhere with no conclusion.

## PROJECT_PLAN.md write budget

- `MINI`: 3–5 lines, small modification or no major conclusion.
- `STANDARD`: default, 6–10 lines; intent, actions, artifacts, evidence, decision, next.
- `DECISION/MILESTONE`: 600–1000 Chinese chars for direction-changing decisions; if longer, create `docs/decisions/ADR-*.md` and link from PLAN.

One normal Hermes turn should usually append at most one STANDARD entry. Do not log every shell command.

## PROJECT_PLAN.md entry template

```markdown
## YYYY-MM-DD HH:MM JST | PHASE | log_id=YYYYMMDD-HHMM-short-slug | status=done/blocked/failed/superseded

Intent:
- Why this step was done.

Actions:
- What was changed or executed, in 1-3 bullets.

Inputs:
- Data/config/code references. Include version, build, commit, checksum, or run_id when relevant.

Outputs / evidence:
- Files, figures, tables, metrics, structures, run IDs, or short observations.

Decision / interpretation:
- What this means for the project. Separate evidence from interpretation.

Next:
- Immediate next action or blocker.

Guide update:
- yes/no. If yes, state the exact PROJECT_GUIDE.md section.
```

## PROJECT_GUIDE.md rules

Read `PROJECT_GUIDE.md` at the beginning of tasks that depend on project background, current results, data/model/figure state, paper storyline, or next-step planning.

Update it only when a durable project fact changes: research question, hypothesis, accepted/rejected dataset, QC caveat, baseline/model result, structural result, figure claim, paper storyline, major risk, or next milestone.

Budget:

- Target: 2,000–4,000 Chinese characters.
- Hard cap: 6,000 characters or 120 lines.
- Main findings: 5–7 items max.
- Next actions: 3 max.
- Risks: 5 max.

If too long, compress old details into `log_id` or artifact pointers. Do not copy `PROJECT_PLAN.md` content into the guide.

## GUIDE update algorithm

1. Append PLAN first for complete provenance.
2. Ask whether the new information affects next decisions, paper claim/figure, data/model/structure protocol, default project knowledge, and has artifact/run/config/log support.
3. If fewer than two are yes, keep it only in PLAN.
4. If durable, update GUIDE current-state sections and keep within budget.
5. Record the GUIDE update status in the PLAN entry.

## Project-specific phase tags

Use phases such as:

`IDEA`, `LITERATURE`, `DATA-DISCOVERY`, `DATA-DOWNLOAD`, `DATA-QC`, `GENETICS-QC`, `VARIANT-ANNOTATION`, `ASSOCIATION`, `STRUCTURE-PREP`, `STRUCTURE-MODELING`, `DOCKING`, `ML-DATASET`, `ML-BASELINE`, `ML-ABLATION`, `ML-VALIDATION`, `FIGURE`, `MANUSCRIPT`, `REVISION`, `RETROSPECTIVE`, `GUIDE-COMPRESSION`.

## AGENTS.md patch

When initializing or repairing a repo, add a concise “Project state files” section from `references/agents-state-files-patch.md`.

## Pitfalls

- Do not read `PROJECT_PLAN.md` in full at normal task start.
- Do not paste raw logs, long command outputs, full code diffs, full tables, VCF/PDB contents, credentials, or patient-identifiable data into PLAN/GUIDE.
- Do not update GUIDE for temporary failed experiments, small formatting changes, or unvalidated exploratory outputs.
- Do not turn GUIDE into a chronology; it is current-state only.

## Verification after rule-file edits

When editing `AGENTS.md`, `PROJECT_GUIDE.md`, `PROJECT_PLAN.md` templates, or state-file routing rules, do not claim the behavior is verified without fresh evidence. If the repo has no canonical lint/test command, run a focused temporary ad-hoc verifier and label it as such, not as suite green.

Recommended pattern:

1. Create a temporary script with an OS-safe tempfile path and `hermes-verify-` prefix.
2. Check the changed file for required hot/cold state rules, targeted PLAN read policy, Directory Card policy if relevant, and context-budget sanity.
3. Run it against the changed file.
4. Remove the temporary script when possible.
5. Summarize explicitly as `ad-hoc verification`, including what was checked.

A reusable verifier is available at `scripts/verify_agents_state_rules.py`; copy or run it when appropriate, adapting checks to the project.

## Completion message

Use a compact final note, but never let verification output replace the task report. If the task did anything beyond checking state, the final response must include the actual task outcome first, then verification as evidence.

中文保险：最终回复必须是完整交付报告，不得只输出最后一个验证步骤。验证输出只能作为证据，不能吞掉任务报告。

Required order:

- Done: concise summary of the actual task outcome.
- Files/artifacts: key paths changed or generated.
- Verification: canonical command or ad-hoc verification result and what it checked; label ad-hoc checks as ad-hoc, not suite green.
- Project state: `PROJECT_PLAN.md` appended log_id=...; `PROJECT_GUIDE.md` updated <section> or not updated because <reason>.
- Next: immediate next action or remaining decision.

Output integrity safeguards:

- Do not return only `AD_HOC_VERIFICATION=passed`, script path, cleanup line, or raw tool stdout. Those are verification evidence only.
- Before finalizing after an ad-hoc verification command, reconstruct the full task narrative from the user's request and actual changes.
- Avoid ending the final response with a fenced code block. Prefer inline code or bullets for short paths/commands. If a fenced block is necessary, ensure opening and closing fences are balanced and followed by normal text.
- Never output orphan language labels such as `text` or `markdown`; language labels belong only on the same line as an opening fence.

