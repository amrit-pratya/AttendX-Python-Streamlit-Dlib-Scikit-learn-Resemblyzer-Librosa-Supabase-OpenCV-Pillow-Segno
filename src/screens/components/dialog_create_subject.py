import streamlit as st
from src.database.db import create_subject


@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
  st.write("Please enter the details for the new subject.")
  sub_code = st.text_input("Subject Code", placeholder="CS101")
  sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
  section = st.text_input("Section", placeholder="A")

  if st.button("Create Subject Now", type="primary", width='stretch'):
    if sub_code and sub_name and section:
      try:
        create_subject(sub_code, sub_name, section, teacher_id)
        st.toast("Subject created successfully!", icon="✅")
        st.rerun()
      except Exception as e:
        st.toast(f"Error creating subject: {str(e)}", icon="❌")
    else:
      st.toast("Please fill in all fields.", icon="❌")