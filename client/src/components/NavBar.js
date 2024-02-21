import { NavLink } from "react-router-dom";

function NavBar({ user, setUser }) {

    function handleLogOut() {
        fetch("http://127.0.0.1:5555/logout", {
            method: 'DELETE',
            credentials: "include"
        })
        .then(response => { if (response.ok) {
            setUser(null);
        }})
    }

    function handleHamburgerClick() {

        const navLinks = document.querySelectorAll(".nav-ul");
        // console.log(navLinks)

        navLinks.forEach(navLink => {
            if (navLink.style.display !== "inline-block") {
                navLink.style.display = "inline-block";
              } else {
                navLink.style.display = "none";
              }
        })
    }

    return (
        <div className="navbar">
            <div id="logo"><NavLink to="/">Logo</NavLink></div>
            <ul className="nav-ul">
                <li className="nav-li"><NavLink to="/courses">Courses</NavLink></li>
            </ul>

            {user ? 
            (<ul className="nav-ul">
                <li className="nav-li"><NavLink to="/profile">Profile</NavLink></li>
                <li className="nav-li"><a onClick={handleLogOut}>Log out</a></li>
            </ul>) :
            (<ul className="nav-ul">
                <li className="nav-li"><NavLink to="/login">Log in</NavLink></li>
                <li className="nav-li"><NavLink to="/signup">Sign up</NavLink></li>
            </ul>)}
            <a id="hamburger-menu" onClick={() => handleHamburgerClick()}>≡</a>
        </div>
    )
}

export default NavBar;