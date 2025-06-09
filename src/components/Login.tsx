import React from "react"
import {useEffect, useState} from "react"
import * as Auth from "./../supabase/auth"

function LoginPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");

    const loginUser = () => {
        console.log("Well that's good innit??");
        // run the supabase authentication
    }

    return (
        <div>
            <h1>Input Username and Password</h1>

            <form> 
                <header>Username</header>
                <input type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <button type="submit" onClick={loginUser}>Login</button>
            </form>
        </div>
    )

}

export default function Login() {


    return (
        <div>
            <h1>Login!</h1>
            <LoginPanel />
        </div>
    )
}