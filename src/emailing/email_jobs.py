""" Email user with job data """

## For now will just email placeholder msg

import os
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("APP_PASSWORD")
sender_email = os.getenv("FROM_EMAIL")
receiver_email = os.getenv("TO_EMAIL")

port = 465
context = ssl.create_default_context()
message = """\
Subject: Test Email

This message was sent as a test by Job Goblin."""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
