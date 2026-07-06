# PROJECT_ENVIRONMENT.md Template

`PROJECT_ENVIRONMENT.md` is local-only by default and should not be committed to GitHub.

```markdown
# PROJECT_ENVIRONMENT

## Privacy

- Local-only file: yes
- Should be committed to GitHub: no
- `.gitignore` protects this file: yes / no / unknown
- Device trust level: regular / temporary / borrowed / public

## Machine

- OS:
- Hostname:
- Username recorded: yes / no / redacted
- Shell:
- Editor:
- WSL / remote server / local:

## Project

- Project root:
- Project GitHub repo:
- Repo visibility: public / private / none / unknown
- Sync policy:
- Large or sensitive data policy:

## Environment

- Conda available:
- Active conda env:
- Recommended project env:
- Python version:
- R version:
- Jupyter available:
- Kernel / notebook notes:

## GitHub

- Is git repo:
- Remote:
- Remote protocol: ssh / https / none
- Branch:
- Upstream:
- GitHub connection tested:
- Push policy:

## Notes

- Last checked:
- Caveats:
- Next environment actions:
```

Keep this file short. It should help the agent know where it is working, not become a full operation log.
