# Research Decision Rubric

## Continue / pivot / stop

| Decision | Use when |
|---|---|
| Continue | Central question remains important, data quality is acceptable, and next evidence can reduce uncertainty. |
| Pivot | The original claim is weak, but a related question is feasible and better supported. |
| Stop | Data cannot answer the question, validation is impossible, or the expected contribution is too small. |

## Use tool / adapt / rewrite

| Option | Use when |
|---|---|
| Use directly | Tool is maintained, documented, licensed, reproducible, and matches the task. |
| Adapt locally | Tool is useful but needs input/output wrappers, plotting changes, or minor parameter control. |
| Borrow ideas only | Tool is poorly maintained or too coupled, but the method is informative. |
| Rewrite | External code is unsafe, incompatible, unlicensed, irreproducible, or the required logic is small. |

## Reviewer attack prompts

- What alternative explanation has not been excluded?
- Which result depends on one fragile parameter?
- Which figure looks convincing but lacks source data?
- Which claim would fail if one dataset were removed?
- Which software or database version is not pinned?
