# Project state file templates

## Initial PROJECT_PLAN.md

```markdown
# PROJECT_PLAN.md

Purpose: append-only project operation log for provenance, reproducibility, retrospective, manuscript methods, and reviewer response.

Read policy: do not read this file by default. Read only for audit, history, reconstruction, methods, reviewer response, retrospective, or targeted log_id lookup.

Write policy: append concise structured entries after material project actions. Do not paste raw logs, long outputs, full tables, secrets, patient-identifiable data, or large code diffs.

---
```

## PLAN entry budgets

- `MINI`: 3–5 lines for a small but material change.
- `STANDARD`: default, 6–10 lines covering intent, action, artifact/evidence, decision and next step.
- `DECISION/MILESTONE`: 600–1,000 Chinese characters for a direction-changing decision. If longer, create a dedicated decision artifact and link it.
- Append at most one normal entry per coherent task; do not log every command.

## PROJECT_PLAN entry

```markdown
## YYYY-MM-DD HH:MM TZ | PHASE | log_id=YYYYMMDD-HHMM-short-slug | status=done/blocked/failed/superseded

Intent:
- Why this step was done.

Actions:
- What changed or ran, in 1–3 bullets.

Inputs:
- Data/config/code references, including version, build, commit, checksum or run_id when relevant.

Outputs / evidence:
- Files, figures, tables, metrics, structures, run IDs or short observations.

Decision / interpretation:
- What the evidence means. Keep evidence separate from interpretation.

Next:
- Immediate next action or blocker.

Guide update:
- yes/no. If yes, name the exact PROJECT_GUIDE.md section.
```

Choose a short domain phase such as `DATA-QC`, `ASSOCIATION`, `STRUCTURE-MODELING`, `DOCKING`, `ML-BASELINE`, `ML-VALIDATION`, `FIGURE`, `MANUSCRIPT`, `REVISION` or `GUIDE-COMPRESSION`. A project may define additional stable phases in its `AGENTS.md`.

## GUIDE initialization handoff

Do not maintain a second full GUIDE template here. During state initialization, invoke `project-guide-maintainer` and use its `references/project-guide-template.md` only if the project needs the expanded schema. A minimal placeholder may contain:

```markdown
# PROJECT_GUIDE.md

## One-line summary
TBD.

## Central question
TBD.

## Current state
- Confirmed facts: none yet.
- Open questions: TBD.

## Next decisions
1. TBD.

## Pointers
- PROJECT_PLAN: `PROJECT_PLAN.md`
```

## Coupled GUIDE/PLAN transaction entries

GUIDE 更新与 PLAN provenance 使用同一个 `change_id`。先构造完整 GUIDE 候选并计算摘要或 hash，然后追加：

```markdown
## YYYY-MM-DD HH:MM TZ | GUIDE-UPDATE | change_id=YYYYMMDD-HHMM-short-slug | status=prepared

Intent:
- Replace or compress named PROJECT_GUIDE.md sections.

Target:
- GUIDE path and candidate hash.

Evidence:
- Artifact/run/config/log pointers supporting the candidate.
```

`prepared` 成功后才原子替换 GUIDE。替换成功时追加 `status=committed` 和实际 GUIDE hash；替换失败时尽力追加 `status=aborted` 并保留旧 GUIDE。若 GUIDE 已替换但 `committed` 追加失败，不回滚已确认 GUIDE；报告 `reconciliation required`，后续核验实际 hash 后补记状态。任何状态记录都只追加，不回写旧条目。

## Repair checklist

1. Preserve existing PLAN entries and record any corrupt range before repair.
2. Detect duplicate GUIDE chronology, stale pointers and facts unsupported by current artifacts.
3. Keep confirmed current state in GUIDE; keep chronology in PLAN.
4. Require explicit authority before rewriting PLAN history.
5. After repair, report exact files, retained evidence, unresolved conflicts and rollback.
