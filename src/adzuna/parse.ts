import "../supabase/connection.js"
import supabase from "../supabase/connection.js"
import { AxiosPromise, AxiosResponse } from "axios";

/**
 * @description callback function when query is successful, 
 *              expected that repsonse is NOT an error 
 * @param response - JSON object of returned jobs 
 * @param num_jobs - Number of fetched jobs
 */
export async function parseSimple(response: AxiosResponse<any>, num_jobs: number) {
    const {data, error} = await supabase.from("test_jobs")
    .insert({
        id: response.data.results[1].id, 
        title: response.data.results[1].title, 
    })
    if (data) {
        console.log("Successful Insert: ", data);
    } else {
        console.log("Error Inserting: ", error);
    }

    // TODO: make sure that number adheres to the MAX constant
   
}

