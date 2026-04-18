import streamlit as st
import requests
from database import complaints
from mail import send_mail



# ---------- LOGIN CHECK ----------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning(f"""Please login first\n
    click on >> icon on top left and click on Home then select signup from the menu""")
    st.stop()

user = st.session_state.user

# ---------- SESSION ----------
if "address" not in st.session_state:
    st.session_state.address = ""

# ---------- FUNCTION ----------
def get_location():
    try:
        data = requests.get("http://ip-api.com/json/").json()
        return f"{data['city']}, {data['regionName']}, {data['country']}"
    except Exception:
        return ""

def set_location():
    st.session_state.address = get_location()

# ---------- UI ----------
web_title = st.title("Yuva Shakti Sangathan")
st.subheader("Complaint Form")

name = st.text_input(
    "Name",
    value = user["name"], 
    # disabled=True
)

mobile = st.text_input(
    "Mobile Number",
    placeholder="Enter 10 digit mobile number",
    max_chars=10,
    key="mobile_input"
)   


email = st.text_input(
    "Email ID",
    value=user["email"], 
    
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
if st.button("Submit Complaint"):
    if (
        not name.strip()
        or not mobile.strip()
        or not email.strip()
        or not address.strip()
        or complaint_type == "Select the type of complaint"
    ):
        st.error("Please fill in all required fields")
    else:
        complaints.insert_one({
            "name": name,
            "mobile": mobile,
            "email": email,
            "address": address,
            "complaint_type": complaint_type,
            "description": description,
            "status": "Pending"
        })

        st.success("Complaint submitted successfully")
        user_message = f"""
        Namaste {name},

        Your complaint {complaint_type} has been received by Yuva Shakti Sangathan. We will review the details and take necessary action to resolve the issue.

        Stay conected with Yuva Shakti Sangathan for updates on your complaint.

        Grow together, create change!
   
        Thank you
        Yuva Shakti Sangathan
        """

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
            "shuklalakshaya108@gmail.com",
            "New Complaint",
            admin_message
        )
        st.success("Sangathan recivwed your complaint and will take action soon! 🙏")

