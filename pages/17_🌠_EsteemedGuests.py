import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Special Visits | NKOCET", layout="wide")

# Enhanced CSS
st.markdown(f"""
<style>
body {{
    background-color: #f0f4f8;
    margin: 0;
}}
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Lora:wght@400;700&family=PT+Serif:wght@400;700&family=Dancing+Script:wght@400;700&display=swap');

h1, h2, .gallery-content p {{
    font-family: 'Playfair Display', 'Lora', 'PT Serif', 'Dancing Script', cursive, serif !important;
    letter-spacing: 0.03em;
}}
h1 {{
    color: #6e8efb;
    font-weight: 700;
    font-size: 3em;
    margin-bottom: 0.2em;
}}

h2 {{
    color: #4a4a4a;
    font-weight: 600;
    font-size: 2em;
    margin-top: 1.5em;
    border-bottom: 2px solid #6e8efb;
    padding-bottom: 0.3em;
    display: inline-block;
}}

.visit-card {{
    background-color: white;
    border-radius: 15px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    height: 100%;
}}

.visit-card:hover {{
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}}

.visit-title {{
    color: #6e8efb;
    font-weight: 700;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}}

.visit-description {{
    color: #4a4a4a;
    font-size: 1.1rem;
    line-height: 1.6;
}}

.header {{
    text-align: center;
    margin-top: 2rem;
}}

.columns-container {{
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}}

.column {{
    flex: 1;
    min-width: 300px;
}}
</style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header">
    <h1>🌟Esteemed Guests at NKOCET</h1>
    <p style="
        font-size: 1.2rem;
        font-weight: 600;
        color: #2c2c2c;
        text-shadow: 1px 1px 3px rgba(255,255,255,0.7), 0px 0px 2px rgba(0,0,0,0.4);
    ">
        Honoring the legendary figures who inspired our students
    </p>
</div>
""", unsafe_allow_html=True)

# Special Visits Section
st.markdown("""
<h2>🎤 Special Visits to Orchid Campus</h2>
""", unsafe_allow_html=True)

# Two-column layout for visit cards
col1, col2 = st.columns(2)

with col1:
    # Visit 1 - Dr. APJ Abdul Kalam
    st.markdown("""
    <div class="visit-card">
        <div class="visit-title">Hon. Ex President Dr. A P J Abdul Kalam's Visit to Orchid Campus</div>
        <div class="visit-description">
            It was a moment of great pride for our institution when the beloved "People's President", 
            Dr. A P J Abdul Kalam graced our campus with his presence. His visionary thoughts on education, 
            innovation, and youth empowerment continue to guide our institution's philosophy.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Visit 3 - Mr. Shriv Khera
    st.markdown("""
    <div class="visit-card">
        <div class="visit-title">Mr. Shriv Khera's Visit to Orchid Campus</div>
        <div class="visit-description">
            We were honored to host Mr. Shriv Khera, a renowned motivational speaker and leadership coach, 
            at our Orchid Campus. His inspiring session on personal development and leadership left an 
            indelible mark on our students and faculty members alike.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    # Visit 2 - Sindhutai Sapkal
    st.markdown("""
    <div class="visit-card">
        <div class="visit-title">Sindhutai Sapkal's Visit to Orchid Campus</div>
        <div class="visit-description">
            We were privileged to welcome the legendary "Mother of Orphans", Sindhutai Sapkal to our campus. 
            Her life journey of resilience and compassion deeply moved everyone present. Her message about 
            the power of education to transform lives resonated strongly with our students.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Empty card for balance (or add another visit if available)
    st.markdown("""
    <div class="visit-card">
        <div class="visit-title">More Inspiring Visits</div>
        <div class="visit-description">
            Our campus continues to welcome distinguished personalities from various fields who share 
            their wisdom and experiences with our students. Watch this space for updates on future visits!
        </div>
    </div>
    """, unsafe_allow_html=True)

st.subheader("📸 Bold Personality Visited")

st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <a href="https://thecampuscoder49.pixieset.com/boldpersonalities/" target="_blank" style="text-decoration: none;">
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
            View Our Amazing Moments ➔
        </button>
    </a>
    <p style="color: #6c757d; margin-top: 10px; font-size: 14px; font-style: italic;">
        Click to view our Memoriable Moments in a new window
    </p>
</div>
""", unsafe_allow_html=True)


# Footer
st.markdown("""
<style>
.footer-black {
    background: #111;
    color: #fff !important;
    padding: 1rem 0;
    text-align: center;
    border-radius: 0 0 20px 20px;
    margin-top: 2rem;
    font-size: 1rem;
}
</style>
<div class="footer-black">
    © 2025 NKOCET · All Rights Reserved
</div>
""", unsafe_allow_html=True)

footer()