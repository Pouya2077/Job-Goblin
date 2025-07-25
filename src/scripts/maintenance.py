""" Script maintains db capacity """

from database import query 

query.delete_jobs(None, 5, None, None, "Toronto, Ontario")
query.delete_jobs(None, 5)
