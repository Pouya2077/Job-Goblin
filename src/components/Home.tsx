import React from "react"
import {useNavigate} from "react-router-dom"

export default function Home() {
    const navigate = useNavigate();

    return (
        <div>
            <header>
                <h1>
                    Welcome to Job Goblin!
                </h1>
                <div>
                    <button onClick={() => {navigate("/login")}}>Login</button>
                    <button onClick={() => {navigate("/signup")}}>SignUp</button>
                </div>
            </header>
        </div>
    )
}