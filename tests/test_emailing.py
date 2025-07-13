# """ Experimenting with basic email capabilities """

from fetching.auth import get_auth
from fetching.fetcher import Fetcher
import emailing

BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
WHAT = "software developer"
RESULTS_PER_PAGE = 1

Adzuna = Fetcher(BASE_URL, "ADZUNA", {"what": WHAT, "results_per_page": RESULTS_PER_PAGE})

response = Adzuna.canada_jobs()
print(response)



