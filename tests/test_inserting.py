""" Experimenting with inserting in db """

from fetching.auth import get_auth
from fetching.fetcher import Fetcher
from database import query

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 2

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

response = Adzuna.get_jobs()
result = response.json()["results"][0]
print(result)

query.insert("adzuna", response.json()["results"][0])
query.insert("adzuna", response.json()["results"][1])

