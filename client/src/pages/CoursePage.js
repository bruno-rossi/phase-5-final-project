import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

function CoursePage() {

    // fetch course details here.
    const [ course, setCourse ] = useState(null);
    const params = useParams();

    useEffect(() => {
        fetch(`http://127.0.0.1:5555/courses/${params.id}`)
        .then(response => response.json())
        .then(course => setCourse(course))
    }, [])

    console.log(course);

    return (
        <div className="main">
            {course ? 
            <>
                <button>Back</button>
                <h1>{course.title}</h1>
                <h2>{course.language.language_name}</h2>
                <p># of lessons: {course.lessons.length}</p>
                <button onClick={console.log("click!")}>Start course</button>
            </> :
            <h1>Loading...</h1>
            }
        </div>
    )
}

export default CoursePage;