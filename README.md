# XP Control Experiment (No AI)

This repository is for **Team A** – the control group. **Strictly prohibited:** the use of ChatGPT, GitHub Copilot, or any Generative AI tool.

## Commit Rules
- Every commit **must** include `[AI:NO]` in the message.
- Format: `SPRINT<num>-STORY<num>-[AI:NO]-<description>`
- Commits containing `[AI:YES]` will be **rejected** by the pre-commit hook.

## Setup
1. Clone the repository.
2. Backend: `cd backend && pip install -r requirements.txt`
3. Frontend: `cd frontend && npm install`
4. Copy `frontend/.env.example` to `frontend/.env` and set `REACT_APP_API_URL`.
5. Run backend: `uvicorn app.main:app --reload`
6. Run frontend: `npm start`
7. No AI tools are to be installed or used.

## Data Collection
- All commits are automatically logged and metrics extracted via scripts.
- Run `python scripts/extract_commits.py .` after each sprint to export commit data.
- Run `python scripts/compute_metrics.py data/commits.csv` to compute throughput metrics.
