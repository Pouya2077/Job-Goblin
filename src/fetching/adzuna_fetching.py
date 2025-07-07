""" Script responsible for fetching Adzuna jobs """

import os
from dotenv import load_dotenv
from fetcher import Fetcher
load_dotenv()

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 1

Adzuna = Fetcher(BASE_URL, {"what": WHAT, "results_per_page": RESULTS_PER_PAGE}, "ADZUNA")

print(Adzuna.canada_jobs())
print(Adzuna.other_params())