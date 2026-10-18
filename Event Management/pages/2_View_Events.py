import streamlit as st
from database import get_connection

st.title("📅 All Events")

conn = get_connection()
c = conn.cursor()

c.execute("SELECT * FROM events")
events = c.fetchall()

if events:
    for event in events:
        with st.container():
            st.subheader(event[1])
            st.write(f"📅 *Date:* {event[2]}")
            st.write(f"📍 *Venue:* {event[3]}")
            st.write(f"📝 *Description:* {event[4]}")
            st.markdown("---")
else:
    st.info("No events added yet.")