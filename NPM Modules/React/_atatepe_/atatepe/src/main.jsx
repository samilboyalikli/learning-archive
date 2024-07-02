import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Header from './layouts/Header.jsx'
import Footer from './layouts/Footer.jsx'
import { Provider } from 'react-redux'
import { store } from './redux/app/store.js'
import { BrowserRouter } from 'react-router-dom'


ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Provider store={store}>
      <Header />
      <App />
      <Footer />
    </Provider>
  </BrowserRouter>
)
