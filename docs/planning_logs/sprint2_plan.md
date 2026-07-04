# Sprint 2 Planning Log

## Date: June 29 – July 12, 2026

### Committed Stories
- STORY-5: Join room (5 pts)
- STORY-6: Send messages (8 pts)
- STORY-7: WebSocket real-time (5 pts)

**Total Committed: 18 points**
**Velocity Last Sprint: 21 points**
**Adjustment**: Reduced due to WebSocket complexity spike

### Estimation Accuracy (from Sprint 1)
- Committed: 21 pts
- Completed: 21 pts
- Estimation error: 0%

### Risk Analysis
1. **WebSocket complexity** — first time implementing real-time
   - Mitigation: Spike on connection management (3 hours)
   - Owner: Alex (Backend)
2. **Frontend-backend sync** — new channel for communication
   - Mitigation: Protocol agreement before implementation
   - Owner: Maya + Alex

### Architecture Decisions
- ConnectionManager pattern for WebSocket state
- Separate router for WS endpoint (`/ws/{room_id}`)
- Message broadcast to all connected clients in room

### Burndown
- Day 1-2: 5 pts (join room) ✓
- Day 3-5: 8 pts (send messages + storage) ✓
- Day 6-10: 5 pts (WebSocket real-time) ✓

### Pair Schedule
- Session 1 (Jun 29): Sarah + Alex (Planning + spike)
- Session 2 (Jun 30): Alex + Jordan (Backend auth fixes)
- Session 3 (Jul 1-2): Maya + Alex (WebSocket protocol + frontend)
- Session 4 (Jul 3-5): Maya + Jordan (Frontend integration + testing)

### Definition of Done
- Code written in pairs
- All tests pass
- Code review (implicit in pairing)
- QA sign-off
- Deployed to staging

### Notes
- Sprint 1 went smoothly; team showing good velocity
- Password validation will be deferred to Sprint 3 refactoring
- Database connection pooling not needed for MVP
