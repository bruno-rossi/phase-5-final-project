function CourseCard({ course }) {

    console.log(course)

    return (
        <div className="course-card">
            <h1>{course.title}</h1>
            <h2>{course.language.language_name}</h2>
            <p># of lessons: {course.lessons.length}</p>
        </div>
    )
}

export default CourseCard