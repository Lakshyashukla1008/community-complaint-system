import streamlit as st
import pandas as pd
from datetime import datetime

from database.database import (
    complaints,
    contributions,
    reviews,
    announcements
)

from services.mail import send_mail

st.set_page_config(page_title="Admin Panel", layout="wide")

st.title("🧑‍💼 Admin Panel")


# ---------- SESSION ----------
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False


# ---------- LOGIN ----------
if not st.session_state.admin_logged_in:

    st.subheader("🔐 Admin Login")

    password = st.text_input("Enter admin password", type="password")

    if st.button("Login"):
        if password == st.secrets["ADMIN_PASSWORD"]:
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password ❌")


# ---------- ADMIN PANEL ----------
if st.session_state.admin_logged_in:

    # ---------- SIDEBAR ----------
    st.sidebar.success("👋 Admin")

    if st.sidebar.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()

    st.success("Welcome Admin! 🎉")

    st.divider()

    # ======================================
    # ---------- ANNOUNCEMENT SECTION -------
    # ======================================

    st.subheader("📢 Post Announcement")

    with st.form("announcement_form"):

        title = st.text_input("Announcement Title")
        message = st.text_area("Announcement Message")

        submit = st.form_submit_button("Post Announcement")

        if submit:

            if not title.strip() or not message.strip():
                st.error("Fill all fields")

            else:
                try:
                    announcements.insert_one({
                        "title": title.strip(),
                        "message": message.strip(),
                        "date": datetime.now()
                    })

                    st.success("Announcement Posted Successfully ✅")

                except Exception as e:
                    st.error(f"Error posting announcement: {e}")

    st.divider()

    # ======================================
    # ---------- SHOW DATA FUNCTION ----------
    # ======================================

    def show_data(collection, title):

        st.subheader(title)

        data = list(collection.find().limit(500))

        if not data:
            st.info("No data found")
            return

        df = pd.DataFrame(data)

        if "_id" in df.columns:
            df = df.drop(columns=["_id"])

        df.index = df.index + 1

        st.dataframe(df, width="stretch")


    # ---------- TABLES ----------
    show_data(complaints, "📋 All Complaints")
    show_data(contributions, "💰 Contributions")
    show_data(reviews, "📝 Community Feedback")

    st.divider()

    # ======================================
    # ---------- FILTER ----------
    # ======================================

    st.subheader("🔍 Filter Complaints")

    filter_status = st.selectbox(
        "Select Status",
        ["All", "Pending", "Resolved"]
    )

    if filter_status == "All":
        all_complaints = list(complaints.find())
    else:
        all_complaints = list(
            complaints.find({"status": filter_status})
        )

    st.info(f"Total Complaints: {len(all_complaints)}")

    st.divider()

    # ======================================
    # ---------- UPDATE STATUS ----------
    # ======================================

    st.subheader("🔄 Update Complaint Status")

    for c in all_complaints:

        with st.container():

            col1, col2, col3 = st.columns([3, 1, 1])

            with col1:
                st.markdown(f"""
**👤 Name:** {c.get('name', 'N/A')}  
**📧 Email:** {c.get('email', 'N/A')}  
**🧾 Type:** {c.get('complaint_type', 'N/A')}  
**📍 Address:** {c.get('address', 'N/A')}  
**📌 Status:** {c.get('status', 'Pending')}
""")

            with col2:
                if st.button("⏳ Pending", key=f"p_{c['_id']}"):
                    complaints.update_one(
                        {"_id": c["_id"]},
                        {"$set": {"status": "Pending"}}
                    )
                    st.rerun()

            with col3:
                if st.button("✅ Resolved", key=f"r_{c['_id']}"):

                    complaints.update_one(
                        {"_id": c["_id"]},
                        {"$set": {"status": "Resolved"}}
                    )

                    try:
                        send_mail(
                            c.get("email"),
                            "Complaint Resolved",
                            f"""Hello {c.get('name','User')},

Your complaint '{c.get('complaint_type')}' has been resolved ✅

Thank you for being a part of Yuva Shakti Sangathan 🙏
"""
                        )
                        st.success("Resolved & Email Sent 📧")

                    except Exception as e:
                        st.warning(f"Resolved but email failed: {e}")

                    st.rerun()

            st.divider()