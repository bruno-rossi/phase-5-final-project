import { Link } from "react-router-dom";

function LessonItem({ course, user_lesson }) {

    // console.log(user_lesson);

    return (
        <>
        {user_lesson['is_unlocked'] ? 
            <Link to={`/lessons/${user_lesson['lesson'].id}`}>
                <li className="lesson-item-unlocked">{user_lesson['lesson'].title}</li>
            </Link> : 
            <li className="lesson-item-locked">{user_lesson['lesson'].title}</li>
        }
        </>
        
    )
}

export default LessonItem;