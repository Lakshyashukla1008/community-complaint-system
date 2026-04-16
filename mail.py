import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


def send_mail(to_email, subject, message):
    sender = os.getenv("EMAIL")
    password = os.getenv("APP_PASSWORD")


    message = MIMEText(message)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(message)
    server.quit()