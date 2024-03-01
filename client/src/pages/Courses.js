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
    const [ languageFilter, setLanguageFilter ] = useState("");
    const [ topicFilter, setTopicFilter ] = useState("");
    const [ filteredCourses, setFilteredCourses ] = useState([]);
    const [ isFiltered, setIsFiltered ] = useState(false);
    
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
                // console.log(data);
                setUserCourses(data);
            })
        }
    }, [user])

    function filterByLanguage(courses) {
        const filteredArray = courses.filter(course => (course.language.language_name === languageFilter))
        setFilteredCourses(filteredArray);
        return filteredArray;
    }

    function filterByTopic(courses) {
        const filteredArray = courses.filter(course => (course.topic.topic_name === topicFilter))
        setFilteredCourses(filteredArray);
        return filteredArray;
    }

    useEffect(() => {
        if (languageFilter === "" && topicFilter === "") {
            setFilteredCourses(allCourses);
        } else if (languageFilter !== "" && topicFilter === "") {
            filterByLanguage(allCourses);
        } else if (languageFilter === "" && topicFilter !== "") {
            filterByTopic(allCourses);
        } else if (languageFilter !== "" && topicFilter !== "") {
            filterByLanguage(filterByTopic(allCourses));
        }

    }, [languageFilter, topicFilter, allCourses])

    // useEffect(() => {
    //     if (topicFilter === "") {
    //         setFilteredCourses(allCourses);
    //     } else {
    //         const filteredArray = allCourses.filter(course => (course.language.language_name === languageFilter))
    //         setFilteredCourses(filteredArray);
    //     }
    // }, [languageFilter, allCourses])
    
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
                <FiltersBar languages={languages} topics={topics} setLanguageFilter={setLanguageFilter} setTopicFilter={setTopicFilter} ></FiltersBar>
                <CoursesContainer courses={filteredCourses}></CoursesContainer>
            </CoursesSection>
        </div>
        
    )
}

export default Courses