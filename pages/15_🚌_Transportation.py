import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Transport Facilities | NKOCET", layout="wide")

st.markdown("""
<style>
    .highlight-box {
        border-left: 4px solid #4b8df8;
        padding-left: 15px;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)

st.header("🚌 Transport Facilities", divider='rainbow')

cols = st.columns(2)

with cols[0]:
    st.markdown("""<div class="highlight-box"><h4>College Bus Services</h4></div>""", unsafe_allow_html=True)
    st.markdown("""
    - **5+ buses** for Solapur city  
    - **Morning/evening trips** as per class schedule  
    - **Special exam buses** with extra hours  
    - **Affordable monthly passes**  
    - **Bus routes cover all major areas**
                """)
# Fee Structure Download Section
st.subheader("💸 Transport Fee Structure", divider='gray')

fee_file_path = r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\Bus Charges for AY 2024-25.pdf"

with cols[1]:
    st.image(
        r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\Transportation.jpg",
        caption="NKOCET College Bus",
        use_container_width=True
    )

with open(fee_file_path, "rb") as file:
    st.download_button(
        label="📥 Download Bus Fee Structure (PDF)",
        data=file,
        file_name="transport_fee_structure.pdf",
        mime="application/pdf"
    )


# st.markdown(f"*{route['stops']}*")

st.subheader("📞 Contact", divider='gray')
st.markdown("""<div class="highlight-box"><h4>Transport Incharge</h4></div>""", unsafe_allow_html=True)
st.markdown("""
**Patel Travels**  
📞 +91 9595881846 
""")

st.markdown("""<div class="highlight-box"><h4>Faculty Coordinator</h4></div>""", unsafe_allow_html=True)
st.markdown("""
**Prof. R. A. Patil**  
📞 +91 7774981989  
""")
st.markdown("<span style='font-size:0.95em; color:#666;'>Office: 10 AM – 5 PM (Mon–Sat)</span>", unsafe_allow_html=True)

st.markdown("""<div style="margin-top: 30px; font-size: 0.8em; color: #666;">Note: Bus timings may vary during exams or holidays.</div>""", unsafe_allow_html=True)
footer()