# Getting Started: Team A (Human-Only Control Group)

This document guides you through the setup and execution of the human-only XP experiment.

---

## What Is This?

**Team A** is the **control group** for the XP-GenAI experiment. You will develop a real-time chat application using **strict Extreme Programming practices** and **NO AI tools whatsoever**.

Your data will be compared to **Team B** (the AI-assisted group) to measure the impact of generative AI on software development.

---

## Key Files You Need to Know

### Instructions & Guides
- **`README.md`** — Quick start, commit rules, data collection overview
- **`SPRINT_EXECUTION_CHECKLIST.md`** — Verification checklist for each sprint
- **`GETTING_STARTED.md`** — This file

### Templates for Each Sprint (Fill in for Sprints 1, 2, 3, 4)
- **`docs/planning_logs/SPRINT_1_TEMPLATE.md`** — Copy and fill for planning data
- **`docs/design_notes/SPRINT_1_TEMPLATE.md`** — Copy and fill for design data
- **`docs/observation_logs/SPRINT_1_TEMPLATE.md`** — Copy and fill for daily observations
- **`docs/nasa_tlx/SPRINT_1_TEMPLATE.csv`** — Copy and fill for cognitive load surveys
- **`docs/nasa_tlx/NASA_TLX_INSTRUCTIONS.md`** — How to complete NASA-TLX surveys

### Data Collection Scripts
- **`scripts/extract_commits.py`** — Extracts commit data from git
- **`scripts/compute_metrics.py`** — Computes throughput metrics
- **`scripts/fetch_sonarqube.py`** — Fetches code quality metrics
- **`scripts/parse_ci_logs.py`** — Parses CI pipeline logs

---

## Step-by-Step Setup (Day 1)

### 1. Verify No AI Tools
```bash
# Disable these immediately:
# - GitHub Copilot (VS Code Extensions)
# - ChatGPT web interface (don't use)
# - GitHub Copilot IDE plugin (disable in VS Code)
# - Tabnine, Codeium, etc. (disable all)
```

**Check VS Code:**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search "Copilot", "ChatGPT", "Tabnine" → Disable all
4. Restart VS Code

### 2. Clone & Setup
```bash
git clone https://github.com/Ikechukwu-Ezugworie/xp-ai-experiment-control
cd xp-ai-experiment-control

# Backend
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend
cd ../frontend
npm install
cp .env.example .env
# Edit .env: REACT_APP_API_URL=http://localhost:8000
```

### 3. Verify Commit Hook
```bash
chmod +x .git/hooks/pre-commit

# Test it
git commit -m "SPRINT0-STORY0-[AI:NO]-test commit"  # Should succeed
git commit -m "SPRINT0-STORY0-[AI:YES]-test commit"  # Should fail
```

### 4. Start Servers
```bash
# Terminal 1: Backend
cd backend && source venv/bin/activate && uvicorn app.main:app --reload

# Terminal 2: Frontend
cd frontend && npm start
```

App runs at **http://localhost:3000**

### 5. Review Protocol
- Read `README.md` for commit rules and data collection
- Review `SPRINT_EXECUTION_CHECKLIST.md` to understand what you'll be graded on
- Skim `docs/nasa_tlx/NASA_TLX_INSTRUCTIONS.md` for the cognitive load survey

---

## Sprint Cycle (4 weeks, 1 sprint/week)

### Monday: Planning Game (9:00-11:00)
1. **Product Owner** presents top stories
2. **Team estimates** using Planning Poker (physical cards)
3. **Team splits** stories >8 points
4. **Team commits** to story points for the week
5. **Fill in:** `docs/planning_logs/SPRINT_X_planning.md`

### Tuesday: Design Session (10:00-11:00)
1. **Whiteboard discussions** (no digital tools)
2. **Team sketches** architecture, database, API, UI
3. **Team self-scores** design simplicity (1-5)
4. **Fill in:** `docs/design_notes/SPRINT_X_design.md`

### Wednesday-Thursday: Implementation (Full Days)
1. **Form pairs:** 2 pairs of 2 developers
2. **Rotate partners:** Wed AM, Wed PM, Thu AM, Thu PM
3. **Follow TDD:** Write tests FIRST (red), then code (green), then refactor
4. **Pair programming:** Driver + Navigator; switch roles every 15 minutes
5. **Commit:** Follow format `SPRINT1-STORY4-[AI:NO]-<description>`
6. **Daily observations:** Brief notes on what happened (challenges, decisions)

