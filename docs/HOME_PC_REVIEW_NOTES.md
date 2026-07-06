# Hermes Review Notes

This branch, `home_PC_codex`, contains the Home PC Codex runtime snapshot for bioinformatics research.

## Review Target

- Root agent: `AGENTS.md`
- Skills: `.codex/skills/`
- Skill discovery pointer: `.agents/skills`
- Manifest: `local_config.yaml`

## Snapshot Scope

Included:

- The local Home PC bioinformatics agent instructions.
- The 26 project-level bioinformatics skills currently active in the Home PC Codex workspace.
- Each skill's `SKILL.md`, `agents/openai.yaml`, and directly associated `references/`.

Excluded:

- Raw data and derived analysis outputs.
- Python/R environments, cache directories, and temporary files.
- Project-specific manuscripts, figures, source data tables, and local execution logs.
- User-level system skills outside this bioinformatics package.

## Hermes Tasks

1. Check whether any local project-specific assumptions should be removed before `main`.
2. Compare this runtime snapshot against `main` and decide whether removed skills should remain removed or be merged back after compression.
3. Validate that each skill has concise trigger metadata and does not over-read context by default.
4. Confirm no secrets, tokens, private paths, raw data, or runtime cache files are present.
5. Promote only stable, reusable agent/skill changes to `main`.
