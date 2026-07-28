# Ranking and consensus contract

Use this contract only when ranking or analytical ambiguity materially affects
the next decision. Small or clearly dominated candidate sets should use a
transparent decision table instead.

## Predeclare the comparison

Freeze:

- eligible candidates and immutable evidence package;
- decision dimensions, hard exclusions and missing-data treatment;
- judge/model/version, prompt or rubric version, temperature and seed where
  controllable;
- number and sampling of comparisons;
- tie, abstention, failure and human-review rules;
- stability checks and the minimum evidence needed to name a winner.

Do not let a candidate's prose length, citation count or order stand in for
evidence quality.

## Pairwise ranking safeguards

1. Compare both `A versus B` and `B versus A`, or use another explicit
   counterbalancing design.
2. Randomize presentation order with a recorded seed and blind irrelevant
   names/IDs when possible.
3. Require the judge to cite decision dimensions and evidence pointers, not
   hidden reasoning.
4. Preserve ties and abstentions; malformed or unsupported judgments are
   failures, not losses.
5. Use Bradley–Terry–Luce or another ranking model only after checking graph
   connectivity, comparison coverage and invalid outcomes.
6. Repeat across seeds and, for high-impact decisions, an independent judge or
   rubric-based human review.
7. Report rank intervals, top-k stability, pairwise reversal rate and
   sensitivity to missing comparisons or dimension weights.

If reversed order frequently changes winners, the comparison graph is weak, or
top candidates exchange ranks across reasonable settings, report a tier or
shortlist rather than a unique winner.

## Multi-trajectory analysis

Use multiple trajectories only when defensible choices such as filtering,
gating, model specification, normalization or annotation could change the
answer. Repeating an identical deterministic command is a software
reproducibility check, not multi-trajectory reasoning.

All trajectories share frozen inputs, required outputs, core controls and
prohibited changes. They may vary only in declared degrees of freedom. Record
each actual choice and failure.

Compare trajectories by:

- sample/feature inclusion and attrition;
- preprocessing, filtering and statistical model;
- effect direction, magnitude, uncertainty and adjusted significance;
- QC and control behavior;
- findings and maximum safe claim;
- deviations, warnings and irreproducible outputs.

## Consensus without false independence

Build a matrix of agreement, partial agreement, contradiction and not-assessed.
Separate:

- robust observations reproduced under defensible choices;
- method-dependent results;
- shared-input or shared-model systematic risks;
- singular but plausible findings requiring targeted validation;
- failed or non-comparable trajectories.

Multiple correlated Agent runs do not create independent biological evidence.
Consensus may raise confidence in computational robustness, but experimental,
external-dataset or orthogonal support is still required for stronger
functional, mechanistic or causal claims.

The final decision belongs to the user. Preserve the dissenting evidence and
state what additional test would resolve the highest-impact disagreement.
