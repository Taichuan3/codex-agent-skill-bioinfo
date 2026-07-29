---
name: project-directory-card-maintenance
description: 用于维护重要研究 artifact 目录的短 README Directory Card，说明目录用途、当前关键文件、生成来源、读取顺序和废弃状态。
metadata:
  hermes:
    tags: [bioinformatics, directory-card, readme, project-organization, cookiecutter-data-science, artifact-index]
    related_skills: [research-data-organization, project-state-maintenance, publication-plotting, ml-benchmarking]
---

# Project Directory Card Maintenance

## 核心问题

如何用短、可维护的目录级 README，为重要科研 artifact 提供当前入口、生成来源、读取顺序和废弃状态，而不复制完整清单或项目日志？

## Purpose

Maintain selective short directory-level `README.md` files as **Directory Cards** for important research artifact folders. A Directory Card explains what a folder contains, which files are current/important, how they were produced, what to read first, and which files to ignore.

Use this skill when the user asks for “Directory Card”, “folder README”, “目录索引”, “结果目录说明”, “更新目录 README”, or asks to organize `data/`, `models/`, `reports/`, `figures/`, `structures/`, `genetics`, or `screening` folders.

## Relationship to project state files

```text
AGENTS.md             agent behavior rules and routing
PROJECT_GUIDE.md      hot current project state
PROJECT_PLAN.md       cold append-only project log
*/README.md           on-demand local directory navigation aid
manifest/registry TSV exact machine-readable file/run metadata
```

A Directory Card is not a log, not a second project guide, and not an agent behavior file.

## Read policy

- Do not read every directory README at session start.
- Before scanning a large artifact directory under `data/`, `models/`, `reports/`, or `experiments/`, check for local `README.md` and read it first.
- Treat `README.md` as a navigation aid, not the final source of truth.
- If README points to manifest/registry/script/config, use those structured files for exact details.
- If README is stale or contradicts structured artifacts, report inconsistency and update only after verifying current truth.

## Creation criteria

Create a Directory Card when any condition is true:

1. The directory contains results that will be reused, cited, shared, or used in a paper/report.
2. The directory has >8–10 files and filenames alone do not reveal priority.
3. There are multiple similar versions requiring current/deprecated labels.
4. The directory supports an independent scientific claim.
5. It contains external data, canonical processed data, models, structures, figures, supplementary tables, or screening/design outputs.
6. It needs a special read order or reproduction command.

Do not create cards for every run directory, every temporary figure folder, or rapidly changing interim/cache folders.

## Update criteria

Update a Directory Card only when a durable artifact changes:

- canonical dataset changes;
- best/baseline model or validation result changes;
- candidate/final figure or paper claim changes;
- structure result, candidate molecule, top hit, screening campaign, reproduction command, deprecation status, or file layout changes;
- project moves from exploratory to candidate/current/final state.

Do not update for failed temporary experiments, unchanged reruns, intermediate cache changes, or exploratory plots not meant for reuse. Log those in `PROJECT_PLAN.md` instead.

## Minimum recommended cards

For Cookiecutter Data Science style projects, the minimal useful set is:

```text
data/README.md
data/processed/README.md
models/README.md
reports/figures/README.md
```

Add only when needed:

```text
reports/genetics/README.md
reports/structures/README.md
reports/tables/README.md
reports/model_eval/README.md
experiments/design/README.md
experiments/screening/README.md
notebooks/README.md
references/README.md
```

## Directory Card template

```markdown
# Directory Card: <relative/path>

## Purpose
<One sentence: what this directory contains and why it exists.>

## Current important files
| path | status | meaning | produced by |
|---|---|---|---|
| <file> | current / candidate / deprecated | <what it is> | <script/notebook/command> |

## Read first
- Start with: <file/manifest/script>
- For exact file metadata, use: <manifest.tsv / registry.tsv>
- For history, search: `PROJECT_PLAN.md` by `<log_id / keyword>` only if needed.

## Reproduce / update
Command: `<make command or python script>`

## Ignore / deprecated
- Ignore: `<pattern>` because <reason>.
- Deprecated: `<file>` replaced by `<file>` on <date>.

## Notes for Hermes/Codex
- Do not inspect all files unless the task requires it.
- Prefer the current files listed above.

## Last updated
YYYY-MM-DD - <reason>
```

## Length budget

- Ordinary card: 800–1,500 chars; hard cap ~2,000.
- Complex data/model/structure card: 1,500–2,500 chars; hard cap ~3,000.
- `reports/figures/README.md`: 1–2 pages; hard cap ~4,000.
- Artifact subdirectory card: 500–1,200 chars; hard cap ~1,500.

Prefer tables and links to manifests over long prose or full file lists.

## AGENTS.md patch

When initializing or repairing a project, add the concise Directory Cards rules from `references/agents-directory-cards-patch.md`. If this edits `AGENTS.md`, pair it with `project-state-maintenance` and perform focused ad-hoc verification of the routing rules when no canonical test/lint command exists.

## Synchronization with GUIDE/PLAN

- Any Directory Card update is a material project action: write a concise `PROJECT_PLAN.md` entry.
- Update `PROJECT_GUIDE.md` only if the Directory Card change affects current project truth, next actions, major findings, risk, or paper/model/structure claim.
- Directory Card updates do not automatically imply GUIDE updates.

## Pitfalls

- Do not use subdirectory `AGENTS.md` as a result catalog. Use nested `AGENTS.md` only for behavior rules.
- Do not copy full metrics tables, sample metadata, variant tables, candidate molecules, all figure versions, or complete file lists into README.
- Do not update README after every exploratory run.
- Do not treat README as exact truth when manifest/registry/script says otherwise.
- For this user's research projects, Directory Cards, `PROJECT_GUIDE.md`, `PROJECT_PLAN.md`, audit/comparison summaries, and README/index files should default to Chinese unless the user explicitly asks for English or the artifact is formal English manuscript/code/API text.
- When the user asks to understand and reorganize project data structure, do not stop after incidental cleanup or verification; deliver the requested Directory Cards/README/audit files that make the data and analyses understandable.
- After long README/structure refactors, the chat summary must be self-contained: what changed, key files, classification decisions, audit/comparison findings, verification boundary, risks, and next decision. Do not make the user open files to learn the result.
- Status updates for README refactors should be task-centered: summarize what entry points were rewritten, how directories are classified, what was verified, and what remains. Avoid making temporary verification-script details the main content.
- When a Hermes/Codex split is expected, use Codex for broad read-only scans or second-pass audits, then compare Codex findings against Hermes findings in the final summary instead of treating Codex output as a hidden artifact.
- For cross-project workflow/self-check tasks, do not stop at the current project. Check whether the governing rule lives in a global workspace `AGENTS.md`, a project-local `AGENTS.md`, memory, and any Codex-visible skill source. If a rule is only present in one project, report the boundary and either patch the global/class-level skill or state the required project initialization step.
