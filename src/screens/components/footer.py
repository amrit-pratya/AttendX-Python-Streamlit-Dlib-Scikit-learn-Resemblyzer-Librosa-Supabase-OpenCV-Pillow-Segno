import streamlit as st

def footer_home():
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            padding: 12px 0;
            text-align: center;
            color: dark-grey;
            font-size: 14px;
            background: transparent;
            z-index: 999;
        }
        </style>

        <div class="footer">
            <strong>© 2026 AttendX</strong><br>
            Powered by AI
        </div>
        """,
        unsafe_allow_html=True,
    )