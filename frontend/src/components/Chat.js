import React, { useState, useEffect } from 'react';
import useWebSocket from '../hooks/useWebSocket';
import api from '../services/api';
import '../styles/Chat.css';

function Chat({ user, onLogout }) {
  const [rooms, setRooms] = useState([]);
  const [selectedRoom, setSelectedRoom] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const { sendMessage, onlineUsers } = useWebSocket(selectedRoom);

  useEffect(() => {
    loadRooms();
  }, []);

  const loadRooms = async () => {
    try {
      const response = await api.get('/api/rooms');
      setRooms(response.data);
    } catch (err) {
      console.error(err);
    }
  };

  const loadMessages = async (roomId) => {
    try {
      const response = await api.get(`/api/messages/${roomId}`);
      setMessages(response.data.reverse());
    } catch (err) {
      console.error(err);
    }
  };

  const selectRoom = (room) => {
    setSelectedRoom(room);
    loadMessages(room.id);
  };

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || !selectedRoom) return;

    try {
      await api.post(`/api/messages/${selectedRoom.id}`, { content: input });
      sendMessage({ type: 'message', content: input });
      setInput('');
      loadMessages(selectedRoom.id);
    } catch (err) {
      console.error(err);
    }
  };

  const handleLogout = async () => {
    await api.post('/api/auth/logout');
    onLogout();
  };

  return (
    <div className="chat-container">
      <div className="sidebar">
        <h2>Rooms</h2>
        <ul>
          {rooms.map((room) => (
            <li
              key={room.id}
              onClick={() => selectRoom(room)}
              className={selectedRoom?.id === room.id ? 'active' : ''}
            >
              {room.name}
            </li>
          ))}
        </ul>
        <button onClick={handleLogout}>Logout</button>
      </div>
      <div className="main">
        {selectedRoom ? (
          <>
            <h2>{selectedRoom.name}</h2>
            <div className="messages">
              {messages.map((msg) => (
                <div key={msg.id} className="message">
                  <strong>{msg.author_id}:</strong> {msg.content}
                </div>
              ))}
            </div>
            <form onSubmit={handleSendMessage}>
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Type a message..."
              />
              <button type="submit">Send</button>
            </form>
          </>
        ) : (
          <p>Select a room</p>
        )}
      </div>
    </div>
  );
}

export default Chat;
