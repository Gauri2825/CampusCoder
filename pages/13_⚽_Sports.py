import streamlit as st
import pandas as pd
import os
from utils.file import footer

# Set Streamlit page configuration
st.set_page_config(page_title="Sports | NKOCET", layout="wide", page_icon="⚽")

# Custom CSS for styling
st.markdown("""
<style>
    /* General Styles */
    .metric-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
    }
    .content-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .explore-card {
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        background-size: cover;
        background-position: center;
        color: white;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        position: relative;
    }
    .explore-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.4);
        border-radius: 10px;
        z-index: 0;
    }
    .explore-card-content {
        position: relative;
        z-index: 1;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
    }
    .stDataFrame {
        border-radius: 10px;
    }
    .section {
        margin-top: 40px;
    }
    .gallery-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .gallery-card {
        padding: 10px;
        border-radius: 10px;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        overflow-y: auto;
    }
    .gallery-caption {
        font-size: 14px;
        text-align: center;
        padding: 5px;
    }
    .fixed-height-scrollable-container {
        height: 400px;
        overflow-y: auto;
        padding-right: 15px;
    }
    
    /* Enhanced Anchor Button Styles */
    .anchor-button {
        display: inline-block;
        padding: 10px 20px;
        background-color: #0d6efd;
        color: white !important;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        border: none;
        cursor: pointer;
        text-align: center;
        margin: 5px 0;
        width: fit-content;
    }
    .anchor-button:hover {
        background-color: #0b5ed7;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        color: white;
    }
    .anchor-button:active {
        transform: translateY(0);
    }
    
    /* Back to top button styling */
    .back-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 99;
        background-color: #0d6efd;
        color: white !important;
        cursor: pointer;
        padding: 12px 20px;
        border-radius: 50px;
        font-weight: 500;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        border: none;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }
    .back-to-top:hover {
        background-color: #0b5ed7;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .back-to-top svg {
        margin-right: 8px;
    }
    
    /* Smooth scrolling for anchor links */
    html {
        scroll-behavior: smooth;
    }
    /* Section anchor styling */
    .section-anchor {
        padding-top: 80px;
        margin-top: -80px;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to get correct image paths
def get_image_path(image_name):
    # Construct the full image path directly from the assets directory
    return os.path.join("assets", image_name)

# Home section
def home_section():
    st.header("⚽ Sports & Athletics", divider='rainbow')
    st.markdown('<div id="home-section" class="section-anchor"></div>', unsafe_allow_html=True)

    st.markdown("""
<div style="text-align: center; margin: 30px 0;">
    <a href="https://orchid85.pixieset.com/sports/" target="_blank" style="text-decoration: none;">
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
            🏅🏏 Explore Our SPORTS facilities  ➔
        </button>
    </a>
    <p style="color: #e2e8f0; margin-top: 10px; font-size: 14px; font-style: italic;">Click to view our photo gallery in a new window</p>
</div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    ## Welcome to Orchid College Sports Department
    
    At our college, we believe in providing world-class sports facilities to nurture talent and promote physical well-being alongside academic excellence. 
    Our sports complex is designed to cater to various sporting interests and skill levels, making it accessible to all students.
    """)

    # Quick stats
    st.subheader("Sports at a Glance", divider="gray")
    cols = st.columns(4)
    with cols[0]:
        st.metric(label="Sports Facilities", value="8+")
    with cols[1]:
        st.metric(label="Annual Events", value="10+")
    with cols[2]:
        st.metric(label="Sports Teams", value="15+")
    with cols[3]:
        st.metric(label="Championships Won", value="5+")

    st.markdown("---")

    # Main content sections in tabs
    tab1, tab2 = st.tabs(["🏟 Facilities & Sports", "🏅 Achievements & Events"])

    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container(border=True, height=500):
                st.subheader("⚽ Sports & Athletics", divider='rainbow')
                st.markdown("""
                - Sprawling playgrounds for cricket, football, volleyball, and basketball
                - Indoor sports complex with badminton, and chess facilities
                - Modern gymnasium with fitness equipment
                - 400m athletic track for running events
                - Dedicated coach for various sports disciplines
                - Regular yoga sessions for mental and physical wellness
                """)
        
        with col2:
            with st.container(border=True, height=500):
                st.subheader("🏐 Sports Offered")
                sports_data = [
                    {"Sport/Event": "Cricket", "Indoor/Outdoor": "Outdoor", "Boys Allowed": "✅", "Girls Allowed": "✅"},
                    {"Sport/Event": "Football", "Indoor/Outdoor": "Outdoor", "Boys Allowed": "✅", "Girls Allowed": ""},
                    {"Sport/Event": "Volleyball", "Indoor/Outdoor": "Outdoor", "Boys Allowed": "✅", "Girls Allowed": "✅"},
                    {"Sport/Event": "Basketball", "Indoor/Outdoor": "Outdoor", "Boys Allowed": "✅", "Girls Allowed": ""},
                    {"Sport/Event": "Badminton", "Indoor/Outdoor": "Indoor", "Boys Allowed": "✅", "Girls Allowed": "✅"},
                    {"Sport/Event": "Chess", "Indoor/Outdoor": "Indoor", "Boys Allowed": "✅", "Girls Allowed": "✅"},
                    {"Sport/Event": "Dodgeball", "Indoor/Outdoor": "Outdoor", "Boys Allowed": "", "Girls Allowed": "✅"},
                    {"Sport/Event": "Tug of War", "Indoor/Outdoor": "Indoor", "Boys Allowed": "", "Girls Allowed": "✅"},
                    {"Sport/Event": "Carrom", "Indoor/Outdoor": "Indoor", "Boys Allowed": "✅", "Girls Allowed": "✅"},
                ]
                df_sports = pd.DataFrame(sports_data)
                st.dataframe(df_sports, use_container_width=True, hide_index=True)

    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            with st.container(border=True, height=500):
                st.subheader("🏆 Achievements & Activities", divider='rainbow')
                st.markdown("""
                - Zonal champions in cricket and volleyball (2022-23)
                - State-level medals in athletics and badminton
                - Annual sports meet with 1000+ participants
                - Inter-college tournaments hosted regularly
                - Participation in national-level university competitions
                - Won zone-level tournaments in football
                """)
        
        with col2:
            with st.container(border=True, height=500):
                st.subheader("📅 Annual Sports Events")
                st.markdown("""
                - Hostel Premier League (Cricket Tournament)
                - Inter-Department Sports Championship (SMASH)
                - Annual Athletic Meet
                - Indoor Games Competition
                - Yoga Day Celebration
                """)

    st.subheader("Explore Our Sports World")
        
    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("""
            <div class="explore-card" style="background-image: url('https://images.pexels.com/photos/274422/pexels-photo-274422.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')">
                <div class="explore-card-content">
                    <h3 style="color: white;">🏟  Sports Facilities</h3>
                    <p style="color: white;">Discover our world-class sports facilities</p>
                    <a href="#facilities-section" class="anchor-button">View Facilities</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown("""
            <div class="explore-card" style="background-image: url('https://images.pexels.com/photos/1198174/pexels-photo-1198174.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')">
                <div class="explore-card-content">
                    <h3 style="color: white;">🖼  Gallery</h3>
                    <p style="color: white;">Browse through our sports memories</p>
                    <a href="#gallery-section" class="anchor-button">View Gallery</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Facilities section
def facilities_section():
    st.markdown('<div id="facilities-section" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("🏅 Sports Facilities", divider='rainbow')
    st.subheader("World-Class Infrastructure for Athletic Excellence")

    # Facilities data - using correct image paths
    facilities = [
        {
            "name": "Cricket Ground",
            "description": "State-of-the-art cricket ground with well-maintained pitch and outfield. Features professional lighting for evening matches.",
            "features": [
                "Digital scoreboard",
                "Seating capacity for 1000 spectators",
                "Practice nets area",
                "Changing rooms"
            ],
            "image": get_image_path("cricketfac.jpeg"),
            "opening_hours": "6:00 AM - 10:00 PM",
            "capacity": 1000
        },
        {
            "name": "Football Field",
            "description": "Standard-size football field with artificial turf to ensure playability in all weather conditions.",
            "features": [
                "Standard dimensions",
                "Flood lights for evening matches",
                "All-weather artificial turf",
                "Digital timing system",
                "Spectator stands"
            ],
            "image": get_image_path("footballfac.jpeg"), 
            "opening_hours": "6:00 AM - 9:00 PM",
            "capacity": 800
        },
        {
            "name": "BasketBAll Court",
            "description": "Outdoor BasketBAll court with flooring and professional-grade equipment.",
            "features": [
                "Standard dimensions",
                "Electronic scoreboard",
                "Professional hoops and backboards",
                "Spectator seating"
            ],
            "image": get_image_path("basketballfac.jpeg"),
            "opening_hours": "6:00 AM - 10:00 PM",
            "capacity": 100
        },
        {
            "name": "Yoga & Meditation",
            "description": "A holistic practice combining physical postures and mindful breathing to promote mental clarity, inner peace, and overall well-being.",
            "features": [
                "Controlled Environment",
                "Privacy and Comfort",
                "Flexible Scheduling",
                "Enhanced Focus",
            ],
            "image": get_image_path("yogafac.jpg"),
            "opening_hours": "5:30 AM - 01:00 PM",
            "capacity": 100
        },
        {
            "name": "Badminton Courts",
            "description": "Badminton court with professional lighting and flooring.",
            "features": [
                "Professional court",
                "Standard dimensions",
                "Air-conditioned facility",
                "Equipment rental available"
            ],
            "image": get_image_path("badmintonfac.jpeg"),
            "opening_hours": "6:00 AM - 9:00 PM",
            "capacity": 50
        },
        {
            "name": "Fitness Center",
            "description": "Modern gymnasium with cardio and strength training equipment for students and faculty.",
            "features": [
                "Latest cardio machines",
                "Free weights section",
                "Dedicated CrossFit area",
                "Nutritional guidance"
            ],
            "image": get_image_path("gymfac.jpeg"),
            "opening_hours": "05:00 AM - 08:00 AM & 06:30 PM - 08:30 PM",
            "capacity": 50
        }
    ]

    # Display all facilities in a grid with consistent cards
    for i in range(0, len(facilities), 2):
        cols = st.columns(2)
        
        for j in range(2):
            if i + j < len(facilities):
                facility = facilities[i + j]
                with cols[j]:
                    with st.container(border=True, height=550):
                        # Check if image exists before displaying
                        if os.path.exists(facility["image"]):
                            st.image(
                                facility["image"], 
                                caption=facility["name"], 
                                use_container_width=True
                            )
                        else:
                            st.warning(f"Image not found: {facility['image']}")
                            st.image(
                                "https://via.placeholder.com/600x400?text=Facility+Image+Not+Found",
                                caption=facility["name"],
                                use_container_width=True
                            )
                        st.markdown(f"### {facility['name']}")
                        with st.container(height=150, border=False):
                            st.markdown(facility["description"])
                            with st.expander("View Details"):
                                st.markdown("Features:")
                                for feature in facility["features"]:
                                    st.markdown(f"- {feature}")
                                
                                st.markdown(f"Opening Hours: {facility['opening_hours']}")
                                st.markdown(f"Capacity: {facility['capacity']} people")

# Gallery section
def gallery_section():
    st.markdown('<div id="gallery-section" class="section-anchor"></div>', unsafe_allow_html=True)
    st.header("📸 Sports Gallery", divider='rainbow')
    st.subheader("Capturing Our Athletic Journey")

    # Gallery images data - using correct paths for local images and placeholders for missing ones
    gallery_images = [
        {
            "category": "Cricket",
            "images": [
                {
                    "src": get_image_path("crickettur.jpg"),
                    "caption": "Annual Cricket Tournament Final Match",
                    "details": "A thrilling final match of the annual cricket tournament."
                },
                {
                    "src": get_image_path("cricketprac.jpg"),
                    "caption": "Cricket Practice Session",
                    "details": "Students honing their skills during practice."
                },
                {
                    "src": get_image_path("HPL Winner.jpg"),
                    "caption": "HPL(Hostel Premier League) Cricket Match Championship",
                    "details": "Hostel Premier League cricket match showcasing talent and teamwork."
                }
            ]
        },
        {
            "category": "Football",
            "images": [
                {
                    "src": get_image_path("football1.jpg"),
                    "caption": "Inter-College Football Tournament",
                    "details": "Our team in action during inter-college tournament."
                },
                {
                    "src": get_image_path("football2.jpg"),
                    "caption": "Football Team in Action",
                    "details": "Team showcasing their prowess on the field."
                }
            ]
        },
        {
            "category": "Dodgeball",
            "images": [
                {
                    "src": get_image_path("dodgeballmatch.jpg"),
                    "caption": "Dodgeball Championship Match",
                    "details": "High-stakes Dodgeball championship match."
                },
                {
                    "src": get_image_path("DodgeballWinningTEAm.jpg"),
                    "caption": "Dodgeball Champion Team",
                    "details": "Champion team celebrating their victory."
                }
            ]
        },
        {
            "category": "Yoga & Gymnasium",
            "images": [
                {
                    "src": get_image_path("yogafac.jpg"),
                    "caption": "Yoga Sessions",
                    "details": "Students practicing yoga for wellness."
                }
            ]
        }
    ]

    # Display images by category in a grid
    for category_data in gallery_images:
        st.markdown(f"### {category_data['category']}")
        
        cols = st.columns(3) 
        
        for i, img in enumerate(category_data["images"]):
            with cols[i % 3]:
                with st.container(border=True, height=450):
                    # Check if image exists before displaying
                    if isinstance(img["src"], str) and img["src"].startswith("http"):
                        # It's a URL
                        st.image(img["src"], use_container_width=True, caption=img["caption"])
                    elif os.path.exists(img["src"]):
                                                # It's a local file that exists
                        st.image(img["src"], use_container_width=True, caption=img["caption"])
                    else:
                        # Image not found
                        st.warning(f"Image not found: {img['src']}")
                        st.image(
                            "https://via.placeholder.com/600x400?text=Image+Not+Found",
                            caption=img["caption"],
                            use_container_width=True
                        )
                    
                    with st.container(height=120, border=False):
                        st.markdown(f"*Details:* {img['details']}")
                    
                    with st.expander("More Info"):
                        st.markdown(f"Category: {category_data['category']}")
                        st.markdown(f"Description: {img['caption']}")
    
    # Back to top button
    st.markdown("""
    <a href="#home-section" class="back-to-top">
        ↑ Back to Top
    </a>
    """, unsafe_allow_html=True)

# Display all sections on the same page
home_section()
facilities_section()
gallery_section()
footer()