Job Goblin 
==========

> **Find jobs without a single click!**
>
> Job Goblin **routinely fetches jobs** from third party REST APIs for you. Enter your job preferences and let **Job Goblin find your dream job!** 

**Configurable Settings**
- Fetching schedule 
- Search parameters
- Database maintenance parameters 
- Emailing parameters

Parameters include: api name, job title, company, location, and number of jobs. 

Job Goblin relies on free APIs and web services (such as Supabase) to fetch and store jobs properly. Keys and URL endpoints must be aquired for Job Goblin to work. For email functionality, Job Goblin needs access to a gmail account and app password provided by the user.

### Setup
1. Clone the repository to your local device.
2. To install dependencies: pip install -r requirements.txt
3. To install the packages of the project: pip install -e .

**User Stories**
1. "I want the program to routinely query jobs on a schedule I give it."
2. "I want the program to query jobs using search parameters I give it (name, company, etc.)."
3. "I want to be emailed about jobs the program found for me."
4. "I want jobs the program queried to be stored for me to look at later."

**Developer Stories**
1. "I want to improve my Python programming skills that includes syntax and mastering built-in, standard functions."
2. "I want to use an OOD to improve my OOP skills and make encapsulated, maintainable code."
3. "I want to build something that is practical for daily use."
4. "I want to learn how to run scripts remotely using GitHub Actions or other services."
5. "I want to learn basics of how APIs work, how to use them, and why they are useful."

This project is meant for a single user, not meant for production. If someone wants to use it they can host it locally or remotely with a few minor script tweaks.

Development will be iterative with modularized stages of development. This ensures that individual components can work somewhat independently of each other so that parts of the program are usable before the entire thing is finished. 