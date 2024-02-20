import { NavLink } from "react-router-dom";

function NavBar() {

    return (
        <div id="navbar">
            <div>Logo</div>
            <ul>
                <li><NavLink to="/login">Log in</NavLink></li>
                <li><NavLink to="/signup">Sign up</NavLink></li>
            </ul>
        </div>
    )
}

export default NavBar;