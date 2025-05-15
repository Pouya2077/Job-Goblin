import "../supabase/connection.js"
import supabase from "../supabase/connection.js"
import { AxiosPromise, AxiosResponse } from "axios";

type Job = {
    id: string, 
    title: string,
    jsonb: any;
}

async function insertInTable(job: Job, table: string) {
    return supabase.from(table).insert({
        id: job.id,
        title: job.title, 
        raw_job: job,
    })
}

/**
 * @description callback function when query is successful, 
 *              expected that repsonse is NOT an error 
 * @param {AxiosResponse} response - JSON object of returned jobs 
 */
export async function simpleParse(response: AxiosResponse<any>) {
    const jobs = response.data.results as Job[];
    const insertPromises = jobs.map(job => insertInTable(job, "test_jobs"));


    const results = await Promise.all(insertPromises);

    results.forEach((result, index) => {
        if (result.error) {
            console.log("Error inserting job ", index, ":", result.error);
        } else {
            console.log("Success inserting job ", index, ".");
        }
    })

    }

    // const Jobs: Job[] = response.data.results as Job;
    // const insertPromises = response.data.results.map(response.data.results => supabase.from("test_jobs").insert(Job));

    // const results = await Promise.all(insertPromises);

    // results.forEach((result, index) => {
    //     if (result.error) {
    //         console.log("Error inserting job ", index, ":", result.error);
    //     } else {
    //         console.log("Success inserting job ", index, ".");
    //     }
    // })
    // }

    // response.data.results.forEach((value: AxiosResponse<any>) => {
    //     console.log(value);
    // })

    // const {data, error} = await supabase.from("test_jobs")
    // .insert({
    //     id: response.data.results[1].id, 
    //     title: response.data.results[1].title, 
    // })
    // if (data) {
    //     console.log("Successful Insert: ", data);
    // } else {
    //     console.log("Error Inserting: ", error);
    // }



