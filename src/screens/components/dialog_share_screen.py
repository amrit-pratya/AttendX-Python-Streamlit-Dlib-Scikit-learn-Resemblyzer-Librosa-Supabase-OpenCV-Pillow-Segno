import streamlit as st
from src.database.db import create_teacher
import segno
import io

@st.dialog("Share Class Link", icon=":material/share:", width="medium")
def share_subject_dialog(subject_name, subject_code):
  app_domain = "http://localhost:8501/"
  join_link = f"{app_domain}?join_code={subject_code}"

  st.header("Scan to join")

  qr = segno.make(join_link)
  output = io.BytesIO()
  qr.save(output, kind='png', scale=10, border=1)

  col1, col2 = st.columns([1, 2])
  with col1:
      st.markdown('### Copy Link')
      st.code(join_link, language='text')
      st.code(subject_code, language='text')
      st.info("Share this link or code with your students to allow them to join the class.")

  with col2:
      st.markdown('### Scan to Join')
      st.image(output.getvalue(),width="stretch", caption="Scan this QR code to join the class.")
