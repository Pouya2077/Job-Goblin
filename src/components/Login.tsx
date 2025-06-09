import React from "react"
import {useNavigate} from "react-router-dom"
import {useEffect, useState} from "react"
import * as Auth from "./../supabase/auth"

function LoginPanel() {
    let navigate = useNavigate();
    let email: string;
    let password: string;
    const [inputValue, setInputValue] = useState("");

    const inputChanged = (event: any) => {
        if (event.target.value != "") {
            setInputValue(event.target.value);
        }
    }

    useEffect(() => {
        if (inputValue != "") {
            navigate("/signup");
        }
    }, [inputValue]);

    return (
        <div>
            <h1>Username</h1>
            <input type="text" value={inputValue} onChange={inputChanged} />

            <h2>Password</h2>
            <input type="password" />
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