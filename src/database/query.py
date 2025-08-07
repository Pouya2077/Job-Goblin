""" INSERT, GET, and DELETE for supabase backend """

from database.client import supabase
from database.job_mappings import API_PATHS, get_api_field
import constants

def insert(api_name, job):
    """ Insert job into supabase db """
    api_name = api_name.lower()
    path = API_PATHS[api_name]

    return supabase.table(constants.TABLE).insert(
                            #entires are case sensitive (includes fetching and deleting filters)
            {
            "title":        get_api_field(job, path["title"]), 
            "company":      get_api_field(job, path["company"]),
            "url":          get_api_field(job, path["url"]),
            "description":  get_api_field(job, path["description"]), 
            "location":     get_api_field(job, path["location"]),
            "source_api":   api_name,
            }).execute()

def get_database_size():
    """ Return size of database in bytes """
    result = supabase.rpc("get_database_size").execute()

    return result.data / (1024 * 1024) #convert to megabytes

def get_num_jobs():
    """ Get number of jobs (rows) in table """

    result = supabase.table(constants.TABLE).select("*", count="exact").execute()

    return result.count

def fetch_jobs(api_name=None, num_jobs=0, title=None, company=None, location=None):
    """ Fetch specific job from db """
    if num_jobs > constants.MAX_FETCH:
        num_jobs = constants.MAX_FETCH

    query = supabase.table(constants.TABLE).select("*")

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
    if num_jobs > constants.MAX_DELETE and get_database_size() < constants.CAPACITY:
        num_jobs = constants.MAX_DELETE

    query = supabase.table(constants.TABLE).select("id")

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
        return []

    job_ids = [job["id"] for job in jobs]
    result = supabase.table(constants.TABLE)\
                .delete()\
                .in_("id", job_ids)\
                .execute()

    return result.data

def delete_all_jobs(api_name=None):
    """ NOT for scripts """

    query = supabase.table(constants.TABLE).select("id")

    if api_name is not None:
        query = query.eq("source_api", f"{api_name.lower()}")

    response = query.execute()
    jobs = response.data

    job_ids = [job["id"] for job in jobs]

    result = supabase.table(constants.TABLE)\
            .delete()\
            .in_("id", job_ids)\
            .execute()

    return result.data
