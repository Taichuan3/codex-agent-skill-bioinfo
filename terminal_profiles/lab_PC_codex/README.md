# lab_PC_codex terminal profile

This directory is a machine-level Codex skill/agent snapshot from the lab PC.

Snapshot date: 2026-07-06
Source branch: `lab_PC_codex`
Source host label: `lab_PC_codex`

## Contents

- `skills/`: the non-system skills installed under `C:\Users\Hu Yajie\.codex\skills`
- `agents/bioinfo/`: the global bioinfo agent package installed under `C:\Users\Hu Yajie\.codex\agents\bioinfo`
- `user-home/AGENTS.md`: the user-home-level AGENTS entry installed at `C:\Users\Hu Yajie\AGENTS.md`

## Counts

- Skills: 26
- Skill metadata files: 26 `agents/openai.yaml`
- Agent package: 1 bioinfo agent package

## Notes

- This profile intentionally excludes secrets, tokens, local Codex auth files, browser state, and runtime caches.
- The repository root `.codex/skills` and `AGENTS.md` were also synchronized from this machine so the branch can be tested directly as a generic package.
- Use this branch as the lab PC input for cross-terminal skill/agent comparison and later Hermes-driven optimization before merging improvements back to `main`.
