""" Experimenting with Fetcher class """

from fetching import Fetcher 
from database import query

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 2

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

response = Adzuna.get_jobs()
print(len(response.json()["results"]))
# query.delete_all_jobs()

# response = Adzuna.jobs_by_params({"where": "Ottawa, Ontario"})
# print(len(response.json()["results"]))

# print(Adzuna.get_name())
# print(Adzuna.get_url())
# print(Adzuna.get_params())
