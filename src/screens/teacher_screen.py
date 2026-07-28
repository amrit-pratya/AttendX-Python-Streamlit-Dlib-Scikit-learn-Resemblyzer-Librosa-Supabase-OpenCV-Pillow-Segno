import streamlit as st

from src.screens.ui.base_layout import style_base_layout,style_bg_dashboard

from src.screens.components.header import header_db

from src.screens.components.footer import footer_home

from src.database.db import check_teacher_exists, create_teacher, teacher_login

def teacher_screen():
    #st.title("Teacher Screen")
    #st.write("Welcome, Teacher! Here you can manage your classes and students.")
    
    style_bg_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


def teacher_dashboard():
    c1, c2 = st.columns(2,vertical_alignment='center', gap="xxlarge")
    with c1:
        header_db()

    with c2:
        if st.button("Go back to Home", type="secondary", icon="🏠", icon_position="right", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header(f"Welcome, {st.session_state.teacher_data['name']}!", text_alignment="center")
    st.space()
    st.write("Here you can manage your classes and students.")
    # Add more functionality for the teacher dashboard here

    footer_home()

def login_teacher(username, password):
    if not username or not password:
        return False
    teacher = teacher_login(username, password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False

def teacher_screen_login():
    #st.title("Teacher Screen")
    #st.write("Welcome, Teacher! Here you can manage your classes and students.")
    
    c1, c2 = st.columns(2,vertical_alignment='center', gap="xxlarge")
    with c1:
        header_db()

    with c2:
        if st.button("Go back to Home", type="secondary", icon="🏠", icon_position="right", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Login using Password", text_alignment="center")
    st.space()
    teacher_username = st.text_input("Enter username", placeholder="Enter your username")
    teacher_password = st.text_input("Enter password", type="password", placeholder="Enter your password")

    st.divider()

    btc1, btc2 = st.columns(2, gap="large")
    with btc1:
        if st.button("Login", icon=':material/passkey:', icon_position="right", shortcut="control+enter", width='stretch'):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Login successful!", icon="✅")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.toast("Invalid username or password.", icon="❌")
    with btc2:
        if st.button("Register Instead",type="primary", icon=':material/passkey:', icon_position="right", width='stretch'):
            st.session_state.teacher_login_type = 'register'
            st.rerun()
    footer_home()


def register_teacher(username, password, confirm_password, name):
    if not username or not password or not confirm_password or not name:
        return False, "Please fill in all fields."

    if password != confirm_password:
        return False, "Passwords do not match."

    if check_teacher_exists(username):
        return False, "Username already exists. Please choose a different username."

    try:
        create_teacher(username, password, name)
        return True, "Teacher registered successfully."
    except Exception as e:
        return False, f"Error occurred while registering teacher: {str(e)}"

def teacher_screen_register():
    c1, c2 = st.columns(2,vertical_alignment='center', gap="xxlarge")
    with c1:
        header_db()

    with c2:
        if st.button("Go back to Home", type="secondary", icon="🏠", icon_position="right", key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    st.header("Register as Teacher", text_alignment="center")

    st.space()
    teacher_username = st.text_input("Enter username", placeholder="Enter your username")

    teacher_name = st.text_input("Enter your name", placeholder="Enter your name")

    teacher_password = st.text_input("Enter password", type="password", placeholder="Enter your password")

    teacher_confirm_password = st.text_input("Confirm password", type="password", placeholder="Confirm your password")

    st.divider()

    btc1, btc2 = st.columns(2, gap="large")
    with btc1:
        if st.button("Register now", icon=':material/passkey:', icon_position="right", shortcut="control+enter", width='stretch'):
            success, message = register_teacher(teacher_username, teacher_password, teacher_confirm_password, teacher_name)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
    with btc2:
        if st.button("Login Instead",type="primary", icon=':material/passkey:', icon_position="right", width='stretch'):
            st.session_state.teacher_login_type = 'login'
            st.rerun()


    footer_home()


