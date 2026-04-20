import streamlit as st
from pymongo import MongoClient

@st.cache_resource
def get_db():
    client = MongoClient(
        st.secrets["MONGO_URI"],
        serverSelectionTimeoutMS=5000
    )
    return client["yss"]

db = get_db()

users = db["users"]
complaints = db["complaints"]
contributions = db["contributions"]