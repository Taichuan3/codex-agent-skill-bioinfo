# External-to-Existing Skill Comparison and Absorption Plan

> Branch: `Hermes-review`. This document implements the updated strategy: audit all collected external repositories first, then compare them with the current runtime and candidate bioinfo skills before merging anything into runtime.

## Baseline groups

- Runtime bioinfo skills: the 10 mature Hermes skills under `~/.hermes/skills/bioinfo/`.
- Source candidate skills: the GitHub source repo under `.codex/skills/`; this remains the source of truth.
- External repositories: all 20 repositories shallow-cloned under `/Users/yajiehu/.hermes/tmp/external-skill-sources/` and summarized in `docs/external-skill-audits/ALL_EXTERNAL_REPOS_STRUCTURE_AUDIT.md`.

## Cross-review conclusions

| External capability | Best external sources | Current overlap | Absorption decision |
|---|---|---|---|
| Scientific database grounding for genes, variants, regulatory tracks, proteins, chemicals and papers | `google-deepmind/science-skills`, selected `GPTomics/bioSkills`, `K-Dense-AI/scientific-agent-skills`, `ClawBio/ClawBio` | Partly overlaps `literature-search-workflow`, `bioinfo-analysis-code`, `paper-reader`, but no dedicated grounding skill | Create candidate skill `scientific-database-grounding`; keep database calls on-demand, not always-loaded runtime |
| Local-first reproducible execution, benchmark mindset, no guessing | `ClawBio/ClawBio`, `GPTomics/bioSkills`, `addyosmani/agent-skills` | Strong overlap with `bioinfo-analysis-code`, `project-environment-bootstrap`, `task-self-check` | Strengthen existing skills with a reference checklist; do not copy execution wrappers wholesale |
| Protein structure, docking, binder design, drug discovery and ADMET | `NVIDIA-BioNeMo/bionemo-agent-toolkit`, `adaptyvbio/protein-design-skills`, `learningmatter-mit/AtomisticSkills`, selected `bioSkills` | No exact current bioinfo skill; only project-specific memory/notes exist | Create candidate skill `protein-docking-drug-discovery`; keep as candidate until real use validates local workflow |
| Scientific writing, figure captions, reviewer response and submission QA | `nature-skills`, selected `scientific-agent-skills`, `superpowers` discipline | Strong overlap with existing writing/reviewer/figure/source-data skills | Keep current user-specific skills as primary; absorb only output-contract/checklist wording when improving existing skills |
| Agent workflow, context engineering, multi-agent coordination | `obra/superpowers`, `Agent-Skills-for-Context-Engineering`, `ECC`, official skills repos | Overlaps collaboration docs and `skill-quality-audit` | Keep as repo-level operating guidance; avoid runtime bloat |
| Official skill spec/style examples | `anthropics/skills`, `openai/skills`, `google/skills`, `agentskills/agentskills` | Overlaps `skill-quality-audit` | Reference-only for validator/style; do not migrate domain content |

## Merge policy after all-repo audit

1. Existing mature runtime skills are not overwritten by external skills.
2. Candidate source skills receive new modules first; only frequently used and stable modules are later promoted to Hermes runtime.
3. Large repositories are treated as dictionaries and design references, not as install targets.
4. Heavy execution dependencies must pass a real local pilot before becoming default-triggered skills.
5. Database/provenance/reproducibility patterns should be absorbed earlier than domain-specific CLI wrappers.

## First absorption actions in this branch

- Add `scientific-database-grounding` as a new candidate skill.
- Add `protein-docking-drug-discovery` as a new candidate skill.
- Add a local-first execution checklist reference to `bioinfo-analysis-code`.
- Update root routing and package metadata so these candidate skills are visible in the source repo but not automatically promoted to runtime.
