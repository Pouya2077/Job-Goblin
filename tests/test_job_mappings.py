from database import get_api_field

TEST_NONE_JOB = {}
TEST_ONE_DEEP_JOB = {
    "name":             "Test one deep name", 
    "company":          "Test one deep company", 
    "location":         "Test one deep location", 
    "description":      "Test one deep description",
}
TEST_TWO_DEEP_JOB = {
    "name":             "Test two deep name",
    "company":          {
                        "display_name": "Test two deep company",
                        },
    "location":         {
                        "display_name": "Test two deep location",
                        "area":         "Test two deep area",
                        "postal_code":  {},
                        },
    "description":      "Test two deep description",
}

def test_get_api_field_returns_none():
    assert get_api_field(TEST_NONE_JOB, "no_path") is None

def test_get_api_field_return_field_one_deep():
    assert get_api_field(TEST_ONE_DEEP_JOB, "name") == "Test one deep name"
    assert get_api_field(TEST_ONE_DEEP_JOB, "company") == "Test one deep company"
    assert get_api_field(TEST_ONE_DEEP_JOB, "location") == "Test one deep location"
    assert get_api_field(TEST_ONE_DEEP_JOB, "description") == "Test one deep description"

def test_get_api_field_return_field_two_deep():
    assert get_api_field(TEST_TWO_DEEP_JOB, "name") == "Test two deep name"
    assert get_api_field(TEST_TWO_DEEP_JOB, "company.display_name") == "Test two deep company"
    assert get_api_field(TEST_TWO_DEEP_JOB, "location.display_name") == "Test two deep location"
    assert get_api_field(TEST_TWO_DEEP_JOB, "location.area") == "Test two deep area"
    assert get_api_field(TEST_TWO_DEEP_JOB, "description") == "Test two deep description"
    assert isinstance(get_api_field(TEST_TWO_DEEP_JOB, "location.postal_code"), dict) is True
