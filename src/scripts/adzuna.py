""" Script fetches, parses, and stores Adzuna jobs """

from fetching import Fetcher
from emailing import email

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
NAME = "ADZUNA"

default_params = {
        "what": "Software Developer Intern", 
        "results_per_page": 10, 
        "where": "Vancouver, BC"
        }

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
                                   })

Adzuna0.get_jobs()
Adzuna1.get_jobs()
Adzuna2.get_jobs()
Adzuna3.get_jobs()

MESSAGE = """\
Subject: Successfully queried and inserted jobs into database. 

Jobs inserted: """
email.email_message(MESSAGE)

