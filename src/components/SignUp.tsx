import React from "react"
import {useState} from "react"
import * as Auth from "./../supabase/auth"
import {useNavigate} from "react-router-dom"

function SignUpPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const [inputName, setInputName] = useState("");
    const navigate = useNavigate();

    const signUpUser = async (event: any) => {
        event.preventDefault(); //prevent page refresh
        const {data, error} = await Auth.signUpWithPassword(inputEmail, inputPassword, inputName);

        if (error) {
            console.log("Error ", error.name, ": ", error.code, " when signing up.");
            console.log(error.message);
        } else if (data) {
            console.log("Successful Sign-Up!");
            alert("SignUp Successful!");
            navigate("/dashboard")
        }
    }

    return (
        <div>
            <h1>Input Email, Password, and Username</h1>
            <form onSubmit={signUpUser}>
                <input required type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input required type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <input required type="text" onChange={(event) => {setInputName(event.target.value)}}/>
                <button type="submit">SignUp</button>
            </form>
        </div>
    )
}

export default function SignUp() {
    return (
        <div>
            <h1>SignUp!</h1>
            <SignUpPanel/>
        </div>
    )
}