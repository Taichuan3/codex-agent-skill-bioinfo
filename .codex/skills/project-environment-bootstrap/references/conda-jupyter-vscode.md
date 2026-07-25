# Conda, Jupyter and VS Code Notes

## Conda

- Do not assume conda environment names are portable across machines.
- Prefer a project-specific environment when reproducibility or dependency isolation matters.
- A shared bioinformatics environment may be acceptable for lightweight inspection, but record that choice and its limitations.
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

These are read-only availability checks. If a required package or environment is missing, hand off installation or repair to `environment-and-tool-adoption`.

## Jupyter

- Notebooks are good for exploration and recording workflows.
- Stable analysis should eventually be converted into scripts when reproducibility matters.
- Important notebook outputs should write tables/figures to explicit paths.
- Record the kernel/environment used for important notebooks.

## VS Code / WSL / server

- Record whether work is local macOS, WSL, server SSH, or VS Code Remote.
- Do not assume paths are portable between Mac, Linux server and WSL.
- Prefer relative project paths in scripts when possible.
- Distinguish the editor host from the execution host and notebook kernel; they may use different filesystems and environments.
