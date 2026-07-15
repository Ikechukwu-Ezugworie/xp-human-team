import { useEffect, useState, useCallback } from 'react';

function useWebSocket(room) {
  const [ws, setWs] = useState(null);
  const [onlineUsers, setOnlineUsers] = useState([]);

  useEffect(() => {
    if (!room) return;

    const wsUrl = `${process.env.REACT_APP_WS_URL || 'ws://localhost:8000'}/ws/${room.id}`;
    const websocket = new WebSocket(wsUrl);

    websocket.onopen = () => console.log('Connected');
    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'users') {
        setOnlineUsers(data.users);
      }
    };
    websocket.onerror = (err) => console.error(err);
    websocket.onclose = () => console.log('Disconnected');

    setWs(websocket);

    return () => websocket.close();
  }, [room]);

  const sendMessage = useCallback(
    (data) => {
      if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(JSON.stringify(data));
      }
    },
    [ws]
  );

  return { sendMessage, onlineUsers };
}

export default useWebSocket;
