import { useState, useEffect } from "react";
import CourseCard from "../components/CourseCard";
import CoursesSection from "../components/CoursesSection";

function Courses() {

    const [ courses, setCourses ] = useState([]);
    const [ languages, setLanguages ] = useState([]);
    const [ topics, setTopics ] = useState([]);


    useEffect(() => {
        fetch("http://127.0.0.1:5555/courses", {
            credentials: "include",
        })
        .then(response => response.json())
        .then(courses => setCourses(courses))
    }, [])

    useEffect(() => {
        fetch("http://127.0.0.1:5555/languages", {
            credentials: "include",
        })
        .then(response => response.json())
        .then(languages => setLanguages(languages))
    }, [])
    
    useEffect(() => {
        fetch("http://127.0.0.1:5555/topics/", {
            credentials: "include",
        })
        .then(response => response.json())
        .then(topics => setTopics(topics))
    }, [])

    return (
        <div className="main">
            <CoursesSection title={"Keep learning"} courses={courses} />
            <CoursesSection title={"Recommended for you"} courses={courses} />
            <div className="filters-container">
                    {/* <h1>Filter by:</h1> */}
                    <select>
                        <option>Language</option>
                        {languages.map(language => {
                            return <option key={language.id} value={language.id}>{language.language_name}</option>
                        })}
                    </select>
                    <select id="topic" onChange={event => console.log(event)}>
                        <option>Topic</option>
                        {topics.map(topic => {
                            return <option key={topic.id} value={topic.id}>{topic.topic_name}</option>
                        })}
                    </select>
                    <input type="text" placeholder="Search for a course..."></input>
                </div>
            <CoursesSection title={"All Courses"} courses={courses} />

            <h1>All Courses</h1>
            <div className="filters-container">
                {/* <h1>Filter by:</h1> */}
                <select>
                    <option>Language</option>
                    {languages.map(language => {
                        return <option key={language.id} value={language.id}>{language.language_name}</option>
                    })}
                </select>
                <select id="topic" onChange={event => console.log(event)}>
                    <option>Topic</option>
                    {topics.map(topic => {
                        return <option key={topic.id} value={topic.id}>{topic.topic_name}</option>
                    })}
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