import streamlit as st

def subject_card(subject_code, subject_name, section,
                 total_students,
                 total_classes,
                 footer_callback=None):

    with st.container(border=True):

        # Subject title
        st.subheader(subject_name)

        # Subject information
        col1, col2 = st.columns([1, 1])

        with col1:
            st.caption("Subject Code")
            st.info(subject_code)

        with col2:
            st.caption("Section")
            st.success(section)

        st.divider()

        # Statistics
        stat1, stat2 = st.columns(2)

        with stat1:
            st.metric(
                label="👥 Students",
                value=total_students
            )

        with stat2:
            st.metric(
                label="📅 Classes",
                value=total_classes
            )

        st.divider()

        # Footer button
        if footer_callback:
            footer_callback()

    st.write("")