import App from "./components/App";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";

const routes = [
    {
        path: '/',
        element: <App />,
        // errorElement: <ErrorPage />,
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
            }
        ]
    }
]

export default routes;
