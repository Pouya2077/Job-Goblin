import React from "react"
import {useState} from "react"
import * as Auth from "./../supabase/auth"

function SignUpPanel() {
    const [inputEmail, setInputEmail] = useState("");
    const [inputPassword, setInputPassword] = useState("");
    const [inputName, setInputName] = useState("");

    const signUpUser = async () => {
        const {data, error} = await Auth.signUpWithPassword(inputEmail, inputPassword, inputName);

        if (error) {
            console.log("Error ", error.name, ": ", error.code, " when signing up.");
        }

        if (data) {
            console.log("Successful Sign-Up!");
        }
    }

    return (
        <div>
            <h1>Input Username, Password, and Name</h1>
            <form>
                <input required type="text" onChange={(event) => {setInputEmail(event.target.value)}}/>
                <input required type="password" onChange={(event) => {setInputPassword(event.target.value)}}/>
                <input required type="text" onChange={(event) => {setInputName(event.target.value)}}/>
                <button type="submit" onClick={signUpUser}>SignUp</button>
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