import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import TopicItem from "../components/TopicItem";

function Profile() {

    const params = useParams();
    
    const [ user, setUser ] = useState({});
    const [ name, setName ] = useState("");
    // const [ topics, setTopics ] = useState([]);
    // const [ userTopics, setUserTopics ] = useState([]);

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/users/${params.user_id}`, {
            credentials: 'include',
          })
        .then(response => {
            if (response.ok) {
                response.json().then(user => {
                    setUser(user);
                    setName(user.name);
                    // console.log(user.topics);

                    // user.topics.forEach(item => {
                    //     setUserTopics([...userTopics, item]);
                    // })
                })
            } else {
                console.log("error");
            }
        })
    }, [])

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/topics/`, {
            credentials: 'include',
        })
        .then(response => {
            if (response.ok) {
                response.json().then(topics => {
                    // setTopics(topics);
                    // console.log(topics);
                })
            }
        })
    }, [])

    // function autoCheckBoxes(topic) {
        
    //     const userTopicNames = userTopics.map(item => item['topic']['topic_name'])

    //     if (userTopicNames.includes(topic['topic_name'])) {
    //         return "checked";
    //     } else {
    //         return "";
    //     };
    // }

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
                response.json().then(updatedUser => setUser(updatedUser));
            }
        })
    }

    // function handleCheckboxChange(event, topic) {
    //     console.log(event.target.checked)
    //     if (event.target.checked === true) {
    //         fetch(`http://127.0.0.1:5555/users/${user.id}/topics/${topic.id}`, {
    //             method: 'POST',
    //             headers: {
    //                 'Accept': 'application/json',
    //                 'Content-Type': 'application/json'
    //             },
    //             credentials: 'include',
    //             body: JSON.stringify({
    //                 user_id: user.id,
    //                 topic_id: topic.id
    //             })
    //         })
    //         .then(response => {
    //             if (response.ok) {
    //                 response.json().then(userTopic => {
    //                     setUserTopics([...userTopics, userTopic])
    //                 })
    //             }
    //         })
    //     } else if (event.target.checked === false) {
    //         fetch(`http://127.0.0.1:5555/users/${user.id}/topics/${topic.id}`, {
    //             method: 'DELETE',
    //             credentials: 'include'
    //         })
    //         .then(response => {
    //             if (response.ok) {
    //                 console.log("Topic successfully removed from user.")
    //             }
    //         })
    //     }
    // }

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
                    </fieldset>
                    {/* <fieldset>
                        {topics.map(topic => {
                            return (
                                <TopicItem topic={topic}></TopicItem>
                            )
                        })}
                    </fieldset> */}
                </div>
                }


            </form>
        </div>
    )
}

export default Profile;