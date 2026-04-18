import streamlit as st
from auth import signup_user, login_user

st.set_page_config(page_title="Yuva Shakti Sangathan", layout="centered")



# ---------- SESSION ----------
if "user" not in st.session_state:
    st.session_state.user = None
# # ---------- LOGIN / SIGNUP ----------
if st.session_state.user is None:
    menu = st.sidebar.selectbox("Menu", ["Login", "Signup"])

    # SIGNUP
    if menu == "Signup":
        st.subheader("Create Account")

        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Signup"):
            if signup_user(name, email, password):
                st.success("Account created! Please login.")
            else:
                st.error("Email already exists")

    # LOGIN
    elif menu == "Login":
        st.subheader("Login")

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(email, password)
            if user:
                st.session_state.user = user
                st.success(f"Welcome {user['name']} 🎉")
                st.rerun()
            else:
                st.error("Invalid credentials")

    st.stop()  # 🚨 STOP here if not logged in

# ---------- MAIN APP (AFTER LOGIN) ----------
st.sidebar.success(f"Logged in as {st.session_state.user['name']}")

if st.sidebar.button("Logout"):
    st.session_state.user = None
    st.rerun()


# ---------- HOME ----------

st.title("Yuva Shakti Sangathan")
st.caption("Empowering youth to solve community problems 🚀")

st.image(
    "https://i.pinimg.com/1200x/6c/dd/13/6cdd13b4bd695b3d30836a18bef0ea18.jpg",
    width=600
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
    st.warning("📊 **Track Status**\n\nSee updates on your complaints")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Raise Complaint"):
        st.switch_page("pages/complaint.py")

with col2:
    if st.button("💳 Contribute Now"):
        st.switch_page("pages/contribution.py")

st.subheader("Events")

col1, col2 = st.columns(2)
with col1:
    st.write("""
        15th August 2024 - Independence Day Celebration \n
        Join us for a grand celebration of India's independence with cultural performances, flag hoisting, and community activities.
             """)

st.markdown("---")
st.caption("Made with ❤️ by Yuva Shakti Sangathan")