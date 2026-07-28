# Discovery artifact contract

Use only the sections required by the active stage. Keep long evidence and
analysis in their owning artifacts and point to them from the cycle manifest.

## Cycle manifest

| Field | Requirement |
|---|---|
| `cycle_id` | Stable identifier, never silently reused for a changed question |
| `question` | Frozen decision question and biological context |
| `mode` | `plan-only`, `dry-run`, `evidence-backed`, or `post-experiment` |
| `role_roster` | Decision owner, execution owner, independent QC/reviewer and claim owner |
| `scope` | Included and excluded stages, data, candidates and actions |
| `inputs` | Immutable paths, IDs, versions, hashes or query pointers |
| `provenance` | Source, access date, version/release, direct/derived relation, verification owner and unresolved status |
| `environment` | Runtime, tool/model versions and material configuration |
| `stages` | `stage_id`, owner Skill/Agent, status, input and output pointers |
| `human_gates` | Decision, options, evidence seen, owner, date and outcome |
| `changes_from_prior` | Changed assumption, evidence, method or stopping rule |
| `stop_rule` | Observable continue/pivot/stop criteria |
| `limitations` | Missing evidence, access limits and untested assumptions |

Statuses are `planned`, `running`, `complete`, `failed`, `blocked`,
`rejected`, or `superseded`. A command exit code cannot by itself set a
scientific stage to `complete`.

The manifest is an index, not a second copy of every result. The evidence map
owns source interpretation, hypothesis cards own hypothesis content, the
feedback ledger owns status transitions, and the claim/validation map is a
derived view. Other artifacts point to these canonical records instead of
repeating them.

When a pilot is recorded inside a portable capability package, keep raw
research inputs and runtime logs outside the package. Retain public source
pointers, expected hashes, a sanitized command template and compact derived
results; verify downloaded inputs against the expected hashes before analysis.

## Hypothesis card

Each card records:

1. stable `hypothesis_id` and concise testable statement;
2. proposed mechanism without upgrading association to causality;
3. evidence for and against, with source pointers and evidence type;
4. predicted observation if the hypothesis is useful;
5. strongest alternative explanation and a discriminating observation;
6. proposed assay or analysis, controls and feasibility constraints;
7. falsification or weakening criterion;
8. current evidence level and unresolved identity/context conflicts;
9. downstream dependencies, risk and human decision status.

Reject cards that are not testable, duplicate another card, rely on an
unverifiable citation, or cannot distinguish the proposal from its strongest
alternative.

## Candidate or assay decision package

Keep dimension-level fields rather than one opaque score:

- identity and context validity;
- directness and quality of supporting and negative evidence;
- assay/model relevance and discriminating power;
- feasibility, controls, cost and implementation risk;
- safety/ethics/data-governance constraints;
- expected information gain and whether it can resolve the leading alternative;
- cost, time and opportunity cost;
- novelty as a separate, non-dominating dimension;
- missingness and conflict;
- sensitivity of the recommendation to weights, order, seed or judge;
- `keep`, `merge`, `defer`, `reject`, or `human-review` action.

The decision record identifies the user-visible alternatives and what evidence
would flip the recommendation.

## Analysis handoff and trajectory record

Freeze the shared analysis contract before execution:

- authoritative inputs, sample/feature universe and immutable identifiers;
- reference build/database, environment and tool versions;
- preprocessing, filters, thresholds, contrasts and statistical definitions;
- required controls, QC, expected outputs and success/failure criteria;
- allowed degrees of freedom and decisions that require a human gate.

Each trajectory adds its seed/model, actual method choices, deviations,
commands/notebook pointer, outputs, QC, failed steps, findings and maximum safe
claim. Never overwrite the shared contract to make a trajectory appear
compliant.

## Feedback ledger

For every material result, record:

| Field | Meaning |
|---|---|
| `result_id` | Stable result or artifact pointer |
| `hypothesis_id` | Hypothesis tested or informed |
| `observation` | Data-supported observation only |
| `status_change` | `supported`, `weakened`, `refuted`, `unresolved`, `new` |
| `alternative` | Remaining or newly raised explanation |
| `claim_boundary` | Strongest wording currently allowed |
| `next_test` | Lowest-cost discriminating analysis or experiment |
| `decision` | Continue, pivot, stop, or repeat |
| `owner` | User or named decision owner |

Starting a new cycle requires a pointer to this ledger and an explicit list of
what changed. Do not recycle rejected candidates unless the new evidence or
assumption is recorded.
