# Sprint Execution Checklist

**Purpose:** Verify that Team A follows strict XP practices without AI assistance.

---

## Pre-Sprint Setup

- [ ] **Environment Verified:** Python 3.11+, Node.js 18+, Git, VS Code (no AI), PostgreSQL
- [ ] **AI Plugins Disabled:** GitHub Copilot, ChatGPT, Gemini all OFF
- [ ] **Repository Setup:** Dependencies installed, git hooks configured
- [ ] **CI Pipeline:** GitHub Actions and SonarQube access verified
- [ ] **Data Directories:** Created (planning_logs, design_notes, observation_logs, nasa_tlx)

---

## Monday: Planning Game

- [ ] **Planning Session:** 2 hours (9:00-11:00)
- [ ] **Story Review:** Team understood acceptance criteria
- [ ] **Planning Poker:** Physical cards used; consensus achieved
- [ ] **Story Splits:** Stories >8 points were split as needed
- [ ] **Data Logged:** `docs/planning_logs/SPRINT_X_planning.md` completed
  - [ ] Estimation duration recorded
  - [ ] Final estimates documented
  - [ ] Total points committed recorded

---

## Tuesday: Design Session

- [ ] **Design Session:** 1 hour (10:00-11:00)
- [ ] **Whiteboard Only:** No digital design tools used
- [ ] **Decisions Made:** Design choices documented with rationale
- [ ] **Data Logged:** `docs/design_notes/SPRINT_X_design.md` completed
  - [ ] Design decisions and rationale recorded
  - [ ] Simplicity assessment (1-5) completed

---

## Wednesday-Thursday: Implementation

### TDD Compliance
- [ ] **Test-First:** Tests written BEFORE implementation
- [ ] **Red-Green-Refactor:** Cycle followed for all features
- [ ] **Commit Order:** Test commits come before implementation commits

### Pair Programming
- [ ] **Pairs Formed:** 2 pairs of 2 developers
- [ ] **Partner Rotation:** Pairs rotated each half-day
- [ ] **Driver/Navigator:** Roles switched every 15 minutes (timer used)
- [ ] **No AI Assistance:** All code written manually
- [ ] **Code Review:** Pair review before every commit

### Quality
- [ ] **All Tests Pass:** No broken tests committed
- [ ] **CI Pipeline:** GitHub Actions passed for all commits
- [ ] **SonarQube:** Quality gate passed

---

## Friday AM: Refactoring

- [ ] **Refactoring Session:** 2 hours (9:00-11:00)
- [ ] **Code Review:** Team reviewed this sprint's code
- [ ] **Refactoring Applied:** Remove duplication, simplify, improve names
- [ ] **Tests Pass:** All refactoring verified with passing tests
- [ ] **Commits:** Atomic, well-documented refactoring commits

---

## Friday PM: Retrospective & Data Collection

- [ ] **Retrospective:** 1 hour (14:00-15:00)
  - [ ] What went well discussed
  - [ ] What could improve identified
  - [ ] Action items for next sprint recorded

- [ ] **NASA-TLX Surveys:** All 4 developers completed
  - [ ] Raw scores (0-100 for each of 6 dimensions)
  - [ ] Pairwise comparisons (15 pairs each)
  - [ ] Weighted averages calculated
  - [ ] Results in `docs/nasa_tlx/SPRINT_X_TEMPLATE.csv`

- [ ] **Observation Log:** `docs/observation_logs/SPRINT_X_observations.md` completed
  - [ ] Pair session durations logged
  - [ ] Switch frequency recorded
  - [ ] Challenges documented
  - [ ] TDD compliance verified

---

## Continuous Requirements

- [ ] **Commit Format:** All commits follow `SPRINT<num>-STORY<num>-[AI:NO]-<description>`
- [ ] **AI Tag:** Every commit includes `[AI:NO]` (enforced by pre-commit hook)
- [ ] **No `[AI:YES]`:** Pre-commit hook would reject these
- [ ] **No Broken Tests:** CI never fails
- [ ] **SonarQube:** Quality gate passes for all code

---

## Post-Sprint Data Extraction

- [ ] **Git Metrics:** `python scripts/extract_commits.py .`
  - Output: `data/commits.csv`, `data/story_metrics.csv`

- [ ] **SonarQube Data:** `python scripts/fetch_sonarqube.py`
  - Output: `data/sonarqube_metrics.json`

- [ ] **CI Logs:** `python scripts/parse_ci_logs.py`
  - Output: `data/ci_builds.csv`

- [ ] **Manual Data:** Spot-check that all data files exist and are complete

---

## Team Sign-Off

**Scrum Master:** I confirm this sprint followed XP practices with no AI assistance.

Name: ________________  
Signature: ________________  
Date: ________________

**Team Members:** All confirm no AI tools were used during this sprint.

1. Dev1: ________________  
2. Dev2: ________________  
3. Dev3: ________________  
4. Dev4: ________________

---

**Any deviations from the protocol?** Document here:

[Use this space if any requirements were not met]

