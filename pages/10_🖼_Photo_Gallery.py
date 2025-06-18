import streamlit as st
from PIL import Image
import base64
from utils.file import footer

st.set_page_config(page_title="Photo Gallery | NKOCET", layout="wide")

def get_base64_of_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Load background image
try:
    image_path = r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\image.jpg"
    image_base64 = get_base64_of_image(image_path)
    background_style = f"background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), url('data:image/png;base64,{image_base64}');"
except:
    SAMPLE_IMAGE_URL = "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80"
    background_style = f"background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), url('{SAMPLE_IMAGE_URL}');"

GALLERY_URL = "https://campuscoders.pixieset.com/orchathon2025-1/"

# Enhanced CSS
st.markdown(f"""
<style>
body {{
    background-color: #f0f4f8;
    margin: 0;
}}
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lora:wght@400;700&family=PT+Serif:wght@400;700&family=Dancing+Script:wght@400;700&display=swap');

h1, .gallery-content p {{
    font-family: 'Playfair Display', 'Lora', 'PT Serif', 'Dancing Script', cursive, serif !important;
    letter-spacing: 0.03em;
}}
h1 {{
    color: #6e8efb;
    font-weight: 700;
    font-size: 3em;
    margin-bottom: 0.2em;
}}

p {{
    font-size: 1.2rem;
    color: #f1f1f1;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.6);
}}

.header {{
    text-align: center;
    margin-top: 2rem;
}}

.gallery-container {{
    position: relative;
    height: 70vh;
    min-height: 500px;
    border-radius: 20px;
    {background_style}
    background-size: cover;
    background-position: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
    overflow: hidden;
    animation: fadeIn 2s ease;
}}

@keyframes fadeIn {{
    0% {{ opacity: 0; transform: translateY(20px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}

.gallery-content {{
    text-align: center;
    color: white;
    padding: 2rem;
    max-width: 800px;
}}

.open-gallery-button {{
    background: linear-gradient(270deg, #6e8efb, #a777e3, #fc67fa, #6e8efb);
    background-size: 800% 800%;
    animation: gradientFlow 10s ease infinite;
    border: none;
    padding: 1rem 2.5rem;
    font-size: 1.5rem;
    font-weight: 700;
    border-radius: 50px;
    color: white;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    box-shadow: 0 6px 15px rgba(0,0,0,0.3);
    cursor: pointer;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    text-decoration: none;
}}

.open-gallery-button:hover {{
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
}}

@keyframes gradientFlow {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header">
    <h1>🎉 College Photo Gallery</h1>
    <p style="
        font-size: 1.2rem;
        font-weight: 600;
        color: #2c2c2c;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.7), 0px 0px 2px rgba(0,0,0,0.4);
    ">
        Explore our vibrant collection of memorable moments & joyful events
    </p>
</div>
""", unsafe_allow_html=True)

# Gallery Section
st.markdown(f'''
<div class="gallery-container">
    <div class="gallery-content">
        <p style="font-size: 1.3rem; font-weight: 600;  font-family: "Playfair Display", serif;">✨ High-resolution memories from NKOCET’s campus life ✨</p>
        <a href="{GALLERY_URL}" target="_blank">
            <button class="open-gallery-button">📸 View Stunning Gallery</button>
        </a>
    </div>
</div>
''', unsafe_allow_html=True)

# Footer
st.markdown("""
<style>
.footer-black {
    background: #111;
    color: #fff !important;
    padding: 1rem 0;
    text-align: center;
    border-radius: 0 0 20px 20px;
    margin-top: -24px;
    font-size: 1rem;
}
</style>
<div class="footer-black">
    © 2025 NKOCET Photo Gallery · All Rights Reserved
</div>
""", unsafe_allow_html=True)

footer()