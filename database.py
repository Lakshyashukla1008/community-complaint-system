import streamlit as st
from pymongo import MongoClient

MONGO_URI = st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)

db = client["yes"]

complaints = db["complaints"]
contributions = db["contributions"]
users = db["users"]