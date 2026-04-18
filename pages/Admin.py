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

    password = st.text_input("Enter admin password", type="password")

    if st.button("Login"):
        if password == "admin@123":
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Incorrect password ❌")

# ---------- ADMIN PANEL ----------
if st.session_state.admin_logged_in:

    # ---------- LOGOUT ----------
    st.sidebar.write("👋 Admin")
    if st.sidebar.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()

    st.success("Welcome Admin! 🎉")


    # ---------- SHOW TABLE ----------
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

    show_data(complaints, "📋 All Complaints")
    show_data(contributions, "💰 Contributions")

    # ---------- FILTER ----------
    filter_status = st.selectbox(
        "Filter Complaints",
        ["All", "Pending", "Resolved"]
    )


    # ---------- FETCH DATA ----------
    if filter_status == "All":
        all_complaints = list(complaints.find())
    else:
        all_complaints = list(complaints.find({"status": filter_status}))

    st.write(f"Total Complaints: {len(all_complaints)}")

    # ---------- STATUS UPDATE ----------
    st.subheader("🔄 Update Complaint Status")

    for c in all_complaints:
        st.write(f"👤 {c['name']} | 📧 {c['email']}")
        st.write(f"🧾 {c['complaint_type']} | 📍 {c['address']}")
        st.write(f"📌 Status: {c.get('status', 'Pending')}")

        col1, col2 = st.columns(2)

        # ---------- PENDING ----------
        with col1:
            if st.button("⏳ Pending", key=f"p_{c['_id']}"):
                complaints.update_one(
                    {"_id": c["_id"]},
                    {"$set": {"status": "Pending"}}
                )
                st.rerun()

        # ---------- RESOLVED ----------
        with col2:
            if st.button("✅ Resolved", key=f"r_{c['_id']}"):
                complaints.update_one(
                    {"_id": c["_id"]},
                    {"$set": {"status": "Resolved"}}
                )

                # SEND EMAIL
                send_mail(
                    c["email"],
                    "Complaint Resolved",
                    f"Hello {c['name']}, your complaint '{c['complaint_type']}' has been resolved ✅"
                    f"\n\nThank you for being a part of Yuva Shakti Sangathan! 🙏"
                )

                st.success("Resolved & Email Sent 📧")
                st.rerun()

        st.markdown("---")