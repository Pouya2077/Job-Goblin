""" Class for fetching job data from API """

import requests
from auth import get_auth

class Fetcher:
    """ Class will be responsible for fetching from a specific API
        by name, from a provided endpoint. 
        
        Will NOT be responsible for validating or parsing response. """

    TIMEOUT = 2

    def __init__(self, url, name, params):
        self.url = url
        self.name = name
        self.params = params

    def canada_jobs(self):
        """ Return jobs in Canada """

        auth_params = get_auth(self.name)
        return requests.get(self.url, {**self.params, **auth_params}, timeout=self.TIMEOUT)

    def other_params(self, params=None):
        """ Specify extra parameters """

        if params is None:
            params = {}
        auth_params = get_auth(self.name)

        params = {**self.params, **auth_params, **params}
        return requests.get(self.url, params, timeout=self.TIMEOUT)
