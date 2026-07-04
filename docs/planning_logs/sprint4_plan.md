# Sprint 4 Planning Log

## Date: July 27 – August 10, 2026

### Committed Stories
- STORY-11: Edit profile (5 pts)
- STORY-12: Unread badges (8 pts)
- STORY-13: UI/UX improvements (3 pts)
- STORY-14: Infinite scroll refinement (5 pts)

**Total Committed: 21 points**
**Velocity (Sprint 3)**: 16 points
**Rationale**: Adding reach-ahead features for final polish sprint

### Sprint 3 Retrospective Review
- Completed: 16 pts (on velocity)
- Defects found: 1 (pagination off-by-one)
- Coverage reached: 84%
- Team morale: High (sustainable pace maintained)

### Stories Breakdown

**STORY-11** (5 pts): Edit profile
- Change username in-place
- Update in DB and WebSocket
- Reflect changes in chat messages
- Pair: Alex + Maya

**STORY-12** (8 pts): Unread badges
- Track unread messages per room
- Display badge count on room list
- Clear count on room select
- Pair: Maya + Sarah

**STORY-13** (3 pts): UI/UX improvements
- Responsive mobile layout
- Better styling (colors, spacing)
- Loading states
- Pair: Sarah + Jordan

**STORY-14** (5 pts): Infinite scroll refinement
- Prevent duplicate loads
- Loading indicator
- Handle edge case: no more messages
- Pair: Alex + Maya

### Definition of Done
- TDD: tests before code
- Code review via pair programming
- All tests pass (>85% coverage target)
- QA sign-off
- No regressions in existing features

### Sprint Goals
- Reach 85%+ test coverage
- Fix all outstanding QA findings
- Ship a production-ready UI
- Complete all backlog items

### Risks & Mitigation
1. **Scope creep** — Stories might expand during implementation
   - Mitigation: Strict story acceptance criteria
   - Owner: Sarah (PM)

2. **Mobile responsive issues** — CSS for mobile complex
   - Mitigation: Test on multiple sizes during pairing
   - Owner: Maya (Frontend)

3. **Unread state consistency** — Tracking across disconnects
   - Mitigation: Persist unread state to localStorage + DB
   - Owner: Alex + Maya

### Success Criteria
- All 4 stories complete ✓
- Coverage 85%+ ✓
- Zero production defects ✓
- Build time <60s ✓
- 100% pair programming ✓

### Final Burndown
- Day 1-3: STORY-11 (profile edit)
- Day 4-7: STORY-12 (unread badges)
- Day 8-9: STORY-13 (UI/UX)
- Day 10-12: STORY-14 (infinite scroll + polish)
