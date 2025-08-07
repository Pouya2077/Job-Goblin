from fetching import Fetcher
from constants import *

URL = "http://api.adzuna.com/v1/api/jobs/ca/search/1?"
NAME = "ADZUNA"  #testing only Adzuna should still covers general functionality for all APIs
PARAMS = {
        "what": "Software Developer Intern", 
        "results_per_page": 10, 
        "where": "Vancouver, BC",
        }

TEST_JOB_0 = {
    "test_title":           "Test Sr. Dev", 
    "test_company":         {"test_display_name":   "Test Enterprises"}, 
    "test_url":             "Test URL 0", 
    "test_description":     "Guide interns at our test company.",
    "test_location":        {"test_area":       "Vancouver, BC"}, 
    "test_source_api":      "test_job_0",
}
TEST = Fetcher(URL, NAME, PARAMS)

def test_fetcher_getters():
    """ Test public getters """
    assert TEST.get_url() == URL
    assert TEST.get_name() == NAME
    assert TEST.get_params() == PARAMS

def test_fetcher_get_no_jobs():
    """ Test case where Fetcher fetches None """
    return #TODO

def test_fetcher_no_extra_params():
    """ Test response has value and no exceptions """
    response = TEST.get_jobs()      #no exceptions if this line runs
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

