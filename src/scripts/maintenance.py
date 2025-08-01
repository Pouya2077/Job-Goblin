""" Script maintains db capacity """

from database import query
from emailing import email
from constants import *
from event_logging import LOG

count = query.get_num_jobs()
query.delete_jobs(None, 5, None, None, "Toronto, Ontario")
query.delete_jobs(None, 20)                                 #delete old jobs

if query.get_database_size() >= CAPACITY:
    count = query.get_num_jobs()
    query.delete_jobs(None, int(count * 0.8))               #check if capacity is being reached

count = abs(count - query.get_num_jobs())

MESSAGE = f"""\
Subject: Successfully deleted jobs from database. 

Jobs deleted: {count}"""
email.email_message(MESSAGE)                                #send msg with total jobs deleted
LOG.info(f"Deleted {count} jobs.")

