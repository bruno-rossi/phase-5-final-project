import { useParams, useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";

function LessonPage() {

    const [ lesson, setLesson ] = useState({});

    const params = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/lessons/${params.lesson_id}`, {
            credentials: "include",
        })
        .then(response => { 
            
            if (response.ok) { 
                return response.json()
            } else if (response.status === 401) {
                navigate('/login');
            } else {
                navigate('/error');
            }
        })
        .then(lesson => setLesson(lesson))
    }, []);

    return (
        <div className="main">
            <button>Course</button>
            <h1>{lesson.title}</h1>
            <p>{lesson.content}</p>
            <button>Prev</button>
            <button>Next</button>
        </div>
    )
}

export default LessonPage;