import streamlit as st

# ---------- USER LOGIN CHECK ----------
def check_login():
    if "user" not in st.session_state or st.session_state.user is None:
        st.warning("Please login first")
        st.stop()
    return st.session_state.user


# ---------- ADMIN LOGIN CHECK ----------
def check_admin():
    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

    if not st.session_state.admin_logged_in:
        st.warning("Admin access required")
        st.stop()


# ---------- LOGOUT ----------
def logout_user():
    st.session_state.user = None
    st.rerun()