import { useParams, useNavigate, Link } from "react-router-dom";
import { useEffect, useState } from "react";
import Question from "../components/Question";
import LessonContent from "../components/LessonContent";

function LessonPage() {

    const [ lesson, setLesson ] = useState({});
    const [ userCourse, setUserCourse ] = useState(null); 
    const [ userLesson, setUserLesson ] = useState(null); 
    const [ nextLesson, setNextLesson ] = useState(null);
    
    console.log(nextLesson);

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
    }, [params.lesson_id]);

    useEffect(() => {

        if (lesson.course_id) {
            fetch(`http://127.0.0.1:5555/courses/${lesson.course_id}/registration/`, {
                credentials: 'include'
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(data => {console.log(data); setUserCourse(data)})
        }

    }, [lesson]);

    useEffect(() => {
        if (userCourse) {
            fetch(`http://127.0.0.1:5555/user-courses/${userCourse.id}/user-lessons/${params.lesson_id}/`, {
                credentials: 'include'
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(data => { console.log(data); setUserLesson(data);})
        }
    }, [userCourse])

    useEffect(() => {
        if (userCourse && lesson.next_lesson) {
            fetch(`http://127.0.0.1:5555/user-courses/${userCourse.id}/user-lessons/${lesson.next_lesson}/`, {
                credentials: 'include'
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(data => { if (data.is_unlocked) {setNextLesson(data.lesson_id); console.log(data.is_unlocked)}})
        }
    }, [userLesson])

    function unlockNext() {
        fetch(`http://127.0.0.1:5555/user-courses/${userCourse.id}/user-lessons/${userLesson.lesson.next_lesson}/`, {
            method: 'PATCH',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                is_unlocked: 1
            })
        })
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => { setNextLesson(data.lesson_id)})
    }

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
                        return <Question key={question.id} question={question} lesson={lesson} unlockNext={unlockNext} />
                    }) : null}
                </div>
            </div>
            <div className="bottom-cta">
                {lesson.prev_lesson ? <button className="button-prev" onClick={() => navigate(`/lessons/${lesson.prev_lesson}`)}>Prev</button> : null}
                {nextLesson ? <button className="button-next" onClick={() => {setNextLesson(null); navigate(`/lessons/${lesson.next_lesson}`)}}>Next</button> : null}
            </div>
        </div>
    )
}

export default LessonPage;