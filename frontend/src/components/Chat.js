import React, { useState, useEffect, useRef, useCallback } from 'react';
import useWebSocket from '../hooks/useWebSocket';
import api from '../services/api';
import '../styles/Chat.css';

function formatTime(ts) {
  if (!ts) return '';
  const iso = ts.endsWith('Z') || ts.includes('+') ? ts : `${ts}Z`;
  return new Date(iso).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function initial(name) {
  return name && name.length > 0 ? name[0].toUpperCase() : '?';
}

function Chat({ username, onLogout }) {
  const [rooms, setRooms] = useState([]);
  const [selectedRoom, setSelectedRoom] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [newRoomName, setNewRoomName] = useState('');
  const [error, setError] = useState('');
  const messagesEndRef = useRef(null);

  const handleIncoming = useCallback((msg) => {
    setMessages((prev) => (prev.some((m) => m.id === msg.id) ? prev : [...prev, msg]));
  }, []);

  const { onlineUsers, connected } = useWebSocket(selectedRoom, username, handleIncoming);

  useEffect(() => {
    loadRooms();
  }, []);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const loadRooms = async () => {
    try {
      const response = await api.get('/api/rooms/');
      setRooms(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  const selectRoom = async (room) => {
    setSelectedRoom(room);
    setMessages([]);
    try {
      const response = await api.get(`/api/messages/${room.id}`);
      setMessages(response.data.slice().reverse());
    } catch (err) {
      console.error(err);
    }
  };

  const handleCreateRoom = async (e) => {
    e.preventDefault();
    const name = newRoomName.trim();
    if (!name) return;
    try {
      const response = await api.post('/api/rooms/', { name });
      setNewRoomName('');
      setError('');
      await loadRooms();
      selectRoom(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Could not create room');
    }
  };

  const handleSendMessage = async (e) => {
    e.preventDefault();
    const content = input.trim();
    if (!content || !selectedRoom) return;
    setInput('');
    try {
      const response = await api.post(`/api/messages/${selectedRoom.id}`, { content });
      handleIncoming(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleLogout = async () => {
    try {
      await api.post('/api/auth/logout');
    } catch (err) {
      // Logging out locally regardless of server response
    }
    onLogout();
  };

  return (
    <div className="chat-container">
      <aside className="sidebar">
        <div className="sidebar-header">
          <span className="logo-dot" />
          <h1>Chatter</h1>
        </div>

        <form className="create-room" onSubmit={handleCreateRoom}>
          <input
            value={newRoomName}
            onChange={(e) => setNewRoomName(e.target.value)}
            placeholder="New room name…"
          />
          <button type="submit" title="Create room" disabled={!newRoomName.trim()}>+</button>
        </form>
        {error && <div className="sidebar-error">{error}</div>}

        <nav className="room-list">
          {rooms.map((room) => (
            <button
              key={room.id}
              type="button"
              className={`room-item ${selectedRoom?.id === room.id ? 'active' : ''}`}
              onClick={() => selectRoom(room)}
            >
              <span className="room-hash">#</span>
              <span className="room-name">{room.name}</span>
            </button>
          ))}
          {rooms.length === 0 && (
            <p className="empty-hint">No rooms yet — create one above.</p>
          )}
        </nav>

        <div className="sidebar-footer">
          <div className="me">
            <span className="avatar small">{initial(username)}</span>
            <span className="me-name">{username}</span>
          </div>
          <button type="button" className="logout-btn" onClick={handleLogout}>
            Log out
          </button>
        </div>
      </aside>

      <main className="main">
        {selectedRoom ? (
          <>
            <header className="room-header">
              <div>
                <h2># {selectedRoom.name}</h2>
                {selectedRoom.description && (
                  <p className="room-desc">{selectedRoom.description}</p>
                )}
              </div>
              <div className={`online ${connected ? '' : 'offline'}`}>
                <span className="online-dot" />
                {connected
                  ? `${onlineUsers.length} online${onlineUsers.length ? `: ${onlineUsers.join(', ')}` : ''}`
                  : 'connecting…'}
              </div>
            </header>

            <div className="messages">
              {messages.length === 0 && (
                <p className="empty-hint center">No messages yet. Say hello 👋</p>
              )}
              {messages.map((msg) => {
                const mine = msg.author_name === username;
                return (
                  <div key={msg.id} className={`message-row ${mine ? 'mine' : ''}`}>
                    {!mine && <span className="avatar">{initial(msg.author_name)}</span>}
                    <div className="bubble">
                      {!mine && <span className="author">{msg.author_name}</span>}
                      <p>{msg.content}</p>
                      <span className="time">{formatTime(msg.created_at)}</span>
                    </div>
                  </div>
                );
              })}
              <div ref={messagesEndRef} />
            </div>

            <form className="composer" onSubmit={handleSendMessage}>
              <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder={`Message #${selectedRoom.name}`}
              />
              <button type="submit" disabled={!input.trim()}>Send</button>
            </form>
          </>
        ) : (
          <div className="no-room">
            <h2>Welcome, {username} 👋</h2>
            <p>Select a room on the left, or create a new one to start chatting.</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default Chat;
