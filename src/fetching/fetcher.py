""" Class for fetching job data from API """

import requests
from fetching.auth import get_auth
from database import query

class Fetcher:
    """ Class represents fetching and storing for an API endpoint.
        
        Responsible for storing jobs it has fetched in db. """

    __TIMEOUT = 2

    def __init__(self, url, name, params):
        self.__url = url
        self.__name = name
        self.__params = params

    def get_url(self):
        """ Get private url """
        return self.__url

    def get_name(self):
        """ Get private name """
        return self.__name

    def get_params(self):
        """ Get private params """
        return self.__params

    def __insert_jobs(self, jobs):
        """ Insert an array of jobs into db """

        results = []
        for job in jobs:
            results.append(query.insert(self.get_name().lower(), job))

        return results

    def get_jobs(self, params=None):
        """ Request jobs from API, extra params optional """

        if params is None:
            params = {}

        auth_params = get_auth(self.__name)
        params = {**self.__params, **auth_params, **params}

        response = requests.get(self.__url, params, timeout=self.__TIMEOUT)
        response = response.json()["results"]

        self.__insert_jobs(response)

        return response
