# lab_PC_codex terminal profile

This directory is the updated machine-level Codex skill/agent snapshot from the lab PC.

Snapshot date: 2026-07-08
Source branch: `lab_PC_codex`
Configured from main commit: `5ff8a50`
Package version: `1.8-integrated`
Source host label: `lab_PC_codex`

## Contents

- `skills/`: the non-system skills installed under `C:\Users\Hu Yajie\.codex\skills`
- `agents/bioinfo/`: the global bioinfo agent package installed under `C:\Users\Hu Yajie\.codex\agents\bioinfo`
- `user-home/AGENTS.md`: the user-home-level AGENTS entry installed at `C:\Users\Hu Yajie\AGENTS.md`
- `standalone-codex/agents-skills-link.txt`: the standalone Codex `.agents/skills` discovery link configured on this machine

## Counts

- Skills: 36
- Skill metadata files: 36 `agents/openai.yaml`
- Agent package: 1 bioinfo agent package
- Standalone Codex discovery: `.agents/skills` junction points to `.codex/skills`

## Notes

- This profile intentionally excludes secrets, tokens, local Codex auth files, browser state, runtime caches, raw data, and project result files.
- The lab PC has been updated from the optimized `main` package and this branch now records that local post-update state.
- Use this branch as the lab PC confirmation/input branch for cross-terminal comparison and future Hermes-driven optimization.
