import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import toast, { Toaster } from 'react-hot-toast';

function Profile() {

    const params = useParams();
    
    const [ user, setUser ] = useState({});
    const [ name, setName ] = useState("");

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/users/${params.user_id}`, {
            credentials: 'include',
          })
        .then(response => {
            if (response.ok) {
                response.json().then(user => {
                    setUser(user);
                    setName(user.name);
                })
            } else {
                console.log("error");
            }
        })
    }, [])

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
            // console.log(response);
            if (response.ok) {
                response.json().then(updatedUser => {
                    setUser(updatedUser);
                    toast.success('Saved profile!');
                });
            } else {
                toast.error("Error saving profile, please try again.")
            }
        })
    }

    return (
        <div className="main">
            <form className="login-form" onSubmit={handleSaveProfile}>
                <h1>Profile</h1>

                {!user ? <h1>Loading...</h1> : 
                <div>
                    <fieldset>
                        <label htmlFor="email">Email:</label>
                        <input id="email" type="email" value={user.email} disabled></input>
                        <label htmlFor="name">Name:</label>
                        <input id="name" type="text" value={name} onChange={event => setName(event.target.value)}></input>
                        <input type="submit" value="Save"></input>
                        <Toaster toastOptions={
                            {duration: 3000,
                            success: {
                                style: {
                                    background: '#79ad5b',
                                    color: '#F8F9F7'
                                }
                            },
                            error: {
                                style: {
                                    background: '#D24E46',
                                    color: '#F8F9F7'}
                            }}}></Toaster>
                    </fieldset>
                </div>
                }


            </form>
        </div>
    )
}

export default Profile;