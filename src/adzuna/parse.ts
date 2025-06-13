import "../supabase/connection"
import supabase from "../supabase/connection"
import { AxiosPromise, AxiosResponse } from "axios"
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
        user_email: job.user_email, 
        min_salary: job.min_salary, 
        company: job.company, 
        location: job.location,
        description: job.description
    })
}

/**
 * @description  convert Adzuna responses to explicit Job type
 * @param result Adzuna job posting 
 * @returns      Promise that is Job type
 */
async function convertToJob(result: any): Promise<Job> {
    const {data, error} = await supabase.auth.getUser();

    if (error || data.user.email == null) {
        throw Error("User possible not signed in!");
    }

    return {
        id: result.id, 
        title: result.title, 
        jsonb: result, 
        user_email: data.user.email, 
        min_salary: result.salary_min, 
        company: result.company.display_name, 
        location: result.location.area,
        description: result.description,
    }

}

/**
 * @description callback function when query is successful, 
 *              expected that repsonse is NOT an error 
 * @param {AxiosResponse} response - JSON object of returned jobs 
 */
export async function simpleParse(response: AxiosResponse<any>) {
    const jobPromises = response.data.results.map((result: any) => convertToJob(result)); //convert to job type
    const jobs = await Promise.all(jobPromises); //throws error if any job rejected

    const insertPromises = jobs.map((job: any) => insertInTable(job, "test_jobs")); //try inserting each 
    const insertResults = await Promise.all(insertPromises);

    insertResults.forEach((result, index) => { //see if inserts were successful
        if (result.error) {
            console.log("Error inserting job ", index, ":", result.error);
        } else {
            console.log("Success inserting job ", index);
        }
    })

    }

    



