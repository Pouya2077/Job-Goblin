""" Class for fetching job data from API """

import requests
from fetching.auth import get_auth

class Fetcher:
    """ Class will be responsible for fetching from a specific API
        by name, from a provided endpoint. 
        
        Will NOT be responsible for validating or parsing response. """

    TIMEOUT = 2

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

    def canada_jobs(self):
        """ Return jobs in Canada """

        auth_params = get_auth(self.__name)
        return requests.get(self.__url, {**self.__params, **auth_params}, timeout=self.TIMEOUT)

    def other_params(self, params=None):
        """ Specify extra parameters """

        if params is None:
            params = {}
        auth_params = get_auth(self.__name)

        params = {**self.__params, **auth_params, **params}
        return requests.get(self.__url, params, timeout=self.TIMEOUT)
