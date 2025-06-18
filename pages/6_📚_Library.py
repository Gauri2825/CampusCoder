import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Central Library | NKOCET", layout="wide")

st.header("📚 NKOCET CENTRAL LIBRARY", divider='rainbow')

# Library Video Tour
st.subheader("🎥 Library Video Tour")
st.video("https://youtu.be/zaMhr3EfHiE?si=HH-iFNo8EIsEZy0o")  # Replace with actual library video link if available


# Library Overview
st.subheader("🏛️ About the Library")
st.markdown("""
The **Central Library** at NKOCET is the heart of the institute and a temple of knowledge that plays a vital role in curricular development. As an invaluable resource center for Engineering and Management, it serves students and faculty members with a comprehensive collection of materials.

*"Engineering is the profession in which knowledge of the mathematical and natural sciences, gained by study, experience and practice, is applied with judgment to develop ways to utilize economically the materials and forces of nature for the benefit of mankind."*  
*— Engineers Council for Professional Development*
""")

# Key Features
st.subheader("✨ Key Features")
st.markdown("""
- **Computerized Library** using DELPLUS automation software
- **Bar-coding technology** for efficient circulation
- **Dewey Decimal Classification (DDC)** system for organization
- **Anglo American Cataloguing Rules II** for cataloguing
- **Multiple specialized sections** serving diverse needs
""")

# Library Sections
st.subheader("📚 Library Sections")
cols = st.columns(3)
with cols[0]:
    st.markdown("""
    - Ekeeda Digital Library Platform
    - The Circulation Section
    - The Periodical Section
    """)
with cols[1]:
    st.markdown("""
    - The Stack Area
    - The Reference Section
    - Personality Development Section
    """)
with cols[2]:
    st.markdown("""
    - The Media Resource Centre
    - Newspaper Section
    - Reprography Section
    - Reading Room Section
    - Internet Resources Centre
    """)

# Location and Facilities
st.subheader("📍 Location & Facilities")
st.markdown("""
- **Location:** First floor of the A building
- **Built-up area:** 10,000 sq. ft.
- **Reading hall capacity:** 250 students
""")

# Working Hours
st.subheader("🕒 Working Hours")
st.markdown("""
- **Monday - Saturday:** 10:00 AM – 5:00 PM
- **Monday - Saturday:** 5.30 PM – 11.00 PM (hostellers)
- **Sunday:** Closed  
*Hours may vary during exams and holidays*
""")

# Additional Information
st.subheader("ℹ️ Additional Information")
st.markdown("""
NKOCET is a reputed institute conducting Engineering & Management courses affiliated to Solapur University, Solapur.  
The central library serves as a knowledge resource center for all academic programs.
""")

footer()