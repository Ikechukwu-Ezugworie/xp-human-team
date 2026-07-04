# Quick Start Guide - XP Chat Application

A faster way to get the application up and running for testing.

## TL;DR - 30 Seconds

### Terminal 1: Start Backend
```bash
cd /Users/mac/Documents/Innopolis/Thesis/Thesis\ LLM\ SE/experiment/xp-human-team/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at **http://localhost:8000**

### Terminal 2: Start Frontend
```bash
cd /Users/mac/Documents/Innopolis/Thesis/Thesis\ LLM\ SE/experiment/xp-human-team/frontend
npm install
npm start
```

The app will open at **http://localhost:3000**

---

## Verify Backend is Running

Open a third terminal and test:

```bash
# Health check
curl http://localhost:8000/health

# Expected output:
# {"status":"ok"}

# View API docs (interactive)
# Open http://localhost:8000/docs in your browser
```

---

## Test the Application

1. **Open http://localhost:3000** in your browser
2. **Register** a new user (any username/password)
3. **Create a room** (click button on sidebar)
4. **Send a message** and watch it appear in real-time
5. Open a **second browser tab/window** and repeat steps 2-3 with different username
6. **Send messages** between users - should appear instantly (WebSocket)

---

## Troubleshooting

### Backend Won't Start
```bash
# Make sure you're in the venv
source venv/bin/activate

# Check Python version (must be 3.9+)
python --version

# Reinstall dependencies
pip install --r requirements.txt
```

### Port Already in Use
```bash
# For port 8000 (backend):
lsof -i :8000
kill -9 <PID>

# For port 3000 (frontend):
lsof -i :3000
kill -9 <PID>
```

### Cannot Connect to Backend from Frontend
- Make sure backend is running on http://localhost:8000
- Check backend logs for errors
- Browser console (DevTools F12) should show WebSocket connecting to ws://localhost:8000

---

## Commands

| Task | Command |
|------|---------|
| **Install backend deps** | `pip install -r backend/requirements.txt` |
| **Run backend** | `uvicorn app.main:app --reload` (in backend dir) |
| **Run frontend** | `npm start` (in frontend dir) |
| **Run backend tests** | `pytest` (in backend dir) |
| **Run frontend tests** | `npm test` (in frontend dir) |
| **View API docs** | Open http://localhost:8000/docs |
| **View database** | `sqlite3 backend/chat.db` then `.tables` |

---

## Architecture

```
Backend (FastAPI)             Frontend (React)
    ↓                              ↓
Port 8000                      Port 3000
/api/auth/*                    /components
/api/rooms/*                   /hooks/useWebSocket
/api/messages/*                /services/api
/ws/{room_id}                  /styles
    ↓
SQLite Database (chat.db)
```

---

## All 14 Stories Implemented

✅ **Sprint 1**: Auth + Rooms (registration, login, list rooms, create room)
✅ **Sprint 2**: Messaging + WebSocket (join, send, real-time)
✅ **Sprint 3**: Features (online users, history, logout)
✅ **Sprint 4**: Polish (edit profile, unread badges, UI/UX, pagination)

---

## Next Steps

After verifying the app works:
1. Read `SIMULATION_SUMMARY.md` for project overview
2. Check `docs/retrospectives/` for team insights
3. Review `data/` for commit history and metrics
4. Compare with AI-assisted team results

**Questions?** See `RUNNING_THE_APP.md` for detailed setup.
