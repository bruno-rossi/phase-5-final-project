import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import LessonItem from "../components/LessonItem";

function CoursePage() {

    // fetch course details here.
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

    console.log(course);

    return (
        <div className="main">
            {course ? 
            <>
                <button onClick={() => navigate(-1)}>Back</button>
                <h1>{course.title}</h1>
                <h2>{course.language.language_name}</h2>
                <p># of lessons: {course.lessons.length}</p>
                <ol>
                    {course.lessons.map(lesson => {
                        return <LessonItem key={lesson.id} lesson={lesson}></LessonItem>
                    })}
                </ol>
                <button onClick={console.log("click!")}>Start course</button>
            </> :
            <h1>Loading...</h1>
            }
        </div>
    )
}

export default CoursePage;