""" Email logic """

import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("APP_PASSWORD")
SENDER_EMAIL = os.getenv("FROM_EMAIL")
RECEIVER_EMAIL = os.getenv("TO_EMAIL")

def email_message(message):
    """ Only sends email, does NOT create message. """

    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

def construct_message(job):
    """ Construct email message out of job """
    #TODO
    return ""

def email_jobs(api_name=None, num_jobs=0, title=None, company=None, location=None):
    """ Send email for jobs that fit filter params """
    #TODO 
    return ""