import React from 'react'
import './navbar/navbar.css'
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <div>
      <nav className="navbar navbar-expand-lg bg-primary">
        <div className="container">
          <a className="navbar-brand text-white fs-1 fw-bold" href="/">ATATEPE</a>
          <img src="/bursalogo.png" alt="Logo" width="80" height="80" className="d-inline-block align-text-top"></img>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link active text-light text-opacity-90" to="/login">Giriş</Link>
              </li>
              <li className="nav-item">
                <a className="nav-link text-light text-opacity-90" href="https://qr.posula.com/?c=nevUCMYllp0=">Menü</a>
              </li>
              <li className="nav-item">
                <Link className="nav-link text-light text-opacity-90" to="/others">Tesislerimiz</Link>
              </li>
              <li className="nav-item">
                <a className="nav-link text-light text-opacity-90" href="https://www.burfas.com.tr/tesis/atatepe-sosyal-tesisi-1/">Sitemiz</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  )
}

export default Navbar
