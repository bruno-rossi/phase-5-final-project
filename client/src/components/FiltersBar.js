import { useEffect } from "react";

function FiltersBar({ languages, topics, setLanguageFilter, setTopicFilter}) {

    
    return (
        <div className="filters-container">
                    <select id="language-filter" onChange={event => setLanguageFilter(event.target.value)}>
                        <option value="">Language</option>
                        {languages.length == 0 ? null : languages.map(language => {
                            return <option key={language.id} value={language.language_name}>{language.language_name}</option>
                        })}
                    </select>
                    <select id="topic-filter" onChange={event => setTopicFilter(event.target.value)}>
                        <option value="">Topic</option>
                        {topics.length == 0 ? null : topics.map(topic => {
                            return <option key={topic.id} value={topic.topic_name}>{topic.topic_name}</option>
                        })}
                    </select>
            </div>
    )
}

export default FiltersBar;