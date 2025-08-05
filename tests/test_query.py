import random
from database import query
from database import get_api_field, API_PATHS

TEST_JOB_0 = {
    "test_title":           "Test Title 0", 
    "test_company":         {"test_display_name":   "Test Company 0"}, 
    "test_url":             "Test URL 0", 
    "test_description":     "Test Description 0",
    "test_location":        {"test_area":       "Test Location/Area 0"}, 
    "test_source_api":      "test_job_0",
}

TEST_JOB_1 = {
    "test_title":           "Test Title 1", 
    "test_company":         "Test Company 1", 
    "test_url":             "Test URL 1", 
    "test_description":     "Test Description 1",
    "test_location":        "Test Location/Area 1", 
    "test_source_api":      "test_job_1",
}

def test_insert_job():
    response = query.insert("test_job_0", TEST_JOB_0)
    inserted_job = response.data[0]

    assert response.data is not None
    assert len(response.data) == 1

    paths = API_PATHS["test_job_0"]
    for key in paths:
        assert inserted_job[key] == get_api_field(TEST_JOB_0, paths[key])

def test_fetch_jobs_by_api_name():
    query.delete_all_jobs("test_job_0")
    for _ in range(5):
        query.insert("test_job_0", TEST_JOB_0)

    response = query.fetch_jobs("test_job_0", 5)
    assert response is not None
    assert len(response) == 5

    paths = API_PATHS["test_job_0"]
    for i in range(5):
        job = response[i]
        for key in paths:
            assert job[key] == get_api_field(TEST_JOB_0, paths[key])

    query.delete_all_jobs("test_job_0")

def test_fetch_jobs_by_search_combination():
    query.delete_all_jobs("test_job_0")
    query.delete_all_jobs("test_job_1")

    job_types = [TEST_JOB_0, TEST_JOB_1]
    for _ in range(8):
        job = random.choice(job_types)
        query.insert(job["test_source_api"], job)

    

    query.delete_all_jobs("test_job_0")
    query.delete_all_jobs("test_job_1")

def test_delete_jobs():
    return #TODO

def test_deleete_all_jobs():
    return #TODO
