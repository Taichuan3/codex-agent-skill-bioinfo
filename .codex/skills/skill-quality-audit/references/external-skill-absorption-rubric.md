# External Skill Absorption Rubric

Use this reference when comparing external Skill/Agent repositories with a canonical source package.

## Four actions

| Action | Use when | Result |
|---|---|---|
| strengthen existing | External material improves a current skill's trigger, checklist, output contract, or caveat discipline | Patch existing skill or add a reference |
| new candidate skill | External material answers a core problem not covered by existing skills | Create a candidate skill in `.codex/skills/`, not runtime |
| reference only | External material is useful as a dictionary, design pattern, or future example but too broad/heavy now | Document in audit; do not install |
| reject | External material is unsafe, too generic, dependency-heavy, medical-advice-like, or encourages unsupported claims | Record reason; do not migrate |

## Decision rules

- One skill should answer one core question.
- Prefer editing an existing skill over adding a near-duplicate.
- Split a skill when it contains two different delivery objects or two different evidence regimes.
- Merge only when two skills are always triggered together and produce the same user-facing deliverable.
- Heavy execution wrappers require a real local pilot before promotion.
- Runtime promotion is separate from source-repo candidate creation.
