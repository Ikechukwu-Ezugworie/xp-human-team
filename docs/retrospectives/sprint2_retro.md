# Sprint 2 Retrospective

## Date: July 12, 2026

### What Went Well ✓
1. **WebSocket real-time messaging works end-to-end**
   - No production issues; edge case caught in testing
   - Pragmatic approach to async TDD paid off

2. **Team confidence growing**
   - Complex features (WebSocket) completed on velocity
   - Estimation improving (5.5% error vs. 0% S1)
   - Morale high

3. **QA integration + pairing = fewer defects**
   - Only 1 defect found, fixed before merge
   - 0 escaped to production
   - Jordan's testing rigor proving valuable

4. **Code quality maintained**
   - Coverage increased 78% → 82%
   - Complexity well-managed (25 vs. 18)
   - No regressions

### What Could Be Better ⚠️

1. **Async testing complexity**
   - Python async/await testing harder than sync
   - Next sprint: pre-plan async test strategy

2. **Frontend-backend protocol definition**
   - Initial misunderstandings about WebSocket message format
   - Could have saved 2 hours with written protocol upfront

3. **Performance not yet tested**
   - What happens with 100 concurrent connections?
   - Deferred to Sprint 3 non-functional requirements

### Metrics

| Metric | S1 | S2 | Change |
|--------|----|----|--------|
| **Velocity (pts)** | 21 | 18 | -14% |
| **Test Coverage** | 78% | 82% | +4% |
| **Complexity** | 18 | 25 | +39% |
| **Defects (QA)** | 0 | 1 | Caught & fixed ✓ |
| **Defects (Prod)** | 0 | 0 | ✓ |
| **Pair Hours** | 12.5 | 13.2 | +6% |
| **Estimation Error** | 0% | 5.5% | Within 5% |

### Code Review Notes
- No formal code review (all pairs = live review)
- Refactoring during pairing kept code clean
- Naming conventions consistent
- No architectural drift

### Team Retrospective Q&A

**Q: Are we going too fast?**
- A: No; sustainable pace. Pair rate 66% still leaves buffer. NASA-TLX scores healthy.

**Q: Should we revisit WebSocket disconnect bug earlier?**
- A: Good catch in testing. Minor: user list inconsistent for <1 sec. Would do same TDD again.

**Q: Is JSON message format stable?**
- A: Yes. Document for next sprint so frontend/backend don't misalign again.

### Action Items (Sprint 3)

1. **Document WebSocket protocol** (Alex, 1 hr)
   - Message format JSON schema
   - Expected error responses
   - Disconnection behavior

2. **Add async test helpers** (Jordan, 2 hrs)
   - Fixture for WebSocket connection mocking
   - Reusable in Sprint 3 (online users)

3. **Performance testing spike** (Sarah, Alex, 3 hrs)
   - Load test: 50 concurrent connections
   - Measure CPU, memory
   - Report in Sprint 3 planning

4. **Password validation** (deferred to S4)
   - Originally planned for S3
   - Low priority; push to polish sprint

### Burndown Analysis

**Velocity Dip (21 → 18 pts)**
- Expected: WebSocket complexity
- Estimation error only 5.5% (good!)
- Team stable at 16–18 pts/sprint baseline

**Workload Distribution**
- Alex (Backend): 4.2 hrs WebSocket, 3.1 hrs messages
- Maya (Frontend): 3.5 hrs Chat component, 2.1 hrs hook
- Jordan (QA): 2.8 hrs testing, 1.2 hrs pair time
- Sarah (PM): 1.2 hrs planning, 0.3 hrs retro
- Total: ~13 hrs pairing (sustainable)

### Next Sprint Planning Notes

- Velocity target: 15–16 pts (sustainable)
- Message history pagination more complex than expected; allocate 10 pts to STORY-9
- Online users display simpler; 5 pts STORY-8 OK
- Logout trivial; 3 pts STORY-10 OK
- Total: 18 pts → pull down to 16 if needed

### Improvements Implemented

From Sprint 1 Retro → Sprint 2 Actions:
- ✓ Increased pairing (maintained 100%)
- ✓ Added async test helpers (pending for S3)
- ✓ Better documentation (protocol doc planned)

### Team Recognition

**Standouts**
- **Jordan**: Caught WebSocket disconnect bug; pushed for edge case testing
- **Alex**: WebSocket complexity handled gracefully; mentored Maya
- **Maya**: Learned React async hooks; shipped Chat.js with minimal rework
- **Sarah**: Excellent sprint planning; velocity estimates realistic

### Release Readiness

**Can we ship Sprint 2 now?**
- ✓ Core functionality works (auth, rooms, messaging)
- ✓ Real-time updates live
- ✓ Test coverage 82% (above 80% bar)
- ✓ 0 production defects
- ⚠️ No performance testing yet
- ⚠️ Mobile responsive not tested

**Recommendation**: Ship as beta. Performance + mobile polish in Sprint 3.

### Velocity Forecast

| Sprint | Committed | Completed | Forecast |
|--------|-----------|-----------|----------|
| S1     | 21        | 21        | — |
| S2     | 18        | 18        | — |
| S3     | 16        | ? (est)   | 15–18 pts |
| S4     | —         | ? (est)   | 14–16 pts |

**Total Forecast**: 63–67 pts (all stories complete by EOW S4)

### Final Notes

**Sustainability**: Team at healthy velocity. No signs of burnout.  
**Quality**: Coverage up, defects caught early. TDD working.  
**Momentum**: Ready for Sprint 3 with confidence.
