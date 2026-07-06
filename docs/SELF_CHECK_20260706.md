# Integrated Skill/Agent Self-check

Date: 2026-07-06
Branch: `integrate-home-lab-hermes-20260706-172538`

## Validation commands run

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .codex/skills/<skill-dir>
python3 - <<'PY'  # custom source-package checks
...
PY
```

## Results

- `quick_validate.py`: passed for all 36 `.codex/skills/*` directories.
- YAML parse: passed for `local_config.yaml` and all `agents/openai.yaml` files.
- Custom self-check: passed.

## Custom self-check assertions

- Skill count is exactly 36.
- Every skill has valid `SKILL.md` frontmatter with matching `name` and non-empty `description`.
- Every skill has `agents/openai.yaml`.
- `.agents/skills` is a symlink to `../.codex/skills`.
- `local_config.yaml` includes `expected_skill_count: 36` and project-level AGENTS preservation policy.
- Root `AGENTS.md` includes:
  - project-level agent file preservation;
  - `PROJECT_GUIDE.md` hot context / `PROJECT_PLAN.md` cold append-only log policy;
  - Directory Cards policy;
  - route entries for `ml-benchmarking`, `project-state-maintenance`, and `project-directory-card-maintenance`.
- `terminal_profiles/lab_PC_codex/skills` duplicate runtime tree is absent.
- Generic source package does not contain project-specific residue patterns checked by the script: `D20S16`, `NIBN`, `motif-hit`, `cage-matched`, `repeat_region`.

## Verification boundary

This validates structure, metadata, discovery compatibility, selected content-policy invariants, and absence of obvious project-specific residue. It does not prove every skill's scientific guidance is perfect; future improvement should use real project tasks plus `skill-quality-audit`.
