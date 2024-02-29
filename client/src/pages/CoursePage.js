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

    // useEffect(() => {
    //     if (user) {
    //         fetch(`http://127.0.0.1:5555/courses/<int:course_id>/registration/`, {
    //             credentials: 'include'
    //         })
    //         .then(response => {
    //             if (response.ok){
    //                 return response.json()
    //             }
    //         })
    //         .then(registration => {
    //             console.log(registration);
    //             navigate(`/lessons/${course.lessons[0].id}`)
    //         })
    //     }

    // }, [user])

    function createCourseRegistration() {
        return
    }

    return (
        <div className="main">
            {course ? 
            <>
                <button onClick={() => navigate(-1)}>Back</button>
                <h1>{course.title}</h1>
                <h2>{course.language.language_name}</h2>
                <h2>{course.topic.topic_name}</h2>
                <p># of lessons: {course.lessons.length}</p>
                <ol>
                    {course.lessons.map(lesson => {
                        return <LessonItem key={lesson.id} lesson={lesson}></LessonItem>
                    })}
                </ol>
                <button onClick={() => navigate(`/lessons/${course.lessons[0].id}`)}>Start course</button>
            </> :
            <h1>Loading...</h1>
            }
        </div>
    )
}

export default CoursePage;