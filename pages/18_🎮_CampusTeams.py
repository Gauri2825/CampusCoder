import streamlit as st
import base64
import os
from utils.file import footer

st.set_page_config(layout="wide")

teams = [
    {
        "name": "Team Ashwamedh",
        "desc": "Designing and building formula racing cars for national-level competitions",
        "details": "Team Ashwamedh is a student-run motorsport team that designs and builds formula-style race cars to compete in national-level events. They emphasize innovation, engineering excellence, and teamwork, providing students with hands-on experience in automotive design and manufacturing.",
        "img": "assets/Ashwamedh.jpg",
        "color": "#756BFF",
        "insta": "https://www.instagram.com/teamashwamedh?igsh=MXBic2docXJ0YW5mdg==",
        "gallery": "https://campuscoders.pixieset.com/teamashwamedh/"
    },
    {
        "name": "Team Avengineers",
        "desc": "Aerospace engineering team specializing in UAV design and development.",
        "details": "Team Avengineers focuses on the design, fabrication, and testing of unmanned aerial vehicles (UAVs) for various applications. The team participates in national and international aeronautical competitions, showcasing their expertise in aerodynamics, propulsion, and control systems.",
        "img": "assets/Avengineers.jpg",
        "color": "#00B4D8",
        "insta": "https://www.instagram.com/team_avengineers?igsh=ZXd5ZGQ0aWgxaGo4",
        "gallery": "https://campuscoders.pixieset.com/teamavengineers/"
    },
    {
        "name": "Team Pushpak",
        "desc": "Aerodesign team from NK Orchid College of Engineering & Technology, Solapur.",
        "details": "Team Pushpak is a group of mechanical engineering students from R.V. College of Engineering who design and build unmanned aerial vehicles (UAVs) capable of lifting maximum payloads within specified constraints. They have represented India in international competitions, including the SAE Brasil Aerodesign competition.",
        "img": "assets/Pushpak.jpg",
        "color": "#3A86FF",
        "insta": "https://www.instagram.com/team_pushpak?igsh=MWNvN2Qzd2Q4eHlpMQ==",
        "gallery": "https://campuscoders.pixieset.com/teampushpak/"
    },
    {
        "name": "Team Suryan",
        "desc": "Solar vehicle research and development team.",
        "details": "Suryan designs and builds solar-powered vehicles, holding the record for longest distance traveled on a single charge in national competitions. Focused on renewable energy solutions.",
        "img": "assets/suryan.jpg",
        "color": "#8338EC",
        "insta": "https://www.instagram.com/team.suryan?igsh=MXV5aTQxcjdvcTJycw==",
        "gallery": "https://campuscoders.pixieset.com/teamsuryan/"
    },
]

# CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
    }

    .team-container {
        display: flex;
        flex-direction: column;
        margin-bottom: 2.5rem;
        background: white;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        overflow: hidden;
        transition: transform 0.3s ease;
    }

    .team-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }

    .team-image {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-bottom: 1px solid #eee;
    }

    .image-wrapper {
        position: relative;
    }

    .insta-icon {
        position: absolute;
        bottom: 10px;
        right: 10px;
        background: #ffffffdd;
        border-radius: 50%;
        padding: 6px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease;
    }

    .insta-icon:hover {
        transform: scale(1.1);
    }

    .team-content {
        padding: 1.5rem;
    }

    .team-separator {
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--team-color), transparent);
        margin: 1rem 0;
        opacity: 0.7;
    }

    .team-name {
        color: var(--team-color);
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .team-desc {
        color: #555;
        font-size: 1rem;
        margin-bottom: 1rem;
    }

    .team-details {
        color: #333;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    @media (max-width: 768px) {
        .team-column {
            width: 100% !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="
    text-align: center; 
    padding: 3rem 1rem; 
    margin-bottom: 2rem; 
    background: linear-gradient(135deg, #b2ebf2 0%, #90caf9 100%); 
    border-radius: 16px; 
    color: #212121; 
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1); 
    max-width: 900px; 
    margin-left: auto; 
    margin-right: auto;
    animation: fadeIn 1.2s ease-in-out;
">
    <h1 style="font-size: 3rem; margin-bottom: 0.5rem; color: #0d47a1; font-family: 'Segoe UI', sans-serif;">
        🏎️ Student Innovation Hub 🛩️
    </h1>
    <p style="font-size: 1.3rem; opacity: 0.9; font-family: 'Segoe UI', sans-serif;">
        Discover the cutting-edge projects and brilliant minds shaping tomorrow's technology.
    </p>
</div>

<style>
@keyframes fadeIn {
  from {opacity: 0; transform: translateY(20px);}
  to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# Team cards
col1, col2 = st.columns(2, gap="large")

for i, team in enumerate(teams):
    column = col1 if i % 2 == 0 else col2

    with column:
        try:
            with open(team["img"], "rb") as f:
                img_data = base64.b64encode(f.read()).decode()

            st.markdown(f"""
                <div class="team-container" style="--team-color: {team['color']}">
                    <div class="image-wrapper">
                        <img class="team-image" src="data:image/jpeg;base64,{img_data}" alt="{team['name']}">
                        <a class="insta-icon" href="{team['insta']}" target="_blank" title="Visit Instagram">
                            <img src="https://img.icons8.com/ios-filled/24/8338EC/instagram-new.png" width="36" height="36"/>
                        </a>
                    </div>
                    <div class="team-content">
                        <div class="team-name">{team['name']}</div>
                        <div class="team-desc">{team['desc']}</div>
                        <div class="team-separator"></div>
                        <div class="team-details">{team['details']}</div>
                    </div>
                </div>
                <div style="text-align: center; margin: 10px 0 40px 0;">
                    <a href="{team['gallery']}" target="_blank" style="text-decoration: none;">
                        <button style="
                            background: linear-gradient(135deg, {team['color']}, #ffffff40);
                            color: white;
                            padding: 14px 30px;
                            font-size: 18px;
                            border: none;
                            border-radius: 40px;
                            cursor: pointer;
                            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
                            transition: all 0.3s ease;
                            font-weight: bold;
                            display: inline-flex;
                            align-items: center;
                            justify-content: center;
                            min-width: 250px;
                        ">
                            📸 View {team['name'].split()[1]} Gallery ➔
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)

        except FileNotFoundError:
            st.error(f"Image not found for {team['name']}")

footer()
