import streamlit as st
from streamlit_extras.colored_header import colored_header
import pandas as pd
import os
from utils.file import footer

# Page Configuration
st.set_page_config(page_title="Departments | NKOCET", layout="wide", page_icon="🏛")

# Anchor target for Go to Top
st.markdown('<div id="top-anchor"></div>', unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
.department-card {
    height: 300px;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    background-size: cover;
    background-position: center;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}
.department-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.55);
    z-index: 1;
    border-radius: 12px;
}
.card-content {
    position: relative;
    z-index: 2;
    text-align: center;
    color: white;
}
.card-title {
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 15px;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
}
.explore-btn {
    background: linear-gradient(45deg, #FF4B4B, #FF8E8E);
    color: white !important;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s;
    text-decoration: none;
}
.explore-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    color: white !important;
}
.scroll-target {
    padding-top: 80px;
    margin-top: -80px;
}
.faculty-card {
    background: white;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
.lab-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    border-left: 4px solid #0072ff;
}
.event-card {
    background: #fff8e1;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    border-left: 4px solid #ffc107;
}
.achievement-card {
    background: #e8f5e9;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    border-left: 4px solid #4caf50;
}
.career-card {
    background: #e3f2fd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    border-left: 4px solid #2196f3;
}
.tab-button {
    margin-right: 5px !important;
    margin-bottom: 5px !important;
}
</style>
""", unsafe_allow_html=True)

# Header
colored_header(
    label="🏛 Academic Departments",
    description="Choose Your Engineering Path",
    color_name="violet-70",
)

# Department Data with additional details
departments = [
    {
        "title": "First Year Department",
        "logo": "🎓",
        "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=500&q=80",
        "id": "foundation",
        "description": "The First Year Department serves as the foundation for all engineering disciplines, providing students with core knowledge in mathematics, physics, chemistry, and basic engineering principles. Our program is designed to build strong fundamentals while helping students transition from school to university education.",
        "faculty": [
    {"name": "Mr. Jadhav S. D.", "designation": "Asst. Professor (Maths), HOD", "qualification": "B.Sc., M.Sc., Ph.D(Pur)", "experience": "18"},
    {"name": "Mr. Kangale A.H.", "designation": "Asst. Professor (Maths)", "qualification": "B.Sc., M.Sc., M.Phil. (Pur)", "experience": "17"},
    {"name": "Ms. Ubale P. A.", "designation": "Asst. Professor (Chemistry)", "qualification": "B.Sc., M.Sc., Ph.D.", "experience": "17"},
    {"name": "Dr. Patil R. R.", "designation": "Asst. Professor(CS), Dean T&P", "qualification": "M.A., M.Phil, PhD.", "experience": "16"},
    {"name": "Dr. Shaikh M. S.", "designation": "Asst. Professor (CS)", "qualification": "M.A. (English) B.Ed., Ph.D", "experience": "18"},
    {"name": "Ms. Ingale M. T.", "designation": "Asst. Professor (Chemistry)", "qualification": "B.Sc., M.Sc.B.Ed, Ph.D (Pur)", "experience": "15"},
    {"name": "Ms. Sadlapurkar A. V.", "designation": "Asst. Professor (Chemistry)", "qualification": "B.Sc., M.Sc., Ph.D. (Pur)", "experience": "12"},
    {"name": "Dr. Jadhav U.K", "designation": "Asst. Professor (CS)", "qualification": "B.A., M.A., M.Phil., Ph.D, SET", "experience": "13"},
    {"name": "Ms. Newale S. S.", "designation": "Asst. Professor", "qualification": "M.Sc, SET, GATE, B.Ed.", "experience": "N/A"},
    {"name": "Mr. Manjare N. B.", "designation": "Asst. Professor", "qualification": "M.Phil, M.Sc.", "experience": "15"},
    {"name": "Mr. Birajdar I N", "designation": "Asst. Professor", "qualification": "M.Sc (Physics)", "experience": "09"},
    {"name": "Mr. Chavan S V", "designation": "Asst. Professor", "qualification": "M.Sc (Mathematics)", "experience": "15"},
    {"name": "Dr. V. S. Birangal", "designation": "Librarian", "qualification": "Ph.D., M.Phil., M.Lib. & I.Sci., M.A.", "experience": "23"},
    {"name": "Mr. A. K. Ohol", "designation": "Asst. Professor", "qualification": "B.E. ENTC M.Tech (pur)", "experience": "09"},
    {"name": "Mr. G. S. Jokare", "designation": "Asst. Professor", "qualification": "M.Sc. Mathematics", "experience": "N/A"},
    ],
        "labs": [
            
    {"name": "Physics Lab", "equipment": "Optical benches, spectrometers, electronics kits", "capacity": "30", "incharge": "Prof. I. N. Birajdar"},
    {"name": "Engineering Chemistry Lab", "equipment": "Analytical instruments, glassware, chemicals", "capacity": "30", "incharge": "Dr. P. A. Ubale"},
    {"name": "Language Lab", "equipment": "Audio-visual systems, language software", "capacity": "30", "incharge": "Prof. Ms. M. S. Shaikh"},
    {"name": "Basic Mechanical Engg. Lab", "equipment": "Strength testing machines, fluid mechanics apparatus", "capacity": "30", "incharge": "Dr. S. S. Kale"},
    {"name": "Workshop", "equipment": "Lathes, welding machines, carpentry tools", "capacity": "30", "incharge": "Prof. Y. B. Patil"},
    {"name": "Basic Civil Lab", "equipment": "Surveying instruments, material testing equipment", "capacity": "30", "incharge": "Prof. V. A. Salimath"},
    {"name": "Basic Electrical Lab", "equipment": "Circuit trainers, measuring instruments", "capacity": "30", "incharge": "Prof. P. B. Sakhare"},
    {"name": "Basic Electronics Lab", "equipment": "Oscilloscopes, function generators, breadboards", "capacity": "30", "incharge": "Prof. R. S. Bakare"},
    {"name": "Basic Computer Programming Lab", "equipment": "Computers with compilers, IDEs", "capacity": "30", "incharge": "Prof. A. P. Pataskar"},
],
        "events": [
    {"name": "Teachers Day Celebration", "date": "5th September", "description": "Honoring teachers with cultural performances and speeches"},  
    {"name": "Creative Expression", "date": "Dec", "description": "Encouraging students to showcase their artistic and creative talents"},  
    {"name": "Study Session", "date": "Feb", "description": "Focused academic preparation and group learning"},  
    {"name": "Engg. Day Celebration", "date": "15th September", "description": "Celebrating engineers with technical events and guest lectures"},  
    {"name": "Sports Activity", "date": "May", "description": "Promoting physical fitness through various sports competitions"},  
    {"name": "Parents Meet", "date": "November", "description": "Interaction between faculty and parents to discuss student progress"},  
    {"name": "Welcome Ceremony of FE 2019 Batch", "date": "August", "description": "Orientation program for new first-year engineering students"},  
    {"name": "Yoga Day Celebration", "date": "21st June", "description": "Promoting health and wellness through yoga sessions"},  
    {"name": "Motivational Lecture", "date": "April", "description": "Inspirational talks by industry experts or alumni"}  
],
        "achievements": [
    {"name": "Topper 1 (Rank 1)", "year": "2017-18", "description": "Secured highest marks in First Year Engineering at DBATU"},  
    {"name": "Topper 2 (Rank 2)", "year": "2017-18","description": "Secured highest marks in First Year Engineering at DBATU"},
    {"name": "General Champoinship", "year": "2024-25", "description": "Winner of SAMSH evenet (GC) in 2024-25"},    
],
        "careers": [
            {"role": "Further Specialization", "description": "Prepares students for advanced engineering studies in chosen disciplines"},
            {"role": "Competitive Exams", "description": "Strong foundation for GATE, GRE, and other competitive examinations"},
            {"role": "Research Opportunities", "description": "Basic research skills development for future researchers"}
        ]
    },
    {
        "title": "Computer Science & Engineering",
        "logo": "💻",
        "image": "https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?auto=format&fit=crop&w=500&q=80",
        "id": "cse",
        "description": "The Computer Science & Engineering department offers cutting-edge education in software development, algorithms, computer systems, and emerging technologies. Our curriculum blends theoretical foundations with practical applications, preparing students for careers in software engineering, data science, cybersecurity, and more.",
        "faculty": [
            
    {"name": "Dr. V. V. Bag", "qualification": "B. Tech. (CSE), M.Tech. (Computer), Ph.D. (Computer Engg)", "designation": "Professor, HOD", "experience": "25"},
    {"name": "Dr. M. B. Patil", "qualification": "B.E. (CSE), M.Tech. (CSE), Ph.D. (CSE), Postdoc in AI (Singapore Institute of Technology, Singapore)", "designation": "Associate Professor, HOD", "experience": "13"},
    {"name": "Prof. M. S. Otari", "qualification": "B.E. (CSE), M.Tech. (CSE), Ph.D. (Pursuing)", "designation": "Assistant Professor", "experience": "17"},
    {"name": "Prof. Z. M. Shaikh", "qualification": "B.E. (CSE), M.E. (Computer)", "designation": "Assistant Professor", "experience": "21"},
    {"name": "Prof. S. C. Papade", "qualification": "B.E. (CSE), M.E. (CSE), Ph.D. (Pursuing)", "designation": "Assistant Professor", "experience": "11"},
    {"name": "Prof. M. B. Rangdal", "qualification": "B.E. (IT), M.E. (CSE)", "designation": "Assistant Professor", "experience": "16"},
    {"name": "Prof. P. D. Jawalkar", "qualification": "B.E. (CSE), M.E. (Computer Engg)", "designation": "Assistant Professor", "experience": "6"},
    {"name": "Prof. S. D. Dudhanikar", "qualification": "B.E. (CSE), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "12"},
    {"name": "Prof. A. S. Adhatrao", "qualification": "B.E. (CSE), M.E. (CSE)", "designation": "Assistant Professor", "experience": "6"},
    {"name": "Prof. S. S. Konda", "qualification": "B.E. (IT), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "13"},
    {"name": "Prof. V. D. Gaikwad", "qualification": "B.E. (CSE), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "15"},
    {"name": "Prof. R. U. Shinde", "qualification": "B.E. (CSE), M.E. (CSE)", "designation": "Assistant Professor", "experience": "6"},
    {"name": "Prof. S. G. Sanmukh", "qualification": "B.E. (IT), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "12"},
    {"name": "Prof. V. A. Sangolgi", "qualification": "B.E. (IT), M.E. (CSE)", "designation": "Assistant Professor", "experience": "4"},
    {"name": "Prof. N. B. Aherwadi", "qualification": "B.E. (ENTC), M.Tech (ML & AI)", "designation": "Assistant Professor", "experience": "3"},
    {"name": "Prof. T. A. Kamusagi", "qualification": "B.E. (CSE), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "5"},
    {"name": "Prof. G. N. Chanderki", "qualification": "B.E. (IT), M.E. (CSE)", "designation": "Assistant Professor", "experience": "5"},
    {"name": "Prof. S. A. Langote", "qualification": "B.E. (CSE), M.E. (CSE)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. R. D. Joshi", "qualification": "B.E. (CSE), M.Tech. (CSE), Ph.D. (Pursuing)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. P. G. Chimanchode", "qualification": "B.Tech. (CSE), MSc Data Science (Glasgow, UK)", "designation": "Assistant Professor", "experience": "1"},
    {"name": "Prof. G. N. Swami", "qualification": "B.E. (CSE), M.E. (CSE)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. P. C. Bhuyyar", "qualification": "B.E. (CSE), M.Tech. (CSE)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. G. R. Shaikh", "qualification": "B.E. (IT), M.E. (CSE)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. N. S. Mehta", "qualification": "B.E. (CSE), M.E. (CSE)", "designation": "Assistant Professor", "experience": "2"},
    {"name": "Prof. B. B. Simpi", "qualification": "B.E. (CSE), M.Tech. (Data Science)", "designation": "Assistant Professor", "experience": "2"}
],

        "labs": [
            {"name": "Computer Programming Lab- I", "equipment": "PCs, programming IDEs", "capacity": "30 students", "incharge": "Prof. S. C. Papade"},
            {"name": "Software Design Lab", "equipment": "Software design tools, modeling software", "capacity": "30 students", "incharge": "Prof. S. S. Konda"},
            {"name": "Computer Network", "equipment": "Networking kits, routers, switches", "capacity": "30 students", "incharge": "Prof. M. B. Rangdal"},
            {"name": "Operating System", "equipment": "PCs, OS simulators", "capacity": "30 students", "incharge": "Prof. M.S. Otari"},
            {"name": "Project Lab-I", "equipment": "PCs, project development kits", "capacity": "30 students", "incharge": "Prof. S. D. Dudhanikar"},
            {"name": "Project Lab-II", "equipment": "PCs, project development kits", "capacity": "30 students", "incharge": "Prof. S. D. Dudhanikar"},
            {"name": "DB lab", "equipment": "Database servers, PCs", "capacity": "30 students", "incharge": "Prof. V.A. Sangolagi"},
            {"name": "CPL-II", "equipment": "PCs, programming IDEs", "capacity": "30 students", "incharge": "Prof. P. D. Jawalkar"},
            {"name": "Web Programming Lab", "equipment": "PCs, web servers", "capacity": "30 students", "incharge": "Mr.Z.M.Shaikh"},
            {"name": "IOT Lab", "equipment": "IoT kits, sensors, microcontrollers", "capacity": "30 students", "incharge": "Prof. V.D. Gaikwad"},
            {"name": "Advanced Computing Lab", "equipment": "High-end workstations, GPU servers", "capacity": "40 students"},
            {"name": "Software Engineering Lab", "equipment": "Projector setups, design tools", "capacity": "35 students"},
            {"name": "Cyber Security Lab", "equipment": "Ethical hacking tools, network simulators", "capacity": "25 students"}
        ],
        "events": [
            {"name": "Teacher’s Day", "date": "05/09/2022", "description": "A day to honor and appreciate the contributions of teachers in shaping the future."},
            {"name": "Guest Lecture on ‘Recent trends in AI and ML’", "date": "08/09/2022", "description": "Guest: Dr. P. J. Kulkarni. An insightful session discussing the latest advancements in artificial intelligence and machine learning."},
            {"name": "TechFest + CSESA Inauguration", "date": "23/09/2022", "description": "Guest: Mr. Sachin Harihar (Associate Solution Architect, KPIT Technologies). A celebration of technology with workshops and competitions."},
            {"name": "Vachan Prerna Diwas", "date": "15/10/2022", "description": "A day dedicated to promoting reading and literature among students."},
            {"name": "Ek Diva Manuskicha", "date": "22/10/2022", "description": "An event focused on human values and ethics, encouraging students to reflect on their responsibilities."},
            {"name": "Diwali Sparkle 2k22 (Range de Rangoli Food Thali Décor, Diwali Vibes Short Video Making)", "date": "28/10/2022", "description": "A festive celebration featuring rangoli decoration and a short video competition capturing the essence of Diwali."},
            {"name": "Unity Day", "date": "31/10/2022", "description": "A day to promote unity and diversity among students through various activities."},
            {"name": "Roadmap for Placement Success (By Seniors)", "date": "08/11/2022", "description": "Seniors share their experiences and tips for successful placements in the industry."},
            {"name": "Guest Lecture on ‘Cyber Security’ (for SE and AI&DS)", "date": "10/11/2022", "description": "Guest: Mr. Akshay Phadke. A crucial discussion on the importance of cybersecurity in today's digital world."},
            {"name": "Fresher’s 2k22", "date": "25/11/2022", "description": "An event to welcome new students and help them integrate into the college community."},
            {"name": "Guest Lecture on ‘Cyber Law’", "date": "30/11/2022", "description": "Guests: 1) Hon. Mr. Manjunath Kakkalmeli, 2) Hon. Mr. Suraj Nimbalkar, 3) Hon. Mr. Narendra Joshi, 4) Adv. Mr. L.N Maradkar. A session on the legal aspects of cybersecurity."},
            {"name": "Guest Lecture on ‘Skill Set for DevOps’", "date": "21/02/2023", "description": "Guest: Mr. Abhijit Kulkarni. Insights into the essential skills required for a career in DevOps."},
            {"name": "International Women’s Day", "date": "08/03/2023", "description": "A celebration of women's achievements and a call for gender equality."},
            {"name": "ORCHATHON’-23 Technical Event Competition", "date": "1/04/2023", "description": "Guest: Mr. Avinash Gavali (Director, Earth Solns). A technical competition showcasing innovative projects by students."},
            {"name": "Shantai Orphanage Donation", "date": "15/4/2023", "description": "A charitable event where students donate essentials to support the orphanage."},
            {"name": "Seniors Farewell (Batch 2023)", "date": "27/05/2023", "description": "A heartfelt farewell event to honor the graduating batch and their contributions."}
],

        "achievements": [
            {"title": "Microsoft Imagine Cup Winners", "year": "2023", "description": "National level winners in AI category"},
            {"title": "100% Placement Record", "year": "2022", "description": "All graduates placed in top companies"},
            {"title": "Best Research Paper Award", "year": "2021", "description": "At IEEE International Conference"},
            {"title": "Peer Reviewed Publications", "year": "2023", "description": "10+ publications in Scopus indexed journals"},
            {"title": "Patents Filed and Published", "year": "2023", "description": "4+ patents filed and published"},
            {"title": "Research Funding Proposals", "year": "2023", "description": "3 research funding proposals submitted"},
            {"title": "Placement Offers", "year": "2023", "description": "144 placement offers in last academic year"},
            {"title": "Result", "year": "2023", "description": "SY CSE: 88%, TY CSE: 93%, Final Year CSE: 100%"},
            {"title": "Avishkar Competition", "year": "2023", "description": "2 Teams won Gold Medal"},
            {"title": "Faculty FDP Participation", "year": "2023", "description": "Six faculty members attended FDP conducted by industry; 80% faculty attended minimum one FDP; 50% completed NPTEL examination"},
            {"title": "Faculty Recognition", "year": "2020", "description": "Prof. M. B. Patil honored with 'Best Faculty Award' for Academic Year 2019-20"},
            {"title": "Faculty as Resource Person", "year": "2023", "description": "One faculty worked as resource person in FDP organized by other college"},
            {"title": "Faculty as Reviewer", "year": "2023", "description": "Two faculty members worked as reviewer for international research conferences"},
            {"title": "CSESA Programs", "year": "2023", "description": "Intra College: 7, Intercollege: 2"},
            {"title": "Extension Activity", "year": "2023", "description": "2 extension activities conducted"},
            {"title": "GATE 2020 Qualified", "year": "2020", "description": "Miss. Kiran Kashinath Gawade qualified GATE-2020 with 85.67 percentile"},
            {"title": "GATE 2019 Qualified", "year": "2019", "description": "Onkar Bharat Raut (81.99 percentile), Apeksha Bharat Sonwane (72.57 percentile) qualified GATE-2019"},
            {"title": "Best Outgoing Student", "year": "2023", "description": "Miss. Nandini Mhamane declared Best Outgoing Student of NKOCET & Department"},
            {"title": "SEED IT IDOL Winner", "year": "2023", "description": "Mr. Sakib Patel from TE CSE bagged first rank in SEED IT IDOL at university level"},
            {"title": "Smart India Hackathon 2019", "year": "2019", "description": "Team participated in nationwide Smart India Hackathon 2019, shortlisted for problem statement 'Daily Construction Site Progress' by Everest Industries, held at R.K.Goyal Institute, Ghaziabad, Delhi. Team gained real-time problem-solving and teamwork experience."}
        ],
        "careers": [
            {"role": "Software Engineer", "description": "Design and develop software applications and systems"},
            {"role": "Data Scientist", "description": "Analyze complex data to derive business insights"},
            {"role": "Cybersecurity Analyst", "description": "Protect systems and networks from digital attacks"}
        ]
    },
    {
        "title": "AI & Data Science",
        "logo": "🤖",
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&w=500&q=80",
        "id": "ai-ds",
        "description": "The AI & Data Science department focuses on artificial intelligence, machine learning, big data analytics, and intelligent systems. Our program combines mathematical foundations with practical applications, preparing students for careers in this rapidly evolving field.",
        "faculty": [
            {"name": "Dr. M. B. Patil", "qualification": "Mtech(CSE), Ph.D(CSE), Postdoc in AI (Singapore Institute of Technology, Singapore)", "designation": "HOD, Associate Professor", "experience": "13"},
            {"name": "Prof. A. S. Adhatrao", "qualification": "M.E (CSE)", "designation": "Assistant Professor", "experience": "6"},
            {"name": "Prof. S. G. Sanmukh", "qualification": "M. Tech (CSE)", "designation": "Assistant Professor", "experience": "13"},
            {"name": "Prof. N. B. Aherwadi", "qualification": "M. Tech (ML & AI)", "designation": "Assistant Professor", "experience": "3"},
            {"name": "Prof. V. A. Sangolgi", "qualification": "BE, Mtech(CSE)", "designation": "Assistant Professor", "experience": "4"},
            {"name": "Prof. S. S. Newale", "qualification": "M.Sc, SET, GATE, B.Ed", "designation": "Assistant Professor", "experience": "6"}
        ],
    "labs": [
            {"name": "Artificial Intelligence Lab","incharge": "Prof. N. B. Aherwadi","equipment": "NVIDIA DGX systems, robotics kits","capacity": "30 students"},
            {"name": "Data Science Lab","incharge": "Prof. A. S. Pawade","equipment": "Big data clusters, visualization tools","capacity": "30 students"},
            {"name": "Machine Learning Lab","incharge": "Prof. A. S. Adhatrao","equipment": "High-performance computing systems, ML frameworks","capacity": "30 students"},
            {"name": "Project Lab","incharge": "Prof. V. D. Gaikwad","equipment": "PCs, project development kits, collaboration tools","capacity": "30 students"}
    ],
        "events": [
        {"name": "Logo Contest","date": "07/10/2022","description": "Logo design competition held in Semester-I of A.Y. 2022-23."},
        {"name": "Inauguration of AIASA","date": "10/12/2022","description": "Official inauguration event of AIASA held in Semester-I of A.Y. 2022-23."},
        {"name": "Vachan Prerna Divas","date": "15/10/2022","description": "Event celebrating the power of reading held in Semester-I of A.Y. 2022-23."},
        {"name": "National Unity Day","date": "31/10/2022","description": "Event commemorating Sardar Vallabhbhai Patel's birth anniversary held in Semester-I of A.Y. 2022-23."},
        {"name": "Fresher’s Party","date": "25/11/2022","description": "Welcome event for new students held in Semester-I of A.Y. 2022-23."},
        {"name": "Roadmap for Programming Skill Enhancement & Hackathon","date": "31/12/2022","description": "Workshop and hackathon to enhance programming skills held in Semester-I of A.Y. 2022-23."},
        {"name": "National Constitution Day","date": "26/11/2022","description": "Event celebrating the adoption of the Indian Constitution held in Semester-I of A.Y. 2022-23."},
        {"name": "Visit to Shantai Orphanage","date": "15/04/2023","description": "Social activity involving a visit to Shantai Orphanage held in Semester-II of A.Y. 2022-23."},
        {"name": "Teacher's Day Program","date": "05/09/2023","description": "Event honoring teachers held in Semester-I of A.Y. 2023-24."},
        {"name": "Technical Competition 'Techno Wiz'","date": "16/09/2023","description": "Technical skills competition held in Semester-I of A.Y. 2023-24."},
        {"name": "National Unity Day","date": "31/10/2023","description": "Event commemorating Sardar Vallabhbhai Patel's birth anniversary held in Semester-I of A.Y. 2023-24."},
        {"name": "Visit to Aai Orphanage","date": "12/11/2023","description": "Social activity involving a visit to Aai Orphanage held in Semester-I of A.Y. 2023-24."},
        {"name": "National Science Day","date": "28/02/2024","description": "Event celebrating scientific achievements held in Semester-II of A.Y. 2023-24."},
        {"name": "First Spark 2024 (Fresher’s Party)","date": "01/03/2024","description": "Welcome event for new students held in Semester-II of A.Y. 2023-24."},
        {"name": "Teachers Day Program","date": "05/09/2024","description": "Event honoring teachers held in Semester-I of A.Y. 2024-25."},
        {"name": "Inauguration of AIASA","date": "14/04/2024","description": "Official inauguration event of AIASA held in Semester-I of A.Y. 2024-25."},
        {"name": "Engineer's Day Program","date": "14/04/2024","description": "Event celebrating engineers held in Semester-I of A.Y. 2024-25."},
        {"name": "Diwali Celebration","date": "25/10/2024","description": "Festival celebration held in Semester-I of A.Y. 2024-25."}
    ],
        "achievements": 
        [
            {"title": "Inter-College Chess Tournament Winner","year": "2023","description": "First prize in the Inter-College Chess Tournament held at Gramin College, Nanded on 15 Nov 2023."},
            {"title": "Inter-Zonal Chess Tournament Winner","year": "2023","description": "First Prize in Inter-Zonal Chess Tournament held at RC Patel College of Engineering, Dhule on 24 Dec 2023."},
            {"title": "State Level Chess Tournament","year": "2024","description": "20th Rank at State Level Women's FIDE Rating Chess Tournament held from 29th to 31st May 2024."},
            {"title": "HackXCelerate Hackathon","year": "2024","description": "Team Tech AI Team got 'First Runner Up' Prize in HackXCelerate Hackathon with Prize Money Rs. 50,000, organized by CBIT College, Hyderabad in Collaboration with Microsoft and ByteXL on 26th and 27th April 2024."},
            {"title": "CIDECODE Hackathon","year": "2024","description": "Team Tech AI Team got 'Second Runner Up' Prize in CIDECODE Hackathon with Prize Money Rs. 30,000, organized by Centre for Cybercrime Investigation Training & Research & CID Karnataka Department on 02nd and 03rd March 2024 at PES University Karnataka."},
            {"title": "Patent Publication","year": "2024","description": "Published Patent titled 'Smart Health Monitoring Robot' on 12/01/2024."},
            {"title": "Paper Publication in Procedia Computer Science","year": "2024","description": "'Enhancing Cross-Linguistic Image Caption Generation with Indian Multilingual Voice Interfaces using Deep Learning Techniques' published in Procedia Computer Science Volume 233, 2024, Pages 547-557."},
            {"title": "Paper Publication in Journal of Integrated Science of Technology","year": "2024","description": "'GenConVirt: Advanced hybrid framework for deep fake detection for safeguarding digital media integrity' published in Journal of Integrated Science of Technology on 2024-03-04."},
            {"title": "Paper Publication in ICDSA12024","year": "2024","description": "'Enhancing Fake Product Review System Using Machine Learning Algorithm' published in ICDSA12024."},
            {"title": "Paper Publication in ICDSA12024","year": "2024","description": "'Stock Price Prediction With LSTM Neural Network Using Deep Learning Techniques' published in ICDSA12024."}
        ],
        "careers": [
            {"role": "AI Engineer", "description": "Develop and implement AI models and systems"},
            {"role": "Data Analyst", "description": "Interpret data to inform business decisions"},
            {"role": "Machine Learning Specialist", "description": "Design and optimize ML algorithms"}
        ]
    },
    {
        "title": "Electronics & Telecommunication",
        "logo": "📶",
        "image": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&w=500&q=80",
        "id": "entc",
        "description": "The Electronics & Telecommunication Engineering department provides comprehensive education in analog and digital electronics, communication systems, signal processing, and embedded systems. Our program emphasizes both hardware and software aspects of modern communication technologies.",
        "faculty":[
            {"name": "Mr. Dhotre S. S.","designation": "Associate Professor, HOD","qualification": "B.E., M.Tech. (Electronics & Telecommunication Engg.), Ph.D. (Pursuing)","experience": 10},
            {"name": "Dr. Bahirgonde P.D.","designation": "Associate Professor","qualification": "B.E., M.E. (Electronics), Ph.D. (E&TC)","experience": 12},
            {"name": "Dr. Shirwal V. S.","designation": "Associate Professor","qualification": "B.E., M.Tech. (E&TC), Ph.D.","experience": 12},
            {"name": "Mrs. Bag S.V","designation": "Assistant Professor","qualification": "B.E. (E&TC), M.Tech. (Embedded & VLSI Design), Ph.D. (Pursuing)","experience": 10},
            {"name": "Mr. Roshan Pushpan","designation": "Assistant Professor","qualification": "B.E., M.E. (E&TC), Ph.D. (Pursuing)","experience": 14},
            {"name": "Mr. Chandanshive A.A.","designation": "Assistant Professor","qualification": "B.E. (Electronics), M.Tech. (VLSI & Embedded Systems), Ph.D. (E&TC) (Pursuing)","experience": 12},
            {"name": "Mr. Nadaf A. I.","designation": "Assistant Professor","qualification": "B.E., M.E. (E&TC), Ph.D. (E&TC) (Pursuing)","experience": 13},
            {"name": "Ms. Shriram R. R.","designation": "Assistant Professor","qualification": "B.E. (E&TC), M.E. (E&TC)","experience": 13},
            {"name": "Mr. Bakare R. S.","designation": "Assistant Professor","qualification": "B.E., M.E. (Electronics)","experience": 12},
            {"name": "Ms. Mulmane S. R.","designation": "Assistant Professor","qualification": "B.E., M.E. (Digital Systems)","experience": 10},
            {"name": "Mrs. Bongale U.A","designation": "Assistant Professor","qualification": "B.E., M.E. (ENTC), Ph.D. (ENTC) (Pursuing)","experience": 18},
            {"name": "Mrs. Kashid S. A.","designation": "Assistant Professor","qualification": "B.E., M.E. (E&TC), Ph.D. (Electronics) (Pursuing)","experience": 14},
            {"name": "Ms. More S. S.","designation": "Assistant Professor","qualification": "B.E., M.E. (E&TC), Ph.D. (Pursuing)","experience": 13},
            {"name": "Ms. A.G.Dhanashetti","designation": "Assistant Professor","qualification": "M.E. (Electronics)","experience": 12}
        ],
        "labs": [
            [
            {"name": "Simulation & Network Lab","equipment": "Network simulators, routers, switches, protocol analyzers","capacity": "30 students","incharge": "Prof. Roshan Pushpan",},
            {"name": "Communication Lab","equipment": "Oscilloscopes, signal generators, spectrum analyzers, SDR kits","capacity": "30 students","incharge": "Prof. U. A. Bongale"},
            {"name": "Digital Electronics Lab","equipment": "Logic analyzers, FPGA boards, microcontroller kits","capacity": "30 students","incharge": "Prof. R. R. Shriram"},
            {"name": "Semiconductor Devices and Circuits Lab","equipment": "Breadboards, power supplies, component testers, curve tracers","capacity": "30 students","incharge": "Prof. S. A. Kashid"},
            {"name": "Project Lab","equipment": "3D printers, soldering stations, measurement tools","capacity": "30 students","incharge": "Prof. A. A. Chandanshive"},
            {"name": "Signal Processing Lab","equipment": "DSP kits, MATLAB workstations, audio processing units","capacity": "30 students","incharge": "Prof. A. I. Nadaf"},
            {"name": "VLSI & Embedded Systems Lab","equipment": "FPGA development boards, VLSI CAD tools, ARM kits","capacity": "30 students","incharge": "VLSI & Embedded Systems Lab"},
            {"name": "IoT & AIML Lab","equipment": "Raspberry Pi clusters, sensor kits, AI acceleration boards","capacity": "30 students","incharge": "Prof. R. S. Bakare"}
] ],
        "events":[
            {"name":"Industrial Visit at Dudh Pandhari & Srujan Food Pvt. Ltd","date":"02/04/2023","description":"4 Faculty with 90 T.Y. A&B students visited"},
            {"name":"Seminar on Internet of Things","date":"26/04/2023","description":"Conducted by Mr. Manish Joshi for faculty and staff"},
            {"name":"Expert Lecture on Mobile & Digital Communication","date":"09/05/2023","description":"By Mr. Suhas Swami for TY A&B students"},
            {"name":"Expert Lecture on Distribution Functions","date":"26/05/2023","description":"Dr. Ajay Deshmukh for S.Y. (NTC) students"},
            {"name":"Guest Lecture on Microwave Engineering","date":"26/08/2023","description":"Mr. Shirish Pataki for 105 Final Year students"},
            {"name":"Knowledge Transfer Activity","date":"01/09/2023","description":"TY to SY students knowledge sharing"},
            {"name":"Teachers Day & AEXS Inauguration","date":"06/09/2023","description":"Chief Guest Mr. D.K. Yadav"},
            {"name":"Online MCQ Test on Open Source","date":"29/08/2023","description":"Conducted by AEXS for S.Y.-I"},
            {"name":"Techmaze Technical Competition","date":"15/09/2023","description":"On Engineers' day for S.Y.-I, T.Y.-I, B.Tech"},
            {"name":"Cyber Security Awareness Session","date":"26/09/2023","description":"Mr. Raghunandan Ghatule for SY-I, TY-I"},
            {"name":"Career Guidance on Embedded Systems","date":"27/09/2023","description":"Mr. G. Sathish for S.Y., T.Y. & B.Tech"},
            {"name":"Hackathons & Placements Talk","date":"30/09/2023","description":"Dr. P.C. Dhage for E&TC students"},
            {"name":"Industrial Robotics & AI Session","date":"30/09/2023","description":"Mr. Rajwardhan Salunke for 131 students"},
            {"name":"Gandhi Jayanti Movie Screening","date":"02/10/2023","description":"Father of Nation for all students"},
            {"name":"Project Exhibition","date":"08/07/2022","description":"Final year projects showcase"},
            {"name":"Study Tour to Police Wireless HQ","date":"04/06/2022","description":"TY students visited Pune facilities"},
            {"name":"Arduino Workshop","date":"19-20/06/2022","description":"2-day hands-on for TY students"},
            {"name":"Alumni Interaction","date":"05/06/2022","description":"For SY students"},
            {"name":"Parent-Teacher Meet","date":"14/05/2022","description":"For all classes"},
            {"name":"Fresher's Welcome","date":"07/05/2022","description":"Organized by AEXS"},
            {"name":"VLSI Practical Session","date":"04/05/2022","description":"For SVIT Polytechnic"},
            {"name":"Espire 2022","date":"29/04/2022","description":"Technical event for diploma colleges"},
            {"name":"VLSI Design Workshop","date":"25/04/2022","description":"For Govt. Polytechnic"},
            {"name":"Android Workshop","date":"18-22/04/2022","description":"3-day for SES Polytechnic"},
            {"name":"Academic Success Session","date":"12/04/2022","description":"Prof. I.I. Mujawar for SY"},
            {"name":"Advanced Arduino Workshop","date":"08/04/2022","description":"For SVSMD's Polytechnic"},
            {"name":"Fibre Optic Session","date":"30/03/2022","description":"Online for PLG Polytechnic"},
            {"name":"Industry Automation Session","date":"11/03/2022","description":"Online for GRWE Polytechnic"},
            {"name":"MATLAB/SCILAB Workshop","date":"17-18/02/2022","description":"2-day for SY students"},
            {"name":"Arduino Workshop","date":"11-12/02/2022","description":"2-day for SY students"},
            {"name":"Art Competition","date":"25/01/2022","description":"By AEXS for SY/TY/Final Year"},
            {"name":"E-Yantra Workshop","date":"08-14/11/2021","description":"1-week on Firebird V platform"},
            {"name":"Python Workshop","date":"23-25/09/2021","description":"3-day online for diploma students"},
            {"name":"Engineers Day Celebration","date":"15/09/2021","description":"Online event"},
            {"name":"Farewell","date":"01/09/2021","description":"Online for Final Year"},                  
            {"name":"Proteus Workshop","date":"30/08-02/09/2021","description":"4-day online for diploma students"},
            {"name":"Essay Writing Competition","date":"14/08/2018","description":"Student activity"},
            {"name":"Teachers Day","date":"05/09/2018","description":"Celebration"},
            {"name":"Engineers Day","date":"15/09/2018","description":"Celebration"},
            {"name":"Fresher's Party","date":"18/09/2018","description":"Student event"},
            {"name":"Quiz Competition","date":"13/01/2019","description":"Student activity"},
            {"name":"Farewell Party","date":"16/04/2019","description":"For graduating students"}],
        "achievements": [
            {"title": "PCB Component Detection Project Win","year": "2023","description": "First Prize in Project Competition by Marathi Vidnyan Parishad for 'Detection of Missing Components on PCB' by team Mangesh Khobare, Piyush Kulkarni, Vaibhav Nalla, Rutik Banda under guidance of Prof. Adesh A. Chandanshive"},
            {"title": "Dual GATE qualification","year": "2022","description": "Prof. A. A. Chandanshive qualified GATE-2022 in both Electronics & Communication (EC) and Electrical Engineering (EE)"},
            {"title": "Best Paper Award at ICCDN 2021","year": "2022","description": "Prof. Akhtar Nadaf received best paper award for 'Decision tree based classification of SEMG and accelerometer data of sign language'"},
            {"title": "AICTE Mentor Certification","year": "2021","description": "Prof S. S. Dhotre certified as AICTE approved mentor after completing NITTT Orientation Program"},
            {"title": "Microsoft Python Certification","year": "2021","description": "Prof R. R. Shriram earned Microsoft certification in 'Introduction to Programming using Python'"},
            {"title": "Idea Exploration Winner","year": "2021","description": "Prof. A. I. Nadaf won first prize at Cummins College of Engineering competition"},
            {"title": "National Animation Hackathon Prize","year": "2021","description": "Prof. A. I. Nadaf received special prize in IIT Bombay's national level 2D animation hackathon using Synfig"},
            {"title": "Texas Instruments Equipment Grant","year": "2020","description": "Department received 45 MSP430 Lunchbox Embedded Systems Kits worth ₹27,824 from Texas Instruments"},
            {"title": "International MS Admission","year": "2020","description": "Mr. Rizwan Irfan Patel secured MS program offer from ESME Sudriya School of Engineering, France"},
            {"title": "GRE qualification for US Admission","year": "2018","description": "Ms. Tejashri Parurkar cleared GRE for MS programs at Pace University, New York"},
            {"title": "PhD Completion","year": "2018","description": "Dr. P. D. Bahirgonde awarded PhD from Solapur University for research on 'High Throughput Optimized Turbo Decoder Architecture'"},
            {"title": "Journal Publication on Deep Fake Detection","year": "2024","description": "'GenConVirt: Advanced hybrid framework for deep fake detection' published in Journal of Integrated Science of Technology (04-03-2024)"},
            {"title": "Conference Publication on Fake Review System","year": "2024","description": "'Enhancing Fake Product Review System Using Machine Learning Algorithm' published in ICDSA12024"},
            {"title": "Conference Publication on Stock Prediction","year": "2024","description": "'Stock Price Prediction With LSTM Neural Network Using Deep Learning Techniques' published in ICDSA12024"}
] ,
        "careers": [
            {"role": "Electronics Engineer", "description": "Design electronic components and systems"},
            {"role": "Telecom Engineer", "description": "Develop and maintain communication networks"},
            {"role": "Embedded Systems Engineer", "description": "Design hardware-software integrated systems"}
        ]
    },
    {
        "title": "Electrical Engineering",
        "logo": "⚡",
        "image": "https://images.unsplash.com/photo-1508514177221-188b1cf16e9d?auto=format&fit=crop&w=500&q=80",
        "id": "ee",
        "description": "The Electrical Engineering department offers comprehensive education in power systems, control systems, electrical machines, and renewable energy technologies. Our program combines theoretical knowledge with practical skills to prepare students for diverse careers in the electrical industry.",
        "faculty": [
        {"name": "Prof. Bhosale V.B.", "designation": "HoD, Asst. Professor", "qualification": "B.E., M.S. (CEPE)", "experience": "15"},
        {"name": "Prof. Mehta A.J.", "designation": "Asst. Professor", "qualification": "B.E., M.E. (Power Electronics and drives)", "experience": "15"},
        {"name": "Prof. Pawar D.D.", "designation": "Asst. Professor", "qualification": "B.E., M.Tech (Electrical Power System)", "experience": "8.5"},
        {"name": "Prof. J. B. Patil", "designation": "Asst. Professor", "qualification": "M.E.(Electrical Engineering)", "experience": "11.5"},
        {"name": "Prof. Auti A. B.", "designation": "Asst. Professor", "qualification": "B.E., M.E.(Power System)", "experience": "11"},
        {"name": "Prof. K. B. Tamboli", "designation": "Asst. Professor", "qualification": "B.E., M.Tech(Electrical Machine & Drives)", "experience": "5"},
        {"name": "Prof. P. B. Sakhare", "designation": "Asst. Professor", "qualification": "B.E., M.Tech(Power Electronics and Power System)", "experience": "4"},
        {"name": "Prof. B. Sampath Kumar", "designation": "Asst. Professor", "qualification": "Ph.D(Perusing), M.Tech.(Power Systems)", "experience": "14.6"},
        {"name": "Prof. CH MallaReddy", "designation": "Asst. Professor", "qualification": "M.Tech.(Electrical Engineering)", "experience": "14.6"},
        {"name": "Prof. M. P. Kokare", "designation": "Asst. Professor", "qualification": "M.Tech.(Electrical Power System)", "experience": "3"},
        {"name": "Dr. Prakash Singh", "designation": "Professor & Head", "qualification": "Ph.D. in Power Systems", "experience": "22"},
        {"name": "Prof. Anjali Reddy", "designation": "Associate Professor", "qualification": "M.Tech, Ph.D", "experience": "13"},
        {"name": "Dr. Sameer Khan", "designation": "Assistant Professor", "qualification": "Ph.D in Control Systems", "experience": "8"}
],
        "labs": [
        {"name": "Power Systems Lab", "equipment": "Transformers, circuit breakers, relays", "capacity": "30", "incharge": "PROF. M.P.KOKARE"},
        {"name": "Renewable Energy Lab", "equipment": "Solar panels, wind turbine models", "capacity": "30", "incharge": "PROF. A.J.MEHTA"},
        {"name": "High Voltage Lab", "equipment": "Insulation testers, HV sources", "capacity": "30", "incharge": "PROF. A.J.MEHTA"},
        {"name": "CONTROL SYSTEMS-I", "equipment": "PID controllers, servo motors, oscilloscopes", "capacity": "30", "incharge": "PROF. M.P.KOKARE"},
        {"name": "ELECTRICAL MACHINE-I", "equipment": "DC motors, alternators, load banks", "capacity": "30", "incharge": "PROF. A.J.MEHTA"},
        {"name": "ELECTRICAL MACHINE-II", "equipment": "Induction motors, synchronous machines", "capacity": "30", "incharge": "PROF. A.J.MEHTA"},
        {"name": "BASIC ELECTRICAL ENGINEERING", "equipment": "Multimeters, power supplies, breadboards", "capacity": "30", "incharge": "PROF. P. B. SAKHARE"},
        {"name": "ANALOG & DIGITAL ELECTRONICS CIRCUITS", "equipment": "Function generators, logic analyzers, IC testers", "capacity": "30", "lab_incharge": "PROF. D.D.PAWAR"},
        {"name": "POWER ELECTRONICS & DRIVES", "equipment": "Thyristors, inverters, choppers", "capacity": "30", "incharge": "PROF. B. SAMPATHKUMAR"},
        {"name": "COMPUTATIONAL LAB_I", "equipment": "Computers with MATLAB/Simulink, PSpice", "capacity": "30", "incharge": "PROF. A. B. AUTI"},
        {"name": "ELECTRICAL PROJECT LAB", "equipment": "Prototyping tools, measurement devices", "capacity": "30", "incharge": "PROF. A. B. AUTI"},
        {"name": "PLC & SCADA", "equipment": "PLC trainers, SCADA simulation software", "capacity": "30", "incharge": "PROF. C.H.MALLAREDDY"},
        {"name": "COMPUTATIONAL LAB-II", "equipment": "ETAP, PowerWorld, MiPower", "capacity": "30", "incharge": "PROF. J.B.PATIL"},
        {"name": "SWITCHGEAR & PROTECTION", "equipment": "Relay test kits, fault simulators", "capacity": "30", "incharge": "PROF. K. B. TAMBOLI"},
        {"name": "ELECTRICAL MEASUREMENT LAB", "equipment": "Wattmeters, energy meters, LCR meters", "capacity": "30", "incharge": "PROF. J.B.PATIL"}
],
        "events":[
        {"name": "PowerTech Symposium", "date": "November", "description": "Annual conference on power engineering"},
        {"name": "Green Energy Challenge", "date": "April", "description": "Competition for sustainable energy solutions"},
        {"name": "Industry Visit Week", "date": "September", "description": "Visits to power plants and substations"},
        {"name": "Energy Literacy Training by Energy Swaraj Foundation", "date": "2021-22", "description": "AICTE-collaborated training for SE students on energy literacy to combat climate change. Coordinated by ACEE Committee."},
        {"name": "Virtual Lab: Effective Tool for Teaching and Learning", "date": "N/A", "description": "Vlab session for faculty & students of Diploma in Electrical Engineering."},
        {"name": "Guest Lecture on Instrumentation and Control", "date": "27th November 2020", "description": "Expert lecture for students on Instrumentation and Control."},
        {"name": "Webinar on SCUBE Standard PLC Logic Development", "date": "N/A", "description": "Webinar on PLC logic development for the automotive industry."},
        {"name": "Expert Lecture on AC Motor Drives", "date": "22nd November 2020", "description": "Lecture for 4th-year Electrical Engineering students."},
        {"name": "VLab Session for Diploma Colleges", "date": "N/A", "description": "Training on virtual lab tools."},
        {"name": "Two-week Online Internship on PLC and SCADA", "date": "N/A", "description": "Hands-on internship program for students."},
        {"name": "Two-week Online Internship on MATLAB", "date": "16-28 Feb 2021", "description": "Training on MATLAB tools and applications."},
        {"name": "Diploma Connect - Virtual Lab", "date": "N/A", "description": "Interactive session for diploma students."},
        {"name": "GATE Expert Lecture", "date": "23rd November 2020", "description": "\"How I got GATE AIR 172 but you could get AIR 1\" by Mr. Nadeem Shaikh."},
        {"name": "SOLAR Ambassador Workshop", "date": "N/A", "description": "\"Role of Youth in Attaining Atmanirbhar Bharat in Energy.\""},
        {"name": "VACHAN PRERANA DIN", "date": "15th October 2020", "description": "Celebration of World Students' Day in memory of Dr. A.P.J. Abdul Kalam."},
        {"name": "Guru Poornima", "date": "AY 2019-20", "description": "Student speeches and cultural activities."},
        {"name": "Fresher’s Party", "date": "AY 2019-20", "description": "Welcome event for 2nd-year students."},
        {"name": "Teachers Day", "date": "5th Sept 2018", "description": "Felicitation of teachers, drama on the importance of teachers."},
        {"name": "Engineer’s Day", "date": "15th Sept 2018", "description": "Technical events: Poster presentation, treasure hunt, quiz competition."},
        {"name": "Motivational Guest Lectures", "date": "8th Sept 2018", "description": "Inspirational talks for students."},
        {"name": "Mahatma Gandhi Jayanti", "date": "3rd Oct 2018", "description": "Drama, speeches, and documentary on Gandhi's life."},
        {"name": "Marathi Bhasha Pandharwada", "date": "5th Jan 2019", "description": "Speeches and poster presentation."},
        {"name": "Technovation 2k19", "date": "9th March 2019", "description": "Technical event for diploma students; non-technical events for 11th & 12th students."},
        {"name": "Cultural Programs", "date": "25-26 Feb 2019", "description": "Themed days: Blue Day, Mismatch Day, Bollywood Day."},
        {"name": "Inter-Department Sports", "date": "27-28 Feb 2019", "description": "Cricket and volleyball matches."},
        {"name": "STTP on Transducers & Actuators", "date": "30 Dec 2019 - 3 Jan 2020", "description": "Short-term training program on industrial applications of transducers and actuators."}
],
        "achievements": [
        {"title": "Best Project Award", "year": "2023", "description": "For innovative solar power solution"},
        {"title": "Placement Record", "year": "2022", "description": "95% placement in core electrical companies"},
        {"title": "Research Collaboration", "year": "2021", "description": "With national power grid for smart grid research"},
        {"title": "Ph.D. Completion (Dr. Vijaykumar Shirwal)", "year": "2020-21", "description": "Topic: 'Efficient implementation of MIMO decoder on FPGA for high-speed wireless' (Shivaji University, Kolhapur)"},
        {"title": "GATE 2020 Qualifiers", "year": "2020", "description": "Mr. Niranjan Lambture (Score: 260), Miss Prerana Futane (Score: 311)"},
        {"title": "GATE 2019 Qualifier", "year": "2019", "description": "Mr. Vikram Badavane (Percentile: 340)"},
        {"title": "Ph.D. Registration (Prof. I.I. Mujawar)", "year": "N/A", "description": "Registered at Shivaji University, Kolhapur in Electrical Engineering"},
        {"title": "Master Trainer Appointment (Prof. V.B. Bhosale)", "year": "2017", "description": "Selected by MNRE & NISE among top 25 trainers in Renewable Energy across India"},
        {"title": "National & International Competitions", "year": "N/A", "description": "Department participation in technical and research competitions"}
],
        "careers": [
            {"role": "Power Systems Engineer", "description": "Design and maintain electrical power systems"},
            {"role": "Control Systems Engineer", "description": "Develop automation and control solutions"},
            {"role": "Renewable Energy Specialist", "description": "Design and implement green energy solutions"}
        ]
    },
    {
        "title": "Mechanical Engineering",
        "logo": "⚙",
        "image": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=500&q=80",
        "id": "mech",
        "description": "The Mechanical Engineering department provides education in design, thermal sciences, manufacturing, and materials science. Our hands-on program prepares students for careers in automotive, aerospace, energy, and manufacturing industries with a strong focus on innovation.",
        "faculty": [
        {"name": "Dr. Sonage B. K.", "designation": "Professor, Principal", "qualification": "BE, ME, PhD", "experience": "27"},
        {"name": "Dr. Metan S.S", "designation": "Professor", "qualification": "BE, MS, PhD", "experience": "28"},
        {"name": "Dr. Kashid A. S.", "designation": "Associate Professor", "qualification": "BE, ME, PhD", "experience": "18"},
        {"name": "Dr. Patil N. R.", "designation": "Associate Professor", "qualification": "BE, ME, PhD", "experience": "24"},
        {"name": "Mr. Kale S. S.", "designation": "Assistant Professor, HOD", "qualification": "BE, ME, PhD(Pur)", "experience": "16"},
        {"name": "Mr. Patil Y. B.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "14"},
        {"name": "Dr. Papade C. V.", "designation": "Assistant Professor", "qualification": "BE, MTech, PhD", "experience": "15"},
        {"name": "Mr. Bhoge D. D.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "14"},
        {"name": "Mr. Khillare S. K.", "designation": "Assistant Professor", "qualification": "BE, MTech, PhD(Pur)", "experience": "14"},
        {"name": "Mr. Awate M. B.", "designation": "Assistant Professor", "qualification": "BE, ME", "experience": "13"},
        {"name": "Mr. Birajdar B. R.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "13"},
        {"name": "Dr. Magar A. B.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD", "experience": "22"},
        {"name": "Mr. Dhobale A. S.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "13"},
        {"name": "Mr. Kamble A.H.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "14"},
        {"name": "Mr. Shaikh K.A.", "designation": "Assistant Professor", "qualification": "BE, ME, PhD(Pur)", "experience": "18"},
        {"name": "Mr. Gaikwad D. R.", "designation": "Assistant Professor", "qualification": "BE, ME", "experience": "19"},
        {"name": "Mr. A. M. Kalje", "designation": "Assistant Professor", "qualification": "BE, M.Tech", "experience": "28"},
        {"name": "Mrs. Sanga R. V.", "designation": "Assistant Professor", "qualification": "BE, M.Tech", "experience": "08"},
        {"name": "Dr. M. B. Kulkarni", "designation": "Assistant Professor", "qualification": "BE, ME, PhD", "experience": "20"},
        {"name": "Mr. T. A. Garande", "designation": "Assistant Professor", "qualification": "BE, ME", "experience": "10"},
        {"name": "Dr. V. S. Hiremath", "designation": "Assistant Professor", "qualification": "BE, M.Tech, PhD", "experience": "10"},
        {"name": "Mr. S. N. Gaikwad", "designation": "Assistant Professor", "qualification": "BE, M.Tech", "experience": "09"}
],
        "labs":[
        {"name": "CAD / CAM Lab", "equipment": "CAD workstations, CNC machines", "capacity": "30", "incharge": "Prof. S. K. Khillare"},
        {"name": "Applied Thermodynamics Lab", "equipment": "Heat engines, calorimeters", "capacity": "30", "incharge": "Prof. D. D. Bhoge"},
        {"name": "Manufacturing Processes Lab", "equipment": "Lathes, milling machines", "capacity": "30", "incharge": "Prof. Y. B. Patil"},
        {"name": "Theory of Machines Lab", "equipment": "Gear systems, vibration analyzers", "capacity": "30", "incharge": "Prof. A. S. Kashid"},
        {"name": "Basic Mechanical Engineering Lab", "equipment": "Material testing kits, basic tools", "capacity": "30", "incharge": "Dr. A. M. Kazi"},
        {"name": "Workshop Lab", "equipment": "Welding tools, carpentry tools", "capacity": "30", "incharge": "Dr. S. E. Gudur"},
        {"name": "Fluid Power & Fluid Machinery Lab", "equipment": "Hydraulic pumps, turbines", "capacity": "30", "incharge": "Dr. A. B. Magar"},
        {"name": "Engineering Metallurgy Lab", "equipment": "Microscopes, hardness testers", "capacity": "30", "incharge": "Prof. A. H. Kamble"},
        {"name": "Metrology & Mechanical Measurement Lab", "equipment": "Micrometers, CMM machines", "capacity": "30", "incharge": "Prof. A. S. Dhobale"},
        {"name": "Automatic Control System Lab", "equipment": "PLC kits, servo motors", "capacity": "30", "incharge": "Dr. A. B. Magar"},
        {"name": "Heat and Mass Transfer Lab", "equipment": "Heat exchangers, thermocouples", "capacity": "30", "incharge": "Prof. D. D. Bhoge"},
        {"name": "Experimental Stress Analysis Lab", "equipment": "Strain gauges, load cells", "capacity": "30", "incharge": "Prof. Mrs. R. V. Sanga"},
        {"name": "Internal Combustion Engine Lab", "equipment": "IC engines, dynamometers", "capacity": "30", "incharge": "Prof. D. D. Bhoge"},
        {"name": "Power Plant & Energy Engineering Lab", "equipment": "Steam turbines, solar panels", "capacity": "30", "incharge": "Dr. C. V. Papade"},
        {"name": "Automobile Engineering Lab", "equipment": "Vehicle diagnostics tools, chassis", "capacity": "30", "incharge": "Prof. K. A. Shaikh"},
        {"name": "Refrigeration & Air Conditioning Lab", "equipment": "Refrigeration units, psychrometers", "capacity": "30", "incharge": "Dr. M. B. Kulkarni"},
        {"name": "Mechatronics Lab", "equipment": "Robotics kits, sensors", "capacity": "30", "incharge": "Dr. S. S. Metan"},
        {"name": "Engineering Graphics Lab", "equipment": "Drafting tables, CAD software", "capacity": "30", "incharge": "Prof. M. B. Awate"},
        {"name": "Solar Research Center", "equipment": "Solar simulators, PV modules", "capacity": "30", "incharge": "Dr. C. V. Papade"}
    ],
        "events": [
        {"name": "Engineers Day Celebration", "date": "15/09/2021", "description": "Annual celebration honoring engineers' contributions"},
        {"name": "Precision Camshaft’s Entry in Electric Vehicle Segment", "date": "05/10/2021", "description": "Expert talk by Mr. Karan Shah on EV industry trends"},
        {"name": "MESA Inauguration", "date": "23/07/2020", "description": "Launch of Mechanical Engineering Students Association (MESA)"},
        {"name": "Teachers Day Celebrations", "date": "05/09/2020", "description": "Event honoring faculty members"},
        {"name": "Engineers Day Celebrations", "date": "15/10/2020", "description": "Technical competitions and guest lectures"},
        {"name": "Technical Session: Corporate Life & Career in Automotive Design", "date": "07/11/2020", "description": "Talk by Mr. Navanath Junghare (Ford Motors)"},
        {"name": "Technical Session: Total Quality Management", "date": "13/12/2020", "description": "Workshop on 5S, 6-Sigma, FMEA, JIT by Mr. Ramesh Kotanur (Mahindra & Mahindra)"},
        {"name": "DSE Connect Activity: Electrical and Electronic Systems", "date": "13/05/2021", "description": "Industry-aligned workshop for students"},
        {"name": "DSE Connect Activity: Automotive Battery", "date": "18/05/2021", "description": "Hands-on session on battery technologies"},
        {"name": "DSE Connect Activity: Cam and Follower", "date": "19/05/2021", "description": "Practical demonstration of mechanical components"},
        {"name": "DSE Connect Activity: Brakes and Clutches", "date": "24/05/2021", "description": "Interactive workshop on automotive systems"},
        {"name": "Expert Lecture: Solar PV Systems & Installations", "date": "26/06/2021", "description": "Training for Sahyadri Vidyut employees"},
        {"name": "Workshop: How to Prepare Effectively for GATE-2022", "date": "30/05/2021", "description": "Guidance session by Prof. Deepak Bhoge"},
        {"name": "Motivational Talk by Prof. A.D. Joshi", "date": "Not specified", "description": "Inspirational session for students"},
        {"name": "DSE Connect Activity: Industrial Pneumatic & Hydraulic Systems", "date": "11/05/2021", "description": "Workshop on fluid power applications"},
        {"name": "DSE Connect Activity: Vapour Compression Refrigeration System", "date": "11/05/2021", "description": "Virtual lab session"},
        {"name": "E-Sendoff", "date": "22/08/2021", "description": "Farewell event for outgoing students"},
        {"name": "Workshop: Vehicle Dynamics", "date": "27/08/2021", "description": "Four-day hands-on training"},
        {"name": "Student Workshop: Fundamentals of Vehicle Dynamics", "date": "27/08/2021", "description": "Practical insights into vehicle engineering"},
        {"name": "Inauguration of MESA", "date": "27/09/2019", "description": "Formal launch of student association"},
        {"name": "Teachers Day Celebration", "date": "05/09/2019", "description": "Annual faculty appreciation event"},
        {"name": "DSE Connect Activity: Metallurgy Workshop", "date": "06/09/2019", "description": "One-day workshop on material science"},
        {"name": "DSE Connect Activity: Recent Trends in Automobile", "date": "06/09/2019", "description": "Industry trends discussion"},
        {"name": "DSE Connect Activity: Recent Trends in Refrigeration & Air Conditioning", "date": "18/01/2020", "description": "Emerging technologies in HVAC"},
        {"name": "Expert Session: Bharat Petroleum Industry Insights", "date": "04/02/2020", "description": "Talk by Mr. Santoshkumar Nivendkar"},
        {"name": "Session: Go Green, Ride with Pride", "date": "05/02/2020", "description": "Sustainability talk by Mr. Parag Bhayani"},
        {"name": "Parent Meet (SE/TE Class)", "date": "05/02/2020", "description": "Interaction with parents of students"},
        {"name": "SAEINDIA WS Student Convention 2020", "date": "04/03/2020", "description": "National-level technical event"},
        {"name": "SAEINDIA Workshop: Vehicle Dynamics", "date": "06-07/03/2020", "description": "Two-day intensive training"},
        {"name": "Online Parent Meeting", "date": "30/05/2020", "description": "Virtual interaction with parents"},
        {"name": "Online Alumni Meeting", "date": "05/07/2020", "description": "Networking session with graduates"},
        {"name": "E-Sendoff Ceremony", "date": "01/07/2020", "description": "Virtual farewell for final-year students"}
],
        "achievements": [
        {"title": "Patent Granted: MECHANIZED CLOTH DUSTER","year": "N/A","description": "Patent granted to Dr. B. K. Sonage & Prof. A. S. Kashid by the Patent Office, Government of India"},
        {"title": "Nation Builder Award 2023","year": "2023","description": "Awarded to Dr. Shriniwas S Metan by the Rotary Club of Solapur"},
        {"title": "Shikshak Gaurav Puraskar 2023","year": "2023","description": "Awarded to Dr. Shriniwas S Metan"},
        {"title": "Best Teacher Award","year": "N/A","description": "Awarded to Dr. N. R. Patil by Annapurna Foundation, Solapur"},
        {"title": "Ideal Teacher Award","year": "N/A","description": "Awarded to Prof. Kadir Shaikh"},
        {"title": "Krantisury Mahatma Jyotiba Phule Gunwant Shikshak Puraskar","year": "N/A","description": "State-level award received by Prof. Yogesh Patil"},
        {"title": "TOYCATHON 2021 Physical Competition Shortlist","year": "2021","description": "Team Designovation (Vishvesh Patil, Rushikesh Lagli, Siddheshwar Madole) shortlisted; Mentor: Prof. Vaibhav Kulkarni"},
        {"title": "Innovation Ambassador Nomination","year": "N/A","description": "Prof. Vaibhav Kulkarni (Convener of IIC 3.0) nominated by MHRD MIC"},
        {"title": "Top Projects in International Competition","year": "N/A","description": "Mechanical students secured 3 top projects out of 100 in Dassault Systèmes competition"},
        {"title": "GATE-2019 Success","year": "2019","description": "Mr. Shubham Gorande secured a score of 417 in GATE"},
        {"title": "GRE/TOEFL Success","year": "N/A","description": "Students cracked IELTS for master's abroad; Coordinated by Dr. S. S. Metan"},
        {"title": "MoU with Dassault Systèmes Foundation","year": "2018","description": "Signed on 14th September 2018 for 'Solar Innovation & Skill Development Center' (Funding: ₹24.8L by Dassault, ₹6.2L by institute)"},
        {"title": "MoU with Tata Technologies Ltd","year": "N/A","description": "Prayatna Scholarship for SUPRA vehicle development (Funding: ₹1.5L)"}
],
        "careers": [
            {"role": "Mechanical Design Engineer", "description": "Design mechanical components and systems"},
            {"role": "Thermal Engineer", "description": "Work on heat transfer and energy systems"},
            {"role": "Manufacturing Engineer", "description": "Optimize production processes and systems"}
        ]
    },
    {
        "title": "Civil Engineering",
        "logo": "🏗",
        "image": "https://images.unsplash.com/photo-1479839672679-a46483c0e7c8?auto=format&fit=crop&w=500&q=80",
        "id": "civil",
        "description": "The Civil Engineering department offers education in structural engineering, construction technology, geotechnical engineering, and environmental engineering. Our program emphasizes sustainable development and prepares students for careers in infrastructure development and urban planning.",
        "faculty": [
        {"name": "Dr. More S. B.","designation": "Professor, HOD","qualification": "BE, ME, PhD","experience": "31"},
        {"name": "Dr. Patki V. K.","designation": "Professor, Vice-Principal (Admin & Academics)","qualification": "BE, ME, PhD","experience": "23"},
        {"name": "Dr. Jahagirdar S. S.","designation": "Professor, Dean (R&D)","qualification": "BE, ME, PhD","experience": "20"},
        {"name": "Dr. Ms. Nirantar S. R.","designation": "Asst. Professor","qualification": "BE, MTech, PhD","experience": "19"},
        {"name": "Mr. Kankuntla A. Y.","designation": "Asst. Professor","qualification": "BE, ME","experience": "14"},
        {"name": "Mr. Kulkarni G. J.","designation": "Asst. Professor","qualification": "BE, ME","experience": "17"},
        {"name": "Mr. Pawar D. S.","designation": "Asst. Professor","qualification": "BE, ME, Ph.D Pursuing","experience": "17"},
        {"name": "Mr. Kale S. M","designation": "Asst. Professor","qualification": "BE, ME","experience": "12"},
        {"name": "Mr. Maske R. G.","designation": "Asst. Professor","qualification": "BE, MTech.","experience": "13"},
        {"name": "Mr. Kulkarni S.R.","designation": "Asst. Professor","qualification": "BE, MTech.","experience": "13"},
        {"name": "Mr. Salimath V. A.","designation": "Asst. Professor","qualification": "B.E, MTech.","experience": "6"},
        {"name": "Mr. F. S. Kazi","designation": "Asst. Professor","qualification": "BE (Civil Engg), MTech (Water Resources Engg)"},
        {"name": "Mr. Jamdar A. S.","designation": "Asst. Professor","qualification": "M.E.(Structures), Ph.D Pursuing",},
        {"name": "Mr. Patil R. A.","designation": "Asst. Professor","qualification": "B.E. (Civil), M.Tech. (Structures)"},
        {"name": "Ms. Vadnal P. A.","designation": "Asst. Professor","qualification": "B.E. (Civil), M.E. (Construction & Management), PhD (Civil) Pursuing",},
        {"name": "Mr. Joshi S. K.","designation": "Asst. Professor","qualification": "B. E. (Civil), M.Tech(Applied Mechanics)"},
        {"name": "Mr. Sangave A. A","designation": "Asst. Professor","qualification": "B.E. (Civil), M.Tech. (Hydraulic)","experience": "8"},
        {"name": "Mr. A. P. Pataskar","designation": "Asst. Professor","qualification": "B.E.(Civil), M.E.(Structures)","experience": "23"},
        {"name": "Mr. S. G. Teggi","designation": "Asst. Professor","qualification": "B.E.(Civil), M.Tech(Geotech Engg) Ph.D Pursuing","experience": "10"}
],
        "labs": [
        {"name": "Environmental Engineering Lab","incharge": "Dr. S. S. Jahagirdar","equipment": "BOD incubators, COD digesters, pH meters, turbidity meters","capacity": "30"},
        {"name": "Geotechnical Engineering Lab","incharge": "Prof. S. G. Teggi","equipment": "Triaxial testing machines, CBR apparatus, direct shear devices, consolidation apparatus","capacity": "30"},
        {"name": "Material Testing Lab","incharge": "Prof. R. G. Maske","equipment": "Universal testing machines, impact testing machines, hardness testers, torsion testing machines","capacity": "30"},
        {"name": "Fluid Mechanics & Machinery Lab","incharge": "Prof. F. S. S. S. Kale","equipment": "Flow measurement devices, hydraulic benches, centrifugal pumps, turbines","capacity": "30"},
        {"name": "Concrete Technology Lab","incharge": "Prof. G. J. Kulkarni","equipment": "Compression testing machines, slump test apparatus, curing tanks, rebound hammers","capacity": "30"},
        {"name": "Transportation Engineering Lab","incharge": "Prof. V. A. Salimath","equipment": "Los Angeles abrasion machine, aggregate impact tester, bitumen testing equipment","capacity": "30"},
        {"name": "Engineering Geology Lab","incharge": "Prof. A. Y. Kankuntala","equipment": "Petrological microscopes, rock testing equipment, mineral identification kits","capacity": "30"},
        {"name": "Surveying & Basic Civil Engineering Lab","incharge": "Prof. D. S. Pawar","equipment": "Total stations, theodolites, leveling instruments, surveying accessories","capacity": "30"},
        {"name": "Applied Mechanics Lab","incharge": "Prof. S. R. Nirantar","equipment": "Beam deflection apparatus, friction experiment setups, moment of inertia apparatus","capacity": "30"},
        {"name": "Computer Lab","incharge": "Prof. S. M. Kale","equipment": "CAD workstations, civil engineering software (STAAD Pro, AutoCAD), plotters","capacity": "30"},
        {"name": "Departmental Library","incharge": "Prof. A. A. Sangave","equipment": "Technical books, journals, research papers, digital resources","capacity": "30"}
],
        "events":{
  "industrial_visits": [
        {"name": "Prestressed Concrete Sleeper Factory, Mohol","date": "20/10/2023","description": "Visit coordinated by Prof. D. S. Pawar for 87 TY students"},
        {"name": "PCMC Water Treatment Plant & Pune Metro Construction","date": "01/10/2023","description": "Visit coordinated by Dr. S. B. More for 40 B.Tech students"},
        {"name": "Shri Sidheswar Sugar Factory (Industrial Waste Management)","date": "22/03/2024","description": "Visit coordinated by Prof. G. J. Kulkarni for 33 TY students"},
        {"name": "Water Treatment Plant - Soregaon & Pakani","date": "05/04/2024","description": "Visit coordinated by Dr. V. K. Patki & Dr. S. S. Jahagirdar for 65 SY students"},
        {"name": "Bullet Train Project & CTARA IIT Bombay","date": "15-16/04/2024","description": "Visit coordinated by Prof. F. K. Maniyar for 40 TY students"},
        {"name": "Water Treatment Plant - Soregaon & Pakni","date": "18/04/2023","description": "Visit coordinated by Dr. V. K. Patki for 103 TY students"},
        {"name": "Ujani Dam","date": "20/06/2022","description": "Visit coordinated by Prof. F. S. Kazi for 109 SY students"},
        {"name": "Pakani & Soregaon Water Treatment Plants","date": "13/06/2022","description": "Visit coordinated by Dr. V. K. Patki for 125 SY students"},
        {"name": "Chincholi MIDC & Degaon Waste Water Treatment Plants","date": "27/04/2022","description": "Visit coordinated by Dr. S. S. Jahagirdar for 150 TY students"},
        {"name": "C&D Waste Processing Plant, PMC","date": "01/12/2021","description": "Visit coordinated by Dr. S. S. Jahagirdar for 5 students"}
  ],
  "expert_lectures": [
        {"title": "International Year of Millets-2023","date": "27/08/2023","description": "Lecture by Dr. Nayna Vyavhare"},
        {"title": "Future Importance of Civil Engineering & Latest Innovations","date": "15/09/2023","description": "Lecture by Mr. Abhijeet Sathe"},
        {"title": "Introduction to Civil Engineering Software","date": "21/02/2024","description": "Session by Mr. Rishikesh Tantak & Mr. Rishikesh Mugutkar"},
        {"title": "Effective Use of MS Project","date": "10/03/2023","description": "Workshop by Mr. Chetan Shivchalappa" },
        {"title": "Business Deals in Construction","date": "20/03/2023","description": "Lecture by Mr. Akshay Vitthal Yeole, MD Samarth Construction"},
        {"title": "Career Guidance","date": "21/03/2023","description": "Session by Shri Shree Krishna Galgali, Retd. Chief Engineer NTPC"},
        {"title": "Importance of Software for Civil Engineers","date": "27/03/2023","description": "Lecture by Mr. Hitesh Lahoti"},
        {"title": "Construction Process","date": "03/05/2023","description": "Lecture by Mr. Ravindra Jagtap, GM Durocrete Engineering"},
        {"title": "The Ultimate Success","date": "14/09/2021","description": "Motivational session by Prof. Touheed Mujawar"},
        {"title": "Career Opportunities After B.Tech","date": "11/11/2021","description": "Lecture by Er. Kedar Wadekar, Cushman and Wakefield"},
        {"title": "Importance of BIM for Civil Engineers","date": "15/09/2021","description": "Technical session by Er. Siddhant Pawar, BIM Manager"},
        {"title": "Personality Development & Skill Enhancement","date": "27/12/2021","description": "Workshop by Prof. Arshad Sayyad, NLP Master"},
        {"title": "Emerging Trends in Civil Engineering","date": "11/01/2022","description": "Lecture by Mr. Abhijeet Patankar, CADD Center"},
        {"title": "Finance Management","date": "23/03/2022","description": "Session by Mr. Avinash Mahagaonkar, Lokmangal Group"},
        {"title": "GATE Preparation Guidance","date": "29/03/2022","description": "Workshop by Mr. Shrikant Kale, Asst. Professor NKOCET"},
        {"title": "Professional E-Tendering in Civil Work","date": "05/06/2022","description": "Technical session by Er. Navnath Nichare, DCE APJ Society"},
        {"title": "Stability Analysis of Chimney","date": "02/06/2022","description": "Technical lecture by Dr. J. B. Dafedar, Principal NKOCET"},
        {"title": "International Yoga Day","date": "05/05/2021","description": "Session by Ms. Vandana Shinde, Yoga Teacher"}
  ]
},
        "achievements": [
        {"title": "Project Presentation Winners","year": "2023","description": "Rohit Sagar, Shrutika Yangali, and Vasanti Aarangi secured 3rd prize in Project Presentation at WIT, Solapur"},
        {"title": "GATE 2022 Qualifier","year": "2022","description": "Mane Vidya qualified GATE-2022 with 23.45 percentile"},
        {"title": "Best Outgoing Student","year": "2023","description": "Mr. Sajjid Tamboli (B.Tech Civil) declared Best Outgoing Student of the Department"},
        {"title": "AGTECH FEST Champions","year": "2023","description": "Team (Shoaib Sayyad, Sourav Pawar, Parth Abhangrao, Padma Govindraj) won 1st prize in BGMI competition"},
        {"title": "AutoCAD Competition Winners","year": "2023","description": "Rayyad Ustad and Akash Sarvade secured 2nd prize in Auto CAD War at AGPIT, Solapur"},
        {"title": "Paper Tower Challenge","year": "2023","description": "Rayyad Ustad won 2nd prize in Paper Tower competition at AGTECH FEST"},
        {"title": "GATE 2022 Top Scorers","year": "2022","description": "Ritik Rajendra Katve (95.36%) and Shruti Ambadas Yemul (86.31%) qualified GATE-2022"},
        {"title": "MPSC Engineering Services Success","year": "2022","description": "Swaminath Pujari (AE-I PWD), Pavan Benjarpe (AE-II PWD), and Megha Gheradi (AE-II WRD) cleared MPSC exam"},
        {"title": "Best Outgoing Student","year": "2022","description": "Ms. Jogdankar Asharani Laxman (B.Tech Civil) declared Best Outgoing Student"},
        {"title": "Green Building Award","year": "2023","description": "For sustainable design project"},
        {"title": "Research Grant","year": "2022","description": "For earthquake-resistant structures study"},
        {"title": "Industry Partnership","year": "2021","description": "With leading construction company"}
],
        "careers": [
            {"role": "Structural Engineer", "description": "Design buildings and infrastructure"},
            {"role": "Construction Manager", "description": "Oversee construction projects"},
            {"role": "Geotechnical Engineer", "description": "Analyze soil and foundation conditions"}
        ]
    }
]

# Create Cards
st.subheader("🔍 Explore Departments")
cols = st.columns(4)
for idx, dept in enumerate(departments):
    with cols[idx % 4]:
        st.markdown(
            f"""
            <div class="department-card" style="background-image: url('{dept['image']}')">
            <div class="card-content">
                <div class="card-title">{dept['logo']} {dept['title']}</div>
                <a class="explore-btn" href="#{dept['id']}">Explore</a>
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.subheader("📚 Department Details")
for dept in departments:
    st.markdown(f'<div class="scroll-target" id="{dept["id"]}"></div>', unsafe_allow_html=True)
    st.markdown(f"## {dept['logo']} {dept['title']}")
    st.markdown(dept["description"])

    # Tabs for different sections (move all content inside this loop)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🏫 About", 
        "👨‍🏫 Faculty", 
        "🔬 Laboratories", 
        "📅 Events", 
        "🏆 Achievements & Careers", 
        "🎥 Know your Department"
    ])

    with tab1:
        # Department Highlights (customized per department)
        highlights = {
            "foundation": {
                "Established": "2008",
                "Student Intake": "600 per year",
                "Research Areas": "Basic Sciences, Engineering Fundamentals, Pedagogy"
            },
            "cse": {
                "Established": "2008",
                "Student Intake": "180 per year",
                "Research Areas": "AI, Data Science, Cybersecurity, Software Engineering"
            },
            "ai-ds": {
                "Established": "2008",
                "Student Intake": "60 per year",
                "Research Areas": "Artificial Intelligence, Machine Learning, Big Data Analytics"
            },
            "entc": {
                "Established": "2008",
                "Student Intake": "60 per year",
                "Research Areas": "Communication Systems, VLSI, Embedded Systems"
            },
            "ee": {
                "Established": "2008",
                "Student Intake": "60 per year",
                "Research Areas": "Power Systems, Renewable Energy, Control Systems"
            },
            "mech": {
                "Established": "2008",
                "Student Intake": "120 per year",
                "Research Areas": "Thermal Engineering, Design, Manufacturing, solaer energy, Drone technology"
            },
            "civil": {
                "Established": "2008",
                "Student Intake": "60 per year",
                "Research Areas": "Structural Engineering, Geotechnical Engineering, Construction Technology"
            }
        }
        dept_high = highlights.get(dept["id"], {})
        if dept_high:
            st.markdown("### Department Highlights")
            st.markdown(
                f"""
                <ul>
                    <li><b>Established:</b> {dept_high.get('Established', 'N/A')}</li>
                    <li><b>Student Intake:</b> {dept_high.get('Student Intake', 'N/A')}</li>
                    <li><b>Research Areas:</b> {dept_high.get('Research Areas', 'N/A')}</li>
                </ul>
                """, unsafe_allow_html=True
            )

    with tab2:
        st.markdown("### Faculty")
        faculty_data = []
        for fac in dept.get("faculty", []):
            faculty_data.append({
                "Name": fac.get("name", ""),
                "designation": fac.get("designation", ""),
                "qualification": fac.get("qualification", ""),
                
            })
        if faculty_data:
            df_faculty = pd.DataFrame(faculty_data)
            st.table(df_faculty)
        else:
            st.info("No faculty information available.")

    with tab3:
        st.markdown("### Laboratories & Facilities")
        lab_data = []
        labs = dept["labs"]
        # Flatten labs if it's a nested list (e.g., for ENTC)
        if isinstance(labs, list) and len(labs) > 0 and isinstance(labs[0], list):
            labs = [lab for sublist in labs for lab in sublist]
        for lab in labs:
            lab_data.append({
                "Lab Name": lab.get("name", "N/A"),
                "Equipment": lab.get("equipment", "N/A"),
                "Capacity": lab.get("capacity", "N/A"),
                "Incharge": lab.get("incharge", "N/A")
            })
        if lab_data:
            df_labs = pd.DataFrame(lab_data)
            st.table(df_labs)
        else:
            st.info("No laboratory information available.")

        st.markdown("""
        <div style="margin-top: 20px; background-color: #f5f5f5; padding: 15px; border-radius: 10px;">
            <h4>Additional Facilities</h4>
            <ul>
                <li>Departmental library with 1000+ titles</li>
                <li>High-speed internet connectivity</li>
                <li>24/7 access to computer labs</li>
                <li>Project work spaces</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### Department Events")
        events = dept["events"]
        # Handle Civil Engineering events (dict) and others (list)
        if isinstance(events, dict):
            # For Civil, show industrial visits and expert lectures separately
            if "industrial_visits" in events:
                st.markdown("#### Industrial Visits")
                for event in events["industrial_visits"]:
                    st.markdown(f"""
                    <div class="event-card">
                        <h4>{event['name']} - {event['date']}</h4>
                        <p>{event['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
            if "expert_lectures" in events:
                st.markdown("#### Expert Lectures")
                for event in events["expert_lectures"]:
                    st.markdown(f"""
                    <div class="event-card">
                        <h4>{event['title']} - {event['date']}</h4>
                        <p>{event['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            for event in events:
                st.markdown(f"""
                <div class="event-card">
                    <h4>{event['name']} - {event['date']}</h4>
                    <p>{event['description']}</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-top: 20px; background-color: #fff3e0; padding: 15px; border-radius: 10px;">
            <h4>Annual Activities</h4>
            <ul>
                <li>Industry visits and guest lectures</li>
                <li>Alumni interaction sessions</li>
                <li>Technical paper competitions</li>
                <li>Workshops on emerging technologies</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Achievements")
            for achievement in dept["achievements"]:
                title = achievement.get("title", achievement.get("name", "Achievement"))
                year = achievement.get("year", "")
                description = achievement.get("description", "")
                st.markdown(f"""
                <div class="achievement-card">
                    <h4>{title} ({year})</h4>
                    <p>{description}</p>
                </div>
                """, unsafe_allow_html=True)
        with col2:
            st.markdown("### Career Opportunities")
            for career in dept["careers"]:
                st.markdown(f"""
                <div class="career-card">
                    <h4>{career['role']}</h4>
                    <p>{career['description']}</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("""
            <div style="margin-top: 20px; background-color: #e8f5e9; padding: 15px; border-radius: 10px;">
                <h4>Placement Statistics</h4>
                <ul>
                    <li>90%+ placement rate</li>
                    <li>Average salary: ₹6.5 LPA</li>
                    <li>Highest package: ₹10.48 (and mores) LPA</li>
                    <li>50+ recruiting companies</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with tab6:
        st.markdown("### 🎥 Know Your Department")
        dept_videos = {
            "foundation": "https://youtu.be/lJtqwoNVJhw?si=oQpp5J5OIi9BrL6X",
            "cse":  "https://youtu.be/9rQYbkPphgo?si=CtxzVR73qPilTw30",
            "ai-ds":"https://youtu.be/TFfh5_muERk?si=2OJ_bGaOXtd95439",
            "entc": "https://youtu.be/ilIK7Jc5wZs?si=Lxs2iPwWUUttt4e3",
            "ee":   "https://youtu.be/rK23wsB6HLw?si=5mGz7SYxYsigPg0n",
            "mech": "https://youtu.be/CGlFi6kz_pk?si=baSePKtPICFdYaha",
            "civil":"https://youtu.be/nxbZaic-O98?si=_-L6nfHurK9UfO53",
        }
        video_path = dept_videos.get(dept["id"])
        if video_path:
            st.info("Watch the department introduction video below:")
            st.video(video_path)
        else:
            st.info("Department video coming soon!")
    
st.markdown("---")

# Why NKOCET Section
st.subheader("🎯 Why Choose NKOCET?")
st.markdown("""
<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">
        <div>
            <h4 style="color: #2b5876;">🏆 Industry Collaborations</h4>
            <p>Regular guest lectures and workshops from industry experts</p>
        </div>
        <div>
            <h4 style="color: #2b5876;">🔬 Research Focus</h4>
            <p>Undergraduate research programs with faculty mentors</p>
        </div>
        <div>
            <h4 style="color: #2b5876;">💼 Placement Support</h4>
            <p>Dedicated placement cell with 90%+ placement record</p>
        </div>
        <div>
            <h4 style="color: #2b5876;">🖥 Modern Labs</h4>
            <p>Well-equipped laboratories with latest equipment</p>
        </div>
        <div>
            <h4 style="color: #2b5876;">📚 Skill Development</h4>
            <p>Value-added courses and certification programs</p>
        </div>
        <div>
            <h4 style="color: #2b5876;">🌍 Global Exposure</h4>
            <p>International collaborations and student exchange programs</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.info("ℹ Students can request department transfers after first year based on academic performance and seat availability.")

# Fixed "Go to Top" button
st.markdown("""
<style>
#go-top-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    background-color: #0072ff;
    color: white;
    padding: 10px 16px;
    font-size: 16px;
    border-radius: 8px;
    text-align: center;
    z-index: 9999;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}
#go-top-btn:hover {
    background-color: #0056cc;
}
</style>

<a href="#top-anchor" id="go-top-btn"> ⬆ </a>
""", unsafe_allow_html=True)
footer()