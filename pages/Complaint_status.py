import streamlit as st
from database.database import complaints

# ---------- LOGIN CHECK (Optional) ----------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first to view announcements")
    st.stop()

st.header("Complaint Status")

st.write("Check your complaint status")

email = st.text_input("Enter your email")

if st.button("Check Status"):

    if not email:
        st.error("Enter email")
    
    else:
        data = list(complaints.find({"email": email.lower()}))

        if not data:
            st.warning("No complaint found")
        else:
            for c in data:
                st.container(border=True)
                st.write(f"your complaint")
                st.write(f"Name:   {c['name']}")
                st.write(f"Complaint:   {c['complaint_type']}")
                st.write(f"Address:   {c['address']}")
                st.write(f"Status:   {c.get('status','Pending')}")