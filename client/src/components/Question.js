import { useState, useEffect } from "react";
import parse from 'html-react-parser';
import apiKey from "../env";
import { useOutletContext } from "react-router-dom";

function Question({ question, lesson }) {

    const [ userQuestion, setUSerQuestion ] = useState({});
    const [ userInput, setUserInput ] = useState("");
    const [ aiResponse, setAiResponse] = useState("");

    const { user, setUser } = useOutletContext();
    
    console.log(question);

    const systemMessageContent = `You are a teacher of ${lesson.language.language_name}. You are reviewing your student's written texts in this language. When given an input, you will review the input in ${lesson.language.language_name} for grammar, spelling, and style. 
    
    Please respond with the corrected input in HTML inside <p> tags. Make sure to provide a new paragraph tag for each paragraph in the input! 
    
    Inside the p tag(s), find the mistakes and wrap them in a <span className="mistakes"> HTML tag. And then, in a new line, list the corrections you made under an HTML unordered list: "<ul><p>Corrections:</p></ul>". Please add a new line for each correction with its corresponding <li> tag. If there are no mistakes to correct, please respond with: "<p>Congratulations! Your response looks great!"</p>"`

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
        .then(message => {console.log(message); setAiResponse(message.choices[0].message.content)})
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


    return (
        <div className='question-container'>
            <form className="question-form" onSubmit={event => handleSubmit(event)}>
                <h3>{question.question_text}</h3>
                <textarea value={userInput} onChange={event => setUserInput(event.target.value)}></textarea>
                <input type="submit" value={"Get AI feedback"} />
            </form>

            {aiResponse ? <div className="ai-feedback">{parse(aiResponse)}<button onClick={handleSave}>Save</button></div> : null}
        </div>
    )
}

export default Question;
