import axios from "axios"
import dotenv from 'dotenv'
import * as Constants from "./constants.js"

dotenv.config();

const appID = process.env.ADZUNA_ID;
const apiKey = process.env.ADZUNA_KEY;
const apiUrl = 'http://api.adzuna.com/v1/api/jobs/ca/search/1?';

/** 
 * @params number of jobs requests (max is MAX_RESULTS) and type of job 
 * @return promise: JSON job object or error 
 */
export async function simpleQuery(num_results: number, job: string) {
    return axios.get(apiUrl, {
        params: {
            app_id: appID, 
            app_key: apiKey, 
            results_per_page: num_results > Constants.MAX_RESULTS ? Constants.MAX_RESULTS : num_results, 
            what: job,
        }
    });
    
}

// axios.get(apiUrl, {
//     params: {
//         app_id: appID, 
//         app_key: apiKey,
//         results_per_page: 3, 
//         what: "software developer", 
//     }

// })
// .then(response => {
//     console.log(response.data);
//     console.log("Status: ", response.data.status);
// })
// .catch(error => {
//     console.log("Error! ", error.response.data);
//     console.log(error.response.status);
//     console.log(error.response.headers);
// })