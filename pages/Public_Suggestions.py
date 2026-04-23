import streamlit as st
from database.database import reviews
from services.auth_helper import check_login
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(__file__))

# ---------- LOGIN CHECK -------- --
user = check_login()

# ---------- UI ----------
st.title("Yuva Shakti Sangathan")
st.header("📢 Community Feedback")

name = st.text_input("Name")
message = st.text_area("Your Feedback/Apke Vichar")

if st.button("Submit"):
    if not message:
        st.error("Please write feedback")
    else:
        reviews.insert_one({
            "name": name,
            "message": message,
            "created_at": datetime.now()
        })
        st.success("Thank you for your feedback")