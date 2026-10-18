import streamlit as st
from database import get_connection

st.title("📝 Register for an Event")

conn = get_connection()
c = conn.cursor()

c.execute("SELECT id, title FROM events")
event_options = c.fetchall()

if not event_options:
    st.warning("No events available for registration.")
else:
    name = st.text_input("Your Name")
    email = st.text_input("Email ID")
    event_choice = st.selectbox("Select Event", event_options, format_func=lambda x: x[1])

    if st.button("Register", type="primary"):
        c.execute("INSERT INTO registrations (name, email, event_id) VALUES (?, ?, ?)",
                  (name, email, event_choice[0]))
        conn.commit()
        st.success("🎉 Registered Successfully!")