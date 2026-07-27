import streamlit as st

def header_home():
    # st.title("AttendX")
    # st.write("Welcome to the AttendX! Please log in as a Teacher or Student.")
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png" 
    
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 20px;">
            <img src="{logo_url}" width="100" height="100">
            <h1 style="display: inline-block; vertical-align: middle; margin-left: 10px;">
                <span style="color: #2C2D2D">Attend</span><span style="color:#E53935;">X</span>
            </h1>
        </div>
    """, unsafe_allow_html=True)


def header_db():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin: 20px 0 30px 0;
        ">
            <img src="{logo_url}" width="75" height="75">
            <h2 style="
                margin: 0;
                color: dark-grey;
                font-size: 48px;
                font-weight: 700;
            ">
                <span style="color: dark-grey">Attend</span><span style="color:#E53935;">X</span>
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )