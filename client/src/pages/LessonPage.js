import { useParams, useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import parse from 'html-react-parser';
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
            {lesson.course ? <div className="breadcrumbs"><p><Link to={`/courses/${lesson.course_id}`}><span>{lesson.course.title}</span></Link> / <span>{lesson.title}</span></p></div> : <h1>Loading...</h1>}
            
            <div className="content-container">
                <div className="lp left-side">
                    <h1>{lesson.title}</h1>
                    <LessonContent content={lesson.content}></LessonContent>
                </div>
                {/* <h2>{lesson.topic.topic_name}</h2> */}
                {/* <p>{lesson.content}</p> */}
                <div className="lp right-side">
                    {lesson.questions ? lesson.questions.map(question => {
                        return <Question key={question.id} question={question} lesson={lesson} />
                    }) : null}
                </div>
            </div>
            <div className="bottom-cta">
                {lesson.prev_lesson ? <button className="button-prev" onClick={() => navigate(`/lessons/${lesson.prev_lesson}`)}>Prev</button> : null}
                {lesson.next_lesson ? <button className="button-next" onClick={() => navigate(`/lessons/${lesson.next_lesson}`)}>Next</button> : null}
            </div>
        </div>
    )
}

export default LessonPage;