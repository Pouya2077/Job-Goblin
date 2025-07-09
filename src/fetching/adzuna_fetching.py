""" Script responsible for fetching Adzuna jobs """

from fetcher import Fetcher

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 1

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

print(Adzuna.canada_jobs())
print(Adzuna.other_params())
