""" Definition of all APIs JSON fields and fnc to iterate through them """

API_FIELD_NAMES = {
    #Dict to give JSON fields name for diff API responses
    "adzuna": {
        "title":        "title", 
        "company":      "company.display_name", 
        "url":          "redirect_url", 
        "description":  "description", 
        "location":     "location.display_name",
    },
    "test": {
        "title":        "test_title", 
        "company":      "test_company.test_company_name", 
        "url":          "test_url", 
        "description":  "test_desc", 
        "location":     "test_location.test_area_name",
    },
}

def get_api_field(job, path):
    """ Return appropriate job field for api """
    value = {}
    keys = path.split(".")

    for key in keys:
        if not value and key in job:
            value = job[key]
        elif isinstance(value, dict) and key in value:
            value = value[key]
        else:
            value = None
            break

    return value