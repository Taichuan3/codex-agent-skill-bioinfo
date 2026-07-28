# Custom Agent routing forward-test protocol — 2026-07-28

Two independent fresh subagent contexts received only the candidate
`AGENTS.md`, the six top-level `.codex/agents/*.toml` definitions, and the 18
query texts. They were explicitly denied `.codex/agents/evals/`, documentation,
Git diff and prior outputs. Expected labels were not exposed. The Codex Desktop
model build was not exposed.

Both runs selected 18/18 expected routes and agreed on 18/18 cases. This covers
two positive cases per custom Agent, the workspace-write implementation worker,
five read-only roles, and six `none` cases for installation, main integration,
scientific decision, curator mutation, private upload and unbounded concurrent
writes.

This is selection behavior evidence, not proof that every Agent will execute
its task correctly. TOML schema and sandbox consistency remain static gates;
task-specific implementation, reproducibility, claim and release quality still
require their own output review.
