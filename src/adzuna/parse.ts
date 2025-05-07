import * as Query from "./query.js"

Query.simpleQuery(2, "software developer")
.then(response => {
    console.log(response.data.results[0].title);
    console.log(response.data.results[0].description);
})