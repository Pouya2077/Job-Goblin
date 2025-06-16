# **IN PROGRESS**

## **Job Goblin**

Interface that routinely queries jobs from third-party REST APIs. Currently, only supports Adzuna, but will be extended to other job sights in the future. 

-  Requires Supabase backend to provide URL and KEY for code to use. Supabase is a free open-source Firebase alternative. 
-  Requires Adzuna API key and ID which is available with the free tier. 

# Installation 

1. Clone repository: git clone <repo-url>
2. Install dependencies: npm install
3. Run project: npm start

webpack.config.js and tsconfig.json can be configured to suit user needs. Querying and parsing files can be changed to suit user needs or for experimentation. 

Authentication is present. Schema and RLS policies of Supabase must be managed by user. 

This project was created with [Create New App](https://github.com/qodesmith/create-new-app).
