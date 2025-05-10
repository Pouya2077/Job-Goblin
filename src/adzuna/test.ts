import * as Query from "./query.js"
import * as Parse from "./parse.js"
import * as Auth from "../supabase/auth.js"
import dotenv from "dotenv"
dotenv.config();

let data, error;

({data, error} = await Auth.signUpWithPassword((process.env.EMAIL as string), (process.env.PASS as string), "John Doe"))

if (data) {
    console.log("Successful Auth ", data);
} else {
    console.log("Error: ", error);
}

({data, error} = await Auth.signInWithPassword((process.env.EMAIL as string), (process.env.PASS as string)))

if (data) {
    console.log("Successful SignIn ", data);
} else {
    console.log("Error Signing In: ", error);
}

Query.simpleQuery(11, "software Developer")
.then(response => {
    Parse.parseSimple(response);
})
.catch(error => {
    console.log("Error: ", error.data);
})

