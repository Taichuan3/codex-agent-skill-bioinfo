# Second-Round External Absorption Matrix

> Branch: `Hermes-review`. Purpose: second-pass review across the five capability blocks requested by the user. Classification uses four actions: strengthen existing, new candidate skill, reference only, reject.

## 1. Database grounding

| External pattern | Sources | Action | Target |
|---|---|---|---|
| Database source map with provenance, version/date, query params | `google-deepmind/science-skills`, selected `GPTomics/bioSkills`, `K-Dense-AI/scientific-agent-skills` | strengthen existing | `scientific-database-grounding`, `source-data-audit` |
| Variant/gene/regulatory cross-checking | ClawBio `variant-annotation`, `gwas-lookup`; science-skills ClinVar/dbSNP/gnomAD/GTEx/ENCODE | strengthen existing | `scientific-database-grounding` |
| Tool-specific API wrappers | science-skills scripts, ClawBio wrappers | reference only | keep as examples until local use validates |
| Full database wrapper import | large external repos | reject | too much dependency/runtime surface |

## 2. Reproducible execution

| External pattern | Sources | Action | Target |
|---|---|---|---|
| preflight → smoke test → full run → output verification | ClawBio, agent-skills, bioSkills | strengthen existing | `bioinfo-analysis-code`, `task-self-check` |
| environment/source/license/adaptation record | ClawBio, official skill examples | strengthen existing | `environment-and-tool-adoption`, `project-environment-bootstrap` |
| nf-core/Galaxy/production wrappers | ClawBio | reference only | candidate future domain execution skills |
| auto-install huge bioinformatics pack | bioSkills installer | reject | too broad and high risk for default triggering |

## 3. Protein / docking / drug discovery

| External pattern | Sources | Action | Target |
|---|---|---|---|
| input-definition QA for sequences, structures, ligands, residue numbering | protein-design-skills, BioNeMo, AtomisticSkills, bioSkills | strengthen existing | `protein-structure-docking`, `scientific-database-grounding` |
| docking/structure tool decision matrix | bioSkills, BioNeMo, ClawBio | strengthen existing | `protein-structure-docking` |
| ADMET/QSAR/target validation candidate table | bioSkills, scientific-agent-skills, ClawBio | new candidate skill | `drug-discovery-admet-screening` |
| GPU/server protein design execution | BioNeMo, protein-design-skills | reference only | future project-specific workflow after pilot |
| medical/personalized drug advice skills | ClawBio drug-photo/pharmgx-like modules | reject | outside research-safety boundary |

## 4. Scientific writing / review / figure QA

| External pattern | Sources | Action | Target |
|---|---|---|---|
| output contract: what belongs in prose vs caption vs source data | nature-skills, scientific-writing skills | strengthen existing | `figure-caption`, `publication-plotting`, `claim-evidence-audit` |
| reviewer attack list and response table discipline | nature-response/reviewer, superpowers planning | strengthen existing | `reviewer-simulation`, `reviewer-response-builder` |
| overly Nature/CNS-flavored polishing | nature-skills | reference only | use style ideas, not claim inflation |
| generic manuscript generation from sparse evidence | broad scientific-writing skills | reject | risks unsupported claims |

## 5. Agent workflow / context engineering

| External pattern | Sources | Action | Target |
|---|---|---|---|
| all-repo scan before selective merging | superpowers, context-engineering skills, user's correction | strengthen existing | `skill-quality-audit`, collaboration docs |
| progressive disclosure and one-core-question skill design | official skills repos, anthropics/openai examples | strengthen existing | all 29 source skills |
| multi-agent orchestration patterns | ECC, Agent-Skills-for-Context-Engineering | reference only | use for repo process, not runtime bioinfo skill content |
| broad agent harness/memory/security import | ECC | reject | too broad and outside bioinfo skill source scope |

## Implemented in this pass

- Split over-broad `protein-docking-drug-discovery` into:
  - `protein-structure-docking`
  - `drug-discovery-admet-screening`
- Added a `## 核心问题` section to each source skill so every skill has one explicit core problem.
- Kept large external repos as reference/coverage dictionaries instead of importing them.
