import * as Query from '../adzuna/query'
import * as Parse from '../adzuna/parse'
import * as Auth from '../supabase/auth'
import React, {useState, useEffect} from 'react'
import { AxiosPromise, AxiosResponse } from "axios"

export default function App() {
    const [result, newResult] = useState(null);

    useEffect(() => {
        Query.simpleQuery(10, "software developer")
        .then(response => {
            newResult(response.data.results[0].title);
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
                    <p>{result}</p>
                </h1>
            </header>
        </div>
    )

}


