import smtplib
import streamlit as st
from email.mime.text import MIMEText

EMAIL = st.secrets["EMAIL"]
PASSWORD = st.secrets["APP_PASSWORD"]

def send_mail(to, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = to

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=10) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

    except Exception as e:
        print("Mail error:", e)