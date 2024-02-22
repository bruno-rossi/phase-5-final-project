import { useNavigate } from "react-router-dom"

function ErrorPage() {

    const navigate = useNavigate();
    
    return (
        <div className="main">
            <h1>Error</h1>
            <p>It looks like something went wrong.</p>
            <button onClick={() => navigate(-1)} value="Back"></button>
        </div>
    )
}

export default ErrorPage