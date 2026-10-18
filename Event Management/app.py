import streamlit as st
from database import get_connection

st.set_page_config(page_title="College Event Management", page_icon="🎉", layout="wide")

st.markdown("""
    <h1 style='text-align:center; color:#4CAF50;'>🎉 College Event Management System 🎉</h1>
    <p style='text-align:center; font-size:20px;'>
        Manage events, add new events, register participants & explore details — all in one place.
    </p>
""", unsafe_allow_html=True)

st.image(
    "https://img.freepik.com/premium-photo/students-party_116547-47393.jpg",
    caption="Campus Events",
    use_column_width=True
)

st.markdown("""
    <h3 style='text-align:center; color:#555;'>Use the sidebar to navigate through the website.</h3>
""", unsafe_allow_html=True)