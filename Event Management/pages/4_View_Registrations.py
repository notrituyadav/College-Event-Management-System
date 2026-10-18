import streamlit as st
from database import get_connection

st.title("👥 View All Registrations")

conn = get_connection()
c = conn.cursor()

query = """
SELECT registrations.name, registrations.email, events.title
FROM registrations
JOIN events ON registrations.event_id = events.id
"""

c.execute(query)
data = c.fetchall()

if data:
    for row in data:
        with st.container():
            st.write(f"👤 *Name:* {row[0]}")
            st.write(f"📧 *Email:* {row[1]}")
            st.write(f"🎫 *Event:* {row[2]}")
            st.markdown("---")
else:
    st.info("No registrations yet.")