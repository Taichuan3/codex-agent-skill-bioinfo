# Self-check Rubric

## Problems scoped to the intended use

The list below blocks the affected claim, computation or formal promotion, not
all work or delivery. Exploration can be useful with unresolved rows or missing
nonessential checks: deliver the interpretable portion with its actual denominator
and caveat. Follow [partial-progress-policy.md](../../bioinfo-analysis-code/references/partial-progress-policy.md) for
record-level isolation. Missing metadata is not an automatic demand to rebuild
the environment. A readable draft need not meet submission-level polish.

## Issues requiring correction for the affected use

- A key claim has no visible evidence source.
- A result is described as causal/mechanistic without direct support.
- Figure or table file cannot be traced to source data.
- Code output cannot be reproduced because input, command, environment, or parameters are missing.
- A figure has unreadable text, overlapping labels, or misleading visual emphasis.
- A manuscript-ready statement promises data/code availability that is not actually prepared.
- Exploration output is written as a confirmed or validated conclusion.
- Machine-learning or predictive analysis lacks a visible train/test/validation split or leakage check.

## Severity

- `High`: likely to mislead the reader, break reproducibility, or fail reviewer scrutiny.
- `Medium`: credibility or usability problem that should be fixed before sharing.
- `Low`: polish or organization issue.

## Minimal report

| Check | Status | Issue | Minimal fix |
|---|---|---|---|

Allowed status values are `Pass`, `Needs fix`, and `Not checked`. Use `Pass` only when the item is visible in the inspected material; missing evidence is `Not checked`, not a failure or an inferred pass.

## Readiness

| Result | Meaning |
|---|---|
| Ready | No hard stop or unresolved High issue in the checked scope. |
| Ready with caveats | Remaining issues do not invalidate the stated exploratory use; affected subsets/claims are separated and limitations disclosed. Formal promotion may still be blocked. |
| Not ready | The affected output cannot be interpreted for its stated use; deliver unaffected outputs rather than blocking the entire task. |

## Phase-aware checks

| Phase | Check |
|---|---|
| Exploration | Are unstable parameters, negative results and caveats recorded? |
| Confirmation | Are parameters, sample set, background set, statistics and output expectations locked? |
| Validation | Is there independent data, orthogonal evidence, negative control, sensitivity analysis or a justified downgraded claim? |
| Submission-ready | Can main figures/tables be regenerated, traced to source data and matched to manuscript statements? |
