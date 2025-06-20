import streamlit as st
import pandas as pd
import os
from PIL import Image
from utils.file import footer

st.set_page_config(page_title="Admission | NKOCET", layout="wide")

st.header("🎓 Admission Information", divider='rainbow')

image_path = "assets/CET admission.jpg"
if os.path.exists(image_path):
  img = Image.open(image_path)
  st.image(img, use_container_width=True, caption="NKOCET Admission 2025-26")
else:
  st.info("Admission banner image not found.")

st.subheader("📌 Eligibility Criteria")
st.markdown("""
- **BeTech Programs (First Year):**  
  - Passed 10+2 with Physics, Math, and Chemistry/Electronics/CS  
  - Grouping of subjects: Physics, Math, and Chemistry/Electronics/CS with minimum 45% (40% for reserved categories)  
  - Appeared for MHT-CET or JEE Main  
  - Must have obtained a non-zero positive score in MHT-CET 2025 or JEE Main Paper-I (for All India seats)
  CET
""")

st.subheader("📝 Admission Process")
st.markdown("""
1. **Online Registration:** via [cetcell.mahacet.org](https://cetcell.mahacet.org/)  
2. **Document Verification:** At facilitation center  
3. **Choice Filling & CAP Rounds**  
4. **Allotment & Confirmation of Admission**  
5. **College Reporting**

**Note:** College code – *6223*
""")

st.subheader("📂 Required Documents")

# Create two tabs side by side
tab_open, tab_reserved = st.tabs(["Open Category", "Reserved Category"])

with tab_open:
    st.markdown("""
    **Common Documents for All Students:**
    
  - MHTCET / JEE main Score card
  - SSC (10th) Marksheet
  - HSC (12th) Marksheet
  - School/College Leaving Certificate (LC)
  - Nationality Certificate or Indian Nationality mentioned on LC
  - Domicile Certificate (if applicable)
  - EWS Certificate (only for EWS category candidates)
  - Aadhar Card
  - Passport-size Photographs
  - CAP Application Form Printout (filled online during admission)

    """)

with tab_reserved:
    st.markdown("""
  - Aadhar Card
  - Passport-size Photographs
  - MHTCET / JEE main Score card
  - SSC (10th) Marksheet
  - HSC (12th) Marksheet
  - School/College Leaving Certificate (LC)
  - Nationality Certificate or Indian Nationality mentioned on LC
  - Domicile Certificate (if applicable)
  - EWS Certificate (only for EWS category candidates)
  - CAP Application Form Printout (filled online during admission)
  - Caste Certificate (Issued by Competent Authority)
  - Caste Validity Certificate (Mandatory for SC, ST, VJ/DT, NT, OBC, SEBC)
  - Non-Creamy Layer Certificate (Valid for current financial year – for OBC/NT/VJ/SEBC)
  - Income Certificate (for Scholarship/Fee Concession)
  - EWS Certificate (only for EWS category candidates)
  - Gap Certificate (if applicable – for students with education gap)
    """)


st.subheader("📞 Admission Helpdesk")
st.markdown("""
- **Phone:** +91 2172990051 
- **Email:** admission@orchidengg.ac.in
- **Office Hours:** 10 AM – 5 PM (Mon–Sat)
""")

st.subheader("🪑 Department-wise Intake (2025-26)")
intake_data = {
  "Department": [
    "Computer Science & Engineering",
    "Artificial Intelligence & Data Science",
    "Electronics & Telecommunication",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering"
  ],
  "Intake": [180, 60, 60, 60, 120, 60]
}
intake_df = pd.DataFrame(intake_data)
st.dataframe(intake_df.set_index("Department"), use_container_width=True)
st.caption("Intake numbers are as per AICTE/DTE approval for 2025-26.")

st.subheader("📊 Department-wise Cut-off (2024-25)")
# Remove the previous detailed tables and add a single summary table


