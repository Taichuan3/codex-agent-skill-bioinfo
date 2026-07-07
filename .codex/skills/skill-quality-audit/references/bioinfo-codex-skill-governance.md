# Bioinfo Codex Skill-System Governance

Use this note when auditing or maintaining the user's bioinfo Codex/Hermes skill system.

## Durable lessons

- Runtime-first: `~/.hermes/skills/bioinfo/` contains the user's locally iterated working skills. Do not replace runtime `SKILL.md` bodies with older GitHub/source versions.
- External corpus purpose: large external skill corpora are primarily used to improve existing local skills and references. New skills are secondary and require a real frequent capability gap after attempted merge.
- Codex compatibility: standalone Codex discovers repo/global skills through `.agents/skills`; `.codex/skills` is the source layout. Use a symlink such as `.agents/skills -> ../.codex/skills` for repo scope or `~/.agents/skills -> <shared source skills>` for global scope.
- GitHub package shape: keep installable repos lightweight: `AGENTS.md`, `README.md`, `local_config.yaml`, `.codex/skills/`, and small scripts/config. Keep long audits, migration notes, and corpus indexes local.
- Guardian workflow: Hermes should define the task constraints and verification gates, delegate deep corpus/diff work to Codex when appropriate, then independently verify structure, counts, runtime/source parity, and Codex visibility.

## Required checks

1. Confirm source and runtime skill counts and names.
2. Confirm every skill has frontmatter, `name`, `description`, body, and `## 核心问题`.
3. Confirm source skills have `agents/openai.yaml`.
4. Confirm `local_config.yaml` count/list matches source.
5. Confirm no long `docs/` audit directory is tracked when the repo is meant to be installable.
6. For global Codex setup, test in a neutral temporary git repo without project `AGENTS.md` or `.agents/skills` and confirm Codex sees the expected global skills.
