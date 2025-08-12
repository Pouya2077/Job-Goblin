""" Experimenting with Jooble API """

import requests
from fetching import get_auth

ENDPOINT = "https://jooble.org/api"
AUTH_PARAMS = get_auth("JOOBLE")
PARAMS = {
    "keywords": "software developer intern", 
    "location": "British Columbia", 
    "page":     1,
}

response = requests.post(ENDPOINT + f"/{AUTH_PARAMS["app_key"]}", json=PARAMS, timeout=2)

results = response.json()["jobs"]
print(results)