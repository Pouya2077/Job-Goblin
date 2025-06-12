import React from "react"
import {useState} from "react"
import * as Auth from "./../supabase/auth"
import {useNavigate} from "react-router-dom"

function LoginPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const navigate = useNavigate();

    const loginUser = async (event: any) => {
        event.preventDefault(); //prevent page refresh
        const {data, error} = await Auth.signInWithPassword(inputEmail, inputPassword); 
        
        if (error) {
            console.log("Error ", error.name, ": ", error.code, " when logging in.");
            console.log(error.message);
        } else if (data) {
            console.log("Successful login.");
            alert("Login Successful!");
            navigate("/dashboard");
        }

    }

    return (
        <div>
            <h1>Input Email and Password</h1>
            <form onSubmit={loginUser}> 
                <input required type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input required type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <button type="submit">Login</button>
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