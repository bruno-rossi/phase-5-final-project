import { useEffect } from "react";

function FiltersBar({ languages, topics, setLanguages, setTopics}) {

    
    return (
        <div className="filters-container">
                    {/* <h1>Filter by:</h1> */}
                    <select>
                        <option>Language</option>
                        {languages.length == 0 ? null : languages.map(language => {
                            return <option key={language.id} value={language.id}>{language.language_name}</option>
                        })}
                    </select>
                    <select id="topic" onChange={event => console.log(event)}>
                        <option>Topic</option>
                        {topics.length == 0 ? null : topics.map(topic => {
                            return <option key={topic.id} value={topic.id}>{topic.topic_name}</option>
                        })}
                    </select>
                    <input type="text" placeholder="Search for a course..."></input>
            </div>
    )
}

export default FiltersBar;