import streamlit as st
from utils.file import footer

st.set_page_config(page_title="Hostel | NKOCET", layout="wide")

# Custom CSS for better styling
st.markdown("""
<style>
    .side-by-side {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
    }
    .card {
        flex: 1;
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .highlight {
        color: #4b8df8;
        font-weight: bold;
    }
    .contact-card {
        background-color: #e6f7ff;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    @media (max-width: 600px) {
        .side-by-side {
            flex-direction: column; /* Stack vertically on small screens */
        }
        .contact-card div {
            flex-direction: column; /* Stack contact details vertically */
        }
    }
</style>
""", unsafe_allow_html=True)

st.header("🏠 Hostel", divider='rainbow')

# Side by side layout for amenities and rules
st.subheader("Hostel Facilities")
col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("### 🏡 Hostel Amenities")
        st.markdown("""
        <div class="card">
        1. Separate boys & girls hostels<br>
        2. Hygienic mess with vegetarian/non-vegetarian options<br>
        3. 24/7 security at all times + CCTV surveillance<br>
        4. Spacious reading rooms and TV lounges<br>
        5. Laundry services available<br>
        6. Indoor games (carrom, chess, table tennis)<br>
        7. High-speed Wi-Fi connectivity<br>
        8. Regular housekeeping services<br>
        9. RO purified drinking water<br>
        10. Emergency power backup<br>
        11. Cooking facilities available for students in cooking area <br>
        </div>
        """, unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown("### 🛏️ Hostel Rules")
        st.markdown("""
        <div class="card">
        1. Strict discipline and code of conduct<br>
        2. No outside visitors allowed in rooms<br>
        3. Quiet hours from 10 PM to 6 AM<br>
        4. Strict prohibition of alcohol/drugs<br>
        5. Mandatory health check-ups<br>
        6. Curfew timings strictly enforced<br>
        7. Proper dress code in common areas<br>
        8. Room inspections twice a month<br>
        9. Immediate reporting of maintenance issues<br>
        10. No cooking or heating appliances allowed in rooms <br>
        </div>
        """, unsafe_allow_html=True)

# Other Facilities
st.subheader("✨ Additional Facilities")
st.markdown("""
<div style="column-count: 2; column-gap: 20px;">
1. Well-equipped gymnasium with trainer<br>
2. Recreation hall with indoor games<br>
3. Medical room with first-aid support<br>
4. Regular wellness and yoga programs<br>
5. Outdoor sports facilities (cricket, football, volleyball)<br>
6. Cultural and recreational activities<br>
7. Career guidance workshops<br>
8. 24/7 power and water supply<br>
9. Fire safety measures and emergency exits<br>
10. CCTV surveillance in common areas<br>
11. Guest lecture halls<br>
12. Separate study zones<br>
13. Cafeteria with snack bar<br>
</div>
""", unsafe_allow_html=True)

# Contact Information
st.subheader("📞 Contact Information")

# Boys Hostel Contacts
st.markdown("""
<div class="contact-card">
<h4>🏢 Boys Hostel</h4>
<div style="display: flex; flex-wrap: wrap; gap: 20px;">
<div style="flex: 1 1 200px;">
<h5>Hostel Rector</h5>
<p>Mr. Dada Rajmane<br>
📞 +91-9561255856<br>
🕒 Available: 8 AM - 8 PM</p>
</div>
<div style="flex: 1 1 200px;">
<h5>Hostel Coordinator</h5>
<p>Prof. Roshan Pushpan<br>
📞 +91-8380048424<br>
🕒 Available: 10 AM - 5 PM</p>
</div>
<div style="flex: 1 1 200px;">
<h5>Emergency</h5>
<p>Security Desk<br>
📞 +91-9561255856<br>
🕒 24/7 Available</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# Girls Hostel Contacts
st.markdown("""
<div class="contact-card">
<h4>🏢 Girls Hostel</h4>
<div style="display: flex; flex-wrap: wrap; gap: 20px;">
<div style="flex: 1 1 200px;">
<h5>Hostel Rector</h5>
<p>Pramod Ligade<br>
📞 +91-9373740598<br>
🕒 Available: 8 AM - 8 PM</p>
</div>
<div style="flex: 1 1 200px;">
<h5>Hostel Coordinator</h5>
<p>Prof. A. V. Sadlapurkar<br>
📞 +91-9552529263<br>
🕒 Available: 10 AM - 5 PM</p>
</div>
<div style="flex: 1 1 200px;">
<h5>Emergency</h5>
<p>Security Desk<br>
📞 +91-9373740598<br>
🕒 24/7 Available</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

import streamlit as st

# Image paths - update these with your actual paths
girl_hostel_images = [
    "C:\\Users\\GAURI\\OneDrive\\Desktop\\Campus Coder\\assets\\girl_hostel1.jpg",
    "C:\\Users\\GAURI\\OneDrive\\Desktop\\Campus Coder\\assets\\girl_hostel2.jpg"
]

boys_hostel_images = [
    "C:\\Users\\GAURI\\OneDrive\\Desktop\\Campus Coder\\assets\\boys_hostel1.jpg",
    "C:\\Users\\GAURI\\OneDrive\\Desktop\\Campus Coder\\assets\\boys_hostel2.jpg",
    "C:\\Users\\GAURI\\OneDrive\\Desktop\\Campus Coder\\assets\\boys_hostel3.jpg"
]

# Create two columns
col1, col2 = st.columns(2)

# Girls Hostel in first column
with col1:
    st.header("Girls Hostel")
    for img in girl_hostel_images:
        st.image(img, use_container_width=True)
    
# Boys Hostel in second column
with col2:
    st.header("Boys Hostel")
    for img in boys_hostel_images:
        st.image(img, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
<p>For any hostel-related queries, please contact the administration office</p>
<p>© 2024 N.K. Orchid College of Engineering & Technology | All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
footer()