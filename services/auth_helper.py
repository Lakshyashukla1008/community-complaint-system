import streamlit as st

# ---------- USER LOGIN CHECK ----------
def check_login():
    if "user" not in st.session_state or st.session_state.user is None:
        st.warning("Please login first")
        st.stop()
    return st.session_state.user




# ---------- LOGOUT ----------
def logout_user():
    st.session_state.user = None
    st.rerun()