### Friday AM: Refactoring (9:00-11:00)
1. **Code review:** Find duplication, complexity, unclear naming
2. **Refactor:** Extract methods, rename, remove duplication, simplify
3. **Verify:** All tests still pass, SonarQube quality gate passes
4. **Commit:** Atomic refactoring commits

### Friday PM: Retrospective & Surveys (14:00-15:00)
1. **Team discusses:** What went well? What to improve? Surprises?
2. **NASA-TLX surveys:** Each dev rates 6 dimensions (0-100)
3. **Pairwise comparisons:** Each dev ranks which dimensions matter most
4. **Calculate:** Weighted average (instructions in NASA_TLX_INSTRUCTIONS.md)
5. **Fill in:** `docs/observation_logs/SPRINT_X_observations.md` and NASA-TLX CSV
6. **Data extraction:** Run scripts to extract git/SonarQube/CI metrics

---

## What You'll Produce

### Code
- **Commits:** Every commit tagged `SPRINT<n>-STORY<n>-[AI:NO]-...`
- **Tests:** All stories have unit tests (TDD-first)
- **Quality:** SonarQube quality gate passes for every commit

### Data (Collected for Statistical Analysis)
- **Planning metrics:** estimation duration, story splits, estimation rounds
- **Design quality:** simplicity scores, design decisions count, alternatives considered
- **Productivity:** time per story, commits per story, test-first ratio
- **Code quality:** complexity, duplication, test coverage (from SonarQube)
- **Pair collaboration:** session duration, switch frequency, decision patterns
- **Cognitive load:** NASA-TLX scores (mental demand, effort, frustration, etc.)
- **CI metrics:** build success rate, mean time to recovery

---

## Important Rules

### Commit Rules (Enforced by Git Hook)
```
✅ SPRINT1-STORY4-[AI:NO]-implement login
❌ SPRINT1-STORY4-[AI:YES]-implement login (REJECTED)
❌ implement login (REJECTED - missing format)
```

### AI Tools (Strictly Prohibited)
- ❌ ChatGPT web interface
- ❌ GitHub Copilot
- ❌ Google Gemini / Bard
- ❌ Anthropic Claude (yes, even the CLI!)
- ❌ Tabnine, Codeium, any code-completion AI
- ❌ Any IDE plugin that suggests code

### TDD Rules
1. **Write test first** (RED) — test fails initially
2. **Write minimal code** (GREEN) — just enough to pass
3. **Refactor** — clean up without changing behavior
4. **Commit in order:** Test commit BEFORE implementation commit

### Pair Programming Rules
1. **Form 2 pairs** of 2 developers each
2. **Rotate daily:** Different partners each half-day
3. **Driver/Navigator:** Roles switch every 15 minutes (use a timer!)
4. **No AI:** All decisions made by humans, no GitHub Copilot suggestions

---

## Verification Checklist (After Each Sprint)

Use **`SPRINT_EXECUTION_CHECKLIST.md`** to verify:
- [ ] All commits follow format with `[AI:NO]`
- [ ] TDD was followed (test-first ratio documented)
- [ ] Pair programming was conducted (session logs documented)
- [ ] No AI tools were used (team attestation signed)
- [ ] CI pipeline passed (all commits green)
- [ ] SonarQube quality gate passed
- [ ] All data files collected (planning, design, observations, NASA-TLX)

**Scrum Master signs off** that all requirements were met.

---

## Key Contacts

- **Scrum Master:** [Name] — Verifies process compliance, reviews checklists
- **Product Owner:** [Name] — Presents stories, clarifies acceptance criteria
- **Researcher:** [Name] — Collects data, runs extraction scripts

---

## Questions?

1. **Commit hook not working?** → Run `chmod +x .git/hooks/pre-commit`
2. **SonarQube data extraction failing?** → Check `SONAR_TOKEN` and `SONAR_HOST_URL`
3. **NASA-TLX unclear?** → Read `docs/nasa_tlx/NASA_TLX_INSTRUCTIONS.md`
4. **Sprint protocol questions?** → Review `SPRINT_EXECUTION_CHECKLIST.md`

---

**Good luck. The data you generate will advance our understanding of AI in software development.**

No AI tools. Strict XP practices. Rigorous data collection. That's Team A.

