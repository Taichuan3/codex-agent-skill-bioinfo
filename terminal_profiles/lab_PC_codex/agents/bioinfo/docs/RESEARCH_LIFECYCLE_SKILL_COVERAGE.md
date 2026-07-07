# Research Lifecycle Skill Coverage

Purpose: compressed package-level map from the Lab PC workflow audit. This is a review/reference document, not a default runtime context and not a replacement for any project-level `AGENTS.md`, `PROJECT_GUIDE.md`, or skill file.

## Core lifecycle

```text
important question
-> knowledge gap
-> testable hypothesis
-> evidence package / figure skeleton
-> reproducible execution
-> exploration
-> confirmation
-> validation
-> manuscript/story convergence
-> submission audit
-> reviewer iteration
```

## Stage-to-skill map

| Research stage | Main decision | Primary skills |
|---|---|---|
| Direction scan | What is known, unknown, controversial, and worth doing? | `literature-search-workflow`, `paper-reader`, `research-question-brief` |
| Project framing | Can the idea become a testable project and paper claim? | `research-project-planner`, `research-decision-review` |
| Project state | What should future agents read first? | `project-state-maintenance`, `project-guide-maintainer` |
| Data/environment setup | Are inputs, environment, and raw-data boundaries safe? | `project-environment-bootstrap`, `research-data-organization` |
| Analysis execution | Are scripts, parameters, outputs, and provenance reproducible? | `bioinfo-analysis-code`, `environment-and-tool-adoption` |
| Evidence audit | Does each claim map to figure/table/source data/caveat? | `claim-evidence-audit`, `evidence-gap-finder`, `validation-strategy-planner` |
| Domain workflows | Does the project need a specialized omics/genetics/structure/drug route? | `rnaseq-singlecell-workflow`, `variant-genomics-interpretation`, `pathway-network-analysis`, `protein-structure-docking`, `drug-discovery-admet-screening`, `scientific-database-grounding` |
| ML benchmark | Are task contract, splits, leakage checks, and controls valid? | `ml-benchmarking`, `bioinfo-analysis-code`, `validation-strategy-planner` |
| Figures/source data | Do figures carry the narrative and remain reconstructable? | `publication-plotting`, `figure-caption`, `source-data-audit` |
| Writing | Is language clear without upgrading evidence strength? | `chinese-scientific-polishing`, `scientific-english-translation`, `scientific-english-polishing` |
| Submission/revision | Would a reviewer accept the evidence chain and reproducibility? | `submission-readiness-audit`, `reviewer-simulation`, `reviewer-response-builder`, `manuscript-consistency-audit`, `citation-verifier` |

## Use rule

Use this file when auditing the skill system, designing a new class-level skill, or deciding whether a workflow gap is already covered. Do not load it for ordinary analysis, plotting, or writing tasks unless the user asks for lifecycle-level planning or skill-system review.
