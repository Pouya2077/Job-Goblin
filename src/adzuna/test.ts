import * as Query from "./query.js"
import * as Parse from "./parse.js"

Query.simpleQuery(11, "software Developer")
// .then(response => {
//     console.log(response.data.status);
//     console.log(response.data);
//     //console.log(response.data.isRawJSON());
// })
// .catch(response => {
//     console.log(response.data.status);
//     console.log(response.data.headers);
//     console.log(response.data)
// })

.then(response => {
    // console.log(JSON.parse(JSON.stringify(response.data)));
    // console.log(response.data.results[0].title);
    // console.log(response.data.results[0].salary_min);
    // console.log(response.data.results[0].location);
    // //console.log(response.data.results[12].title);

    Parse.parseSimple(response, 11);
})

