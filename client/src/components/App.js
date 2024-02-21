import { useState, useEffect } from "react";
import { Outlet, Navigate, useNavigate, NavLink } from "react-router-dom";
import NavBar from './NavBar';
import Footer from './Footer';

function App() {

  const [ user, setUser ] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5555/check_session", {
      credentials: "include",
    })
    .then(response => response.json())
    .then(user => setUser(user))
  }, [])

  return (
    <div className="App">
        <NavBar user={user} setUser={setUser} />
        <Outlet context={{user: user, setUser: setUser}} />
        <Footer />
    </div>
  );
}

export default App;
