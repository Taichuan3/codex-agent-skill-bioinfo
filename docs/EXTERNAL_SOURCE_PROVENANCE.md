# External source provenance

## Scope

This record reconstructs the external-source review behind historical commits
`a2f35f4`, `e4ee03a`, `e649474`, and `875cb4a`. The source registry below is
linked to the file-level disposition in `EXTERNAL_FILE_LINEAGE.tsv` and the
expression review in `EXTERNAL_EXPRESSION_REVIEW_2026-07-25.tsv`.

The package uses independently written workflow concepts and scientific facts.
It does not vendor upstream repositories, Skill bodies, scripts, wrappers,
models, datasets, binaries, or API clients. `THIRD_PARTY_NOTICES.md` retains
conservative attribution for the material sources even though the current
review found no copied expressive text in the comparisons that could be
retrieved at the audited refs.

At the implementation boundary, no executable wrapper copied from an upstream
source is present in this package.

## Source registry

| ID | Repository and audited snapshot | License evidence at that snapshot | Disposition |
|---|---|---|---|
| `clawbio` | [`ClawBio/ClawBio@fbb0910761ab12a9a403060d04248e155b862437`](https://github.com/ClawBio/ClawBio/tree/fbb0910761ab12a9a403060d04248e155b862437) | [MIT `LICENSE`](https://github.com/ClawBio/ClawBio/blob/fbb0910761ab12a9a403060d04248e155b862437/LICENSE) | Material workflow-map reference; no wrapper copied |
| `gptomics` | [`GPTomics/bioSkills@c8d403984b1f35c14861b0064d24695f82d44904`](https://github.com/GPTomics/bioSkills/tree/c8d403984b1f35c14861b0064d24695f82d44904) | [MIT `LICENSE`](https://github.com/GPTomics/bioSkills/blob/c8d403984b1f35c14861b0064d24695f82d44904/LICENSE) | Material capability-dictionary reference; no implementation copied |
| `science-skills` | [`google-deepmind/science-skills@33557e0f1faf0f281d255940de58935c61b2143b`](https://github.com/google-deepmind/science-skills/tree/33557e0f1faf0f281d255940de58935c61b2143b) | [Apache-2.0 `LICENSE`](https://github.com/google-deepmind/science-skills/blob/33557e0f1faf0f281d255940de58935c61b2143b/LICENSE) | Material database/provenance-map reference; no client or code copied |
| `bionemo` | [`NVIDIA-BioNeMo/bionemo-agent-toolkit@54fc67cd87b240f98ffc3223268c77c5eae6e028`](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/tree/54fc67cd87b240f98ffc3223268c77c5eae6e028) | [`LICENSE`](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit/blob/54fc67cd87b240f98ffc3223268c77c5eae6e028/LICENSE): Skill/docs/content CC-BY-4.0; code Apache-2.0 | Material structure/drug workflow-map reference; no workflow definition or code copied |
| `adaptyv` | [`adaptyvbio/protein-design-skills@59dd63374314baa2fb1f9864f190775bd7466647`](https://github.com/adaptyvbio/protein-design-skills/tree/59dd63374314baa2fb1f9864f190775bd7466647) | [MIT `LICENSE`](https://github.com/adaptyvbio/protein-design-skills/blob/59dd63374314baa2fb1f9864f190775bd7466647/LICENSE) | Material protein-workflow reference; no Skill body copied |
| `atomistic` | [`learningmatter-mit/AtomisticSkills@ca695e1b89ea48613291c88bd8c73e71af2025c7`](https://github.com/learningmatter-mit/AtomisticSkills/tree/ca695e1b89ea48613291c88bd8c73e71af2025c7) | [MIT `LICENSE`](https://github.com/learningmatter-mit/AtomisticSkills/blob/ca695e1b89ea48613291c88bd8c73e71af2025c7/LICENSE) | Material method/risk-map reference; no Skill body or code copied |
| `nature-skills` | [`Yuan1z0825/nature-skills@af29cdd0201fd9158f140adcda24bc8b2506d246`](https://github.com/Yuan1z0825/nature-skills/tree/af29cdd0201fd9158f140adcda24bc8b2506d246) | [Apache-2.0 `LICENSE`](https://github.com/Yuan1z0825/nature-skills/blob/af29cdd0201fd9158f140adcda24bc8b2506d246/LICENSE) | Reference-only style comparison; no current file derives from it |
| `addyosmani` | [`addyosmani/agent-skills@aba7c4e9695c363e65cb59effe926c7f1d1abe3d`](https://github.com/addyosmani/agent-skills/tree/aba7c4e9695c363e65cb59effe926c7f1d1abe3d) | [MIT `LICENSE`](https://github.com/addyosmani/agent-skills/blob/aba7c4e9695c363e65cb59effe926c7f1d1abe3d/LICENSE) | Material verification-concept reference; no Skill body copied |
| `superpowers` | [`obra/superpowers@896224c4b1879920ab573417e68fd51d2ccc9072`](https://github.com/obra/superpowers/tree/896224c4b1879920ab573417e68fd51d2ccc9072) | [MIT `LICENSE`](https://github.com/obra/superpowers/blob/896224c4b1879920ab573417e68fd51d2ccc9072/LICENSE) | Material review/workstream-concept reference; no Skill body or script copied |
| `context-engineering` | [`muratcankoylan/Agent-Skills-for-Context-Engineering@175cee7c25b5d98d919369f53427c646cdd86d93`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/tree/175cee7c25b5d98d919369f53427c646cdd86d93) | [MIT `LICENSE`](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/175cee7c25b5d98d919369f53427c646cdd86d93/LICENSE) | Material context-management reference; no Skill body or script copied |
| `kdense-historical` | [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills) historical short ref `0807ddb` | Historical audit recorded MIT; the full historical SHA is no longer reachable. Current upstream declares [MIT in `LICENSE.md`](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/LICENSE.md). | Reference-only because the exact audited object cannot be revalidated; never a copy source |
| `robin` | [`Future-House/robin@4a5cce310f3bc7663a67117db88af43b84733ffe`](https://github.com/Future-House/robin/tree/4a5cce310f3bc7663a67117db88af43b84733ffe) | [Apache-2.0 `LICENSE`](https://github.com/Future-House/robin/blob/4a5cce310f3bc7663a67117db88af43b84733ffe/LICENSE) | Material staged-discovery and feedback-loop mechanism reference; local Skill and contracts independently rewritten; no code, prompt or Skill body copied |

The historical 20-repository inventory also listed official specifications,
indexes, and repositories with unknown licenses. They remain reference-only or
rejected and are not sources for current package expression. In particular,
unknown-license sources cannot be promoted to material sources.

## Capability map

| Local capability | Material source IDs | Independently retained mechanism |
|---|---|---|
| `scientific-database-grounding` | `science-skills`, `gptomics`, `clawbio` | source hierarchy, identifier and provenance fields |
| `rnaseq-singlecell-workflow` | `clawbio`, `gptomics` | task stages, preflight/QC and evidence boundaries |
| `variant-genomics-interpretation` | `clawbio`, `science-skills`, `gptomics` | entity/QC/evidence categories |
| `pathway-network-analysis` | `clawbio`, `gptomics` | method-selection and interpretation checks |
| `clinical-bioinformatics-evidence` | `clawbio`, `gptomics`, `science-skills` | source classes and research-only safety boundary |
| `protein-structure-docking` | `bionemo`, `adaptyv`, `atomistic` | structure/docking stages, QC and evidence limits |
| `drug-discovery-admet-screening` | `bionemo`, `gptomics`, `clawbio` | campaign-stage decisions and prediction limits |
| writing/publication Skills | none; `nature-skills` is reference-only | package-owned router/reference layering and output contracts |
| governance/self-check Skills | `addyosmani`, `superpowers`, `context-engineering` | verification, review and context-management concepts |
| `research-discovery-orchestration` | `robin` | stage transitions, structured handoffs, lab-in-the-loop feedback and disagreement-preserving multi-trajectory review |

## Expression review and limitations

On 2026-07-25, seven externally influenced current Skill bodies were compared
with 18 retrievable upstream `SKILL.md` files at the exact refs. After
whitespace/case normalization, every pair had zero shared 40-character shingles
and zero identical normalized lines of at least 35 characters. The exact pairs
and method are recorded in `EXTERNAL_EXPRESSION_REVIEW_2026-07-25.tsv`.

Five initially unavailable path guesses were corrected from exact-ref repository
documentation and then tested: two `science-skills`, two `bionemo`, and one
`AtomisticSkills` path. The comparison is still representative rather than an
exhaustive copyright determination, so the package retains conservative source
attribution and a no-vendoring boundary.

On 2026-07-28, `research-discovery-orchestration/SKILL.md` was compared with
the fixed Robin `README.md` and eight Python source files using normalized
40-character shingles and normalized lines of at least 35 characters. Both
shared counts were zero. The related Nature article
[`10.1038/s41586-026-10652-y`](https://doi.org/10.1038/s41586-026-10652-y)
was used only as method evidence; its CC BY-NC-ND 4.0 text and figures were not
copied, adapted or redistributed.

This record supports the repository owner's explicit authorization of
canonical `main` for the copyright holder's own multi-device installation. It
does not authorize external reuse or redistribution, describe the package as a
license-cleared public release, or authorize a stable release/tag.
