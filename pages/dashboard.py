import streamlit as st
import pandas as pd
from database.database import db
import matplotlib.pyplot as plt
from services.auth_helper import check_login

user = check_login()

complaints = db["complaints"]
contributions = db["contributions"]

st.set_page_config(page_title="Dashboard", layout="wide")

# ---------- HEADER ----------
st.markdown(
    "<h1 style='text-align:center;'>Yuva Shakti Sangathan</h1>",
    unsafe_allow_html=True
)
st.caption("Empowering youth to solve community problems 🚀")
st.markdown("---")

# ---------- FETCH ----------
all_complaints = list(complaints.find())
all_contributions = list(contributions.find())

# ---------- METRICS ----------
total = len(all_complaints)

pending = len([
    c for c in all_complaints 
    if c.get("status","Pending") == "Pending"
])

resolved = len([
    c for c in all_complaints 
    if c.get("status") == "Resolved"
])

# 🔥 FIXED contribution
total_amount = sum([
    int(c.get("payment", 0)) if str(c.get("payment","")).isdigit() else 0
    for c in all_contributions
])

# ---------- SPACING ----------
st.markdown("<div style='margin-top:20px;'></div>", unsafe_allow_html=True)

# ---------- METRIC CARDS ----------
col1, col2, col3, col4 = st.columns(4)

col1.metric("📋 Total", total)
col2.metric("⏳ Pending", pending)
col3.metric("✅ Resolved", resolved)
col4.metric("💰 ₹", total_amount)

st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)

# ---------- CHART SECTION ----------
col1, col2 = st.columns(2)

# 🔹 PIE CHART
with col1:
    with st.container(border=True):
        st.subheader("📊 Complaint Status")

        import matplotlib.pyplot as plt

        labels = ["Pending", "Resolved"]
        sizes = [pending, resolved]

        # ⚠️ edge case handle (0,0)
        if sum(sizes) == 0:
            sizes = [1, 1]

        fig, ax = plt.subplots()

        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.axis("equal")  # perfect circle

        st.pyplot(fig)
# 🔹 BAR CHART
with col2:
    with st.container(border=True):
        st.subheader("📊 Complaint Types")

        types = {}
        for c in all_complaints:
            t = c.get("complaint_type", "Other")
            types[t] = types.get(t, 0) + 1

        labels = list(types.keys())
        values = list(types.values())

        fig, ax = plt.subplots()

        ax.bar(labels, values)
        plt.xticks(rotation=30)  # fix label tilt
        plt.tight_layout()

        st.pyplot(fig)
# ---------- FOOTER ----------
st.info("🔒 Data privacy maintained. Detailed data visible only to admin.")