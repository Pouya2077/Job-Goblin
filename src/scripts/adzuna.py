""" Fetching and parsing Adzuna jobs """

from fetching import Fetcher, get_auth
from emailing import email_message
from database import supabase

DEFAULT_PARAMS = {"results_per_page": 1, 
                  "what": "software developer",
                  }
ENDPOINT = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"

Adzuna = Fetcher(ENDPOINT, "ADZUNA", DEFAULT_PARAMS)

response = Adzuna.get_jobs()
result = response.json()["results"][0]

MESSAGE = f"""\
Subject: {result["title"]} job at {result["company"]["display_name"]}

description: {result["description"]}
url:         {result["redirect_url"]}"""

MESSAGE_BYTES = MESSAGE.encode("utf-8")

email_message(MESSAGE_BYTES)
