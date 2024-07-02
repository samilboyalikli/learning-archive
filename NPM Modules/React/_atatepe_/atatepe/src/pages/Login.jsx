import React from 'react'
import UserPage from './UserPage'
import { useState } from 'react';
import StuffPage from './StuffPage';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loggedIn, setLoggedIn] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (username === 'dogru_kullanici' && password === 'dogru_sifre') {
      setLoggedIn(true);
    } else {
      alert('Hatalı kullanıcı adı veya şifre.');
    }
  }
  return (
    <div>
      <div className='container'>
        <div className='text-center mt-3'>
          {!loggedIn && ( 
            <form onSubmit={handleSubmit}>
              <div>
              <input
                type="text"
                placeholder="Kullanıcı Adı"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              </div>
              <div>
              <input
                type="password"
                placeholder="Şifre"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              </div>
              <button type="submit">GİRİŞ</button>
            </form>
          )}
        </div>
      </div>
      <UserPage />
      {loggedIn && <StuffPage />}</div>
  )
}

export default Login
