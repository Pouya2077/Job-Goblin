import * as Query from "./query.js"

Query.simpleQuery(11, "software developer")
.then(response => {
    console.log(response.data.status);
    console.log(response.data)
})