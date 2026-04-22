import streamlit as st
from database.database import reviews

# ---------- LOGIN CHECK -------- --
if "user" not in st.session_state or st.session_state.user is None:
    st.warning(
        "Please login first\nClick on >> icon and go to Home page"
    )
    st.stop()

user = st.session_state.user

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
            "message": message
        })
        st.success("Thank you for your feedback")