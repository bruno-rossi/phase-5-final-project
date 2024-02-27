import { useState, useEffect } from "react";
import { useOutletContext } from "react-router-dom";
import CoursesSection from "../components/CoursesSection";
import CoursesContainer from "../components/CoursesContainer";
import FiltersBar from "../components/FiltersBar";

function Courses() {

    const { user, setUser } = useOutletContext();
    const [ allCourses, setAllCourses ] = useState([]);
    const [ userCourses, setUserCourses ] = useState([]);
    const [ languages, setLanguages ] = useState([]);
    const [ topics, setTopics ] = useState([]);

    console.log(userCourses);
    
    useEffect(() => {
        fetch("http://127.0.0.1:5555/courses/", {
            credentials: "include",
        })
        .then(response => response.json())
        .then(allCourses => setAllCourses(allCourses))
    }, [])

    useEffect(() => {
        fetch("http://127.0.0.1:5555/languages/", {
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

    useEffect(() => {
        if (user) {
            fetch(`http://127.0.0.1:5555/users/${user.id}/courses/`, {
                credentials: "include",
            })
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(data => {
                console.log(data);
                setUserCourses(data);
            })
        }
    }, [user])

    // useEffect(() => {

    //         allCourses.forEach(course => {
    //             console.log(userCourses.includes(course))
    //         })
            
    // }, [userCourses])
    
    return (
        <div className="main">
            { user && userCourses ? 
            <>
                <CoursesSection title={"Keep learning"} >
                    <CoursesContainer courses={userCourses}></CoursesContainer>
                </CoursesSection>

                {/* <CoursesSection title={"Recommended for you"}>
                    <CoursesContainer courses={allCourses}></CoursesContainer>
                </CoursesSection> */}
            </>
            : null }
            
            <CoursesSection title={"All Courses"}>
                <FiltersBar languages={languages} topics={topics} setLanguages={setLanguages} setTopics={setTopics}></FiltersBar>
                <CoursesContainer courses={allCourses}></CoursesContainer>
            </CoursesSection>
        </div>
        
    )
}

export default Courses