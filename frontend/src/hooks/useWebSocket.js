import { useEffect, useRef, useState } from 'react';

function useWebSocket(room, username, onMessage) {
  const [onlineUsers, setOnlineUsers] = useState([]);
  const [connected, setConnected] = useState(false);
  const onMessageRef = useRef(onMessage);
  onMessageRef.current = onMessage;

  useEffect(() => {
    if (!room) {
      setOnlineUsers([]);
      return undefined;
    }

    const base = process.env.REACT_APP_WS_URL || 'ws://localhost:8000';
    const ws = new WebSocket(
      `${base}/ws/${room.id}?username=${encodeURIComponent(username || 'anonymous')}`
    );

    ws.onopen = () => setConnected(true);
    ws.onclose = () => setConnected(false);
    ws.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.type === 'presence') {
          setOnlineUsers(data.users || []);
        } else if (data.type === 'message' && data.message) {
          onMessageRef.current?.(data.message);
        }
      } catch (err) {
        console.error('Failed to parse WebSocket payload', err);
      }
    };

    return () => ws.close();
  }, [room, username]);

  return { onlineUsers, connected };
}

export default useWebSocket;
