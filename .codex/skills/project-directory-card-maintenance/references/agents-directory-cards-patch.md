# AGENTS.md patch: Directory Cards

Add this section to project-level `AGENTS.md` when adopting Directory Cards.

```markdown
## Directory Cards

This project uses short directory-level `README.md` files as on-demand directory cards for important artifact folders.

Purpose:
- Help future agents understand what a result/data/model/figure folder contains without opening every file.
- Preserve local provenance and navigation information.
- Keep `PROJECT_GUIDE.md` short and keep `PROJECT_PLAN.md` as the detailed append-only log.

Read policy:
- Do not read all directory READMEs at startup.
- Before scanning a large directory under `data/`, `models/`, `reports/`, or `experiments/`, check for a local `README.md` and read it first.
- Use the local README as a navigation aid, then read only the specific manifest, registry, script, config, or artifact needed for the task.
- If a directory README is stale or contradicts manifests/scripts, report the inconsistency and update the README only after verifying the current truth.

Update policy:
- Update a directory README only when a durable artifact, canonical dataset, best model, candidate/final figure, structure result, genetics result, screening campaign, reproduction command, deprecation status, or file layout changes.
- Do not update directory READMEs for failed experiments, temporary files, intermediate caches, or reruns with unchanged conclusions.
- Do not copy large file lists, full metrics tables, sample metadata, variant tables, or candidate molecule lists into README files. Link to TSV/CSV/JSON/MLflow/manifest files instead.

Naming policy:
- Use `README.md` for directory cards.
- Use nested `AGENTS.md` only for directory-specific behavior rules, not for result catalogs.
- Keep ordinary directory cards under ~2,000 characters; complex artifact cards under ~3,000 characters.
```
