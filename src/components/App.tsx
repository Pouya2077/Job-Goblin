import * as Query from '../adzuna/query'
import * as Parse from '../adzuna/parse'
import * as Auth from '../supabase/auth'
import React, {useState, useEffect} from 'react'
import {Job} from "../types"


export default function App() {
    const [result, newResult] = useState<Job | null>(null);
    let job: Job

    useEffect(() => {
        Query.simpleQuery(10, "software developer")
        .then(response => {
            job = response.data.results[0];
            newResult(job);
        })
        .catch(error => {
            console.log("Fetched data is corrupted: ", error.data.error);
        })
        
    }, []);
    
    if (!result) {
        return (
            <div>
                <header>
                    <h1>Loading...</h1>
                </header>
            </div>
        )
    }

    return (
        <div>
            <header>
                <h1>
                    By Pouya Khoshnavazi
                    <p>{result.title}</p>
                </h1>
            </header>
        </div>
    )

}


