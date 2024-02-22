import { useState, useEffect } from "react";
import CourseCard from "../components/CourseCard";

function Courses() {

    const [ courses, setCourses ] = useState([])

    useEffect(() => {
        fetch("http://127.0.0.1:5555/courses", {
            credentials: "include",
        })
        .then(response => response.json())
        .then(courses => setCourses(courses))
    }, [])

    return (
        <div className="main">
            <h1>Courses</h1>
            <div className="filters-container">
                {/* <h1>Filter by:</h1> */}
                <select>
                    <option>Language</option>
                </select>
                <select>
                    <option>Topic</option>
                </select>
                <input type="text" placeholder="Search for a course..."></input>
            </div>
            <div className="courses-container">{
                courses.length !== 0 ? courses.map(course => {
                    return <CourseCard key={course.id} course={course}>{course.title}</CourseCard>
                }) : <div><h1>No courses yet.</h1><p>It looks like there are no courses to display! Try adjusting the filters.</p></div>
            }</div>
        </div>
        
    )
}

export default Courses