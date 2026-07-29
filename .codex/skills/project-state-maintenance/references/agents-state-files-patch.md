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

Update PROJECT_GUIDE.md only when a durable project fact changes: research question, hypothesis, dataset status, QC result, model baseline, structural result, major failure, paper claim, figure plan, risk, or next milestone. Keep PROJECT_GUIDE.md concise: target 2,000-4,000 Chinese characters, hard cap 6,000 characters or 120 lines. If it grows beyond the cap, compress old details into pointers to PROJECT_PLAN.md or output artifacts.

### Reading budget

Never load PROJECT_PLAN.md into the context window unless necessary. If needed, read by grep, tail, log_id, or line range. PROJECT_GUIDE.md is the normal startup context for project tasks.
```
