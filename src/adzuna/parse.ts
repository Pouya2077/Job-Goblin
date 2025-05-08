import * as Query from "./query.js"
import "../supabase/connection.js"
import supabase from "../supabase/connection.js"
import { AxiosPromise, AxiosResponse } from "axios";

/**
 * @description callback function when query is successful, 
 *              expected that repsonse is NOT an error 
 * @param response - JSON object of returned jobs 
 */
export async function parseSimple(response: AxiosResponse<any>, num_jobs: number) {
    

    const {data, error} = await supabase
    .from("test_jobs")
    .insert({id: response.data.results[0].id, title: response.data.results[0].title});

    if (data) {
        console.log(data);
    } else {
        console.log(error);
    }

   
}

