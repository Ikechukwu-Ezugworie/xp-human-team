# Sprint 3 Planning Log

## Date: July 13–26, 2026

### Committed Stories
- STORY-8: Show online users (5 pts)
- STORY-9: Message history + pagination (8 pts)
- STORY-10: Logout endpoint (3 pts)

**Total Committed: 16 points**
**Velocity (Sprint 2)**: 18 points (conservative estimate)
**Capacity Planning**: 16 pts as sustainable base

### Sprint 2 Review
- Completed: 18 pts
- Defects found by QA: 1
  - WebSocket disconnect not removing connection from manager
  - Fixed before merge ✓
- Estimation error: 5.5%
- Team velocity stabilizing

### Stories Detail
1. **STORY-8** (5 pts): Online users display
   - Show active WebSocket connections in sidebar
   - Update user list on connect/disconnect
   - Pair: Sarah + Maya

2. **STORY-9** (8 pts): Message history pagination
   - Load last 50 messages on room join
   - Implement offset/limit API
   - Infinite scroll on client
   - Pair: Alex + Jordan

3. **STORY-10** (3 pts): Logout endpoint
   - Clear token from localStorage
   - Redirect to login
   - Pair: Maya + Sarah

### Technical Considerations
- Message query optimization (need DB index on room_id + created_at)
- WebSocket should send online user list on any connect/disconnect
- Frontend infinite scroll should prevent duplicate loads

### Testing Strategy
- Test pagination with various message counts (0, 1, 50, 100)
- Test offline user removal from list
- Test logout invalidates session

### Risks
- Pagination off-by-one errors (common in history loading)
- WebSocket state consistency under rapid connect/disconnect
- Infinite scroll race condition if not careful

### Burndown Prediction
- Day 1-3: STORY-8 (online users) ✓
- Day 4-7: STORY-9 (history + pagination) ✓
- Day 8-10: STORY-10 (logout) ✓

### Quality Goals
- Coverage >84%
- Zero production defects
- Pairing 100%
- Code review via pair programming only
