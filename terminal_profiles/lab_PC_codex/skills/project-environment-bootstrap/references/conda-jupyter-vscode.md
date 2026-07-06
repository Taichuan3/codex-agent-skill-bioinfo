# Conda, Jupyter and VS Code Notes

## Conda

- Do not assume conda environment names are portable across machines.
- On the user's MacBook, `bioinfo` may be a general bioinformatics environment.
- For real projects, prefer a project-specific environment when practical.
- Do not install packages into `base` unless the user explicitly asks.
- Before installing packages, check the active environment and package manager.

Useful checks:

```bash
conda info --envs
conda env list
python --version
which python
R --version
jupyter --version
```

## Jupyter

- Notebooks are good for exploration and recording workflows.
- Stable analysis should eventually be converted into scripts when reproducibility matters.
- Important notebook outputs should write tables/figures to explicit paths.
- Record the kernel/environment used for important notebooks.

## VS Code / WSL / server

- Record whether work is local macOS, WSL, server SSH, or VS Code Remote.
- Do not assume paths are portable between Mac, Linux server and WSL.
- Prefer relative project paths in scripts when possible.
