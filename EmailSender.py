
# By Raj Shekhar Aryal
# Simple Email Sender made in python

# Instructions:
# 1. Enable 2-Step Verification on your Google account
# 2. Generate an App Password: https://myaccount.google.com/apppasswords
# 3. Replace the placeholders below with your actual credentials

import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'your_email@gmail.com'          # Your Gmail address
email_password = 'xxxx xxxx xxxx xxxx'         # Your 16-character Gmail App Password

email_recipient = 'recipient_email@gmail.com'  # Recipient's email address
email_subject = 'Your Subject Here'

body = """
    Your email body goes here. Edit this message as you like!
"""
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_recipient
em["Subject"] = email_subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_recipient, em.as_string())
    server.quit()
