import React, { useState, useEffect } from 'react';
import Login from './components/Login';
import Chat from './components/Chat';
import './App.css';

function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const token = localStorage.getItem('token');

  useEffect(() => {
    if (token) {
      setAuthenticated(true);
      const user_id = localStorage.getItem('user_id');
      setUser({ id: user_id });
    }
  }, [token]);

  const handleLogin = (token, user_id) => {
    localStorage.setItem('token', token);
    localStorage.setItem('user_id', user_id);
    setAuthenticated(true);
    setUser({ id: user_id });
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user_id');
    setAuthenticated(false);
    setUser(null);
  };

  return (
    <div className="App">
      {authenticated ? (
        <Chat user={user} onLogout={handleLogout} />
      ) : (
        <Login onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;
