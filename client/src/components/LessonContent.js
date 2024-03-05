import parse from 'html-react-parser';
import { v4 as uuidv4 } from 'uuid';


function LessonContent({ content }) {

    return (
        <div>
            {!content ? <h1>Loading...</h1> : <div id='lesson-content-text'>{parse(content)}</div> }
        </div>
    )
}

export default LessonContent;