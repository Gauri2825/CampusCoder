import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Achievements | NKOCET", layout="wide")

st.header("🏆 Student Achievements", divider='rainbow')

st.subheader("🎓 Academic Excellence")
st.markdown("""
- University toppers  
- Research papers & patents  
- Scholarships & grants  
- GSOC selections
- International conference presentations
- Hackathon winners
- Competitive exam qualifiers
- MaTPO Winners
- Inter-college quiz champions
and more! 
""")

st.subheader("🏅 Extracurricular Achievements")
st.markdown("""
- National debate winners  
- Sports & cultural champs  
- Social innovation awards
""")
# Button to view achievements
st.markdown("""
<div style="text-align: center; margin-top: 30px;">
    <a href="https://thecampuscoder.pixieset.com/thecampuscoder/" target="_blank">
        <button style="background-color: #4CAF50; color: white; padding: 12px 24px; border: none; border-radius: 4px; font-size: 16px; cursor: pointer;">
           SEE THE ACHIEVEMENTS (📸ORCHID CHAMPPIONS)
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

footer()