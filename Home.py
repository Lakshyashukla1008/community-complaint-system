import streamlit as st
from auth.auth import signup_user, login_user
from services.auth_helper import logout_user
import sys
import os

sys.path.append(os.path.dirname(__file__))

st.set_page_config(page_title="Yuva Shakti Sangathan", layout="centered")

# ---------- SESSION ----------
if "user" not in st.session_state:
    st.session_state.user = None

if "show_login" not in st.session_state:
    st.session_state.show_login = False

if "signup_email" not in st.session_state:
    st.session_state.signup_email = ""


# ---------- LOGIN / SIGNUP ----------
if st.session_state.user is None:

    menu = st.sidebar.radio(
        "Menu",
        ["Signup", "Login"],
        index=1 if st.session_state.show_login else 0
    )

    # ---------- SIGNUP ----------
    if menu == "Signup":
        st.markdown("### 📝 Create Account")

        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if not name or not email or not password:
                st.error("Please fill all fields")
            else:
                if signup_user(name, email, password):
                    st.success("Account created! Redirecting to login...")

                    # save email for login autofill
                    st.session_state.signup_email = email

                    # switch to login
                    st.session_state.show_login = True
                    st.rerun()

                else:
                    st.error("Email already exists")


    # ---------- LOGIN ----------
    elif menu == "Login":
        st.subheader("Login")

        email = st.text_input(
            "Email",
            value=st.session_state.signup_email
        )

        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(email, password)

            if user:
                st.session_state.user = user
                st.session_state.show_login = False
                st.success(f"Welcome {user['name']} 🎉")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()


# ---------- MAIN APP (AFTER LOGIN) ----------
st.sidebar.success(f"Logged in as {st.session_state.user['name']}")

if st.sidebar.button("Logout"):
    logout_user()
    st.session_state.signup_email = ""
    st.session_state.show_login = False


# ---------- HOME ----------
st.title("Yuva Shakti Sangathan")
st.caption("Empowering youth to solve community problems 🚀")

st.image(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDzZXduiBsTAv2aKpH6_AfmovEVBiLKfIHtw&s",
    width=200
)

st.markdown("""
### 🙌 Welcome to Yuva Shakti Sangathan

A platform where citizens can:
- 📝 Raise complaints  
- 📍 Report local issues  
- 🤝 Contribute to society  
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📢 **Raise Complaint**\n\nReport issues like roads, water, garbage")

with col2:
    st.success("💰 **Contribute**\n\nSupport community initiatives")

with col3:
    st.warning("📊 **Track Status**\n\nCheck your complaint status")


col1, col2, col3 = st.columns(3)


with col1:
    if st.button("🚀 Raise Complaint"):
        st.switch_page("pages/complaint.py")

with col2:
    if st.button("💳 Contribute Now"):
        st.switch_page("pages/contribution.py")

with col3:
    if st.button("📈 Check Status"):
        st.switch_page("pages/complaint_status.py")


st.markdown("---")
st.caption("© 2026 Yuva Shakti Sangathan. All rights reserved.")