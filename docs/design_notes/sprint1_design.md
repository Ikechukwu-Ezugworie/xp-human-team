# Sprint 1 Design Notes

## Authentication Architecture
- JWT tokens issued on login/register
- Tokens stored in localStorage (frontend)
- Bearer token in Authorization header (all requests)

## Database Schema
- Users: id, username, password_hash, created_at
- Rooms: id, name, description, created_by, created_at
- RoomMembers: room_id, user_id (join table)
- Messages: id, room_id, author_id, content, created_at

## API Endpoints (Sprint 1)
- POST /api/auth/register
- POST /api/auth/login
- GET /api/rooms
- POST /api/rooms
- GET /api/rooms/{id}

## Frontend Components
- Login: registration/login form
- RoomList: sidebar with room selection
- (Chat messaging deferred to Sprint 2)
