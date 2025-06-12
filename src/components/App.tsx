import React from "react"
import {Routes, Route} from "react-router-dom"
import Login from "./Login"
import SignUp from "./SignUp"
import Home from "./Home"
import Dashboard from "./Dashboard"

export default function App() {

    return (
        <Routes>
            <Route path="/" element={<Home/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/signup" element={<SignUp/>} />
            <Route path="/dashboard" element={<Dashboard/>}/>
        </Routes>
    )

}


