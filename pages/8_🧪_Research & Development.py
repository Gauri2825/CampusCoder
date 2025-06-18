import streamlit as st
import pandas as pd
from io import BytesIO
from pathlib import Path
from utils.file import footer

st.set_page_config(page_title="Labs & Research | NKOCET", layout="wide")

st.header("🧪 Research & Development", divider='rainbow')

# Load patent data from the Excel file
@st.cache_data
def load_patent_data():
    # This would be replaced with actual file loading in a real app
    # For now, we'll create a DataFrame from the provided patent data
    # Ensure all columns have the same length (58 entries in this example)
    num_entries = 58
    patent_data = {
        "Status": ["Granted"]*13 + ["Published"]*(num_entries-13),
        "Title": [
            "Smart Pants Using Haptic Feedback", "Mechanized Cloth Duster", 
            "Solar Powered hydroponic System", "Hand Operated Water Bottle Crusher",
            "Simple Straight line gas Cutter Machine", "Simple pipe and rod bending attachment",
            "Purification Of Impotable And Waste Water", "Triangular Roller Scale",
            "Improved roof top Ventilator", "Alidade Having Central Compass",
            "Solar Powered Solar PV Panel Lamination Machine", "IOT Based Solar Operated Dehydration System",
            "Solar Cooker Using Nano-Mixed Phase Change Materials"
        ] + [f"Patent Title {i}" for i in range(14, num_entries+1)],
        "Inventors": [
            "Prof. A.A. Chandanshive", "Dr B K Sonage", "Prof. Akhtar Nadaf",
            "Prof. A. S. Kashid", "Prof. A. S. Kashid", "Prof. A. S. Kashid",
            "Dr. B. K. Sonage", "Prof. B. R. Birajdar", "Prof. B. R. Birajdar",
            "Prof. B. R. Birajdar", "Prof.C.V.Papade", "Prof.C.V.Papade",
            "Prof.C.V.Papade"
        ] + [f"Inventor {i}" for i in range(14, num_entries+1)],
        "Year": [
            2024, 2020, 2023, 2022, 2021, 2021,
            2021, 2023, 2023, 2023, 2022, 2022,
            2022
        ] + [2020 + (i % 5) for i in range(14, num_entries+1)]
    }
    return pd.DataFrame(patent_data)

# Load research publications data
@st.cache_data
def load_research_data():
    # This would be replaced with actual data loading in a real app
    departments = {
        "AI&DS and CSE": 18,
        "Civil Engineering": 7,
        "Electronics and Telecommunication": 13,
        "Electrical Engineering": 5,
        "General Engineering": 9,
        "Mechanical Engineering": 23
    }
    return departments

patent_df = load_patent_data()
research_data = load_research_data()

# Calculate metrics
total_patents = len(patent_df)
granted_patents = len(patent_df[patent_df["Status"] == "Granted"])
current_year_patents = len(patent_df[patent_df["Year"] == 2024])

total_papers = sum(research_data.values())
current_year_papers = 58  # From the document's title "A.Y. 2023-24"

# Create columns for metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Patents Filed", f"{total_patents}+", f"{current_year_patents} this year")
with col2:
    st.metric("Research Papers Published", f"{total_papers}+", f"{current_year_papers} in A.Y. 2023-24")
with col3:
    st.metric("Ongoing Research Projects", "18", "6 industry collaborations")

st.subheader("🔬 Research Activities")
tab1, tab2, tab3, tab4 = st.tabs(["Student Research", "Faculty Research", "Facilities", "Patent Dashboard"])

with tab1:
    st.markdown("""
    ### 🎓 Student Research Programs
    - Annual research paper presentations (50+ papers yearly)
    - Patent filing support and guidance (5 student-led patents)
    - Undergraduate research fellowship program
    - National conference participation funding
    - Best research paper awards (₹50,000 prize pool)
    """)
    
with tab2:
    st.markdown(f"""
    ### 👩‍🏫 Faculty-Led Research
    - {len(research_data)} departments with active research programs
    - ₹2.5Cr+ in external research funding
    - Collaboration with 8+ international universities
    - Industry consultancy projects (15+ ongoing)
    - PhD supervision and guidance
    
    #### Department-wise Publications (A.Y. 2023-24):
    """)
    
    for dept, count in research_data.items():
        st.markdown(f"- **{dept}**: {count} papers")
    
with tab3:
    st.markdown("""
    ### 🏛️ Research Facilities
    - Advanced computing lab (100+ GPU cluster)
    - Material science research center
    - IoT and embedded systems lab
    - 24/7 access to research scholars
    - Subscription to 50+ international journals
    - Incubation center with prototyping equipment
    """)

with tab4:
    st.markdown("### 📊 Patent Analytics")
    
    # Patent status distribution
    st.subheader("Patent Status")
    status_counts = patent_df["Status"].value_counts()
    st.bar_chart(status_counts)
    
    # Patents by year
    st.subheader("Patents Filed by Year")
    year_counts = patent_df["Year"].value_counts().sort_index()
    st.line_chart(year_counts)
    
    # Search patents
    st.subheader("Patent Search")
    search_term = st.text_input("Search patent titles or inventors")
    
    if search_term:
        filtered_df = patent_df[
            patent_df["Title"].str.contains(search_term, case=False) | 
            patent_df["Inventors"].str.contains(search_term, case=False)
        ]
    else:
        filtered_df = patent_df
        
    st.dataframe(filtered_df[["Title", "Inventors", "Status", "Year"]], 
                height=400, use_container_width=True)

st.subheader("📚 Research Initiatives", divider='gray')
st.markdown(f"""
- **Industry-funded projects**: 6 ongoing projects with ₹1.2Cr funding  
- **Research publications**: {total_papers}+ papers across departments  
- **Patents**: {granted_patents} granted, {total_patents-granted_patents} in process  
- **Incubation support**: 5 student startups currently being mentored  
- **MoUs**: Signed with 3 national research labs for joint projects
""")

st.subheader("📄 Research Documents")

pdf_files = {
    "Patent Data": r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\Patent data.pdf",
    "Research Publications and Awards": r"C:\Users\GAURI\OneDrive\Desktop\Campus Coder\assets\Research publications and awards.pdf"
}

for name, path in pdf_files.items():
    st.markdown(f"#### {name}")
    with open(path, "rb") as f:
        pdf_bytes = f.read()
        st.download_button(
            label=f"Download {name}",
            data=pdf_bytes,
            file_name=Path(path).name,
            mime="application/pdf"
        )
        # st.pdf(pdf_bytes)  # Removed because Streamlit has no st.pdf method
footer()