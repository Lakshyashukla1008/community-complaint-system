import streamlit as st
from database import contributions

from mail import send_mail


if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first")
    st.stop()
    
user = st.session_state.user

st.title("Yuva Shakti Sangathan")

st.subheader("Contribution")

name = st.text_input(
    "Name",
    value= user["name"],
)

email = st.text_input(
    "Email",
    value= user["email"]
)

payment = st.number_input(
    "Payment Amount",
    min_value=100,
    max_value=100000,
    placeholder="Enter amount",
    key="payment_input",
    help="Please enter a valid amount between 100 and 10000"

)

method = st.selectbox(
    "Payment Method",
    ["UPI","Card","Cash"]
)


if st.button("Contribute"):
    if not name or not email or not payment:
        st.error("please fill in all the fields")
    else:   
        # order = create_order(payment)

        contributions.insert_one({
            "name": name,
            "email": email,
            "payment": payment,
            "method": method,
            # "status":"Pendeng",
            # "order_id": order["id"]
        })
        st.success(f"Thank you for your {payment} contribution! 🙏")

        send_mail(
            email,
            "Payment Initiated",
             f"Hello {name}, your payment of ₹{payment}"
        )

        send_mail(
            "shuklalakshaya108@gmail.com",
            "New Contribution",
            f"{name} is Contirbution ₹{payment}"
        )

        st.success("Payment Initiated ✅")


      