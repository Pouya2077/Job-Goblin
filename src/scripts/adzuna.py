""" Script fetches, parses, and stores Adzuna jobs """

from fetching import Fetcher
from emailing import email
from database import query

count = query.get_num_jobs()
BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
NAME = "ADZUNA"

default_params = {
        "what": "Software Developer Intern", 
        "results_per_page": 10, 
        "where": "Vancouver, BC"
        }                           #basic search params                                

Adzuna0 = Fetcher(BASE_URL, NAME, default_params)
Adzuna1 = Fetcher(BASE_URL, NAME, {"what": "Software Engineer Intern",
                                   "results_per_page": 10,
                                   "where": "Vancouver, BC",
                                   })
Adzuna2 = Fetcher(BASE_URL, NAME, {"what": "Software Engineer Intern",
                                   "results_per_page": 5,
                                   "where": "Ontario",
                                   })
Adzuna3 = Fetcher(BASE_URL, NAME, {"what": "Software Developer Intern",
                                   "results_per_page": 5,
                                   "where": "Ontario",
                                   })                                       #create fetchers for each search type

Adzuna0.get_jobs()
Adzuna1.get_jobs()
Adzuna2.get_jobs()
Adzuna3.get_jobs()      #search for the jobs, parse, and store them

count = abs(count - query.get_num_jobs())

MESSAGE = f"""\
Subject: Successfully queried and inserted jobs into database. 

Jobs inserted: {count}"""
email.email_message(MESSAGE)    #msg with total jobs inserted

