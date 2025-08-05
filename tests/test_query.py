from database import query
from database import get_api_field, API_PATHS

TEST_JOB = {
    "test_title":           "Test Title", 
    "test_company":         {"test_display_name":   "Test Company"}, 
    "test_url":             "Test URL", 
    "test_description":     "Test Description",
    "test_location":        {"test_area":       "Test Location/Area"}, 
    "test_source_api":      "Test Job",
}

def test_insert_job():
    response = query.insert("test_job", TEST_JOB)
    inserted_job = response.data[0]

    assert response.data is not None
    assert len(response.data) == 1

    paths = API_PATHS["test_job"]
    for key in paths:
        inserted_job[key] = get_api_field(TEST_JOB, paths[key])

def test_get_num_jobs():
    return #TODO

def test_fetch_jobs():
    return #TODO

def test_delete_jobs():
    return #TODO

