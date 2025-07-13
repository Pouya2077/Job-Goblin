""" Email user with job data """

## For now will just email placeholder msg

import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

PASSWORD = os.getenv("APP_PASSWORD")
SENDER_EMAIL = os.getenv("FROM_EMAIL")
RECEIVER_EMAIL = os.getenv("TO_EMAIL")

def email_jobs():
    """ Basic email jobs function, wide variety of job type. """

    port = 465
    context = ssl.create_default_context()
    # TODO come back and change messages when jobs 
    message = """\
    Subject: Test Email

    This message was sent as a test by Job Goblin."""

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
