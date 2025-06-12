import "../supabase/connection"
import supabase from "../supabase/connection"
import { AxiosPromise, AxiosResponse } from "axios";
import {Job} from "../types"

/**
 * @description function inserts Job type into Supabase
 * @param job   of Job type
 * @param table name of table to insert into 
 * @returns     Supabase response for insert 
 */
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
    if (response.data.error) {
        console.log("Error with recieved AxiosResponse: ", response.data.error);
        console.log(response.data.error.message);
    }

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

    



