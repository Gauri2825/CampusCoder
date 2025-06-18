import streamlit as st
import os
from pathlib import Path
from utils.file import footer

# Header section
st.header("📄 Download Brochure", divider='rainbow')

# Brochure content preview
st.subheader("📚 What's Inside?")
st.markdown("""
- Program details  
- Fee structure  
- Scholarships  
- Facilities  
- Admission process  
- Placements  
- Industry collaborations  
- Student achievements
""")

# Specify the folder path where the brochure is stored
BROCHURE_FOLDER = "assets"  # Folder where the brochure is stored
BROCHURE_FILENAME = "NKOCET-Brochure.pdf"  # The filename of your brochure

# Function to get the brochure file path
def get_brochure_path():
    # Create the assets folder if it doesn't exist
    os.makedirs(BROCHURE_FOLDER, exist_ok=True)
    # Return the full path to the brochure
    return Path(BROCHURE_FOLDER) / BROCHURE_FILENAME

# Function to read the brochure file
def read_brochure():
    brochure_path = get_brochure_path()
    if brochure_path.exists():
        with open(brochure_path, "rb") as f:
            return f.read()
    return None

# Download button
col1, col2 = st.columns(2)
with col1:
    brochure_data = read_brochure()
    if brochure_data:
        st.download_button(
            label="📥 Download Brochure (English)",
            data=brochure_data,
            file_name=BROCHURE_FILENAME,
            mime="application/pdf",
            help="Click to download the NKOCET brochure in PDF format"
        )
    else:
        st.error(f"Brochure file not found at: {get_brochure_path()}")

# Additional information
st.markdown("---")
st.subheader("About NKOCET")
st.markdown("""
Nagesh Karajagi Orchid College of Engineering and Technology (NKOCET) is an AICTE-approved institution 
affiliated with DBATU, Lonere. With state-of-the-art infrastructure and industry collaborations, 
NKOCET provides quality technical education and excellent placement opportunities.
""")

st.subheader("Key Highlights")
st.markdown("""
- ✅ NAAC A+ Accredited Institute  
- ✅ 4.5 STAR MHRD Ministry Ranked  
- ✅ Industry Linked Technical Institute (Platinum Band)  
- ✅ Outstanding Education Institute (West) - ABP News 2018  
- ✅ Over 400 placements annually  
- ✅ Student exchange programs with international universities  
""")

st.subheader("Contact Information")
st.markdown("""
**Address:** Solapur-Tuljapur Road, Tale-Hipparaga, Solapur-413 002  
**Phone:**  2172990051  
**Email:** office@orchidengg.ac.in  
**Website:** [www.orchidengg.ac.in](http://www.orchidengg.ac.in)  
**Institute Code:** EN6223
""")
footer()