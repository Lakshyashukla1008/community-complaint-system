import streamlit as st
from database.database import announcements

# ---------- LOGIN CHECK (Optional) ----------
if "user" not in st.session_state or st.session_state.user is None:
    st.warning("Please login first to view announcements")
    st.stop()

st.set_page_config(page_title="Announcements", layout="wide")

st.title("📢 Announcements")
st.divider()



# ---------- FETCH DATA ----------
data = list(announcements.find().sort("_id", -1))


# ---------- DISPLAY ----------
if not data:
    st.info("No announcements yet")
else:
    for a in data:
        with st.container(border=True):
            st.subheader(a["title"])
            st.markdown(a["message"].replace("\n", "  \n"))

            if "date" in a:
                st.caption(f"Posted on: {a['date']}")

        st.divider()
