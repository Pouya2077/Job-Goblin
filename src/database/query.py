""" INSERT, GET, and DELETE for supabase backend """

from database.client import supabase
from database.job_mappings import API_FIELD_NAMES, get_api_field
from constants import *

def insert(api_name, job):
    """ Insert job into supabase db """
    api_name = api_name.lower()
    field_names = API_FIELD_NAMES[api_name]

    return supabase.table(TABLE).insert(
                            #entires are case sensitive (includes fetching and deleting filters)
            {
            "title":        get_api_field(job, field_names["title"]), 
            "company":      get_api_field(job, field_names["company"]),
            "url":          get_api_field(job, field_names["url"]),
            "description":  get_api_field(job, field_names["description"]), 
            "location":     get_api_field(job, field_names["location"]),
            "source_api":   api_name,
            }).execute()
    
def get_database_size():
    """ Return size of database in bytes """
    result = supabase.rpc("get_database_size").execute()
    
    return result.data / (1024 * 1024)

def get_num_jobs():
    """ Get number of jobs (rows) in table """

    result = supabase.table(TABLE).select("*", count="exact").execute()

    return result.count

def fetch_jobs(api_name=None, num_jobs=0, title=None, company=None, location=None):
    """ Fetch specific job from db """
    if num_jobs > MAX_FETCH:
        num_jobs = MAX_FETCH

    query = supabase.table(TABLE).select("*")

    if api_name is not None:
        query = query.eq("source_api", f"{api_name.lower()}")
    if title is not None:
        query = query.eq("title", f"{title}")
    if company is not None:
        query = query.eq("company", f"{company}")
    if location is not None:
        query = query.eq("location", f"{location}")

    response = query.order("created_at", desc=True)\
                .limit(num_jobs)\
                .execute()

    return response.data

def delete_jobs(api_name=None, num_jobs=0, title=None, company=None, location=None):
    """ Delete specific job from db """
    if num_jobs > MAX_DELETE:
        num_jobs = MAX_DELETE

    query = supabase.table(TABLE).select("id")

    if api_name is not None:
        query = query.eq("source_api", f"{api_name.lower()}")
    if title is not None:
        query = query.eq("title", f"{title}")
    if company is not None:
        query = query.eq("company", f"{company}")
    if location is not None:
        query = query.eq("location", f"{location}")

    response = query.order("created_at", desc=False)\
                .limit(num_jobs)\
                .execute()

    jobs = response.data
    if not jobs:
        return None

    job_ids = [job["id"] for job in jobs]
    result = supabase.table(TABLE)\
                .delete()\
                .in_("id", job_ids)\
                .execute()

    return result.data

def delete_all_jobs(api_name=None):
    """ Not used by scripts, for manual maintenance """

    query = supabase.table(TABLE).select("id")

    if api_name is not None:
        query = query.eq("source_api", f"{api_name.lower()}")

    response = query.execute()
    jobs = response.data

    job_ids = [job["id"] for job in jobs]

    result = supabase.table(TABLE)\
            .delete()\
            .in_("id", job_ids)\
            .execute()

    return result.data
