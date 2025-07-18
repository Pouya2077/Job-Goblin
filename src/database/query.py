""" INSERT, GET, and DELETE for supabase backend """

from database import supabase

API_FIELD_NAMES = {
    #Dict to give JSON fields name for diff API responses
    "adzuna": {
        "title": "title", 
        "company": "company.display_name", 
        "url": "redirect_url", 
        "description": "description", 
        "location": "location.display_name",
    }
}

def get_api_field(field_names, field):
    """ Return appropriate job field for api """

    return field_names[field]

def insert(name, job):
    """ Insert job into supabase db """
    name = name.lower()
    field_names = API_FIELD_NAMES[name]

    supabase.table("jobs").insert(

        {
        "title":        get_api_field(field_names, "title"), 
        "company":      get_api_field(field_names, "company"),
        "url":          get_api_field(field_names, "url"),
        "description":  get_api_field(field_names, "description"), 
        "location":     get_api_field(field_names, "location"),
        "source_api":   name,
        }).execute()

def fetch_num_jobs(name, num):
    """ Fetch num latest jobs from db """
    #TODO
    
    return None

def fetch_job(name, job_info):
    """ Fetch specific job from db """
    #TODO
    
    return None

def delete_num_jobs(name, num):
    """ Delete num oldest jobs from db """
    #TODO
    
    return None 

def delete_job(name, job_info):
    """ Delete specific job from db """
    #TODO
    
    return None 