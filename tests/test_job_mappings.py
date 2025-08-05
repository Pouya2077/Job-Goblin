from database import get_api_field

TEST_NONE_JOB = {}
TEST_ONE_DEEP_JOB = {
    "name":             "Test one deep job", 
    "company":          "Test one deep company", 
    "location":         "Test one deep location", 
    "description":      "Test one deep description",
}
TEST_TWO_DEEP_JOB = {
    "name":             
}

def test_get_api_field_returns_none():
    assert get_api_field(TEST_NONE_JOB, "no_path") is None

def test_get_api_field_return_field_one_deep():
    assert get_api_field(TEST_ONE_DEEP_JOB, "name") == "Test one deep job"
    assert get_api_field(TEST_ONE_DEEP_JOB, "company") == "Test one deep company"
    assert get_api_field(TEST_ONE_DEEP_JOB, "location") == "Test one deep location"
    assert get_api_field(TEST_ONE_DEEP_JOB, "description") == "Test one deep description"

def test_get_api_field_return_field_two_deep():
    