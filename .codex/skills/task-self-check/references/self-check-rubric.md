# Self-check Rubric

## Hard-stop issues

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
| Ready with caveats | Only disclosed Medium/Low issues remain and they do not invalidate the intended use. |
| Not ready | A hard stop or unresolved High issue can mislead, break reproducibility, or invalidate delivery. |

## Phase-aware checks

| Phase | Check |
|---|---|
| Exploration | Are unstable parameters, negative results and caveats recorded? |
| Confirmation | Are parameters, sample set, background set, statistics and output expectations locked? |
| Validation | Is there independent data, orthogonal evidence, negative control, sensitivity analysis or a justified downgraded claim? |
| Submission-ready | Can main figures/tables be regenerated, traced to source data and matched to manuscript statements? |
