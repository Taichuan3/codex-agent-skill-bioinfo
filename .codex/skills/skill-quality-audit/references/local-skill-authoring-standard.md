# Local Skill Authoring and Review Standard

Use this reference when creating a new local Skill or substantially updating
portable Skill source. It records the stricter host/package contract learned
from the 37-Skill standardization pass. The official `skill-creator` remains
the generic design and initialization authority.

## 1. Ownership before files

Before creating a directory, define:

- one core question;
- one primary user-facing deliverable;
- positive requests that should trigger it;
- close-neighbor requests that must route elsewhere;
- the existing Skill that would own the work if no new Skill were created.

Prefer strengthening an existing Skill or adding a focused reference. Create a
new Skill only when its core question, deliverable and trigger boundary are all
independent and likely to recur.

## 2. Canonical source and scope

- Edit the canonical source repository, not an installed mirror or stale
  project copy.
- Keep portable, de-identified mechanisms in source. Keep credentials, native
  memory/session/cache, machine topology, absolute private paths, raw data and
  unpublished project facts outside it.
- Treat source edit, commit, push, PR, merge, installation and memory update as
  separate actions requiring their own authority.
- Record the pre-change branch/commit and dirty-file boundary before material
  work. Do not overwrite unrelated changes.

## 3. Required package shape

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── evals/trigger-evals.json
├── evals/outcome-evals.json
├── references/              # optional
├── scripts/                 # optional
└── assets/                  # optional
```

For a new Skill, use the official `skill-creator` `init_skill.py`; do not clone
an unrelated Skill as a shortcut. Only create resource directories that the
Skill needs.

## 4. SKILL.md contract

- Frontmatter contains only `name` and `description`.
- `name` equals the lowercase hyphenated directory name and stays under 64
  characters.
- `description` states what the Skill does, concrete trigger contexts and
  important exclusions. For this package keep it within 300 characters.
- The body answers one `## 核心问题` and defines ownership, authority/evidence
  boundaries, a bounded workflow, output contract, stopping conditions and
  direct resource routing.
- For this package keep the body within 6,000 characters and 120 lines.
- Put detailed schemas, examples, variants and long checklists in one-level
  references. Do not duplicate them in the body.
- Every bundled reference/script/asset must be named and conditionally routed
  from `SKILL.md`; remove unused resources.
- Use scripts only when deterministic behavior or repeated implementation
  justifies them, and test added scripts directly.

These are local portable-package budgets, stricter than the generic
`skill-creator` limits. A justified exception requires an explicit package
decision and validator update rather than silent drift.

## 5. UI metadata contract

`agents/openai.yaml` normally contains exactly:

```yaml
interface:
  display_name: "Human-facing title"
  short_description: "A 25-64 character summary"
  default_prompt: "Use $skill-name to perform a representative task."
```

- Quote every string.
- Make metadata match the current Skill, not its historical purpose.
- `default_prompt` explicitly names `$skill-name`.
- Optional icons, colors, dependencies or policy fields allowed by the generic
  format require an explicit local package need; do not add them by default.

## 6. Trigger and outcome eval contract

For each portable Skill in this package:

- `trigger-evals.json` contains exactly 20 unique cases;
- 10 cases trigger and 10 do not;
- 10 are `train` and 10 are `validation`;
- each split contains five positive and five negative cases;
- positive cases route primarily to the Skill;
- negative cases name the correct close-neighbor Skill or `none`;
- include phrasing variation and boundary cases, not cosmetic paraphrases.

`outcome-evals.json` contains at least five cases spanning:

- the primary deliverable;
- authority and evidence boundaries;
- provenance/reproducibility;
- failure or stop conditions;
- prohibited behavior and the correct handoff.

Static evals define expected behavior; they do not prove runtime behavior. For
ambiguous or high-impact routing, run a blinded forward test that exposes only
frontmatter and raw requests, not expected answers or the eval corpus.

## 7. Validation ladder

Run the smallest complete ladder appropriate to the change:

1. official `quick_validate.py`;
2. JSON/YAML/TOML parsing and local metadata assertions;
3. direct-resource routing and body/description budgets;
4. trigger balance, neighbor ownership and duplicate-query checks;
5. package manifest/count and discovery validation;
6. privacy, secret, raw-data, runtime-artifact and symlink gates;
7. `git diff --check` and exact scoped diff review;
8. representative or blinded behavioral forward test when routing is material;
9. independent scientific, reproducibility or release review when risk/public
   scope warrants it;
10. clean-commit installer dry-run and source/runtime parity only when
    publication or installation is separately authorized.

Report `pass`, `not run` and `not covered` separately. A validator log is
evidence, not a substitute for scientific or release judgment.

## 8. External sources and licensing

- Inventory source URL, exact ref, license path and the local target before
  absorption.
- Prefer mechanism-level `keep/merge/split/reference-only/reject`; never treat a
  large corpus as an install list.
- Independently rewrite reusable mechanisms. Do not vendor Skill bodies,
  wrappers, scripts or expressive text without the applicable license and
  attribution.
- For public candidates, preserve file-level lineage, tombstones for removed
  targets, notices and review evidence when historical absorption is material.
- Unknown-license sources remain reference-only or rejected.

## 9. Maintenance and lifecycle

- After real use, capture repeated mis-triggering, missing gates or context
  bloat as a candidate; do not silently auto-edit the Skill.
- Route durable evolution through `controlled-self-improvement`.
- Keep authoring/reviewer roles separate for public or high-impact changes.
- Publish only a reviewed clean commit to an authorized branch. Verify the
  remote SHA and keep `main`, stable tags and installation behind explicit
  decisions.
- Roll back when routing broadens incorrectly, evidence/privacy weakens,
  context cost rises without benefit, or runtime diverges from reviewed source.

## Delivery checklist

Report:

- whether an existing owner was strengthened or a new Skill was justified;
- exact files changed and resources added/removed;
- trigger neighbors and eval counts;
- validation commands and behavioral coverage;
- privacy/provenance/license decisions;
- source, publication and installation lifecycle states;
- rollback pointer and the next action requiring user authority.
