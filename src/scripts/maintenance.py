""" Script maintains db capacity """

from database import query 
from constants import *

query.delete_jobs(None, 5, None, None, "Toronto, Ontario")
query.delete_jobs(None, 5)

# print(query.get_database_size())
# if query.get_database_size() >= CAPACITY:
#     count = query.get_num_jobs()
#     print(count)
#     query.delete_jobs(None, (count/2))
# TODO