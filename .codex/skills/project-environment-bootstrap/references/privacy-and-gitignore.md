# Privacy and Gitignore Rules

## Local-only environment file

`PROJECT_ENVIRONMENT.md` records local machine details and should not be committed, even for private repos.

Default `.gitignore` entries:

```gitignore
PROJECT_ENVIRONMENT.md
PROJECT_ENVIRONMENT.local.md
.env
.env.*
*.pem
*.key
*.token
```

Do not automatically ignore all `data/`, `results/` or `figures/`. Lightweight result tables, plots and documentation may be intentionally synced.

## Before GitHub sync

Check:

```bash
git check-ignore PROJECT_ENVIRONMENT.md
git ls-files PROJECT_ENVIRONMENT.md
git status --short
```

If `PROJECT_ENVIRONMENT.md` is tracked or staged, stop and ask before proceeding.

## Sensitive patterns to flag

Use `rg` as a lightweight warning check when preparing public uploads:

```bash
rg -n "token|password|secret|github_pat|BEGIN .*PRIVATE KEY|ssh-rsa|/Users/|/home/|\\\\wsl\\$" .
```

This may create false positives. Treat it as a warning, not an automatic deletion rule.

## If sensitive data was committed

Do not assume deletion of the current file is enough. Git history may still contain it. Follow GitHub guidance for removing sensitive data, and rotate exposed credentials when relevant.
