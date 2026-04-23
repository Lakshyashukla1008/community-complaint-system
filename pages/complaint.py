import streamlit as st
from database.database import complaints
from services.mail import send_mail
from datetime import datetime
from services.auth_helper import check_login


# ---------- LOGIN CHECK ----------
user = check_login()

# ---------- UI ----------
st.title("Yuva Shakti Sangathan")
st.subheader("Complaint Form")

name = st.text_input(
    "Name",
    value=user["name"],
    disabled=True
)

mobile = st.text_input(
    "Mobile Number",
    placeholder="Enter 10 digit mobile number",
    max_chars=10
)

email = st.text_input(
    "Email ID",
    value=user["email"],
    disabled=True
)

address = st.text_area(
    "Address",
    placeholder="Enter your full address"
)

complaint_type = st.selectbox(
    "Complaint Type",
    [
        "Select the type of complaint",
        "Light Complaint",
        "Road Complaint",
        "Parking",
        "Street Dog",
        "Sewer Overflow",
        "Personal Complaint",
        "Garbage Issue",
        "Water Supply",
        "Noise Complaint",
        "Other"
    ]
)

description = st.text_area(
    "Complaint Description (Optional)",
    placeholder="Describe your complaint..."
)


# ---------- SUBMIT ----------
if st.button("Submit Complaint",type="primary"):

    if (
        not mobile.strip()
        or not address.strip()
        or complaint_type == "Select the type of complaint"
    ):
        st.error("Please fill all required fields")

    elif len(mobile) != 10 or not mobile.isdigit():
        st.error("Enter valid 10 digit mobile number")

    else:

        complaints.insert_one({
            "name": name,
            "mobile": mobile,
            "email": email,
            "address": address,
            "complaint_type": complaint_type,
            "description": description,
            "status": "Pending",
            "created_at": datetime.now()
        })

        # USER MAIL
        user_message = f"""
Namaste {name},

Your complaint '{complaint_type}' has been received by
Yuva Shakti Sangathan.

We will review and take action soon.

Thank you 🙏
"""

        # ADMIN MAIL
        admin_message = f"""
New Complaint Received

Name: {name}
Mobile: {mobile}
Email: {email}
Address: {address}
Complaint Type: {complaint_type}
Description: {description}
"""

        send_mail(email, "Complaint Submitted", user_message)

        send_mail(
            "yuvashaktisangathan108@gmail.com",
            "New Complaint",
            admin_message
        )

        st.success("Complaint submitted successfully 🎉")