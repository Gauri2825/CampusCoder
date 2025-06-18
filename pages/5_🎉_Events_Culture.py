import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from utils.file import footer

# Set page configuration
st.set_page_config(page_title="Events & Culture | NKOCET", layout="wide")

# Header
st.header("🎉 Events & Campus Culture", divider='rainbow')

col1, col2 = st.columns(2)

with col1:
    # Events
    st.subheader("📅 Annual Events")
    st.markdown("""
    - 🌐 Technical Fest – Orchid Tech Week  
    - 🎭 Cultural Fest – Rainbow Festival  
    - ⚽ Sports Week – General Championship  
    - 🎤 Guest Lectures & Workshops  
    - 🎓 Project Exhibitions, Hackathons, Avishkar
    """)

with col2:
    # Clubs
    st.subheader("🎨 Clubs & Activities")
    st.markdown("""
    - Music, Dance, Drama, Photography  
    - Debate & Literary Societies  
    - Community Service Clubs
    """)

st.subheader("📸 EVENT GALLERY")

st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <h3 style="margin-bottom: 1.5rem;">Explore Our Incredible Moments</h3>
    <a href="https://campuscoders.pixieset.com/events/" target="_blank" style="text-decoration: none;">
        <button style="
            background: linear-gradient(135deg, #4b6cb7, #182848);
            color: white;
            padding: 18px 36px;
            font-size: 20px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
            font-weight: bold;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-width: 300px;
            margin-bottom: 1rem;
        ">
            🎓 View Event Moments ➔
        </button>
    </a>
    <p style="color: #6c757d; margin-top: 10px; font-size: 14px; font-style: italic;">
        Click to view our full event gallery in a new window
    </p>
</div>
""", unsafe_allow_html=True)
# Event Videos
st.subheader("🎬 Event Videos")
st.video("https://youtu.be/vnd-0VX5wcI?si=IN6v7rUuVVoZfsj4")
st.subheader("Annual Day Fest: Traditional Day")
st.video("https://youtu.be/ocf9zLCvyA0?si=i8Rh_4PyevoiPLLp")
st.subheader("Annual Day Fest: Rainbow")
st.video("https://youtu.be/QmC-6wwcoVM?si=1u3tc4c37hjKTFc1")

# Campus Info
st.markdown("---")
st.subheader("About Campus Life at NKOCET")
st.markdown("""
N.K. Orchid College of Engineering and Technology fosters a vibrant campus culture with:
- Regular technical and cultural events  
- Student-led clubs and committees  
- Industry interaction programs  
- Sports and wellness activities
""")

st.subheader("Recent Highlights")
st.markdown("""
- 🏆 Winners at national-level technical competitions  
- 🌍 International student exchange programs  
- 🤝 Industry collaborations for student projects  
- 🎤 Guest lectures from industry experts
""")

# Footer
footer()