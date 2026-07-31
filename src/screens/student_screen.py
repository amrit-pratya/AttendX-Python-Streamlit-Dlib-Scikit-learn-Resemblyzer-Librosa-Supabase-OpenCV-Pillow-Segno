import streamlit as st
import numpy as np
import time
from PIL import Image

from src.screens.ui.base_layout import style_base_layout,style_bg_dashboard

from src.screens.components.header import header_db

from src.screens.components.footer import footer_home

from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_all_students, create_student

from src.pipelines.face_pipeline import predict_attendence, get_face_embeddings, train_classifier

from src.pipelines.voice_pipeline import get_voice_embedding


def student_dashboard():
    st.header('Dashboard Here!')

def student_screen():
    #st.title("Student Screen")
    #st.write("Welcome, Student! Here you can view your classes and attendance.")
    # Add more functionality for the student screen here

    style_bg_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2,vertical_alignment='center', gap="xxlarge")
    with c1:
        header_db()

    with c2:
        if st.button("Go back to Home", type="secondary", icon="🏠", icon_position="right", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login using FaceID", text_alignment="center")
    st.space()
    st.space()

    show_registration = False

    photo_source = st.camera_input("Position your face in front of the camera and click on the button below to capture your image.", key="student_camera_input")

    if photo_source:
        img = np.array(Image.open(photo_source))  # Convert the captured image to a NumPy array

        with st.spinner('AttendX is scanning..'):
            detected, all_ids, num_faces = predict_attendence(img)

            if num_faces == 0:
                st.warning('Face not found!')

            elif num_faces > 1:
                st.warning('Multiple faces found!')
            else:
                if detected:
                   student_id = list(detected.keys())[0]
                   all_students = get_all_students()

                   student = next(s for s in all_students if s['student_id'] == student_id)
                   if student:
                       st.session_state.is_logged_in = True
                       st.session_state.user_role = 'student'
                       st.session_state.student_data = student
                       st.toast(f'Welcome back {student['name']}')
                       time.sleep(1)
                       st.rerun()
                else:
                    st.info("Face not recognized! You might be a new student.")
                    show_registration = True
        if show_registration:
            with st.container(border=True):
                st.header('Register new Profile')
                new_name = st.text_input("Enter your name", placeholder='E.g. Ryan Butcher')

                st.subheader('Optional : Voice Enrollment')
                st.info("Enroll your for voice only attendence")

                audio_data = None

                try:
                    audio_data = st.audio_input('Record a short phrase like I am present, My name is Bruce Wayne.')
                except Exception:
                    st.error('Audio data failed!')

                if st.button('Create Account', type='primary'):
                    if new_name:
                        with st.spinner('Creating profile..'):
                            img = np.array(Image.open(photo_source))
                            encoding = get_face_embeddings(img)
                            if encoding:
                                face_emb = encoding[0].tolist()

                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())
                                response_data = create_student(new_name, face_embedding=face_emb, voice_embedding = voice_emb)

                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = 'student'
                                    st.session_state.student_date = response_data[0]
                                    st.toast(f"Profile created. Hi! {new_name}")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error("Couldn't capture your facial features for registration.")
                    else:
                        st.warning('Please enter your name!')
    footer_home()