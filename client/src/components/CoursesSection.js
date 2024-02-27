
function CoursesSection({ title, children }) {
    return (
        <div className="courses-section">
            <h1>{title}</h1>
            {children}
        </div>
    )
}

export default CoursesSection;