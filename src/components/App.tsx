import React from "react"
import {Routes, Route} from "react-router-dom"
import Login from "./Login"
import SignUp from "./SignUp"
import Home from "./Home"

export default function App() {

    return (
        <Routes>
            <Route path="/" element={<Home></Home>} />
            <Route path="/login" element={<Login></Login>} />
            <Route path="/signup" element={<SignUp></SignUp>} />
        </Routes>
    )

}


