import { useState, useEffect } from "react";
import apiKey from "../env";
import { useOutletContext } from "react-router-dom";

function Question({ question, lesson }) {

    const [ userQuestion, setUSerQuestion ] = useState({});
    const [ userInput, setUserInput ] = useState("");
    const [ aiResponse, setAiResponse] = useState("");

    const { user, setUser } = useOutletContext();
    console.log(question);

    const systemMessageContent = `You are a teacher of ${lesson.language.language_name}. When given an input, you will review the input in ${lesson.language.language_name} for grammar and spelling. Please respond with the corrected input, and then, in a new line, list the corrections you made. Please add a new line for each correction.`

    useEffect(() => {

        if (user && question) {
            fetch(`http://127.0.0.1:5555/users/${user.id}/questions/${question.id}/`, {
                credentials: 'include'
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                } else {
                    setUSerQuestion({});
                    setUserInput("");
                    setAiResponse("");
                    return response.json();
                }
            })
            .then(userQuestion => {
                console.log(userQuestion);
                setUSerQuestion(userQuestion);
                setUserInput(userQuestion['user_input']);
                setAiResponse(userQuestion['ai_feedback']);
            })
        }
        
    }, [lesson])

    function handleSubmit(event) {
        event.preventDefault();
        setAiResponse("Loading...");
        
        fetch(`https://api.openai.com/v1/chat/completions`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                "model": "gpt-3.5-turbo",
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": systemMessageContent},
                    {"role": "user", "content": userInput}
                ],
            })
        })
        .then(response => response.json())
        .then(message => setAiResponse(message.choices[0].message.content))
    }

    function handleSave() {

        if (userQuestion.id) {
            fetch(`http://127.0.0.1:5555/users/${user.id}/questions/${question.id}/`, {
                method: 'PATCH',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    user_id: user.id,
                    question_id: question.id,
                    user_input: userInput,
                    ai_feedback: aiResponse
                })
            })

        } else {
            fetch(`http://127.0.0.1:5555/users/${user.id}/questions/${question.id}/`, {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    user_id: user.id,
                    question_id: question.id,
                    user_input: userInput,
                    ai_feedback: aiResponse
                })
            })
            .then(response => { 
                if (response.ok) {
                    console.log("saved")
                }
            })
        }
    }

    function formatAiResponse(aiResponse) {

        if (aiResponse === "Loading") {
            return <p>Loading...</p>;
        } else {
            return <div>
                {formatAiCorrection(aiResponse)}
                {formatAiFeedback(aiResponse)}
                <button onClick={handleSave}>Save</button>
            </div>
        }
    }

    function formatAiCorrection(aiResponse) {

        {
            const responseArray = aiResponse.split("Corrections:");

            const correctedInputArr = responseArray[0].split(/\r?\n/).map(paragraph => {
                if (paragraph === "") {
                    return
                } else {
                    return <p>{paragraph}</p>
                }
            })

            console.log(responseArray);

            return correctedInputArr
        }
    }

    function formatAiFeedback(aiResponse) {

        if (aiResponse === "Loading...") {
            return
        } else {
            const responseArray = aiResponse.split("Corrections:");
            const bulletPoints = responseArray[1].split("\n");
    
            console.log(bulletPoints);
            
            return <ul>Corrections: {bulletPoints.map(line => {
                    if (line === "\n") {
                        return
                    } else {
                        return <li>{`${line};`}</li>
                    };
            })}</ul>
        }
    }


    return (
        <div className='question-container'>
            <h3>{question.question_text}</h3>

            <form className="question-form" onSubmit={event => handleSubmit(event)}>
                <textarea value={userInput} onChange={event => setUserInput(event.target.value)}></textarea>
                <input type="submit" />
            </form>

            {/* {aiResponse ? <div><p>{aiResponse}</p><button onClick={handleSave}>Save</button></div> : null} */}
            {aiResponse ? formatAiResponse(aiResponse) : null}
        </div>
    )
}

export default Question;
