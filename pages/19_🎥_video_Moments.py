import streamlit as st
from PIL import Image
from utils.file import footer

# Set page config
st.set_page_config(page_title="🎥 Video Moments | Campus Coder", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .header {
        font-size: 45px !important;
        font-weight: 700 !important;
        color: #E50914 !important;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        font-family: 'Segoe UI', sans-serif;
    }
    .subheader {
        font-size: 20px !important;
        color: #555;
        text-align: center;
        margin-bottom: 40px;
        font-style: italic;
    }
    .card {
        background-color: #fff;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        text-align: center;
        transition: all 0.3s ease-in-out;
        cursor: pointer;
        height: 100%;
        border: 2px solid transparent;
    }
    .card:hover {
        transform: scale(1.03);
        border-color: #FF0000;
    }
    .card-title {
        font-size: 22px;
        font-weight: bold;
        color: #E50914;
        margin-top: 10px;
    }
    .card-description {
        font-size: 16px;
        color: #555;
        margin: 10px 0;
    }
    .youtube-icon {
        font-size: 50px;
        color: #FF0000;
    }
    .footer-note {
        text-align: center;
        font-size: 16px;
        color: #6C757D;
        margin-top: 30px;
    }
    a.card-link {
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="header">🎥 Video Moments</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Click on a card below to visit our official YouTube channels and explore campus memories!</p>', unsafe_allow_html=True)

# YouTube links
campus_coder_url = "https://www.youtube.com/@CampusCoder-s5t"
nkocet_url = "https://www.youtube.com/@NKOCETSOLAPUR"

# Card Columns
col1, col2 = st.columns(2)

# Campus Coder Card
with col1:
    st.markdown(f"""
    <a href="{campus_coder_url}" target="_blank" class="card-link">
        <div class="card">
            <div class="youtube-icon">🎬</div>
            <div class="card-title">Campus Coder Channel</div>
            <div class="card-description">Explore for more incredible moments through Videos and Photos.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# NKOCET Channel Card
with col2:
    st.markdown(f"""
    <a href="{nkocet_url}" target="_blank" class="card-link">
        <div class="card">
            <div class="youtube-icon">🏫</div>
            <div class="card-title">NKOCET  Channel</div>
            <div class="card-description">Explore official college events, academic activities, and inspirational moments.</div>
        </div>
    </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer-note">Don’t forget to like, comment, and subscribe! 🔔</div>', unsafe_allow_html=True)
st.markdown("---")
footer()
