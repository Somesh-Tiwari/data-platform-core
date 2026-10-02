# Week 2: Git, Virtual Environments & Repo Setup

Notes and practice for Git workflows, virtual environments, and secret management.

| File | What It Covers |
|------|----------------|
| `venv.py` | Creating, activating, and deactivating virtual environments |
| `.env` | Local secrets file (not committed — listed in `.gitignore`) |
| `config.py` | Reading environment variables with `os.getenv()` |
| `requirements.txt` | Project dependencies |
| `.gitignore` | Excludes `env/`, `venv/`, `__pycache__/`, and `.env` |

## Key Git Commands

```bash
git checkout -b feature-branch      # Create and switch to a new branch
git merge feature-branch            # Merge branch into main
git branch -d feature-branch        # Delete branch after merging
git rm --cached .env                # Stop tracking a file without deleting it