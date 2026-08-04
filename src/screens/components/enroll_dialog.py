import streamlit as st
from src.database.db import create_students
from src.database.config import supabase


@st.dialog("Enroll in Subject", icon=":material/class:")
def enroll_dialog():
  st.write("Enter the subject code provided by your teacher to enroll.")
  join_code = st.text_input("Subject Code", placeholder="CS101", max_chars=10, key="join_code_input", width="stretch")

  if st.button("Enroll", type="primary", icon="➕", icon_position="right", width="stretch"):
    if join_code:
      res = supabase.table("subjects").select("subject_id, name, subject_code").eq("subject_code", join_code).execute()
      if res.data:
          subject = res.data[0]
          student_id = st.session_state.student_data['student_id']

          check = supabase.table('subject_students').select("*").eq("subject_id", subject['subject_id']).eq("student_id", student_id).execute()
          message = create_students(student_id, subject['subject_code'])
          if message == "Student enrolled successfully.":
              st.success(message)
              st.session_state.student_data['enrolled_subjects'].append(subject)
              st.rerun()
      else:
          st.error(message)
    else:
        st.warning("Please enter a valid subject code.")