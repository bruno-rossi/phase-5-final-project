import { useOutletContext } from "react-router-dom";
import { useState } from "react";

function Profile() {

    const { user, setUser } = useOutletContext();
    
    const [ name, setName ] = useState(user.name);

    function handleSaveProfile(event) {

        event.preventDefault();

        fetch(`http://127.0.0.1:5555/users/${user.id}`, {
            method: 'PATCH',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            credentials: 'include',
            body: JSON.stringify({
                name
            })
        })
        .then(response => {
            console.log(response);
            if (response.ok) {
                response.json().then(updatedUser => setUser(updatedUser));
            }
        })
    }

    return (
        <div className="main">
            <form className="login-form" onSubmit={handleSaveProfile}>
                <h1>Profile</h1>

                {!user ? <h1>Loading...</h1> : 
                <fieldset>
                    <label htmlFor="email">Email:</label>
                    <input id="email" type="email" value={user.email} disabled></input>
                    <label htmlFor="name">Name:</label>
                    <input id="name" type="text" value={name} onChange={event => setName(event.target.value)}></input>
                    <input type="submit" value="Save"></input>
                </fieldset>
                }
            </form>
        </div>
    )
}

export default Profile;