cutoff_data = {
  "Department": [
    "Computer Science & Engineering",
    "Artificial Intelligence & Data Science",
    "Electronics & Telecommunication",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering"
  ],
  "Open": ["79.54 – 83.67", "77.54 – 81.34", "66.54 – 70.34", "60.29 – 76.24", "51.21 – 60.50", "53.82 – 70.50"],
  "OBC": ["76.54 – 80.23", "74.54 – 78.23", "63.54 – 67.34", "54.08 – 68.71", "39.53 – 52.81", "47.45 – 54.08"],
  "SC": ["60.89 – 70.23", "60.12 – 68.22", "50.45 – 55.67", "22.30 – 57.86", "15.49 – 38.86", "22.22 – 52.81"],
  "ST": ["--", "--", "--", "--", "--", "--"],
  "VJ/DT": ["57.34 – 62.45", "55.23 – 60.45", "43.89 – 48.12", "30.32", "30.32", "31.68 – 59.05"],
  "NT1": ["67.12 – 73.21", "66.10 – 71.21", "56.54 – 60.34", "50.09", "13.59 – 32.09", "47.98"],
  "NT2": ["73.45 – 77.32", "70.67 – 75.32", "60.67 – 64.12", "27.51 – 56.95", "26.12 – 50.76", "16.88 – 52.51"],
  "NT3": ["69.23 – 75.12", "69.23 – 73.12", "58.89 – 62.34", "60.62", "47.01 – 59.88", "31.31"],
  "SEBC": ["72.67 – 76.12", "70.67 – 74.12", "59.67 – 63.12", "41.03 – 59.05", "39.23 – 44.36", "32.83 – 49.61"],
  "EWS": ["75.54 – 79.34", "73.54 – 77.34", "62.54 – 66.34", "29.63 – 55.07", "24.30 – 54.75", "52.02 – 52.81"],
  "JEE (Open)": ["~70+", "~68+", "~60+", "~55+", "~50+", "~50+"],
  "TFWS": ["79.00+", "77.00+", "66.00+", "60.00+", "53.00+", "54.00+"]
}

df = pd.DataFrame(cutoff_data)
st.markdown("#### Department-wise Cut-off Range (2025-26)")
st.dataframe(df.set_index("Department"), use_container_width=True)
st.caption("Cut-off ranges are based on CAP rounds (MHT-CET percentile). JEE and TFWS (Tuition Fee Waiver Scheme) cut-offs are indicative. '--' means data not available or not applicable.")
# Removed detailed Electronics & Telecommunication Engineering cut-off table as per instructions.
st.subheader("💰 Fee Structure (2025-26)")
import os
from PIL import Image
pdf_path = "assets/FY fee structure for AY 2025-26.pdf"
if os.path.exists(pdf_path):
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()
    st.download_button(
      label="Download Fee Structure (PDF)",
      data=pdf_bytes,
      file_name="FY fee structure for AY 2025-26.pdf",
      mime="application/pdf"
    )
else:
    st.warning("Fee structure PDF not found. Please contact the admission office for details.")

st.subheader("🎓 Scholarships & Application Criteria")
st.markdown("""
- **Government Scholarships:**  
  - *EBC, SC, ST, OBC, Minority, and other state/national schemes available.*
- **Eligibility:**  
  - Admission through CAP  
  - Annual family income as per scheme guidelines  
  - Valid caste/income certificates (if applicable)
- **Application Process:**  
  1. Register at [mahadbt.maharashtra.gov.in](https://mahadbt.maharashtra.gov.in/)  
  2. Fill scholarship form and upload required documents  
  3. Submit printout to college office
""")

st.subheader("📑 Additional Documents for Scholarship Application")
st.markdown("""
- Income Certificate (from Tehsildar)  
- Caste Certificate & Validity (if applicable)  
- Non-Creamy Layer Certificate (for OBC/SBC/VJNT)  
- Aadhaar Card  
- Bank Passbook (student's account)  
- Previous year marksheet  
- Gap Certificate (if applicable)
""")
footer()