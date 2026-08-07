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




def subject_card2(
    subject_code,
    subject_name,
    section,
    attended_classes,
    total_classes,
    footer_callback=None
):

    with st.container(border=True):

        st.subheader(subject_name)

        c1, c2 = st.columns(2)

        with c1:
            st.caption("Subject Code")
            st.info(subject_code)

        with c2:
            st.caption("Section")
            st.success(section)

        st.divider()

        s1, s2 = st.columns(2)

        with s1:
            st.metric(
                "✅ Attended",
                attended_classes
            )

        with s2:
            st.metric(
                "📅 Total Classes",
                total_classes
            )

        if total_classes > 0:
            percentage = attended_classes / total_classes * 100
            st.progress(percentage / 100)
            st.caption(f"Attendance: **{percentage:.1f}%**")

        st.divider()

        if footer_callback:
            footer_callback()

    st.write("")