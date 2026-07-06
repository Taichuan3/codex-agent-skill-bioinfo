# Tool Adoption Rubric

## Source review

Check before adopting external code:

- Source: GitHub, paper, official protocol, package registry.
- Maintenance: recent commits, issues, releases, documentation.
- License: compatible with intended use.
- Installation: package manager, container, source build, system dependencies.
- Inputs/outputs: match local data or need wrappers.
- Reproducibility: version, seeds, environment, reference databases.
- Citation: paper, DOI, software citation or URL.

## Decision

| Choice | Use when |
|---|---|
| Use directly | Mature, documented, licensed and matches task. |
| Wrap locally | Good tool but needs input/output conversion. |
| Borrow ideas | Useful method but code is hard to run or maintain. |
| Rewrite | Code is unsafe, unlicensed, obsolete, incompatible, or the needed logic is small. |

## Install record

```text
Tool/package:
Version:
Source:
License:
Install command:
Verification command:
Local adaptation:
Citation:
```
