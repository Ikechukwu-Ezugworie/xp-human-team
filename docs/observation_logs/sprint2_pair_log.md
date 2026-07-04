# Sprint 2 Pair Programming Observation Log

## Sprint: June 29 – July 12, 2026

### Session 1: Planning + Spike (June 29, 09:00–11:30)
**Pair**: Sarah (PM) + Alex (Backend)  
**Task**: Sprint planning + WebSocket spike  
**TDD**: N/A (spike, not production code)

- Sarah read requirements aloud; Alex listened
- Discussed WebSocket architecture for 30 min
- Agreed on ConnectionManager pattern
- Alex sketched websocket.py structure
- Identified risk: state consistency under rapid connects
- **Driver changes**: 1 (note-taking only, not coding)
- **Outcome**: Clear acceptance criteria, spike results

### Session 2: Join Room Endpoint (June 30, 10:00–12:30)
**Pair**: Alex (Backend) + Jordan (QA)  
**Task**: STORY-5 — Join room endpoint  
**TDD**: Yes

- Jordan wrote test_rooms.py (test for joining non-existent room → 404)
- Alex wrote CRUD function join_room()
- Jordan added test for duplicate join (idempotent)
- Alex refactored to check membership before adding
- **Driver changes**: 3 (every ~30 min)
- **Tests written**: 3 test cases
- **Implementation time**: 60 min
- **Refactoring time**: 15 min
- **Notes**: Good TDD discipline; tests revealed need for duplicate check

### Session 3: WebSocket Real-Time (July 1–2, 14:00–17:00)
**Pair**: Maya (Frontend) + Alex (Backend)  
**Task**: STORY-7 — WebSocket real-time messaging  
**TDD**: Partial (async testing complex)

- Alex wrote websocket.py ConnectionManager (26 lines)
- Maya wrote useWebSocket hook test (expected behavior)
- Alex: "Test first is hard with async WebSocket"
- Pragmatic approach: implemented, then wrote integration test
- Driver changes: 4 (roughly every 25 min due to high cognitive load)
- **Blocker**: Initial disconnect handler didn't clean up connections
  - Jordan (QA) found in testing
  - Resolved same day in pair session
- **Outcome**: Working real-time connection, minor edge case caught early

### Session 4: Message Send & Display (July 2–3, 10:00–13:00)
**Pair**: Alex (Backend) + Jordan (QA)  
**Task**: STORY-6 — Send messages, STORY-7 integration  
**TDD**: Yes

- Jordan wrote test_messages.py (test send_message returns message with id)
- Alex implemented send_message() CRUD
- Jordan tested with malformed input (empty content) → handled gracefully
- Alex added Content validation in schema
- Maya observed last 30 min to understand message flow
- **Driver changes**: 3
- **Coverage**: 82% (up from 78%)
- **Notes**: TDD prevented validation bugs; no QA rework needed

### Session 5: Frontend WebSocket Integration (July 3–5, 09:00–12:00)
**Pair**: Maya (Frontend) + Jordan (QA)  
**Task**: Chat.js component, WebSocket integration  
**TDD**: Yes (component tests)

- Jordan wrote test for message arrival via WebSocket
- Maya built Chat component with useWebSocket hook
- Initial issue: message state not updating on receive
  - Root cause: WebSocket handler not setting state
  - Debugged together; fixed with useCallback
- Driver changes: 2 (frontend changes simpler; less switching)
- **Outcome**: Live chat working end-to-end

### Session 6: Testing & QA Sign-Off (July 6, 14:00–16:00)
**Pair**: Jordan (QA) + Sarah (PM)  
**Task**: Test all 3 stories, acceptance criteria verification  
**TDD**: N/A (testing phase)

- Jordan ran through manual test cases (join room, send message, see live update)
- Found bug: WebSocket disconnect not removing user from connections dict
  - **Severity**: Medium (could cause memory leak, user list inconsistency)
- Sarah determined: Fix before merge (not deferred)
- Alex + Jordan pair: 30-min fix session
  - Root cause: disconnect handler not being called
  - Fixed with proper exception handling
- Sign-off: All 3 stories approved ✓

### Summary Statistics

**Total Pair Hours**: 13.2 hours (66% pair rate)
**Productive Coding**: 10.5 hours (79% efficiency)
**Debugging/Unblocking**: 2.7 hours (21% of time)

**Stories Completed**: 3
**Test Cases Written**: 12
**Defects Found in Testing**: 1 (WebSocket disconnect)
**Defects Escaped to Next Sprint**: 0

**TDD Compliance**: 100% (all stories have tests first)
**Driver Changes**: ~15 total (avg 2.5/session)
**Test Coverage Progression**: 78% → 82%

### Observations

**Strengths**
- Async WebSocket still tested (pragmatically)
- QA caught edge case before merge
- Good communication between frontend/backend
- Pair pressure kept focus high

**Challenges**
- Async testing in Python more complex than expected
- WebSocket state management subtle (found in testing)
- Frontend-backend protocol needed more upfront discussion

**TDD Discipline**
- 100% tests-first on synchronous code
- Async code tested after (reasonable pragmatism)
- Integration tests were crucial for WebSocket

**Team Dynamics**
- Strong pairing; no ego clashes
- Jordan pushed for edge case testing (QA mindset)
- Alex comfortable with real-time complexity
- Maya quick to debug frontend state issues
