import App from "./components/App";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Courses from "./pages/Courses";
import Profile from "./pages/Profile";
import CoursePage from "./pages/CoursePage";
import ErrorPage from "./pages/ErrorPage";
import LessonPage from "./pages/LessonPage";

const routes = [
    {
        path: '/',
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: '/',
                element: <Home />
            },
            {
                path: '/login',
                element: <Login />
            },
            {
                path: '/signup/',
                element: <Signup />
            },
            {
                path: '/courses/',
                element: <Courses />
            },
            {
                path: '/users/:user_id',
                element: <Profile />
            },
            {
                path: '/courses/:course_id',
                element: <CoursePage />
            },
            {
                path: 'lessons/:lesson_id',
                element: <LessonPage />
            }
        ]
    }
]

export default routes;
