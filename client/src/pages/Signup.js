import { Link } from "react-router-dom";
import { useState } from "react";
import toast, { Toaster } from 'react-hot-toast';

function Signup() {

    const [ email, setEmail ] = useState("");
    const [ password, setPassword ] = useState("");
    const [ confirmPassword, setConfirmPassword ] = useState("");

    function handleSubmit(event) {
        event.preventDefault();

        if (password !== confirmPassword) {
            console.log("Passwords must match!")
        } else {
            fetch("http://127.0.0.1:5555/signup", {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    "Content-Type": "application/json"
                },
                credentials: "include",
                body: JSON.stringify({
                    email,
                    password
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else if (response.status === 409) {
                    throw new Error('Failed to create user');
                };
            })
            .then(newUser => {
                toast.success('Account created! Please log in.');
            })
            .catch(error => {
                toast.error('Error while creating account. Please try again.');
              });
            
            setEmail("");
            setPassword("");
            setConfirmPassword("");
    }
    }

    return (
        <div className="main">
            <div className="login-form">
                <form onSubmit={handleSubmit}>
                    <h1>Welcome!</h1>
                    <p>Enter your email and password to create a new account.</p>
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
                        <label className="sr-only" htmlFor="confirm-password">Confirm password:</label>
                        <input 
                            id="confirm-password" type="password" placeholder="Confirm password"
                            value={confirmPassword} onChange={event => setConfirmPassword(event.target.value)}
                        ></input>
                        <input type="submit" value="Submit"></input>
                    </fieldset>
                </form>

                <hr />
                <p>Already have an account? <Link to="/login">Log in</Link></p>
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

export default Signup