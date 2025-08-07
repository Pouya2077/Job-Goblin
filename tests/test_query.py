import random
from database import query
from database import get_api_field, API_PATHS

TEST_JOB_0 = {
    "test_title":           "Test Sr. Dev", 
    "test_company":         {"test_display_name":   "Test Enterprises"}, 
    "test_url":             "Test URL 0", 
    "test_description":     "Guide interns at our test company.",
    "test_location":        {"test_area":       "Vancouver, BC"}, 
    "test_source_api":      "test_job_0",
}
TEST_JOB_1 = {
    "test_title":           "Test Jr. Dev", 
    "test_company":         "Test Enterprises", 
    "test_url":             "Test URL 1", 
    "test_description":     "Intern at our test company.",
    "test_location":        "Vancouver, BC", 
    "test_source_api":      "test_job_1",
}
TEST_JOB_2 = {
    "test_title":           "Test Jr. Dev", 
    "test_company":         "Test Enterprises", 
    "test_url":             "Test URL 2", 
    "test_description":     "Part-time Jr. dev work.",
    "test_location":        "Toronto, ON", 
    "test_source_api":      "test_job_2",
}
TEST_JOB_3 = {
    "test_title":           "Test Jr. Dev", 
    "test_company":         "Test Incorporation", 
    "test_url":             "Test URL 3", 
    "test_description":     "Full time Jr. dev position",
    "test_location":        {"test_area":       "Vancouver, BC"}, 
    "test_source_api":      "test_job_3",
}

def helper_delete_jobs():
    """ Helper: delete jobs (for use after testing is finished) """
    api_names = ["test_job_0", "test_job_1", "test_job_2", "test_job_3"]
    for api_name in api_names:
        query.delete_all_jobs(api_name)

def compare_fields(job, test_job, paths):
    """ Helper: assert that fields of two jobs are the same """
    for key in paths:
        assert job[key] == get_api_field(test_job, paths[key])

def get_test_job_type(job):
    """ Hellper: return which test_job type corresponds to the fetched job """
    if job["source_api"] == "test_job_0":
        return TEST_JOB_0
    if job["source_api"] == "test_job_1":
        return TEST_JOB_1
    if job["source_api"] == "test_job_2":
        return TEST_JOB_2

    return TEST_JOB_3

def test_insert_one_job():
    """ Test that inserted job is intact """
    response = query.insert("test_job_0", TEST_JOB_0)
    inserted_job = response.data[0]

    assert response.data is not None
    assert len(response.data) == 1
    compare_fields(inserted_job, TEST_JOB_0, API_PATHS["test_job_0"])

    helper_delete_jobs()

def test_fetch_jobs_by_api_name():
    """ Ensure that fetching a job by api_name only fetches one job group """
    for _ in range(5):
        query.insert("test_job_0", TEST_JOB_0)
    for _ in range(5):
        query.insert("test_job_1", TEST_JOB_1)

    response = query.fetch_jobs("test_job_0", 5)
    assert response is not None
    assert len(response) == 5

    for job in response:
        compare_fields(job, TEST_JOB_0, API_PATHS["test_job_0"])

    helper_delete_jobs()

def test_fetch_jobs_by_company_name():
    """ Test that company name fetches one job group """
    job_types = [TEST_JOB_0, TEST_JOB_1]
    query.insert("test_job_0", TEST_JOB_0)
    query.insert("test_job_1", TEST_JOB_1)
    query.insert("test_job_2", TEST_JOB_2)
    for _ in range(5):
        job = random.choice(job_types)
        query.insert(job["test_source_api"], job)

    response = query.fetch_jobs(None, 8, None, "Test Enterprises")
    assert response is not None

    for job in response:
        compare_fields(job, get_test_job_type(job), API_PATHS[job["source_api"]])

    helper_delete_jobs()

def test_fetch_jobs_by_title_and_company_name():
    """ Test that company name and title fetches only one job group """
    job_types = [TEST_JOB_0, TEST_JOB_1, TEST_JOB_2, TEST_JOB_3]
    query.insert("test_job_3", TEST_JOB_3)
    for _ in range(10):
        job = random.choice(job_types)
        query.insert(job["test_source_api"], job)

    response = query.fetch_jobs(None, 3, "Test Jr. Dev", "Test Incorporation")
    assert response is not None

    for job in response:
        compare_fields(job, TEST_JOB_3, API_PATHS[job["source_api"]])

    helper_delete_jobs()

def test_fetch_jobs_by_title_company_name_and_location():
    """ Test all three main search params fetch only one job group """
    job_types = [TEST_JOB_0, TEST_JOB_1, TEST_JOB_2, TEST_JOB_3]
    query.insert("test_job_2", TEST_JOB_2)
    for _ in range(10):
        job = random.choice(job_types)
        query.insert(job["test_source_api"], job)

    response = query.fetch_jobs(None, 3, "Test Jr. Dev", "Test Enterprises", "Toronto, ON")
    assert response is not None

    for job in response:
        compare_fields(job, TEST_JOB_2, API_PATHS[job["source_api"]])

    helper_delete_jobs()

def test_delete_jobs():
    return #TODO

def test_delete_all_jobs():
    """ Test that deleting all jobs leaves nothing behind """
    job_types = [TEST_JOB_0, TEST_JOB_1, TEST_JOB_2, TEST_JOB_3]
    query.insert("test_job_0", TEST_JOB_0)
    query.insert("test_job_1", TEST_JOB_1)
    query.insert("test_job_2", TEST_JOB_2)
    query.insert("test_job_3", TEST_JOB_3)

    for test_job in job_types:
        for _ in range(13):
            query.insert(test_job["test_source_api"], test_job)

    for test_job in job_types:
        response = query.delete_all_jobs(test_job["test_source_api"])
        assert response is not None
        assert len(response) == 14
