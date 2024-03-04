import { Link } from "react-router-dom";

function LessonItem({ course, user_lesson }) {

    // console.log(user_lesson);

    return (
        <>
        {user_lesson['is_unlocked'] ? 
            <Link to={`/lessons/${user_lesson['lesson'].id}`}>
                <li className="lesson-item unlocked"><span className="book-emoji">📖</span>{user_lesson['lesson'].title}</li>
            </Link> : 
            <li className="lesson-item locked"><span className="lock-emoji">🔒</span> {user_lesson['lesson'].title}</li>
        }
        </>
        
    )
}

export default LessonItem;