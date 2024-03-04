import { useState, useEffect } from "react";
import { useParams, useNavigate, useOutletContext } from "react-router-dom";
import LessonItem from "../components/LessonItem";

function CoursePage() {

    // fetch course details here.
    // 3 use cases:
    // 1) No user - all lessons locked
    // 2) User - not registered, all lessons locked
    // 3) User registered, lessons locked or unlocked 
    const { user, setUser } = useOutletContext();
    const [ course, setCourse ] = useState(null);
    const [ userCourse, setUserCourse ] = useState(null);
    const params = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/courses/${params.course_id}`, {
            credentials: "include",
        })
        .then(response => { 
            if (response.ok) { 
                return response.json()
            } else {
                navigate('/error')
            }
        })
        .then(course => setCourse(course))
    }, [])

    useEffect(() => {

        if (user && course) {
            fetch(`http://127.0.0.1:5555/courses/${course.id}/registration/`, {
                credentials: 'include'
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(registration => {
                setUserCourse(registration);
            })
        }

    }, [user, course])

    function createCourseRegistration() {

        if (user) {
            fetch(`http://127.0.0.1:5555/courses/${course.id}/registration/`, {
                method: 'POST',
                credentials: 'include',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: user.id,
                    course_id: course.id
                })
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(new_registration => {
                setUserCourse(new_registration);
                navigate(`/lessons/${course.lessons[0].id}`)
            })
        }
    }

    function buildPage(course, userCourse) {

        if (!course) {
            return <h1>Loading...</h1>;
        }
        else if (course && !userCourse) {
            return <>
                <div className="cp left-side">
                    <h1>{course.title}</h1>
                    <div className="cp-img-div"><img src={course.image}/></div>
                    <h5>{course.language.language_name} · {course.topic.topic_name}</h5>
                    <p>{course.description}</p>
                </div>
                <div className="cp right-side">
                    <h1>Lessons: {course.lessons.length}</h1>
                    <ul className="lessons-list">
                        {course.lessons.map(lesson => {
                            return <li key={lesson.id} className="lesson-item locked"><span className="lock-emoji">🔒</span>{lesson.title}</li>
                        })}
                    </ul>
                </div>
                </>
        } else if (userCourse) {
            return <>
                    <div className="cp left-side">
                        <h1>{course.title}</h1>
                        <div className="cp-img-div"><img src={course.image}/></div>
                        <h5>{course.language.language_name} · {course.topic.topic_name}</h5>
                        <p>{course.description}</p>
                    </div>
                    <div className="cp right-side">
                        <h1>Lessons: {course.lessons.length}</h1>
                        <ul className="lessons-list">
                            {userCourse.user_lessons.map(user_lesson => {
                                console.log(user_lesson);
                                return <LessonItem key={user_lesson['lesson'].id} user_lesson={user_lesson}></LessonItem>
                            })}
                        </ul>
                    </div>
                    
                </>
        }
    }

    return (
        <div className="main">
            <div className="breadcrumbs">
                <button className="back-button" onClick={() => navigate(-1)}>Back</button>
            </div>
            <div className="content-container">
                {buildPage(course, userCourse)}
            </div>
            <div className="bottom-cta">
                <button onClick={() => {!user ? navigate('/login') : createCourseRegistration()}}>{userCourse ? "Keep learning" : "Start course"}</button>
            </div>
        </div>
    )
}

export default CoursePage;