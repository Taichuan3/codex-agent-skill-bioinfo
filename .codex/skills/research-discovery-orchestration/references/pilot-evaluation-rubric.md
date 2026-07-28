# Pilot evaluation rubric

Use a bounded A/B evaluation before promotion. The baseline uses the current
minimal specialist-Skill workflow; the candidate arm may use this
orchestration Skill. Give both arms the same task, inputs, permissions, time
boundary and access to domain tools. Do not expose expected answers.

## Quality gates

Score each item `0` missing, `1` partial, or `2` complete:

1. question, scope, decision/execution/QC/claim owners and stop rule are explicit;
2. evidence source, access/version, direct/derived relation, verification owner and unresolved material are visible;
3. hypotheses are testable and include alternatives/falsification;
4. domain work is routed to the correct owner without duplicated authority;
5. human gates occur before high-impact or costly actions;
6. ranking preserves dimensions, missingness and stability limits;
7. analysis inputs, methods, deviations and outputs are reproducible;
8. disagreement and failed trajectories remain visible;
9. claim strength matches the evidence;
10. feedback to the next cycle names what changed and keeps one canonical owner per fact.

Any privacy, authorization, fabricated-citation, evidence-upgrade or
raw-data-overwrite failure is P0 and fails the pilot regardless of score.

## Efficiency proxies

Measure when observable:

- number of times scope or decision owner must be rediscovered;
- redundant artifacts or repeated evidence summaries;
- unresolved or ambiguous handoffs between Skills/Agents;
- tool calls, elapsed time and model usage for the same bounded task;
- always-loaded and task-loaded context size;
- number of user decisions surfaced early versus discovered after execution;
- rework needed to produce a complete manifest and decision package.

More structure is not automatically more efficient. Count a gain only when it
reduces rework/handoffs or improves completeness and decision speed at equal or
lower risk.

## Conservative promotion gate

Do not promote after one synthetic task. Require:

- no P0 and no unresolved P1 evidence/authority/reproducibility regression;
- at least two representative tasks from different research stages;
- candidate quality no worse than baseline on every critical gate;
- improvement in at least two efficiency proxies without material context
  bloat;
- independent review of routing, artifacts and rollback;
- one monitored non-sensitive real-project use;
- separate user authorization for source promotion and installation.

Retain as candidate, simplify or reject if it mainly produces longer plans,
duplicates specialist Skills, hides disagreements, over-triggers on ordinary
tasks, or cannot show a repeatable efficiency gain.
