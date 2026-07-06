# Skill Audit Rubric

## Rating

- `Ready`: can be used as-is.
- `Usable draft`: works but needs better triggers, references, or examples.
- `Needs revision`: likely to misfire, bloat context, or miss important safety/research checks.
- `Do not use`: missing required structure or has serious safety/research-integrity risks.

## Checks

| Area | Good sign | Risk |
|---|---|---|
| Trigger | Description names task and boundaries | Too broad, vague, or overlaps many skills |
| Context | SKILL.md is concise | Long examples and protocols always loaded |
| References | Details split into one-level references | Deep reference chains or hidden dependencies |
| Research integrity | Blocks fabricated claims and overclaim | Encourages unsupported mechanisms or citations |
| Reproducibility | Inputs, outputs, versions and caveats are requested | Results without provenance |
| Safety | Install/run steps are explicit and reviewable | Unreviewed scripts, credentials, destructive commands |

## Priority

- `P0`: must fix before use.
- `P1`: important for reliability.
- `P2`: polish or future enhancement.
