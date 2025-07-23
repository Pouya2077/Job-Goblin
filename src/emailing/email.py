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

def construct_message():
    """ Construct message based on jobs from database """
    #TODO determine which jobs to consider for message
    #TODO construction of the message

    return ""
