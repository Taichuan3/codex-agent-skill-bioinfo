# AGENTS.md patch: Project state files

Add this section to project-level `AGENTS.md` when initializing or repairing a research repo.

```markdown
## Project state files

This project uses two local state files:

- PROJECT_GUIDE.md: hot project context. Read this file at the beginning of any task that depends on project background, current results, data/model/figure state, paper storyline, or next-step planning.
- PROJECT_PLAN.md: cold append-only project log. Do not read this file by default. Only read it when the user asks for audit/history/reconstruction/methods/reviewer-response/retrospective, or when PROJECT_GUIDE.md points to a specific log_id that must be checked.

### PROJECT_PLAN.md write rule

After any material project action, append a concise entry to PROJECT_PLAN.md without reading the full file. Each entry must include timestamp, phase, intent, action summary, artifacts, evidence, decision, next step, and whether PROJECT_GUIDE.md should be updated.

Do not paste raw logs, long command outputs, full code diffs, full tables, VCF/PDB contents, credentials, or patient-identifiable information into PROJECT_PLAN.md. Store paths, run IDs, config names, checksums, metrics, and short interpretations instead.

### PROJECT_GUIDE.md update rule

At authorized task closeout, check artifact paths/versions, completion/blockers, next steps and durable facts. Update PROJECT_GUIDE.md only when its summary is affected; otherwise report unchanged with a reason. Default target is 1,000-2,000 characters, warning above 3,000 characters or 80 lines. Preserve critical caveats and acceptance when compressing. The legacy 6,000-character/120-line limit requires repair or an explicit exception, never automatic truncation.

The main agent or sole owner merges worker deltas and writes shared state after checking concurrent edits. Root README links the stable result index instead of duplicating lists. Read-only tasks do not write. Report updated/unchanged/blocked; generated outputs alone do not establish complete handoff or scientific acceptance.

### Reading budget

Never load PROJECT_PLAN.md into the context window unless necessary. If needed, read by grep, tail, log_id, or line range. PROJECT_GUIDE.md is the normal startup context for project tasks.
```
