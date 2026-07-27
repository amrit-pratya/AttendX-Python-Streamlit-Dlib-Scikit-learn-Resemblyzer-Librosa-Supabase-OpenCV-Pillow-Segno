import streamlit as st

def header_home():
    # st.title("AttendX")
    # st.write("Welcome to the AttendX! Please log in as a Teacher or Student.")
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png" 
    
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 20px;">
            <img src="{logo_url}" width="100" height="100">
            <h1 style="display: inline-block; vertical-align: middle; margin-left: 10px;">AttendX</h1>
        </div>
    """, unsafe_allow_html=True)