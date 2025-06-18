import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Development Team", layout="wide")

# Load images
team_image = Image.open("assets/1.png")
supervisor_image = Image.open("assets/2.png")

# Header
st.markdown("<h1 style='text-align: center; color: #4B4B4B;'>👨‍💻 Meet Our Development Team</h1>", unsafe_allow_html=True)
st.markdown("---")

# Team Image
st.image(team_image, use_container_width=True, caption="Development Team Overview")

# Interactive Section
with st.expander("👥 View Team Roles and Responsibilities"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Gauri Pandhare")
        st.markdown("**Team Leader**  \n**(Developer & Tester)**")

        st.subheader("Pranav Pawale")
        st.text("Data Collection & Content Writer")

    with col2:
        st.subheader("Diya Tank")
        st.text("Frontend Developer")

        st.subheader("Onkar Jamdade")
        st.text("Frontend Developer")

    with col3:
        st.subheader("Nivedita Sindhagi")
        st.text("Chatbot Designer")

        st.subheader("Prathamesh Solankar")
        st.text("Gallery & Media Editor")

st.markdown("---")

# Supervisors Section
st.markdown("<h2 style='text-align: center; color: #4B4B4B;'>🧑‍🏫 Meet Our Supervisors</h2>", unsafe_allow_html=True)

# Supervisors Image
st.image(supervisor_image, use_container_width=True, caption="Project Supervisors")

# Details
with st.expander("📘 View Supervisor Roles"):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Prof. Viteshkumar Gaikwad")
        st.text("Project Guide")

    with col2:
        st.subheader("Dr. Shriniwas Metan")
        st.text("Project Mentor")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by Our Dev Team</p>", unsafe_allow_html=True)
