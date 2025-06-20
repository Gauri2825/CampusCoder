import streamlit as st
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageFilter
import io
import base64
from utils.file import footer

st.set_page_config(page_title="Infrastructure | NKOCET", layout="wide")

# Function to set blurred background
def set_blurred_background(image_path, blur_radius=5):
    try:
        img = Image.open(image_path)
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
        buffered = io.BytesIO()
        blurred_img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        st.markdown(
            """
            <style>
            .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), #22223b;
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            }
            .main .block-container {
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 3rem;
            margin-top: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            h1 {
            color: #FFD700 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
            }
            h2 {
            color: #00BFFF !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
            }
            h3 {
            color: #90EE90 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
            }
            .stMarkdown p, .stMarkdown li {
            color: white !important;
            font-size: 1.1rem;
            line-height: 1.6;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        st.error(f"Error setting background: {e}")

set_blurred_background("assets/header_img4.jpg", blur_radius=10)

# 🌟 Main Header
st.header("🎗️ World-Class Infrastructure", divider='rainbow')

@st.cache_data(ttl=3600)
def get_infrastructure_data():
    try:
        url = "https://www.orchidengg.ac.in/"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        highlights = []
        infra_section = soup.find('section', {'id': 'infrastructure'}) or soup.find('div', class_='infra')
        if infra_section:
            items = infra_section.find_all('li') or infra_section.find_all('p')
            highlights = [item.get_text(strip=True) for item in items][:6]
        return {
            'highlights': highlights or [
                "15-acre lush green campus",
                "Smart classrooms & seminar halls",
                "500+ capacity auditorium",
                "High-speed WiFi throughout campus",
                "Modern cafeteria with multiple cuisines",
                "24/7 medical and stationary facilities"
            ]
        }
    except requests.RequestException:
        return None

with st.container():
    data = get_infrastructure_data()

    # 📌 Subheader
    st.subheader("🏛️ Campus Highlights")

    if data:
        st.markdown("\n".join([f"<div style='margin-bottom: 0.5rem; color: white;'>• {item}</div>" for item in data['highlights']]), unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style='margin-bottom: 0.5rem; color: white;'>• 15-acre lush green campus</div>
        <div style='margin-bottom: 0.5rem; color: white;'>• Smart classrooms & seminar halls</div>
        <div style='margin-bottom: 0.5rem; color: white;'>• 500+ capacity auditorium</div>
        <div style='margin-bottom: 0.5rem; color: white;'>• High-speed WiFi throughout campus</div>
        <div style='margin-bottom: 0.5rem; color: white;'>• Modern cafeteria with multiple cuisines</div>
        <div style='margin-bottom: 0.5rem; color: white;'>• 24/7 medical and stationary facilities</div>
        """, unsafe_allow_html=True)

# Spacer
st.markdown("""<div style="height: 40px;"></div>""", unsafe_allow_html=True)

# 📸 Explore Section
st.subheader("📸 Explore Our Campus")

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h3 style="margin-bottom: 1.5rem;">Take a Virtual Tour of Our World-Class Facilities</h3>
        <a href="https://orchid85.pixieset.com/infrastrucuture/" target="_blank" style="text-decoration: none;">
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
                🏛️ Explore Infrastructure Gallery ➔
            </button>
        </a>
        <p style="color: #e2e8f0; margin-top: 10px; font-size: 14px; font-style: italic;">Click to view our photo gallery in a new window</p>
    </div>
    """, unsafe_allow_html=True)

# Final Spacer
st.markdown("""<div style="height: 40px;"></div>""", unsafe_allow_html=True)
footer()