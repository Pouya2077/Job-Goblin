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

---------
### Setup 

1. Create a GitHub copy of the repository
    - Option 1: Fork original repo
    - Option 2: Import original repo
    - Option 3: clone original repo and push it to GitHub
2. Open repository (connected to your GitHub clone) in your IDE of choice.
3. Install dependencies: `pip install -r requirements.txt`
4. Install custom packages: `pip install -e`
5. [Navigate to Env-Setup](#env-setup) for further instructions

**Note:** `pip install -e` assumes the Python "src layout" structure, which defines packages within the "src" directory that are denoted by `__init__.py`.

[src layout vs. flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

-------
### Env-Setup

> Job Goblin relies on free APIs and web services to work. A list of these services and their env variables are provided in "env.example".
>
> **Once Aquired:** 
> 1. Create a `.env` file in the root of your repository and insert your env variables. 
> 2. Add your env variables to your repo's GitHub secrets for your workflows to use.

**Supabase:** a free account can be created to aquire an API key and Supabase URL. Afterwards, create a table in your database (name can be anything as long as `constants.py` is updated) with columns...

- Title
- Company
- Url
- Description
- Location
- Source api

**Adzuna:** a free developer account can be created to aquire an API key and Adzuna ID. 

**Gmail:** create a free gmail account that can email your primary email. An app password can be aquired to bypass security by following this [tutoriel.](https://support.google.com/mail/answer/185833?hl=en)

---------
### Usage

#### GitHub Workflows

#### Testing 

---------
### Adding New APIs

 