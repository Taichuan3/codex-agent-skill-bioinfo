# GitHub Sync Checklist

Use this only when environment bootstrap needs to inspect GitHub readiness.

## Basic checks

```bash
git rev-parse --is-inside-work-tree
git remote -v
git branch --show-current
git status --short --branch
git rev-parse --abbrev-ref --symbolic-full-name @{u}
```

## Connectivity

Prefer SSH if configured:

```bash
ssh -o BatchMode=yes -T git@github.com
```

For HTTPS remotes, check whether `gh auth status` is available, but do not require it if SSH works.

## Push policy

- Do not commit or push automatically unless the user asks.
- It is acceptable to suggest commit/push after changes to agent, skills, scripts, lightweight docs, tables or figures.
- Stop before pushing if local-only files are tracked or staged.

## Repo visibility

- Public agent/skill repositories need strict privacy checks.
- Private project repositories may sync code, lightweight result tables and figures according to project policy.
- Private repos still should not receive secrets, tokens, local environment files or unnecessary machine paths.
