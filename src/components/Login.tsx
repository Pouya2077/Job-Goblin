import React from "react"
import {useEffect, useState} from "react"
import * as Auth from "./../supabase/auth"

function LoginPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const [message, setMessage] = useState("");

    const loginUser = async (event: any) => {
        event.preventDefault();
        const {data, error} = await Auth.signInWithPassword(inputEmail, inputPassword); 
        
        if (error) {
            console.log("Error ", error.name, ": ", error.code, " when logging in.");
            console.log(error.message);
        } else if (data) {
            console.log("Successful login.");
            setMessage("Successful Login!");
        }

    }

    return (
        <div>
            <h1>Input Username and Password</h1>
            <form onSubmit={loginUser}> 
                <input required type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input required type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <button type="submit">Login</button>
            </form>
            <title>{message}</title>
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