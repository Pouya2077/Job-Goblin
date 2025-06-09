import React from "react"
import {useEffect, useState} from "react"
import * as Auth from "./../supabase/auth"

function LoginPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");

    const loginUser = () => {
        Auth.signInWithPassword(inputEmail, inputPassword); //Auth will handle exceptions
    }

    return (
        <div>
            <h1>Input Username and Password</h1>
            <form> 
                <input required type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input required type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <button type="submit" onSubmit={loginUser}>Login</button>
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