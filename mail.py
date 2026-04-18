import smtplib
from email.mime.text import MIMEText
import streamlit as st

def send_mail(to_email, subject, message):
    sender = st.secrets["EMAIL"]
    password = st.secrets["APP_PASSWORD"]

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()