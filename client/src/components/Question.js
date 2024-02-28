import { useState, useEffect } from "react";
import apiKey from "../env";
import { useOutletContext } from "react-router-dom";

function Question({ question, lesson }) {

    const [ questionInput, setQuestionInput ] = useState("");
    const [ aiResponse, setAiResponse] = useState("");

    const { user, setUser } = useOutletContext();

    const systemMessageContent = `You are a teacher of ${lesson.language.language_name}. When given an input, you will review the input in ${lesson.language.language_name} for grammar and spelling. Please respond with the corrected input, and then, in a new line, list the corrections you made. Please add a new line for each correction.`

    // useEffect(() => {

    //     if (user && question) {
    //         fetch(`http://127.0.0.1:5555/users/${user.id}/questions/${question.id}/`, {
    //             credentials: 'include'
    //         })
    //         .then(response => {
    //             if (response.ok) {
    //                 response.json()
    //             }
    //         })
    //         .then(userQuestion => console.log(userQuestion))
    //     }
        
    // }, [user])

    function handleSubmit(event) {
        event.preventDefault();
        fetch(`https://api.openai.com/v1/chat/completions`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "messages": [
                    {"role": "system", "content": systemMessageContent},
                    {"role": "user", "content": questionInput}
                ],
            })
        })
        .then(response => response.json())
        .then(message => setAiResponse(message.choices[0].message.content))
    }

    function handleSave() {
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
                user_input: questionInput,
                ai_feedback: aiResponse
            })
        })
        console.log("saved")
    }

    return (
        <div className='question-container'>
            <h3>{question.question_text}</h3>

            <form className="question-form" onSubmit={event => handleSubmit(event)}>
                <textarea value={questionInput} onChange={event => setQuestionInput(event.target.value)}></textarea>
                <input type="submit" />
            </form>

            {aiResponse ? <div><p>{aiResponse}</p><button onClick={handleSave()}></button></div> : null}
        </div>
    )
}

export default Question;
