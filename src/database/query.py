""" INSERT, GET, and DELETE for supabase backend """

from database.client import supabase
from database.job_mappings import API_FIELD_NAMES, get_api_field

def insert(name, job):
    """ Insert job into supabase db """
    name = name.lower()
    field_names = API_FIELD_NAMES[name]

    supabase.table("jobs").insert(

        {
        "title":        get_api_field(job, field_names["title"]), 
        "company":      get_api_field(job, field_names["company"]),
        "url":          get_api_field(job, field_names["url"]),
        "description":  get_api_field(job, field_names["description"]), 
        "location":     get_api_field(job, field_names["location"]),
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
