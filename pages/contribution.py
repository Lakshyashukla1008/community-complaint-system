import streamlit as st
from database.database import contributions
from services.mail import send_mail
from datetime import datetime

# ---------- LOGIN CHECK ----------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("""Please login first

click on >> icon on top left and click on Home then select signup from the menu""")
    st.stop()
    
user = st.session_state.user


# ---------- UI ----------
st.title("Yuva Shakti Sangathan")
st.subheader("Contribution")

name = st.text_input(
    "Name",
    value=user["name"]
)

email = st.text_input(
    "Email",
    value=user["email"]
)

payment = st.number_input(
    "Payment Amount",
    min_value=100,
    max_value=100000,
    placeholder="Enter amount",
    key="payment_input",
    help="Please enter a valid amount between 100 and 100000"
)

method = st.selectbox(
    "Payment Method",
    ["UPI", "Card", "Cash"]
)


# ---------- SUBMIT ----------
if st.button("Contribute"):
    
    if not name.strip() or not email.strip():
        st.error("Please fill all fields")
        
    else:
        contributions.insert_one({
            "name": name,
            "email": email,
            "payment": payment,
            "method": method,
            "status": "Pending",
            "created_at": datetime.now()
        })

        # ---------- USER MAIL ----------
        send_mail(
            email,
            "Contribution Received",
            f"Hello {name}, thank you for contributing ₹{payment} to Yuva Shakti Sangathan 🙏"
        )

        # ---------- ADMIN MAIL ----------
        send_mail(
            "yuvashaktisangathan108@gmail.com",
            "New Contribution",
            f"{name} contributed ₹{payment} via {method}"
        )

        st.success("Contribution submitted successfully 🙏")