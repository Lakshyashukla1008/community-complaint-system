# 
import streamlit as st
import pandas as pd
from database import complaints, contributions
from mail import send_mail

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
        if password == "admin@123":
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

    # ---------- SHOW DATA ----------
    def show_data(collection, title):
        st.subheader(title)

        data = list(collection.find())
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

    st.markdown("---")

    # ---------- FILTER ----------
    st.subheader("🔍 Filter Complaints")

    filter_status = st.selectbox(
        "Select Status",
        ["All", "Pending", "Resolved"]
    )

    # ---------- FETCH DATA ----------
    if filter_status == "All":
        all_complaints = list(complaints.find())
    else:
        all_complaints = list(complaints.find({"status": filter_status}))

    st.info(f"Total Complaints: {len(all_complaints)}")

    st.markdown("---")

    # ---------- UPDATE STATUS ----------
    st.subheader("🔄 Update Complaint Status")

    for c in all_complaints:

        with st.container():

            col1, col2, col3 = st.columns([3,1,1])

            with col1:
                st.markdown(f"""
**👤 Name:** {c['name']}  
**📧 Email:** {c['email']}  
**🧾 Type:** {c['complaint_type']}  
**📍 Address:** {c['address']}  
**📌 Status:** {c.get('status', 'Pending')}
""")

            # ---------- PENDING ----------
            with col2:
                if st.button("⏳ Pending", key=f"p_{c['_id']}"):
                    complaints.update_one(
                        {"_id": c["_id"]},
                        {"$set": {"status": "Pending"}}
                    )
                    st.rerun()

            # ---------- RESOLVED ----------
            with col3:
                if st.button("✅ Resolved", key=f"r_{c['_id']}"):
                    complaints.update_one(
                        {"_id": c["_id"]},
                        {"$set": {"status": "Resolved"}}
                    )

                    send_mail(
                        c["email"],
                        "Complaint Resolved",
                        f"""
Hello {c['name']},

Your complaint '{c['complaint_type']}' has been resolved ✅

Thank you for being a part of Yuva Shakti Sangathan 🙏
"""
                    )

                    st.success("Resolved & Email Sent 📧")
                    st.rerun()

            st.divider()