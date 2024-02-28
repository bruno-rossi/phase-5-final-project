function ClickableWord({ word }) {

    function handleClick(event) {
        event.target.style.color = "red";
        console.log(event.target);
    }

    return (
        <span onClick={event => handleClick(event)}>{word}<span> </span></span> 
    )
}

export default ClickableWord;