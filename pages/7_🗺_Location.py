import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic
from utils.file import footer

st.set_page_config(page_title="Location | NKOCET", layout="wide")

st.header("🗺️ Location & Map", divider='rainbow')

# College information
college = {
    "name": "N.K. Orchid College of Engineering & Technology",
    "lat": 17.72018,
    "lon": 75.91949,
    "image": "https://i.imgur.com/LgZ1mcb.jpeg",
    "website": "https://www.orchidengg.ac.in/",
    "university": "DBATU"
}

# Transport Hub Coordinates
station_coords = [17.666921710311527, 75.89394143431612]  # Solapur Railway Station
bus_stand_coords = [17.680824887006022, 75.89883304182453]  # Solapur Central Bus Stand

# University information
dbatu = {
    "name": "DBATU",
    "coords": [18.17005454144283, 73.33945567384438],
    "image": "https://i.ibb.co/yFdqW9bx/DBATU.jpg",
    "website": "https://dbatu.ac.in/",
    "color": "black",
    "icon": "university"
}

# Display address
st.subheader("📍 Address")
st.markdown(f"""
**{college['name']}**  
Tale-Hipparaga, Solapur-Tuljapur Road  
Solapur, Maharashtra 413002  
[Website]({college['website']})
""")

# Create tabs
tab1, tab2 = st.tabs(["🗺️ Interactive Map", "ℹ️ College Information"])

with tab1:
    # Create map centered on the college
    m = folium.Map(location=[college["lat"], college["lon"]], zoom_start=15)
    
    # Add college marker with popup
    college_popup = f"""
    <b>{college['name']}</b><br>
    Affiliated to: {college['university']}<br>
    <a href="{college['website']}" target="_blank">Visit College Website</a><br>
    <img src="{college['image']}" width="200">
    """
    folium.Marker(
        location=[college["lat"], college["lon"]],
        popup=folium.Popup(college_popup, max_width=300),
        icon=folium.Icon(color="darkblue", icon="graduation-cap", prefix="fa")
    ).add_to(m)
    
    # Add transport hubs
    rail_distance = round(geodesic(station_coords, [college["lat"], college["lon"]]).km, 2)
    bus_distance = round(geodesic(bus_stand_coords, [college["lat"], college["lon"]]).km, 2)
    
    folium.Marker(
        location=station_coords,
        popup=f"Solapur Railway Station<br>Distance: {rail_distance} km",
        icon=folium.Icon(color="darkgreen", icon="train", prefix="fa")
    ).add_to(m)
    
    folium.Marker(
        location=bus_stand_coords,
        popup=f"Solapur Central Bus Stand<br>Distance: {bus_distance} km",
        icon=folium.Icon(color="orange", icon="bus", prefix="fa")
    ).add_to(m)
    
    # Add connection lines
    folium.PolyLine(
        locations=[station_coords, [college["lat"], college["lon"]]],
        color="blue",
        weight=2,
        opacity=0.7,
        tooltip=f"Railway to College: {rail_distance} km"
    ).add_to(m)
    
    folium.PolyLine(
        locations=[bus_stand_coords, [college["lat"], college["lon"]]],
        color="green",
        weight=2,
        opacity=0.7,
        tooltip=f"Bus Stand to College: {bus_distance} km"
    ).add_to(m)
    
    # Add university connection
    uni_distance = round(geodesic(dbatu["coords"], [college["lat"], college["lon"]]).km, 2)
    folium.Marker(
        location=dbatu["coords"],
        popup=f"""
        <b>{dbatu['name']}</b><br>
        Distance: ~{uni_distance} km<br>
        <a href="{dbatu['website']}" target="_blank">University Website</a><br>
        <img src="{dbatu['image']}" width="200">
        """,
        icon=folium.Icon(color=dbatu["color"], icon=dbatu["icon"], prefix="fa")
    ).add_to(m)
    
    folium.PolyLine(
        locations=[dbatu["coords"], [college["lat"], college["lon"]]],
        color="black",
        weight=2,
        opacity=0.5,
        dash_array="5,5",
        tooltip=f"University Affiliation: {uni_distance} km"
    ).add_to(m)
    
    # Display the map
    st_folium(m, width=1200, height=600)

with tab2:
    st.subheader("🏛️ University Affiliation")
    st.markdown(f"""
    **{college['name']}** is affiliated with:
    
    ### {dbatu['name']} (Dr. Babasaheb Ambedkar Technological University)
    - Location: Lonere, Raigad District
    - Distance from College: ~{uni_distance} km
    - [Official Website]({dbatu['website']})
    """)
    st.image(dbatu["image"], width=300)
    
    st.subheader("🚍 Transportation Information")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### 🚂 Railway Station
        **Solapur Railway Station**  
        Distance: {rail_distance} km  
        Approx travel time: {int(rail_distance*2.5)} minutes by road
        """)
    
    with col2:
        st.markdown(f"""
        ### 🚌 Bus Stand
        **Solapur Central Bus Stand**  
        Distance: {bus_distance} km  
        Approx travel time: {int(bus_distance*2.5)} minutes by road
        """)
footer()