import { useState, useEffect } from "react";
import { Outlet, Navigate, useNavigate, NavLink } from "react-router-dom";
import NavBar from './NavBar';
import Footer from './Footer';

function App() {

  const [ user, setUser ] = useState({});

  return (
    <div className="App">
        <NavBar user={user} setUser={setUser} />
        <Outlet context={{user: user, setUser: setUser}} />
        <Footer />
    </div>
  );
}

export default App;
