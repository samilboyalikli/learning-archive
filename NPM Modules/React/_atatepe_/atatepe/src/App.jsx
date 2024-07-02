import './App.css'
import Login from './pages/Login';
import Others from './pages/Others';
import UserPage from './pages/UserPage'
import { Route, Routes } from 'react-router-dom';

function App() {

  return (
    <>
      <div className='container mb-5'>
        <Routes>
          <Route path="/login" element={<Login />}/>
          <Route path="/others" element={<Others />}/>
          <Route path="/" element={<UserPage />}/>
        </Routes>
      </div>
    </>
  )
}

export default App
