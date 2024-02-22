import { Link } from "react-router-dom";

function LessonItem({ course, lesson }) {

    console.log(lesson);

    return (
        <Link to={`/lessons/${lesson.id}`}>
            <li className="lesson-item">{lesson.title}</li>
        </Link>
        
    )
}

export default LessonItem;