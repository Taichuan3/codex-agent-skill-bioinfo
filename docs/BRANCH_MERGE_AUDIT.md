# Branch Merge Audit: Hermes-review + Home PC + Lab PC

Date: 2026-07-06
Working branch: `integrate-home-lab-hermes-20260706-172538`
Base: `origin/Hermes-review` (`9b5b87a`)
Compared branches: `origin/home_PC_codex`, `origin/lab_PC_codex`

## 1. Input branch summary

| Branch | Role | Skills | AGENTS.md files | Main finding |
|---|---:|---:|---:|---|
| `Hermes-review` | reviewed source base | 33 | 1 | Best source layout; includes 7 domain expansions and Codex `.agents/skills` compatibility. |
| `home_PC_codex` | Home PC runtime snapshot | 26 | 1 | Older/smaller set; useful as regression input but would delete mature domain skills if merged directly. |
| `lab_PC_codex` | Lab PC runtime/profile snapshot | 33 root + profile copy | 3 | Root skills mostly older than Hermes-review; valuable part is machine/profile AGENTS snapshot under `terminal_profiles/`. |
| local Hermes runtime | newest local iterative source | 36 | n/a | Adds project-state, directory-card, and ML benchmarking skills plus updated workflow references. |

## 2. Merge decisions

| Area | Decision | Reason |
|---|---|---|
| Root source base | Keep `Hermes-review` as base | It is already curated and newer than Home/Lab snapshots for source structure. |
| Home branch | Keep `docs/HOME_PC_REVIEW_NOTES.md`; do not downgrade skills | Home branch has 26 skills and deletes mature Hermes-review domain skills. |
| Lab branch | Keep selected `terminal_profiles/lab_PC_codex/*/AGENTS.md` and README | User wants project/agent files retained; duplicate old `skills/` snapshot was not copied to avoid bloat/regression. |
| Runtime skills | Backport mature local Hermes runtime bioinfo skills to `.codex/skills` | Runtime is newest user-iterated source. |
| Project-specific residue | Remove project-specific references before source commit | Generic source package should not include AlphaGenome/D20S16/repeat-specific notes. |
| Project-level AGENTS | Explicitly preserve project AGENTS policy | Codex should still read project-level agent files for project-specific operation logic. |

## 3. Added or backported skills

- `ml-benchmarking`: benchmark task contract, baseline, split protocol, leakage checks, negative controls, ablation, validation, model card.
- `project-state-maintenance`: `PROJECT_GUIDE.md` hot context + `PROJECT_PLAN.md` cold append-only log policy.
- `project-directory-card-maintenance`: selective README Directory Cards for important artifact folders.

Final expected source skill count: 36.

## 4. Agent updates

Root `AGENTS.md` now integrates:

- repository guardian rules for Hermes-review;
- standalone Codex `.agents/skills` discovery explanation;
- Chinese-by-default project document rule;
- Hermes/Codex division-of-labor gate;
- hot/cold project state policy;
- Directory Card read/update policy;
- explicit preservation of concrete project `AGENTS.md` files;
- skill route entries for 36 skills.

## 5. Self-check focus

Validation should confirm:

1. every `.codex/skills/*/SKILL.md` has frontmatter `name` and `description`;
2. every skill has `agents/openai.yaml`;
3. source skill count is 36;
4. `.agents/skills` points to `../.codex/skills`;
5. no obvious secrets or machine cache files are committed;
6. project-specific AlphaGenome/D20S16/repeat-result references are absent from the generic source package;
7. retained `terminal_profiles` contains agent/profile documentation, not duplicate full skill runtime cache.
