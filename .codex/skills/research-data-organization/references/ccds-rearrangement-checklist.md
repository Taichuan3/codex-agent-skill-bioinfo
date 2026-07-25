# CCDS rearrangement checklist for mature bioinfo projects

Use when reorganizing an existing analysis-heavy project into a Cookiecutter Data Science / CCDS-inspired structure.

## Safe sequence

1. **Restate the main task before acting**
   - Confirm whether the user wants documentation/index cleanup, physical directory moves, or both.
   - Do not let incidental tasks such as privacy cleanup, PDF export, or verification become the perceived main deliverable.

2. **Start with a no-move audit**
   - Identify primary report/manuscript outputs.
   - Classify analyses as primary report support, technical/provenance support, supplementary/exploratory, raw/local-only, or archive/provenance.
   - In a read-only audit, report proposed README/Directory Cards in chat without creating them.
   - Only in an authorized documentation/index cleanup may you write or update README/Directory Cards.

3. **Create a migration map before moving**
   Minimum columns:
   ```text
   source_path	target_path	move_type	reason	report_link_impact	script_path_impact	compatibility_action	status
   ```

4. **After explicit physical-move authorization, move low-risk top-level directories first**
   Common mature-project moves:
   - `figures/` -> `reports/figures/`
   - root `scripts/` -> `src/scripts/`
   - `sync_reports/` and local `logs/` -> `metadata/`
   - local release packages -> `release/`
   - raw/reference data -> `data/raw/` **only with compatibility symlinks if old scripts/docs use the old path**

5. **Preserve high-risk scientific paths unless explicitly migrated**
   - Keep numbered `analyses/` workflows stable when scripts and reports rely on relative paths.
   - Keep final report bundles stable if they are already submission/backup artifacts.

6. **Add targeted Directory Cards within the authorized write scope**
   Add short README files only for durable new namespaces: `metadata/`, `src/`, `release/`, `notebooks/`, `reports/figures/`, or important stage directories. Do not create them during a read-only audit.

7. **Verify after moves**
   Focused ad-hoc checks should confirm:
   - target directories exist;
   - old high-risk paths are either intentionally gone or symlinked;
   - migration map statuses are `done`/`keep`;
   - git sees tracked moves as renames;
   - final report image links still resolve;
   - `.gitignore` still excludes raw data, caches, symlinks, and large release artifacts;
   - personal/contact tokens were not reintroduced in navigation docs.

8. **Report task-centered status**
   Summarize: what structure changed, what stayed stable and why, what was verified, what remains. Do not make temporary verification-script paths the main content.
