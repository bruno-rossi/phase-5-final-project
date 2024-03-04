
function CoursesSection({ id, title, children }) {
    return (
        <div id={id} className="courses-section">
            <h1>{title}</h1>
            {children}
        </div>
    )
}

export default CoursesSection;