import React from "react"
import {useState} from "react"
import * as Query from "../adzuna/query"
import * as Parse from "../adzuna/parse"

function AdzunaQuery(num: number, name: string) {
    event?.preventDefault();

    Query.simpleQuery(num, name)
    .then((response) => {
        Parse.simpleParse(response);

        console.log("Successful Simple Query!");
        console.log("Headers: ", response.headers);
        console.log("Status: ", response.status);
        alert("Successful Query!");
    })
    .catch((error) => {
        console.log("Query Error!");
        console.log("Error Code: ", error.code);
        console.log("Error Headers: ", error.headers);
        console.log("Error Message: ", error.message);
    });
}

export default function Adzuna() {
    const [numJobs, setNumJobs] = useState<number>(0);
    const [jobName, setJobName] = useState<string>("");

    return (
        <div>
            <form onSubmit={() => {AdzunaQuery(numJobs, jobName)}}>
                <input required type="number" onChange={(event) => {setNumJobs(parseFloat(event.target.value))}}/>
                <input required type="text" onChange={(event) => {setJobName(event.target.value)}}/>
                <button type="submit">Submit Query</button>
            </form>
        </div>
    )
}