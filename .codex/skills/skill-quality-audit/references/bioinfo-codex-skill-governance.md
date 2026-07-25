# Bioinfo Codex Skill-System Governance

Use this note when auditing or maintaining a portable bioinformatics Codex capability package.

## Durable lessons

- Provenance before precedence: canonical source, installed runtime, project-local copies and upstream bundles may each contain useful differences. Compare provenance, hashes and semantic changes before promoting any one copy.
- External corpora primarily strengthen existing Skills and references. A new Skill requires a frequent, distinct delivery object and trigger boundary after attempted merge.
- Discovery must be verified in the intended repo/global scope using the package's supported installation mechanism; do not assume source layout alone proves runtime visibility.
- Keep installable repositories lightweight: Agent rules, Skill source, small metadata, validators and necessary references. Keep long audits, inventories and machine overlays outside portable source.
- Separate authoring and review for public or high-impact changes. Validate structure, counts, trigger behavior, privacy and source/runtime parity independently.

## Required checks

1. Confirm source and installed Skill counts, names and provenance.
2. Confirm every `SKILL.md` has only `name` and `description` frontmatter, a body, a core question and direct resource routing.
3. Confirm each source Skill has parseable `agents/openai.yaml` with only required interface metadata unless extras were explicitly supplied.
4. Confirm package config and inventory match source names and counts.
5. Confirm references, scripts and assets are necessary, one level deep and directly discoverable from `SKILL.md`.
6. Confirm trigger evals cover close neighbors and outcome evals cover authority, evidence and failure modes.
7. Confirm no long audit corpus, private path, credential, runtime database, unpublished fact or machine overlay enters portable source.
8. Test discovery in a neutral target context when installation or parity is in scope.
