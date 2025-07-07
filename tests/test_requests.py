import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
APP_ID = os.getenv("ADZUNA_ID")
APP_KEY = os.getenv("ADZUNA_KEY")

response = requests.get(URL, {
    "app_id": APP_ID,
    "app_key": APP_KEY, 
    "results_per_page": 1, 
    "what": "software developer"
})

print(response.status_code)
print(response.json())