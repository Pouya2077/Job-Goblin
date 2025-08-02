""" Experimenting with inserting in db """

from fetching.auth import get_auth
from fetching.fetcher import Fetcher
from database import query

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 10

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

response = Adzuna.get_jobs()
result = response.json()["results"]
# print(result)

# query.insert("adzuna", result[0])
# query.insert("adzuna", result[1])
# query.insert("adzuna", {})

for job in result:
    query.insert("adzuna", result[result.index(job)])

query.insert("adzuna", {})
result = query.insert("test", {})

print(result)

