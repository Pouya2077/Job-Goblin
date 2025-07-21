""" INSERT, GET, and DELETE for supabase backend """

from database.client import supabase
from database.job_mappings import API_FIELD_NAMES, get_api_field
from constants import *

def insert(api_name, job):
    """ Insert job into supabase db """
    api_name = api_name.lower()
    field_names = API_FIELD_NAMES[api_name]

    supabase.table(TABLE).insert(

        {
        "title":        get_api_field(job, field_names["title"]), 
        "company":      get_api_field(job, field_names["company"]),
        "url":          get_api_field(job, field_names["url"]),
        "description":  get_api_field(job, field_names["description"]), 
        "location":     get_api_field(job, field_names["location"]),
        "source_api":   api_name,
        }).execute()

def fetch_jobs(api_name, num_jobs):
    """ Fetch num latest jobs from db """
    if num_jobs > MAX_JOBS:
        num_jobs = MAX_JOBS

    response = supabase.table(TABLE)\
        .select("*")\
        .eq("source_api", f"{api_name.lower()}")\
        .range(0, num_jobs)\
        .execute()

    return response.data

def fetch_filter_jobs(api_name, job_info):
    """ Fetch specific job from db """
    #TODO
    
    return None

def delete_num_jobs(api_name, num_jobs):
    """ Delete num oldest jobs from db """
    #TODO
    
    return None 

def delete_job(api_name, job_info):
    """ Delete specific job from db """
    #TODO
    
    return None 
