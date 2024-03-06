import { Link, useOutletContext, useNavigate } from "react-router-dom";
import { useState } from "react";
import toast, { Toaster } from 'react-hot-toast';

function Login() {

    const [ email, setEmail ] = useState("");
    const [ password, setPassword ] = useState("");

    const { user, setUser } = useOutletContext();

    const navigate = useNavigate()

    function handleSubmit(event) {
        event.preventDefault();

        fetch("http://127.0.0.1:5555/login", {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                credentials: 'include',
                body: JSON.stringify({
                    email,
                    password
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } 
                else if (response.status == 409) {
                    throw new Error('Failed to log in');
                };
            })
            .then(newUser => {
                setUser(newUser);
                toast.success('Success! Logging you in...');
                navigate("/courses/")
            })
            .catch(error => {
                toast.error('Error logging in, please try again..');
            });
    }

    return (
        <div className="main">
            <div className="login-form">
                <form onSubmit={handleSubmit}>
                    <h1>Welcome back!</h1>
                    <p>Use your email and password to log into your account.</p>
                    <fieldset>
                    <label className="sr-only" htmlFor="email">Email:</label>
                        <input 
                            id="email" type="email" placeholder="Email"
                            value={email} onChange={event => setEmail(event.target.value)}>
                        </input>
                        <label className="sr-only" htmlFor="password">Password:</label>
                        <input 
                            id="password" type="password" placeholder="Password" 
                            value={password} onChange={event => setPassword(event.target.value)}>  
                        </input>
                    </fieldset>
                    <input type="submit" value="Submit"></input>
                </form>

                <hr />
                <p>Don't have an account yet? <Link to="/signup">Sign up</Link></p>
            </div>
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
        </div>
    )
}

export default Login