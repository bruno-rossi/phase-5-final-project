import { Link } from "react-router-dom";

function CourseCard({ course }) {

    // console.log(course);

    return (
        <>{course ? (
                <Link to={`/courses/${course.id}`}>
                    <div className="course-card">
                        <div className="card-img-div">
                            <img src={course.image}></img>
                        </div>
                        <h5>{course.language.language_name}</h5>
                        <h1>{course.title}</h1>
                        <p># of lessons: {course.lessons.length}</p>
                    </div>
                </Link>
        ) : null}
        </>
        
    )
}

export default CourseCard