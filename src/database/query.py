""" INSERT, GET, and DELETE for supabase backend """

from database import supabase

def insert(job):
    """ Insert job into supabase db """
    
    supabase.table("jobs").insert(
        {"title":       f"{job["title"]}", 
        "company":      f"{job["company"]["display_name"]}",
        "url":          f"{job["redirect_url"]}",
        "description":  f"{job["description"]}", 
        "location":     f"{job["location"]["display_name"]}",
        }).execute()

def fetch_num_jobs(num):
    """ Fetch num latest jobs from db """
    #TODO
    
    return None

def fetch_job(job_info):
    """ Fetch specific job from db """
    #TODO
    
    return None

def delete_num_jobs(num):
    """ Delete num oldest jobs from db """
    #TODO
    
    return None 

def delete_job(job_info):
    """ Delete specific job from db """
    #TODO
    
    return None 