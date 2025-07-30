""" Script maintains db capacity """

from database import query
from emailing import email
from constants import *

query.delete_jobs(None, 5, None, None, "Toronto, Ontario")
query.delete_jobs(None, 15)

if query.get_database_size() >= CAPACITY:
    count = query.get_num_jobs()
    query.delete_jobs(None, int(count * 0.8))
    
MESSAGE = """\
Subject: Successfully deleted jobs from database. 

Jobs deleted: """
email.email_message(MESSAGE)
