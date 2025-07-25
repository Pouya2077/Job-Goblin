""" Script maintains db capacity """

from database import query 
from constants import *

query.delete_jobs(None, 5, None, None, "Toronto, Ontario")
query.delete_jobs(None, 5)

if query.get_database_size() >= CAPACITY:
    count = query.get_num_jobs()
    query.delete_jobs(None, int(count * 0.8))
