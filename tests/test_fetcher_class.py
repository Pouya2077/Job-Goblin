import pytest
import requests
from unittest.mock import patch
from fetching import Fetcher
from constants import *

URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
NAME = "ADZUNA"  #testing only Adzuna should still covers general functionality for all APIs
PARAMS = {
        "what": "Software Developer Intern", 
        "results_per_page": 10, 
        "where": "Vancouver, BC",
        }
TEST = Fetcher(URL, NAME, PARAMS)

def test_fetcher_getters():
    """ Test public getters """
    assert TEST.get_url() == URL
    assert TEST.get_name() == NAME
    assert TEST.get_params() == PARAMS

def test_fetcher_json_decode_exception_raised():
    """ Test if JSONDecode Exception raised """
    none_params = {
        "none_param":   "none",
    }

    with pytest.raises(requests.exceptions.JSONDecodeError):
        TEST.get_jobs(none_params)

def test_fetcher_timeout_exception_raised():
    """ Test if Timeout Exception raised """
    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        with pytest.raises(requests.exceptions.Timeout):
            TEST.get_jobs()

def test_fetcher_http_exception_raised():
    """ Test if HTTP Exception raised """
    with patch("requests.get", side_effect=requests.exceptions.HTTPError):
        with pytest.raises(requests.exceptions.HTTPError):
            TEST.get_jobs()

def test_fetcher_connection_exception_raised():
    """ Test if ConnectionException raised """
    with patch("requests.get", side_effect=requests.exceptions.ConnectionError):
        with pytest.raises(requests.exceptions.ConnectionError):
            TEST.get_jobs()

def test_fetcher_request_exception_raised():
    """ Test if general RequestException raised """
    with patch("requests.get", side_effect=requests.exceptions.RequestException):
        with pytest.raises(requests.exceptions.RequestException):
            TEST.get_jobs()

def test_fetcher_returns_none():
    """ Test response is None for invalid requests """
    test = Fetcher(URL, NAME, {"what":              "nothing job",
                               "results_per_page":  10,
                               "where":             "Vancouver, BC"})

    response = test.get_jobs()
    assert response is not None

def test_fetcher_no_extra_params():
    """ Test response has value and no exceptions """
    response = TEST.get_jobs()
    assert response is not None
    assert len(response) <= MAX_FETCH

def test_fetcher_use_extra_params():
    """ Test case where Fetcher uses extra params """
    extra_params = {
        "full_time":    1,
        "permanent":    1,
    }

    response = TEST.get_jobs(extra_params)
    assert response is not None
    assert len(response) <= MAX_FETCH

#TODO refactor so that these tests don't clog database