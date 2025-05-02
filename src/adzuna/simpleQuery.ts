import axios from "axios"
import dotenv from 'dotenv'
dotenv.config();

const appID = process.env.ADZUNA_ID;
const apiKey = process.env.ADZUNA_KEY;
const apiUrl = 'http://api.adzuna.com/v1/api/jobs/ca/search/1?';

axios.get(apiUrl, {
    params: {
        app_id: appID, 
        app_key: apiKey,
    }

})
.then(response => {
    console.log(response.data);
    console.log("Status: ", response.data.status);
})
.catch(error => {
    console.log("Error! ", error.response.data);
    console.log(error.response.status);
    console.log(error.response.headers);
})