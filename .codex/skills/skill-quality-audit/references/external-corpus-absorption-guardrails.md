# External Corpus Absorption Guardrails

Use when auditing or improving local skills from a large external skill corpus.

## Primary rule

A large external corpus is not a reason to create many new local skills. Its primary value is to improve the user's existing class-level skills.

Order of operations:

1. Identify the local skill that already owns the task class.
2. Extract reusable mechanisms from external skills: trigger design, input contract, output contract, evidence boundary, validation, provenance, tool-decision criteria.
3. Merge those mechanisms into the matching local skill or a focused `references/` file.
4. Create a new skill only if the capability is frequent, class-level, and cannot fit cleanly under an existing umbrella.

## Reject by default

Do not import directly:

- Whole external repositories.
- Cloud/GPU/API wrappers without a local pilot.
- Tool manuals that are better referenced as optional implementation details.
- Session-specific audit matrices into the GitHub source repo.
- Many narrow candidate skills just because an external repo contains them.

## Runtime/source rule for this user

For the bioinfo skill system, runtime skills under `~/.hermes/skills/bioinfo` are the newer, locally iterated working versions. GitHub source is the installable package. Never overwrite runtime bodies with older source bodies. Instead, compress runtime experience and external mechanisms into stable source structure.

## Quality checks

A successful absorption pass should answer:

- Which existing skill was improved?
- Which external mechanism was absorbed?
- Why was it not a new skill?
- What evidence boundary or validation got stronger?
- Does the main `SKILL.md` remain concise, with detail moved to references?
