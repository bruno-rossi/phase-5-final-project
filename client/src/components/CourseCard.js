import { Link } from "react-router-dom";

function CourseCard({ course }) {

    console.log(course)

    return (
        <Link to={`/courses/${course.id}`}>
            <div className="course-card">
                <h1>{course.title}</h1>
                <h2>{course.language.language_name}</h2>
                <p># of lessons: {course.lessons.length}</p>
            </div>
        </Link>
    )
}

export default CourseCard