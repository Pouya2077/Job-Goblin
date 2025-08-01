""" Script emails user about jobs """

from emailing import email
from event_logging import LOG

email.email_jobs(None, 5, None, None, "Greater Vancouver, British Columbia")
email.email_jobs(None, 5, None, None, "Vancouver, Greater Vancouver")
email.email_jobs(None, 5, None, None, "Toronto, Ontario")   #email diff searches to user
LOG.info("Jobs emailed to user.")
