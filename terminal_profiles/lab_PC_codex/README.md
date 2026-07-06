# lab_PC_codex terminal profile

This directory is a machine-level Codex skill/agent snapshot from the lab PC.

Snapshot date: 2026-07-06
Source branch: `lab_PC_codex`
Source host label: `lab_PC_codex`

## Contents retained in this integrated source package

- `agents/bioinfo/`: the lab PC global bioinfo agent package snapshot.
- `user-home/AGENTS.md`: the lab PC user-home-level AGENTS entry.

## Source snapshot note

The original `lab_PC_codex` input branch also contained a full skill runtime snapshot. In this integrated package, those duplicate skills are **not** copied under `terminal_profiles/` because the curated source of truth is `.codex/skills/`. This profile keeps only machine/profile agent files needed for comparison and future setup repair.

## Notes

- This profile intentionally excludes secrets, tokens, local Codex auth files, browser state, runtime caches, raw data, and duplicate skill runtime trees.
- The repository root `.codex/skills` and `AGENTS.md` are the installable generic package.
- Use this profile as lab PC agent context input for cross-terminal comparison, not as default runtime rules.
