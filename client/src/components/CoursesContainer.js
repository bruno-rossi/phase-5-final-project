import CourseCard from "./CourseCard";

function CoursesContainer({courses}) {
    return (
        <div className="courses-container">
            {courses.length !== 0 ? courses.map(course => {
                return <CourseCard key={course.id} course={course} />
            }) : <div><h1>No courses yet.</h1><p>It looks like there are no courses to display! Try adjusting the filters.</p></div>}
        </div>
    )
}

export default CoursesContainer;