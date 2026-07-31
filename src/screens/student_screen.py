import streamlit as st
import numpy as np
from PIL import Image

from src.screens.ui.base_layout import style_base_layout,style_bg_dashboard

from src.screens.components.header import header_db

from src.screens.components.footer import footer_home

from src.database.db import check_teacher_exists, create_teacher, teacher_login


def student_screen():
    #st.title("Student Screen")
    #st.write("Welcome, Student! Here you can view your classes and attendance.")
    # Add more functionality for the student screen here

    style_bg_dashboard()
    style_base_layout()


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

    photo_source = st.camera_input("Position your face in front of the camera and click on the button below to capture your image.", key="student_camera_input")

    if photo_source:
        np.array(Image.open(photo_source))  # Convert the captured image to a NumPy array
    footer_home()