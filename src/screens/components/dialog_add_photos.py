
'''
import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
import time


@st.dialog("Capture or upload photos")
def add_photos_dialog():
  st.write('Add classroom photos to scan for attendence')

  if 'photo_tab' not in st.session_state:
    st.session_state.photo_tab = 'camera'

  t1, t2 = st.columns(2)

  with t1:
    type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
    if st.button('Camera', type=type_camera, width='stretch'):
      st.session_state.photo_tab = 'camera' 

  with t2:
    type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
    if st.button('Upload photos', type=type_upload, width='stretch'):
      st.session_state.photo_tab = 'upload'

  if st.session_state.photo_tab == 'camera':
    cam_photo = st.camera_input('Take Snapshot', key='dialog_cam')
    if cam_photo:
      st.session_state.attendence_images.append(Image.open(cam_photo))
      st.toast('Photo Captured')
      st.rerun()

  if st.session_state.photo_tab == 'upload':
    uploaded_files = st.file_uploader('Choose image files', type=['jpg', 'png', 'jpeg'], accept_multiple_files=True, key='dialog_upload')

    if uploaded_files:
      for f in uploaded_files:
        st.session_state.attendence_images.append(Image.open(f))

      st.toast('Photo Uploaded Successfully!')
      st.rerun()

  st.divider()
  if st.button('Done', type='primary', width='stretch'):
    st.rerun()


'''

import streamlit as st
from PIL import Image


@st.dialog("Capture or upload photos", width="medium")
def add_photos_dialog():

    st.write("Add classroom photos to scan for attendance")

    # Initialize session state
    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    if "attendence_images" not in st.session_state:
        st.session_state.attendence_images = []

    # -------------------------
    # Camera / Upload tabs
    # -------------------------

    t1, t2 = st.columns(2)

    with t1:
        if st.button(
            "📷 Camera",
            type="primary" if st.session_state.photo_tab == "camera" else "secondary",
            width="stretch",
        ):
            st.session_state.photo_tab = "camera"

    with t2:
        if st.button(
            "📁 Upload photos",
            type="primary" if st.session_state.photo_tab == "upload" else "secondary",
            width="stretch",
        ):
            st.session_state.photo_tab = "upload"

    st.divider()

    # -------------------------
    # Camera
    # -------------------------

    if st.session_state.photo_tab == "camera":

        cam_photo = st.camera_input(
            "Take Snapshot",
            key="dialog_cam"
        )

        if cam_photo:

            image = Image.open(cam_photo)

            st.session_state.attendence_images.append(image)

            st.toast("📸 Photo captured successfully!")

            # DON'T call st.rerun() here

    # -------------------------
    # Upload
    # -------------------------

    elif st.session_state.photo_tab == "upload":

        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="dialog_upload",
        )

        if uploaded_files:

            # Prevent adding the same uploaded files repeatedly
            existing_names = st.session_state.get(
                "uploaded_file_names",
                set()
            )

            for file in uploaded_files:

                if file.name not in existing_names:

                    image = Image.open(file)

                    st.session_state.attendence_images.append(image)

                    existing_names.add(file.name)

            st.session_state.uploaded_file_names = existing_names

            st.toast("📤 Photos uploaded successfully!")

            # DON'T call st.rerun() here

    # -------------------------
    # Show uploaded photos
    # -------------------------

    if st.session_state.attendence_images:

        st.divider()

        st.write(
            f"**Photos selected:** "
            f"{len(st.session_state.attendence_images)}"
        )

        cols = st.columns(3)

        for i, image in enumerate(
            st.session_state.attendence_images
        ):
            with cols[i % 3]:
                st.image(
                    image,
                    width="stretch"
                )

    # -------------------------
    # Done
    # -------------------------

    st.divider()

    if st.button(
        "Done",
        type="primary",
        width="stretch",
    ):
        st.rerun()
