import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Placements | NKOCET", layout="wide")

# Custom CSS for better spacing and styling
st.markdown("""
<style>
    .metric-card {
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    }
    .highlight-box {
        border-left: 4px solid #4b8df8;
        padding-left: 15px;
        margin: 10px 0;
    }
    .placement-link {
        display: inline-block;
        padding: 10px 18px;
        background: #4b8df8;
        color: #fff !important;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        margin-top: 16px;
        transition: background 0.2s;
    }
    .placement-link:hover {
        background: #2563c9;
        color: #fff !important;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)
# Placement Video Section
st.markdown("""
<div class="highlight-box">
<h4>🎥 Placement Cell Introduction Video</h4>
</div>
""", unsafe_allow_html=True)
video_url = "https://youtu.be/xtI-O-L3oJo?si=msxZSbuloVHnlgSB"
st.video(video_url)
# Placement Team Section
with st.expander("👥 Placement Team"):
    st.markdown("""
    <div class="highlight-box">
    <h4>Meet the Placement Team</h4>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - **Dr. R . R. Patil** – (DEAN) Training & Placement Officer  
    - **Prof. A. K. Ohol** – Aptitude Trainer
    - **Dr. U. K. Jadhav** – Softskill Trainer
    - **Dr. M. S. Shaikh** – Softskill Trainer
    - **Prof. S. D. Dudhanikar** – Placement Coordinator (CSE)  
    - **Prof. N. B. Aherwadi** – Placement Coordinator (AI & DS)  
    - **Prof. A. Pushpan**  – Placement Coordinator (ENTC)  
    - **Prof. Y. Patil** – Placement Coordinator (Mech)  
    - **Prof. J. B. Patil** – Placement Coordinator (Electrical)  
    - **Prof. R. G. Maske** – Placement Coordinator (Civil)  
    """)

st.header("💼 Placement Cell", divider='rainbow')
st.subheader("📝 PPW (PrePlacement Workshop)")# Add a local placement image
local_image_path = r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\placement.jpg"  # Update with your actual image filename
st.image(local_image_path, caption="Recent Placement Event", use_container_width=True)

# Section 1: Key Metrics
st.subheader("📊 Placement Highlights")
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("#### 📈 Placement Offers (Last 5 Years)")
        st.markdown("""
        | Year      | Offers |
        |-----------|--------|
        | 2020–21   | 474    |
        | 2021–22   | 450    |
        | 2022–23   | 421    |
        | 2023–24   | 441    |
        | 2024–25   | 436*   |
        """)
        st.caption("*Ongoing process")

with col2:
    with st.container(border=True):
        st.markdown("#### 🎯 Branch-wise Placement (2024–25)")
        st.markdown("""
        | Branch                         | Students Placed |
        |--------------------------------|------------------|
        | Computer Science & Engineering | 124              |
        | AI & Data Science              | 50               |
        | Electronics & Telecomm. Engg.  | 60               |
        | Mechanical Engineering         | 102              |
        | Electrical Engineering         | 51               |
        | Civil Engineering              | 51               |
        | **Total**                      | **438***         |
        """)

with col3:
    with st.container(border=True):
        st.markdown("#### 🏢 Top Recruiters (Last 5 Years)")
        st.markdown("""
        | Company          | Offers |
        |------------------|--------|
        | TIAA             | 68     |
        | ZenSar           | 38     |
        | Infosys          | 158    |
        | Wipro            | 62     |
        | Persistent       | 56     |
        | Accenture        | 44     |
        | Capgemini        | 49     |
        | Cognizant        | 58     |
        | LTI              | 62     |
        | TCS              | 258    |
        """)
        
tab1, tab2 = st.tabs(["📋 Placement Process", "🛠️ Career Support"])

with tab1:
    st.markdown("""
    <div class="highlight-box">
    <h4>Placement Process Overview</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    1. **Registration:** Eligible students register for campus placements at the start of the academic year.
    2. **Pre-Placement Talks:** Companies conduct sessions to explain job roles, growth opportunities, and selection process.
    3. **Aptitude & Technical Tests:** Shortlisting through online/offline assessments.
    4. **Group Discussions & Interviews:** Evaluation of communication, technical, and problem-solving skills.
    5. **Offer Letters:** Selected students receive offer letters and guidance for onboarding.
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>Eligibility Criteria</h4>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Minimum academic percentage as specified by recruiters
    - No active backlogs (unless specified)
    - Good communication and interpersonal skills
    """)
    
    st.markdown("""
    <div class="highlight-box">
    <h4>Key Highlights</h4>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    - Multiple job offers for eligible students
    - Opportunities in core and IT sectors
    - Regular training and skill development sessions
    """)

with tab2:
    st.markdown("""
    <div class="metric-card">
    <h4>Comprehensive Career Support Services</h4>
    <ul>
        <li>Aptitude & technical training</li>
        <li>Mock interviews and resume building</li>
        <li>Internship & placement guidance</li>
        <li>Industry interaction and coding sessions</li>
        <li>Alumni mentoring</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Section 3: Visual Element
st.subheader("📸 PPW (PrePlacement Workshop)")

st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <h3 style="margin-bottom: 1.5rem;">Explore Our Student Placement Journey</h3>
    <a href="https://thecampuscoder.pixieset.com/ppwpreplacementworkshop/" target="_blank" style="text-decoration: none;">
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
            🎓 View Placement Activities ➔
        </button>
    </a>
    <p style="color: #6c757d; margin-top: 10px; font-size: 14px; font-style: italic;">
        Click to view our full placement gallery in a new window
    </p>
</div>
""", unsafe_allow_html=True)


# Section 4: Contact Information
st.markdown("---")
st.subheader("📞 Contact the Placement Cell")
contact_col1, contact_col2 = st.columns(2)

with contact_col1:
    st.markdown("""
    **Phone Numbers:**  
    - 2172990051    
    """)

with contact_col2:
    st.markdown("""
    **Email:**  
    office@orchidengg.ac.in 
    
    **Office Hours:**  
    9:00 AM - 5:00 PM (Mon-Fri)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 10px;">
    <p>© 2025 Nagesh Karajagi Orchid College of Engineering & Technology, Solapur</p>
</div>
""", unsafe_allow_html=True)
footer()