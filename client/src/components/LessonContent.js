import ClickableWord from "./ClickableWord";
import { v4 as uuidv4 } from 'uuid';


function LessonContent({ content }) {

    return (
        <div>
            {!content ? <h1>Loading...</h1> : <p>{content.split(/ /g).map(word => {
                
                return <ClickableWord key={uuidv4()} word={word}/>;
            })}</p> }
        </div>
    )
}

export default LessonContent;