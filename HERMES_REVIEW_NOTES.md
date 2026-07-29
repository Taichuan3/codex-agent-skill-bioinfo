# Hermes Review Notes

This branch, `home_PC_codex`, contains a reviewed candidate snapshot of the Home PC Codex bioinformatics skills. It is input for comparison with `main`, not a directly installable release.

## Review Target

- Skills: `.codex/skills/`
- Skill discovery pointer: `.agents/skills`
- Manifest: `local_config.yaml`

## Snapshot Scope

Included:

- The 36 bioinformatics skills active in the Home PC project runtime on 2026-07-29.
- Each skill's `SKILL.md`, `agents/openai.yaml`, and directly associated `references/`.
- A manifest updated to treat `main` as owner-canonical.

Excluded:

- Raw data and derived analysis outputs.
- Python/R environments, cache directories, and temporary files.
- Project-specific manuscripts, figures, source data tables, and local execution logs.
- User-level system skills outside this bioinformatics package.
- The current research project's project-level `AGENTS.md`; the branch's existing generic `AGENTS.md` was retained.
- Two machine-local Mac reference paths found in the runtime source; these were removed from the candidate copy.

## Hermes Tasks

1. Check whether any local project-specific assumptions should be removed before `main`.
2. Compare the 36 runtime skills against `main`; all same-name `SKILL.md` files differ from current `main`, so review them semantically rather than treating file-level difference as automatic improvement.
3. Validate that each skill has concise trigger metadata and does not over-read context by default.
4. Confirm no secrets, tokens, private paths, raw data, or runtime cache files are present.
5. Promote only stable, reusable agent/skill changes to `main`.

## Local Validation

- Official `quick_validate.py`: passed for all 36 source skills before packaging.
- Candidate structural gate: every skill has `SKILL.md`, `agents/openai.yaml`, frontmatter, body, and `## 核心问题`.
- Privacy scan: no project identifier/path, Windows absolute path, user home path, email, credential value, raw data, result table, or runtime cache is intended to be present.
- Scope boundary: this candidate does not include the 38-skill eval/agent/release framework currently maintained on `main`.
