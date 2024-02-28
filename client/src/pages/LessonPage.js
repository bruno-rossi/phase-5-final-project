import { useParams, useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import Question from "../components/Question";
import LessonContent from "../components/LessonContent";

function LessonPage() {

    const [ lesson, setLesson ] = useState({});
    console.log(lesson)

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
    }, [params]);

    return (
        <div className="main">
            <div><p><Link to={`/courses/${lesson.course_id}`}>{lesson.course_id}</Link> - {lesson.title}</p></div>
            <button>Course</button>
            <h1>{lesson.title}</h1>
            {/* <h2>{lesson.topic.topic_name}</h2> */}
            {/* <p>{lesson.content}</p> */}
            <LessonContent content={lesson.content}></LessonContent>
            {lesson.questions ? lesson.questions.map(question => {
                return <Question key={question.id} question={question} lesson={lesson} />
            }) : null}
            {lesson.prev_lesson ? <button onClick={() => navigate(`/lessons/${lesson.prev_lesson}`)}>Prev</button> : null}
            {lesson.next_lesson ? <button onClick={() => navigate(`/lessons/${lesson.next_lesson}`)}>Next</button> : null}
        </div>
    )
}

export default LessonPage;