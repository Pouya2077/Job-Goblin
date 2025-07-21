""" Experimenting with basic email capabilities """

from fetching.auth import get_auth
from fetching.fetcher import Fetcher
from emailing.email import email_message
from constants import *

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 1

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

response = Adzuna.get_jobs()
result = response.json()["results"][0]

print(response)
print(response.json())
print(response.json()["results"][0]["title"])
print(result["location"])

message = f"""\
Subject: {result["title"]} job at {result["company"]["display_name"]}

description: {result["description"]}
url:         {result["redirect_url"]}"""

message_bytes = message.encode("utf-8")

email_message(message_bytes)
