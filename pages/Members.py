import streamlit as st
from services.auth_helper import check_login
import sys
import os

sys.path.append(os.path.dirname(__file__))

# ---------- LOGIN CHECK ----------
user = check_login()
st.set_page_config(page_title="Committee Members", layout="wide")


# ---------- UI ----------
st.title("Yuva Shakti Sangathan")
st.subheader("Committee Members")

st.divider()

committee = [
    {
        "position": "Patron",
        "members": [
            {
                "name": "Mayank Ji",
                "mobile": "9876543210",
                "image": "assets/images/mayank.jpeg"
            }
        ]
    },
    {
        "position": "Operations & Information Head",
        "members": [
            {
                "name": "Vipin Ji",
                "mobile": "9876543210",
                "image": "assets/images/vipin_dev.jpeg"
            }
        ]
    },
    {
        "position": "Special Advisor",
        "members": [
            {
                "name": "Jayant Ji",
                "mobile": "9876789056",
                "image": "assets/images/jayant_sharma.jpeg"
            }
        ]
    },
    {
        "position": "Vice President",
        "members": [
            {
                "name": "Jayant Ji",
                "mobile": "9876789056",
                "image": "assets/images/jayant_sharma.jpeg"
            }
        ]
    },
    {
        "position": "Treasurer & Co-Treasurer",
        "members": [
            {
                "name": "Nishant Ji",
                "mobile": "9876543210",
                "image": "assets/images/golu_bhaiya.jpg"
            }
        ]
    }
]


for item in committee:

    with st.container(border=True):

        st.subheader(item["position"])

        for member in item["members"]:
            col1, col2 = st.columns([1,4])

            with col1:
                st.image(member["image"], width=100)

            with col2:
                st.write(f"**{member['name']}**")
                st.write(f"📞 {member['mobile']}")

    st.divider()