# Controlled self-improvement lifecycle and governance

## Lifecycle

Use these states in order; skipped states require a recorded reason.

| Status | Meaning | Write authority |
|---|---|---|
| `observed` | A possible reusable signal was detected. | None |
| `triaged` | Stability, scope, target, privacy, and duplication were assessed. | None |
| `drafted` | A candidate record and semantic diff exist. | Draft scope only |
| `reviewed` | An independent or explicit review checked evidence and risks. | None |
| `approved` | The user authorized the specified next mutation. | Exact approved action |
| `implemented` | Source files changed in the approved scope. | Source write |
| `validated` | Structural and behavioral checks passed within a stated boundary. | Test outputs only |
| `published` | A reviewed branch/commit/PR exists. | Authorized Git write |
| `installed` | The reviewed source was installed to named runtime targets. | Authorized runtime write |
| `monitored` | A later relevant use was checked. | Usually read-only |
| `rolled_back` | Source/runtime was restored to a recorded backup or commit. | Authorized rollback |
| `rejected` | The candidate was declined, duplicated, unsafe, or not durable. | None |

Approval is action-specific. Approval to edit a draft is not approval to push, install, merge, update memory, or modify an automation.

## Signal types

- `explicit_long_term_instruction`
- `repeated_correction`
- `workflow_failure`
- `capability_drift`
- `reusable_pattern`
- `context_bloat`
- `privacy_or_safety_gap`
- `cross_device_parity_gap`

One occurrence is sufficient only when the user explicitly declares a durable rule or a high-severity safety failure is demonstrated. Otherwise prefer repeated evidence or a bounded forward test.

## Target decision

| Target | Use for | Do not use for |
|---|---|---|
| Memory | Stable, short, user-specific preference or fact | Long workflows, secrets, speculative personality |
| Global Agent | Stable behavior needed in most host tasks | Domain/project detail, tool manuals |
| Project Agent | Project operation and safety boundaries | General reusable workflow |
| Project Guide | Current project truth and next decisions | Behavioral policy or history log |
| Skill | Reusable multi-step procedure with a clear trigger | One-off command or broad identity |
| Reference | Detailed schema, rubric, examples, or variants | Trigger logic |
| Custom Agent | Long-lived responsibility, state, or permission boundary | A checklist that a Skill can express |
| Checklist/eval | Repeatable acceptance or quality gate | Background narrative |
| Local config/template | Machine-only values and secret-free defaults | Portable research truth |
| Public package | De-identified cross-project mechanism | Native memory/session/cache or private project facts |

Choose one canonical home and use links or pointers elsewhere. Do not copy the same rule into every layer.

## Privacy classes

- `public-safe`: generic, de-identified, licensed, and portable.
- `project-private`: unpublished fact, project parameter, server detail, or project-only rule.
- `personal-local`: personal preference, finance, travel, relationship, or private history.
- `secret`: credential, token, key, cookie, OAuth/SSH material, or secret-bearing config.
- `runtime-only`: session, cache, database, generated state, or machine overlay.

Only `public-safe` content may enter the public package. Generalize mechanisms rather than redacting isolated words from private material.

## Required review checks

1. Is the signal explicit or supported by repeated evidence?
2. Does a more specific Agent, existing Skill, memory entry, or project artifact already own it?
3. Will the change reduce future rework enough to justify its context and maintenance cost?
4. Could it cause broad mis-triggering, weaken evidence boundaries, or override user judgment?
5. Is the diff attributable to a clean source state?
6. Are private paths, raw conversations, secrets, unpublished facts, and non-portable configuration excluded?
7. Is there a structural and behavioral validation plan?
8. Is installation separate from source publication?
9. Is rollback exact, tested when risk warrants, and recoverable?

## Validation ladder

- Structure: frontmatter/TOML/YAML parsing, required files, links, manifest counts.
- Semantics: target/scope consistency, no duplicate or contradictory rules, bounded trigger.
- Privacy: secret/private-path scan and public/private classification.
- Discovery: neutral repo or host check confirms the intended Skill/Agent is visible.
- Behavior: apply the rule to a representative prompt or artifact without leaking the intended answer.
- Parity: source and installed runtime match the reviewed files and modes.
- Monitor: confirm a later relevant task improved or did not regress.

## Rollback gates

Roll back or disable the candidate when:

- it triggers outside its stated use cases;
- it overrides a more specific project rule or user instruction;
- it causes measurable context bloat without repeated benefit;
- it weakens privacy, safety, evidence, or reproducibility requirements;
- runtime differs from the reviewed source;
- installation breaks discovery or another validated capability;
- the user withdraws the preference or changes the workflow.

Record the pre-change backup or Git commit before installation. Verify rollback using the same discovery, structure, and parity checks used for installation.
