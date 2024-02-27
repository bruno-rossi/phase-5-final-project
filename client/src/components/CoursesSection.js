import CourseCard from "./CourseCard";

function CoursesSection({ title, courses }) {
    return (
        <div className="couses-section">
            <h1>{title}</h1>
            <div className="courses-container">
                {courses.map(course => {
                    return <CourseCard key={course.id} course={course} />
                })}
            </div>
        </div>
    )
}

export default CoursesSection;