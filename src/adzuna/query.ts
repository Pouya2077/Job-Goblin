import axios from "axios"
import * as Constants from "./constants"
// import dotenv from 'dotenv'
// dotenv.config()

const appID = process.env.ADZUNA_ID;
const apiKey = process.env.ADZUNA_KEY;
const apiUrl = 'http://api.adzuna.com/v1/api/jobs/ca/search/1?';

/** 
 * @param {number} num_results - number of fetched results
 * @param {string} job         - searched job 
 * @returns {AxiosPromise}    - JSON object of fetched jobs
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

