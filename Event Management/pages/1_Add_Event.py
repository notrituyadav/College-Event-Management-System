import streamlit as st
import sqlite3
from database import get_connection

st.title("➕ Add New Event")

title = st.text_input("Event Title")
date = st.date_input("Event Date")
venue = st.text_input("Event Venue")
description = st.text_area("Event Description")

if st.button("Add Event", type="primary"):
    conn = get_connection()
    c = conn.cursor()

    c.execute("INSERT INTO events (title, date, venue, description) VALUES (?, ?, ?, ?)",
              (title, str(date), venue, description))
    conn.commit()
    conn.close()

    st.success("🎉 Event added successfully!")