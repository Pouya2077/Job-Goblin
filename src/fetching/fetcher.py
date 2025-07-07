""" Class for fetching job data from API """
import requests
from auth import get_auth

import os
from dotenv import load_dotenv 
load_dotenv()

class Fetcher:
    """ Class will be responsible for fetching from a specific API
        by name, from a provided endpoint. 
        
        Will NOT be responsible for validating or parsing response. """

    BASE_URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
    TIMEOUT = 2

    def __init__(self, params, name):
        self.params = params
        self.name = name

    def canada_jobs(self):
        auth_params = get_auth("ADZUNA")
        return requests.get(self.BASE_URL, {**self.params, **auth_params}, timeout=self.TIMEOUT)

    def other_params(self, params):
        auth_params = get_auth("ADZUNA")
        return requests.get(self.BASE_URL, {**self.params, **auth_params, **params}, timeout=self.TIMEOUT)
    
