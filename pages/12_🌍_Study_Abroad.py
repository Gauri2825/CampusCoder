import streamlit as st
import pandas as pd
from utils.file import footer

st.set_page_config(page_title="Study Abroad | Orchid College", layout="wide")

st.header("🌍 Study Abroad Opportunities", divider='rainbow')

# Create tabs
tab1, tab2 = st.tabs(["🏫 Study Abroad Program", "🤝 Partner Universities & Initiatives"])

with tab1:
    #Introduction section
    st.subheader("Welcome to Our Study Abroad Program")
    video_path = video_path = "assets/Metan Sir.mp4"
    with open(video_path, "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", start_time=0)
    
    st.markdown("""
    Orchid College is committed to providing global exposure to its students through various international programs.
    Explore the opportunities below to embark on your international academic journey.
    """)
    
    # Success Stories Table
    st.subheader("🎯 Our Success Stories")
    
    # Adjusted data with total 78 students (removed leading zeros)
    data = {
        "Branch": ["Civil", "CSE", "Electrical", "E&Tc", "Mechanical", "Total"],
        "No. of Students": [10, 10, 3, 15, 40, 78],
        "USA": [7, 8, 2, 10, 12, 39],
        "Germany": [0, 0, 1, 0, 20, 21],
        "France": [0, 0, 0, 0, 5, 5],
        "Canada": [3, 2, 0, 3, 3, 11],
        "Other": [0, 0, 0, 2, 0, 2]
    }
    
    df = pd.DataFrame(data)
    
    # Display the table with some styling
    st.dataframe(
        df,
        column_config={
            "Branch": "Branch",
            "No. of Students": st.column_config.NumberColumn("No. of Students"),
            "USA": st.column_config.NumberColumn("USA"),
            "Germany": st.column_config.NumberColumn("Germany"),
            "France": st.column_config.NumberColumn("France"),
            "Canada": st.column_config.NumberColumn("Canada"),
            "Other": st.column_config.NumberColumn("Other")
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.markdown("---")
    st.markdown("78 students were selected for Masters of Science (M.S.) program abroad")
    st.markdown("""
    """)
    st.subheader("🎯Objectives of the Study Abroad Program")
    st.markdown("""
    - Provide the right educational match to students.
    - Assist in admissions to top global universities, especially with scholarship opportunities.
    - Guide students for qualifying exams like GRE, TOEFL, and IELTS.
    - Facilitate domain- and country-specific university applications.
    - Offer VISA counseling and mock VISA interviews.
    - Conduct cross-cultural training and provide international exposure.
    - Enable student exchange programs.
    - Offer foreign language courses.

""")
    # Study Abroad Cell section
    st.subheader("📚 Our Study Abroad Services")
    st.markdown("""
    Our dedicated Study Abroad Cell assists students with:
    
    - Program Guidance: Helping you choose the right international program
    - Application Support: Assistance with documentation and application process
    - Pre-Departure Orientation: Preparing you for your international experience
    - Scholarship Information: Guidance on available funding opportunities
    - Alumni Network: Connecting with past participants
    """)
    
    st.subheader("Distinctive Work Plan")
    st.markdown("""
        - 360° counseling involving students and parents.
        - Guidance on resume building.
        - GRE/TOEFL/IELTS preparation support.
        - Help in drafting SOPs, LORs, and transcripts.
        - University and domain selection support.
        - Assist in funding options, including loan facilities.
        - Guidance on university applications and assistantships.""")

    
    st.subheader("✉ Contact Us")
    st.markdown("""
    For more information, please reach out to our Study Abroad Cell:
    - Name: Dr. Metan Sir
    - Phone: +91 9552529283
    - Email: office@orchidengg.ac.in  
    - Office: Mechanical Department
    - Hours: Mon-Fri, 10:00 AM - 5:00 PM
    """)

    # Global Gallery section (keep as before)
    st.divider()
    st.subheader("🌐 Global Gallery")

    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <a href="https://campuscoders.pixieset.com/studyabroad/" target="_blank" style="text-decoration: none;">
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
                ✨ Explore Our Study Abroad Photo Gallery ➔
            </button>
        </a>
        <p style="color: #e2e8f0; margin-top: 10px; font-size: 14px; font-style: italic;">Click to view our photo gallery in a new window</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    # Partner Universities section with cards in columns
    st.subheader("🤝 Foreign University Tie-Ups")
    
    # University cards CSS
    st.markdown("""
    <style>
        .university-card {
            background-size: cover;
            background-position: center;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            color: #fff;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }
        .university-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(34, 40, 49, 0.75); /* dark blue overlay for readability */
            z-index: 0;
        }
        .university-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .university-content {
            position: relative;
            z-index: 1;
        }
        .university-name {
            font-size: 1.2rem;
            font-family: 'Arial', sans-serif;    
            font-weight: bold;
            margin-bottom: 8px;
            color: #ffd700; /* gold color for university name */
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
        }
        .university-desc {
            font-size: 0.9rem;
            line-height: 1.4;
            color: #e0e0e0; /* light gray for description */
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }
        .cards-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        @media (max-width: 900px) {
            .cards-container {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Create two columns for the cards
    col1, col2 = st.columns(2)
    
    with col1:
        # NTI Gymnasiet, Sweden
        st.markdown(f"""
        <div class="university-card" style="background-image: url('assets/university.jpg');">
            <div class="university-content">
                <div class="university-name">NTI Gymnasiet, Sweden</div>
                <div class="university-desc">
                    A Swedish high school focused on technical education, offering programs in engineering, IT, and science with strong industry connections.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Texas A&M University, USA
        st.markdown(f"""
        <div class="university-card" style="background-image: url('https://i.ytimg.com/vi/2GrPabIMviE/sddefault.jpg');">
            <div class="university-content">
                <div class="university-name">Texas A&M University, USA</div>
                <div class="university-desc">
                    A top-tier public research university known for engineering, agriculture, and business programs, with a strong global alumni network.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Supareo University (ISAE-SUPAERO), France
        st.markdown(f"""
        <div class="university-card" style="background-image: url('https://www.isae-supaero.fr/local/cache-gd2/20/31b6467e4fdb11a585214c202e8fd2-resp640.png');">
            <div class="university-content">
                <div class="university-name">Supareo University (ISAE-SUPAERO), France</div>
                <div class="university-desc">
                    A leading French aerospace engineering institute, specializing in aviation, space research, and advanced aeronautics.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Toulouse University, France
        st.markdown(f"""
        <div class="university-card" style="background-image: url('assests/Toulouse University.jpg');">
            <div class="university-content">
                <div class="university-name">Toulouse University, France</div>
                <div class="university-desc">
                    A prestigious French university cluster excelling in aerospace, AI, and biotechnology, with strong industry partnerships.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Polytech Nancy, France
        st.markdown(f"""
        <div class="university-card" style="background-image: url('data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTExMVFRUXFhobGRgYFh0fGBcYFxgXGBcYGBgYHSggGholHRUaITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGxAQGyslHiUtLS03LS4tLS0tLy0rLS0rLS8tLS0tLS0tLTAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIALEBHAMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAAEBQMGAAECBwj/xABGEAACAQIEAgcFAwkGBgMBAAABAhEAAwQSITEFQQYTIlFhcYEyQpGhsXLB0RQjUmKCkrLh8AcVM1Oi0hY0Q3PC8WOD4kT/xAAZAQADAQEBAAAAAAAAAAAAAAAAAgMBBAX/xAAyEQACAgIBAgMGBQQDAQAAAAAAAQIRAyESMUEEE1EUImFxofAygZHh8RUjwdFCUrEF/9oADAMBAAIRAxEAPwAThONt2LgN6219sSLR7WR2zG5dDe2DAYZZ56TNF3sPZt2y3VLAGnZEkLoI01Lafv0DwzDhn6xiS6Kq29B2QQyyIGpVS0TTHFEFgumVIc90qfzY8s/a/wDqrY0AqxvDyEtW1t2zcJBuHIupLAsJOyjtegimF3hSul421RbihgvZTeARAy6nUek0I+MyujG4ArOFDZMx7Q0J11GnIc6YJxGzmyo9247Agt1eW2ComdQNOXPcVDxHPpBPldqvT77FOUcNvItV/gSX7aXbdlyFPWW1IEe+krc221FL7OCyudAVgHIRrImII2BgTTrEYkWFS3dtz2yxI0y5j2mgjU9oGDpSzGL1Vy05YZZKOFOoXNAnu9mR4EU3lzcm6q+zE8KvaMEs0e1a7+n0NcRK3GFwW2stlyleyLciSSQJBbWPTnFWLoVxAOGsN7vaUGPZIGZdNNGM/t1BicGiKQoJyr3ySI3pBh8UcPfW4PcbUDmp9oeoJ9YpoSkp1IWUbRfL+ZWVuVvKH8UuFkB9DlYn9U1JxZfzbN+hD+iEMw9RI9axlVrqyZtXrItsRzD5ih/1fM1q/LYW4H9oI6N4soKNHgSCR4EV3Rejn7lw4VxAmzbJMkLBPivZb5qakxOLBFV/oneJtvbIM223MQR7J57l1c01uCjihXJgV9aDuCmFwUK61REmBEVyanZKjZaYw4RoM1YeE8UnRjVeisRiDpSSjyQ0Z8WXwwRVb45w+DmUelM+FYkumu9G3bGYVzJ8GdTXJFAuJUDCnfFsEUbbQ0pdK7IytHJJUyCK3FSBa2EphTlBUoWsCVIq1jNRirXFyp2GlRZaxGsiiicFhc7BdgTqa4C1PZcrtQ36BH4lkt4+1ZhF5f1J8aV8T4ln0Xb60tJrIqSxpOyjyNqjBTTgmDLuDyXU0vtpTzB8QW2uUD176Jt1oIJXbHwAG8V2l3eTGv3CkC8UJ5UULbNJPM6ajaBXM4ep0876HlXCQAWPlA5Ty9f50BxzHBLDNI7bgba5BoQJ5wCf26NwFosGUaAxJ7hrmPmBMeNB48G5ctwq5QMwJEgZtUCjmcuXy9RU5OkUpvSB+LZQMMqCIur/AKQxHwEUVbxARLaZQCpJJklmDTIMnTQ01wWEzEjLbd4BAYezrqVMgjTcilmL4hh7Vx0ewGZZByswAbv9o955UuXlkknjW1tb6/x8SnieKb5PT07HNzh4coWhyXE5tfaEA678viO6kuOtWy/V3FdzoGVQd0/WMfogaVlzj5vB0tjqoUeJIBMENvOkUfxHiEM5VioGUNlQBzm5ydT38vvpss5vJcn0+/X/AAJ4ZrHFxxaTTXzXcmt2rhEdWtoZYm60tlAn2R3Dy2qrcQ4cFZgHPnETpvlMkUxwl1QLV3K7sr9tyyjMGOVjkJmcrjuEg71xetgHKCTl7Mnc5RGvjpWfi2Y9Dvoy3WYVreaWt6DwHtJEctx6U6v3Mylv85UJ/wC4rJaujw9z51TOj2M6jEAE9h+yfInQ+hj0mrpigFBDGAty3dHo6rcHj2TMeFXxS7EJruMOBjLiri8nUN6jYfK4fWnl63SJzkxNhvFh4Qcsk+QzfGrRiLVVvZNoU3Eod0phdt0O9unTJtC90qFlo57dQtbphQJkrgii2SomStsw7wmLZDodKsOB4oGEHeqzkonB3FUyZqc4JlITaHfFGDWzVXe3VixVxWXKP68KTXbBB1BFZj0Nl2B9XWBKK6uuWAESQJMCTue4VWyVEISpFSpltV26VjYJAjVzFTlK1lrbAjArddxWBaAOAtSIldKlT2rM0rYyVkYWiLGFLeFMMKqIAcsnvNSdbUnN9iqgu5JhMIFHInvqYkD3hU1rDSAWaB3VNKjQKsVFsskeMYZj1dwD3gEB5gu2UH0DE+lRflQDk6QSY8hAHloK3bJWTyUZpP6UFV/jJ9KHuYJmQgFlKicwOqCCBPiZJI8OUGo8ZTmoxOzwuHJlnWPqt/fz6BNnimV+tUDu19R9fpS04a/cb8oFnrFNxx2suVmMkjLMx58xTBsQDYtrcZOt1LlFiApIUt5jXzBoXh1whxcS7mtkQUC+0QYmTtzpceTysjb+K9CHiYyk3Cenf1B+CcKuNfKtNsEqTEeyhct3wJIFMceXi8SwKznVSJYZdlMgCCGXaY19XvA+HgW2vL2xcJRUBh1Cn85JAJgSJYCBpTjF8AxD9tMFbcOCZXEqRGUBIDKBDCNqtuXvyXUljqK4p7RQuKcO6kG2yq0i2xKrouY9mWBmO8gRqdooPHcRGckIChCkaz7ShiJ56mvROIdF8XdKXPyXK5UKwF9AFCaoJG+u8fOvPMfhyjkMgXkVBkKw0YTzgyJqT0itC+/xO1zVlPlP0r0jgmMF2xbuHtNaZc36yiDPjK/MGvNMdhKe/wBn/FOrudUx0PZM9xPZPoxjyani62JJXo9CuKjLkDhjbRxIYEnI1sqfNlAPqat1i71ltHO7KCfONfnXmPF8GEcgjTl6bHzywP2DTHABgkh3UydmI2JE9k84n1q3KybhpF4uW6He1VaXHXxtef1hv4gakHGr45o3mn+0imUhHBjm5aqFrVLx0gf3rSnycj5FTWx0gTnauDyykfUH5U6mhHBhT2qHa3WJxuw3vEeaN9YipFxllvZu2z4ZhPwmnUkTcWQFK11dGG3WurpjCCyIYGmGIWVEGZ+VClK6t2Cd5A+Z/CpzaW2VxpvSICp2A15nkPxPh9KX9IVFrDvcluwVYsD2oUyQDpynTQamnwSKV9KbObCXx32z+FczyOTOmGNLRSLHS1CzMvWqCxIhw4AJ00YxTfDdKUaPzqH7alT+8IWvLjgxElSPQiuxaZdFdhoNJ0Gg2Bqa8RNI9Cf/AMxcqiz2C1xhGE5Z+w4b8KlXH2j72X7QI+e3zryTht5WcWWW412GbOpXUAtyMRERvTTDX74zlbzgK0AMpPJTrGYDU10RzSroeXPAoycb2en2sreyQ3kZ+lSC3Xl+F43fLsItPljXSSTO2o10NOMJ0tuoSClxSpg6lgNAdmEbGn86JPyWehWcN3ii0Xwqk4Pp4pOrL+0pB+KmBTrC9LLT+P2HBPwMGlcrHUaHxWthSKBTjln9Ig/rKR89vnUi3zc1Vgw/VM/ShJg2g25xH1oVsc1RC14UvxPSDD22KNeRSNCO48xtQ+MeovJso91TGUE6xMcsskfOPhUd64QDlnUajafA+FFvbYRtQt20e/4VzRbjLkmejg8TkwNvG6sBUlUKxNx/bYxtyA30AP1rixhsSTkt5RLAL7PvExqTAjQUTcSJ/rmBR1+1MgTJGkb70SSn+I531LbwvH4jB2raZWAkWwQttg7OF1/xAQcwbnG01i9PcJZyW2tXly9gEldSnZILbTK7THxqtcBwrjEWg2aOsX2hGxn7qGGGS6rBiDLuSp7i7GqcpNUScVF2+vzZeMD/AGh4O8xVMPdLDcbHSSQQSNdTVP4thTcDMywWZmjuliRtz1FKegdom60mYDAeAEACee9XTF2JFQmmy8GjzJbkiCf67qAfEdW4ccjqO8cx8KmsX1LkMNSTHcYk/GB8qJfAq4/nQnRtJnonXjFYW3eU5mWA3jzU+oMftnuo7h0m2D3lv4jVP6A3WsO2HuH81d7KmR2WMlfgTp9o91NbHGLlpxYIUw+Uk7g8/wDUTV8fvLRGb49SxFK5NuhjxI80Hx/lUf8AfKzBRtuRHlzp3jmuwiywfcKNuo2s1D/fVrnmHp+FS4TiNq6SqMSQJ9kjQEDmPGscZLsOpRfcGtWeyPKsbD0ZaTsjyrZSlbNSFy4YDYR5aH4ii7TXBs7/ALxP1qTq6lS3WW0bSfU6THuhTM0guo1A95gOQ8asAFU7jZhR4EH5irhhrmZFYe8oPxE0rbe2aklpGyKB46k4e6P1fvFMBQ/FVmxcH6v4ULqa+h4rw21bupKO6xGhCt5agr3H4UXb4cCBqp7K7gyOyPAj5034d0Qw9sTZxW4GhZSNPmP51JwfhOILuCi5EhQcwl40kAbDTn306xxaH9tz3t380irYDhrpj1YgBerYE5lGpzEaEzGo1irNg8Mfzunvg7d6r+FRdJOCYl7udLJK5QNGWdBG00jHD8QmrWrqnMdkPcvNfKtWRw1Whn4aGZKfOm+wfewCnMDG4n43KCwHD8ufKWWHPskjkvdW+G3rn56XYHOsZ+6Dp2+UmicNjGVnByGYPsgco92O6m8+PdEn4Ge+LXoDIXAgmZJPaUGeWsieVSHhxGGV8qSVPs5gQZ33I593KibLK4MpsxAysRyVuc/pUUnElXD9WVPZDgEQTGZu+O6lcsbZnkZloXvbu2+ryG6mcgdlgywQT+r3d1TW+J4kXCoZXyiSXtkR6gDvBme/uppc4hbK2dTKOk9nwKnae+u7OMtjFlpEZJ1I2ykGZ8hWa7MVxn3X0BV6Yv1TF8+QTLWrxkAEglYJIGm4NQPicNfZrptX5YzoBAnU6KG5yd+dK8Zw626tKrMOAY2zEjQ+tWTA2VyLlAgiR5GtUeX4icqRl1paoMQ3jXPWiTQty7v6/fUi5EfbXnqv1mmYw73GATU6E6gdkHXU+dLQ+qn9aPlNPMDierAYASc27AaSo94ifZO1MuhjV6DeEYYreslhBL3G3B06tiNj4Uqw/DL72wUtsVYZgQw1C+2YnkXA2505wmIY3czAArbuEQwOgtEcvE/Ol/D+k/5PbS24YAWWVYgznCNsQDEjcE1tWiUtaYB0Dtdtz+qfmUq4XRoarvQZNXP6sfMfhVjxeiN9k/Q0OJqkeNGMyyQIW4Se6LTifnROBc69sepFav8AaDAgzkua6AEGF0jzr0nhfEWVrilJyHPJU5W/OMAo5zKRSUCnopfW3Mu//unlqybjszkdYSCSCB2oXZSdNRPrT3iXFJtOHs2mBLgAIJDZ5U5ipHfuRVYsXEOJYAiS4DAkAyCYy98jzOgrMeRLaFnKy7jh+YBgAQROjDn6UA/DTmbsnYfVvHwpJd4r1S9q9dCqeQQ6aQACm33+FMeCcVAs3sQ7PcHYVJVRvO4XLpJPwrp85rqR4RfQjxeBCglgQO8r31vowEN1srBoQgxy7SUrtN1txmusxtIqFoYgjMFgAndidh5k7V1/Z+D+UYrfLC5RIMLO07/Gkedy0UhjSdlutr2V8h9K2QK6sjsr5D6VuKRl0RhalVa0BUgpTRLx8dn1H1FWPo1dzYdf1ZX4HT5EVXePns+o+opp0Nu9l08mHrofoKb/AIh3H5FD8R/wn+yaMK0LxAfm3+w30NKuo3Y+f1uhYCsZG/KjsPimGUByCVBidyRJj1oK9ibILD8pggkEFLmmpHIGY8KY4Phb3Ajo1t1yxJDCYJ1BKbVyxhNWe5k8T4ebXvL7/ItHRi67W7jOzGLgH+IwgZF/RMR6UYOJHrHUO4ChdnDanNr218B8KW8It9VavW7pVGd0ZdRBAABIP7NS4NrYuuS6QUTXrE3BuT73lXXC62eLnjc24rX0JjxLPdZZeEEHNbQ6tkYRlYSIjurbY6wzNnWwQoEk2WGpnTn3cqXcQxBS9ee2ouEi2QARroqttO0T6Us4Rcv3esNywyNmELkb2QDrqNe6as0jmTaLDZu4MyAtgAmZF4rJ2MAqNRA+VRnh+HuBsgubkDLctlSTqYJaSJJpabBAI7mbkecd4rVq+yWsoMLrp4zP3il4IZZpLuxo/CbeQEXLqgZT2rRPskHUr5Uv4jwY55F6320NsBlZORbMZ5d9KMSIdSDAzWzoYkdidvCmdgtnINy4YGkuxAMkSATAOtYoJsf2maXUQ4no/fzZE6tyqzmW4Mp7RIAmDOvdV34Wp6pJ0IUA+YEGq3evXe1+cJOb3lVtIWPaU99O+FKRaCjYSB5AwPpTwjxFzZ5ZKsDLanz/AAqBj4c6nuzr50MT41AodIssveDPxH8qNv8ADTiBlVwCibH9YnXf7qEwzdr9n+vrSTjfHWtX8oJACZTB3DD+Q508dEsm0XPA28hxLd9m4ef6FpOfkfjVExXGCLrIrn2yuU6r7UeywK/KrPwXG9ZhLr82sx6s6L/40g4twa3bZbq3GJdi8HQatOkHXembomh5w7GC3bVrjlQxaSMwBMg7J60xt9IMORBxBI7iz/fS9MPnwY8yapHEbUZvI0sm0x4pNHo6XOGkam1/RB7vAUZa4jgwSVvhS28XCJ1J19SfjXi1q+wI7RjT4VeOE4TD3cG9wZjeSyGJzHRpQeydDuay9dDaRcHuYF+yb6toTHW8t2PympBwnCZy+btE5ic3Pv1qn9EeHnKLl1pNyxeI0UAKUKrqNyZn1FQcL4CwVusS6GB013HKOXKsTXYx0XfE8IwjLlNzSZ/xANfOtfkOGFsWuvAQGQOsTfWNYnmfjVYXhjCIS/6RHrTa3wzLgMQS7G45QKpK5+y4MoNwdefdWt+oq4hT8Pw3+f3f9RdcogT3wK3w1bOHZ2tXlBeAZZTttA5Uj4PwhnZVu3L1uCJZpjQ8yD/KheK8JdMwS7ffLcygg+0Obacu7lUvMrsMqLgvFiAB11sx4r9xo3h/EA7gM6EQxIXeFRm7z+jXkNzCYpUdj1jgrEMrHJmKyZJ0YRv4mrX/AGecNtraLO3VsVGubKTOYMJ8jB86dNyRSNWW3C8bzKGNthI5EEfMj6VMOMD9B/8AT/urz2/xnFZrpR7WVGaJUklQ0LqDBNR2eM4w5iOrIUajLtuddZHmdNPOhyS6oS36l54hiesEBT6x+NF9HccLNyXBgqQYE9xHzFednpFisgeEO8nLoDmYD+EfGucV0kxIQFSgckDKV1nTl3azrW89UF7Pa24/ZgkZtO9Tp47UZjFm0570b+E146nHL4dDIUNh1Lgj32ZgUA0grInmJEivV+CYnrcGjf8AxlT+yCv3T60iex07PG739nl5nd1uQHctGQcySBOfxp1wLo5dsMGZCzKmTTKFILFjoSe8ePZpFjeNYlbtxVv3ABccAZtgGIH0rqzx3EABmxFzUHc8wxH0G1L7RC3o7f6ZlSTtb+fp8iz8cwV24ylbDaJHLvJ7/EUmucJv6/mH5cu6e7zph0Wxl6/cdTeYwqkamNc87eQ+FWU4C9/nfM06jGfvb3/BN5cmD+1rX8nnj8PvA3QbNwZrULKHtMCTAjn+FAf3ZfCt+auAypEW2Hskju/W5VfOMpeRrf5yfaI1kSFIE6D9KfShRxDFfpp+6fxoeFaNj46avS20/wBK/wBFOCYgWzlW+pzL+nMENO3IQPjXX5TiAo7V4dpp1ce7bgnXz37quQ4pif0rf7v860eK4nvtn9n+fhWPDrqxvbvWKKRjeI3gFGYkZNZAOsmZkb6URZ4lcOJClhl6xh7K8s0CQJ5CrY3GcQN+r+FCYvjd4oQVtmdO7Q6aGPGmjjad8mJLxUJRry10++xVv7ycqxlZkToOYPd5Vauj10tYQnc7+Z1++h8Vxa5/lWtPDfl3Vu1cY6uEUtByogIAIBG7LqRrAnfeZArjUk6tv8mSyuORe7FR/NL/ANo1B7jUV0UTnioLxkipCHWCPt+AA9a02FwD9q6LJcntFrrA6SACAYECpMJsx/W+lcWFUDUDzqiEkM+FYGw9t7eHKZOyCEuE5e0W3ZTuZOtF4nopbMBm2EDQ6Dwlqzo0R2oEdobeA/nTvENvVEr6kZCG5gRatZA2YcpH4V55x63AfyP0q/cd4lbtgB2gnYczvy9DXn/Fcal227JqNdx5fjSzibBnGAwo07I2HKnPRywXxTYdAAt0QxmAqhZJgeJAnvIpVZtsPe+VFcJxF1WvdW+R+yAw0YCRm1HgKk46NUtl5xPDittsty3cQ2iVyz7pQbEbQIB1FCnhWIzBz2bSydwN3bu1Iy5d9vjWxe/xTnDMbJBOZmPtWwJLE99BYfpaLWfM85m94EiFJGWCsRGnoKXHjaglZrkmEXcHCqucAgvEuZbeNc3Lumh8PZcO4ZpBZCO1PLXSSBqTp5V3d6QoHt3zkGbPl/NqU5A9kwPlXH97LfuM6x7s5VCroOQB8KpGL5dRbDx0TuqbFzrXeGQ3FJJBABzawAV25UuxnBrjteugsFS02UK0TcAkZh+jqPxFatdJZayA9zKNIEgCRHaEmk3SPi922zi0zqxVQSPZIJ1GUiJ8aRQdffxHTTN4+1cNhwpBi2cxzESNBGmjeyd/jVq6K2AtoLKt2B7JmJAMMI0PhXnuPYstjPqTbJOnvE7iIA1FX3o7eb8mDuxJ6vnEAARyFNGFdBfUX/3IdhlCjYaTHnzoWzwO4LrAOR2VIIjaXkbj+jVcw+PvAdskT390CCpB8TRPDse25mO9nJ8DoRtuKlPJJLoSUt0XvDcNshUFxVBLakJkPZJKg5ZCk6nQEGOUmecXwiyzpcaFK9pSNM5B0zjcr6TEaxSBek1trYQrljYidMo1XsnQR/Ed+TXh/FVd1IOYBRy1GuoyggagD90aV4+Tz9tWWUojXFcPG4HZLLmyQGARlKBWY5csjUxJB8BT/o+WtILRckEg85AiI121GutVPivEltktKmfZ7cEkjLJ07W3ft30Hw7pYiaZwNZ+JMhnEk6xqo5ctaliebrtodZIpgnGuDXXusy2kVC7ayQSMzZnbXl9CN9gsucObRcmYKTO45zzIPOnvGYvBYLoCSzALIKQTmOXn466cqUPYf/p6wdc7AMTC7D05mvQ8PHlFun9s7f6nKKS1r/Q46FWmt4g9mJUbmdg+2p7/AJ1e+trzjhGJuW7ys/ZX9KVOkCe/+jVhHSS0P+svqJ0117IHd8q9LHFKKR5+bxSyTcmF9I39g+J+cUiHEbYHtr8RXfGeJi6qhSphpPZYaA+vd8qU2OGggNGWAJ7MyWzLHLSY5fzJzkq4qzcWTA03OVdBknErR0zrsTv3R8q4/va0PfHL76D/ACWCMqjVY9jU5j/6FcXsAzAFoAiZFsaxJnX9Uj+tKRZJ+hXn4a/xa+/gd43HdYJs3LYO3bD7wD7o8aWXcVcGUs9vKcsgI+adJgxG801w3D8sgFYgnULuFCnkeYmu34YMplrcCDqBOihiRC+Io55LEn4jwiWm2/v4AmKftkBhBU+6ZDAr8tat3B8XgTYtyLbOFAfOboIce2I6toEydDzpBew4LQwntZZAA5AkghtvSoRhltyBbOpnXOdTvrmrVbfvdCXt2KK/t3ZJr3VE5MzW2u+NcX5y7xrQdBPhyerJ86xbtcG5lt66DSfIkVr8qTYH+vSqImx/0Zffxf6KtNsVdqv8AxiAc5zMdtanxmLuvogCjvJ1+HKqxaJNNspXTi9GLt67WnPrleKSYePyYpkbOxkd0aePhV5fgWdszsCeZ3Pxqe3wBBrStWUWkefWmv8AL6VOGxR5n4D8K9DHCFA2ri5wdSaKRlFW6PNeQXjdkyihZAHvgmI8BWLhLxJjJuTr4meQq0DhK9woheFxtpWhRXbmDulbYDAZQZ1IBJM6fGswlh1JzXAZI5kwBM6nzq0pw4c6lOAXuoDiU23wZ8yuXzZSDGusftVDxLhFy65YkrtoD/Kr2mDFafBig2ihXOCaJPWEoIBVlgjxBXX+dNxjBawdxGVgVsuAcpg9kxqNvWKsJwo7qFxmBDCCYBHIwflWBSPP+iuDF1kBEhUmJMGbl0QQCJ+I2qwYzqgnZswO1GmYTGgMwVE68/Ot4XgX5O2a055CG1BAMx3jn8aKS/bdOruDKQ435yQQR9K58kLdsHFMquCxzgvEHsNpHMAFZGxH1FdWnyskZlMgBQ+sa667Ea93jGlWPHcBsmcgOaCsruQZBIGxMCfSk2J6OXFaetDLPaMkEgQdhpsTUZwtCSxvsM7F2y1xFuAlVRVJLMWIQH2oJgdocgSANp0ixeHjLmChVDHNbKRBJyglwDyBIn4mTQmD4b1bssoy3FAGZtVIJ7YbvAzf1pUeELWy4F4IunsgwYgrmE+GkiRJFcXktS0xuLLR0a4j1ga2+XbQwNihGrT4ba01tYO0127mClTljM0e7bzRJ/XNLeG9LXRB2rS8ycmpPP3oHwrgdM7Yu9b1iliCsDbXJyB37A+ffTwxS9Pr+xssTaQ8s8FwubRIJ3Kkk6kkmJ11CmpDweyY/MuQP1XjYCNu6RSf/j1joonytk93fPfXZ6SYt/YtXjHdZj4HLTeVP4/r+wywJIavwCy2ow7EzMgROrHWY5kfvGpLuD6sAiy4HWJPanTNEauY0I5RJ8TSgXuJMJFu9qAQJI10kGSAN/LQ1zY4RxK4R1isAQc2a4DGnZAGfvJkzsBGuzRjJbtmS8NGS/YeXeHNmkWwvZAGbcESSeyAKHxinIFJtCAYLXF37hPLSJ13pNc6HY5iYa0qsNcznMDoZGUHYjvNFDoNiSYOIQKe4MW8F2Agd/1rana2N5EVqiYG0NTcsRr7smdNikjU776edQHEYSGW4wiSBkQjskREFdNBG/Kibf8AZ7JlsTd1AkKFjTTmDRi/2f4fLkdrriI7TCRvscsjfvqjv1M9lx3dCHEYjBMCVa4CJbQWzyyk9oeEH0pfe4rYk/nbw8JtjTloR3Vd7XQnCKAMjQJgZyBrvoseHwFEjophIA6lTHfJoi5ruP5MP+q/Q83B8a4xb9gedQs3pUeJuA5QK6TAu/f0Hp8daKwlq2fbuD7Kz8z+FBWsIbsAbDUk8uQk7d9H2+HqPavWl82H41VCDW26xC6DuFSgigEu4ZN8Sh8tfpU1riOGOis7/Ztuf/Gt0FML64DlWmxB8K1auKT2MJi3/wDqIH+oiiUs3j7HD3P23RfqTRYUCqzMdIoi3ajvJo6zw/GnbC2E+1dmPPKtTjg2O965hbfkrn6xRZgFat/q/Kp0sEnapjwxx/icRQeCW0n5k1ycFh/ex2IbwXT4Qn30G6MGFburi8CoMgg95y5dtPemZ02jzrHsYDmMRd+1cf8A3itJdwyGbOFtgkEHrEzTqD+lvp400HUk2TyxcoOMdNoh/KrYA6y4ik82cDmZ7PPQDUd+tc/l2H5Xgx/UVm/hBoteKiZ6izoDAFtQBMSeyJOw3NS/33fPsIo+yhP3mtnLlJtGYYuGNRltruAdch9m3iX+zYePiQK76hzthL7faKL9XkUxw+MxZYZlfLOoChTHgSKKxPFLCkqTdJB1Evv5EikKWJhwm+22Etr9u8P/ABBqG5wS77wwSHxzMfmFppc43Y5WS32gPvmuP+JCNEtKvr+AFYYLLvRh3ENiEjutYcn55j9KDv8AQEFMqXsRqZM2wAfAzBHnT88YxTezb+Ftj8zNbBxzfpD0VfrrWOKfUCh8Q6B3FYO+dROhBlRr4betd4bophWfNeNyTuwGaTzLZjPoKvX904t/auwO4ufoBFdW+ix966PRZ+prOETU6FfD+guCYg27isO4qoaPgNfQ06s9DbCGQDHcYP1FLcd0eu2+0kOBzGjD0/A1BhOkF+3pnzDuYT6d9I8b7Mqpr0LRY4TbQyJE8hA/hANGLb/on8aR4XpYh/xEK+I1H403w2Nt3NUdT5HX4VGUWupRNPoTFRXNdEVzNKMaLeFZmrC3nUbE+VAEhauSajzVzNAHReuc1aJrgmgDyK1wLEOcs21J5lj9ToKecP6I2lOa/ikO3Zt6/PWj8g7zXJsjx+NdvFHLbJRwThq+1nufv/yFTKnDU9nCqftAH+JjQfVL3CuoXwrTBja4phl/w8JaHkBPySpj0iu7LbRfMH8RS63bZtlJ8gT9KJtcLvHZG9RH1igDtuOYg9w8gv3g1G/EcQd7pHkSPpFFJwO8fdA82H3TRCdHX5ug8gT+FBgna650Nwn1P3mt4LBl2CiSTzPLvNP7fR1ebsfIR+NLr2IFm4wsnbQsYJkbxpoPwoALTo33v8F/nRCdHrfNnPqPwpK/E7zb3G/Z/wDyK5OFv3PduN5z99AD5uF4ZdyP2n/mK5zYRf8ALPpm/GlCcDvn3APNh91Ep0cuHd0HlJ+4UAG/3xh19kfupH1iornSNeSMfMgfjXSdG1964x8gB+NTp0fsjfMfNvwAoAX3OkbcrajzJP0ioMLi7d66OvUaiAVJEHlmg+k1YLfCbK/9NT56/WaJW2qjQKo8ABQAC2Fwibi0PtMD/Ea0eKYZNmUfZU/cKS8ZwSm4DZZSzboCJneRrtUVvo9fPJV82/CaAG9zpRa91Xb0AH1n5ULd6VH3bYHiWn6AVxY6KNoXvbclX7zR9rozYG+ZvMx9AKAFN3pLeOxRfJdf9RNBXOMYhzHWtP6pj+Grja4VYXa0vqJ+s0UiBRoAB4CPpQBQvyDE3N0uN5zHxaibXRjEHcKvm3+2aur3IEnagMRxm0u9xfIGf4ZoCyv3eitwLKuhbu1A+P8A6pLisLdtHtKynv8A/wBDQ/GrRielFseyrN8h8T+FLcT0luEQqIJ75P4fSg1AeE6QX7fvZx3MJ+dOcH0tttpcQqe8aiqrcbMSYGvcAB8BsK4+JpHBMdTaPR8Ni7dwSjqfI1MUrzJdNQSD3gmfjTPBdJb9vQkOvjvU3ifYosi7l3dajINKsJ0pstAcFD46im1q8jiVYEeBqTi11HTs4FcsRUsVyaUYDw/Q28faaPIAfUmu7nRy0hhnLsNwDoPMiueK9NrjkrbARduZJ8yCPhSJ+O3jsQPJRHzrsVvqcj+BY7fCLI9wHzk/U0UmGRdkRfGAKpl3iF473H15SfugVC90nU6+PPzNMLReGxlsb3EHhmE/CoX4zYHvk+QP4RVNB/rwqe3hbjeyjnyU/hQFFhudI7Y9lGPnAHx1oa50mb3UUeZJ+kUFa4FePuBfNh91EDo4wHauKoG51Og+FAaDeG4q9f1ytAJkooCkaCASZnf4UYnDgv8A/OOe6j03qrvfstbFsvfXKt1ZRoDC6dGyzowGnkWGs1nSDGJiWUksIt5INhW0zo8yXEDsbeXdQkvUG36FzFpx7No+gA7/AOVZLzqhAjnG+nj50jfpMh1Iu+sf7qjHSC13P8B/updm0h8+IA3B9BP0oa5xMDa1dbyUfeRSr/iC1+jc/dH+6tHpBa/Rf90f7qNhSDH4zc93Cv6kD6TQl3i2L5WQPST9Yri/jluoyC3iIYRmRYI8Q2bSpbljrLXVZb6iAM2cB9O9g0knnO9aABcxWNbcXAPAAfw60vuYPEEyyXG8/wCZqz4rBrcFsM11Qjq3ZOpy+63a1B50Rdwtlnt3G66bRYgAgA5lynMAfvrTLKcuAvggi24IOhHKNjNXPhmKd0BdGVx7Q0+I12NTTZD58lyYiJlfPKWia6bE2zPZua+Og8QC0CsNNXMWByb0E/ShbnGI2s3W9AB8z91LcXxpLblGW5IE+yNR3jWo/wDiG1+jc/dH+6jYUia/xnE+7hyPMyfgCKAu4rGsf+oPIAfTWp16RWonLc/dH+6t3eO2mBUi4PEBfPm0UBQpu4LENqyXGP6xn6neozwu9/lN8B+OlOLOKR0VFW8QGVsxRSDlIO8gDbl41PdwKvat2yXXJl1CpqBAIiSBI7tq0wr/APdl7/Kf5ULctlSVYEEQCDvVu4ngLV4iWvrCMoyQPby676kZdPHXlUj2EzFlTuEtq2ihdTvOlAWVOzgHb2VPwgfE0ws8Ffmyj5n+vWn5rWvcaAsUngSHdmmN9NPSleM4NcXVe2PDf4fhNWsWzWwg86As8+ZORkd/f86yxfdNUZl8j91XvF4G3c9tQfHmPIjWq5xbgfVgsrjL3MYPodj8qxo1M3held5NLgDjv2Ip1a6UYciWJBPhVIe36fzrnqp1E/CpvHFlFkaLJx3/AB73/db+Kgk29R9TWVlVRPuSp7Z8vvFZa2rdZQBbOA8vX605besrKBThaXce/wCXvfYP3VusoApK7f131DY9r4fdWVlAxJz/AK7xW/6+QrVZQB0f6/epzwP26ysoAsJ3rFrKygU5FY1ZWUAcNvWxWVlAFc6U/wCLb+w31pG2w8h9a1WUDIkTceZ++mHBvaHp91ZWVphaLn3VwK1WVhhKKxudZWUGkXOpU51usoMMrBtWVlAHJqmcY/5lvsH6VlZQagCx7R8jXoX9nX/Kt/3T/ClZWUsh11P/2Q==');">
            <div class="university-content">
                <div class="university-name">Polytech Nancy, France</div>
                <div class="university-desc">
                    Part of the University of Lorraine, offering engineering programs in materials, IT, and industrial systems with practical training.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Rest of the tab2 content (Programs Offered, Initiatives, Scholarships)
    st.subheader("📌 Programs Offered")
    st.markdown("""
    - Student Exchange Programs (1-2 semesters)
    - Dual Degree Programs
    - Summer/Winter Schools
    - Research Collaborations
    - Faculty Development Programs
    - International Internships (3-6 months)
    """)
    
    st.subheader("🌍 Foreign University Initiatives & Collaborations")
    
    # Add custom CSS for initiative cards
    st.markdown("""
    <style>
        .initiative-card {
            background: linear-gradient(135deg, #3a4a6b, #1f2a48);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .initiative-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .initiative-title {
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ffd700;
        }
        .initiative-details {
            font-size: 0.9rem;
            line-height: 1.4;
            color: #e0e0e0;
        }
        .initiative-coordinator {
            font-size: 0.85rem;
            font-style: italic;
            margin-top: 10px;
            color: #a0aec0;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create two columns for initiative cards
    col1, col2 = st.columns(2)
    
    with col1:
        # Rotary Youth Exchange Student
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Rotary Youth Exchange Student</div>
            <div class="initiative-details">Argentina, Austria, Brazil</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan (Coordinator)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visit to NTI Gymnasiet
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Visit to NTI Gymnasiet</div>
            <div class="initiative-details">Eskilstuna, Sweden</div>
            <div class="initiative-coordinator">Dr V V Bag & Prof K N Vhatkar and 8 students</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visit to Tyreso Exchange Program
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Visit to Tyreso Exchange Program</div>
            <div class="initiative-coordinator">Prof V S Shirval and Prof S S Kale and 4 students</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visit to Texas A&M University
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Visit to Texas A&M University</div>
            <div class="initiative-details">USA</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visit to Supareo University
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Visit to Supareo University</div>
            <div class="initiative-details">France</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Visit to Toulouse University
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Visit to Toulouse University</div>
            <div class="initiative-details">France</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan</div>
        </div>
        """, unsafe_allow_html=True)
        
        # German University Delegates Visit
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">German University Delegates Visit</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan (Coordinator)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Polytech Nancy Internship
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Three Months Internship at Polytech Nancy</div>
            <div class="initiative-details">France</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan (Program Coordinator)<br>Prof C V Papade (Course Coordinator)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Meeting with Prof. Sama Mbang
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Meeting with Prof. Sama Mbang</div>
            <div class="initiative-details">Founder, Digital Transformation Alliance Cameroon for Solar Ready Engineer Course</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan (Coordinator)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Meeting with Prof. Mikhail Stepanov
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Meeting with Prof. Mikhail Stepanov</div>
            <div class="initiative-details">From Supaero University France for Aircraft Domain</div>
            <div class="initiative-coordinator">Dr Shriniwas S Metan (Coordinator)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Alumni Group Meeting
        st.markdown(f"""
        <div class="initiative-card">
            <div class="initiative-title">Alumni Group Meeting</div>
            <div class="initiative-details">Networking with international alumni</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Objectives
    st.markdown("""
    ### 🎯 Objectives
    - Offer global exposure to students and faculty
    - Enable international student/faculty exchanges
    - Provide internship and job placement opportunities
    - Support scholarship-based admissions to top global institutions
    - Encourage joint academic and cultural collaborations
    """)
    
    # Strategic Work Plan
    st.markdown("""
    ### 📋 Strategic Work Plan
    """)
    
    work_plan_data = {
        "Focus Area": [
            "MoUs",
            "Exchange Programs",
            "Curriculum Collaboration",
            "Joint Research",
            "Public Relations",
            "Monitoring & Compliance"
        ],
        "Description": [
            "Formalize global institutional collaborations",
            "Facilitate student and faculty mobility",
            "Joint design and academic enhancement",
            "Initiate research-driven partnerships",
            "Showcase international activities and partnerships",
            "Track progress and adhere to regulations"
        ]
    }
    
    st.dataframe(
        pd.DataFrame(work_plan_data),
        hide_index=True,
        use_container_width=True
    )
    
    # International Engagements
    st.markdown("""
    ### 🌍 International Engagements
    """)
    
    # Polytech Nancy Exchange Programs
    st.markdown("""
    #### Polytech Nancy University, France
    - **NKOCET Students in France (Apr-Aug 2024):**  
      4 students participated in a Students Orientation Program at Nancy University Hospital  
      • Interaction with Mayor Sir Hablot of Vandoeuvre  
      • Industry visit to Dassault Systèmes Headquarters in Vélizy  
      • First-hand insights into industrial innovation and engineering practices
    
    - **French Students at NKOCET (Apr-Aug 2024):**  
      4 students completed internship on *"Solar Energy Engineering for Sustainable Cities and Product Development"*  
      • Hands-on experience in renewable energy solutions  
      • Focus on sustainability-driven innovation
    
    - **French Students at NKOCET (Mar-Jun 2025):**  
      2 students completed project on *"Solar Tree for Sustainable Cities"*  
      • Innovative applications of solar technology in urban environments  
      • Strengthened collaborative efforts in sustainable engineering
    """)
    
    # Work Plan & Strategic Roles
    st.markdown("""
    ### 🛠️ Work Plan & Strategic Roles
    """)
    
    roles_data = {
        "Key Focus Area": [
            "MoU Development",
            "Relationship Management",
            "Curriculum Development",
            "Joint Research",
            "Visiting Faculty",
            "Cultural Exchange",
            "Logistical Support",
            "Compliance",
            "Monitoring & Reporting"
        ],
        "Role": [
            "Build formal agreements with international institutions",
            "Cultivate ongoing international relations",
            "Collaborate on enhancing academic programs",
            "Initiate global research collaborations",
            "Invite foreign faculty for guest lectures and exchange",
            "Encourage international cultural immersion",
            "Provide operational help for travel, stay, documentation",
            "Adhere to international academic and legal standards",
            "Periodic assessment and progress tracking"
        ]
    }
    
    st.dataframe(
        pd.DataFrame(roles_data),
        hide_index=True,
        use_container_width=True
    )
    
    # Initiatives & Engagements
    st.markdown("""
    ### 🔥 Initiatives & Engagements
    - Rotary Youth Exchange (Argentina, Austria, Brazil)
    - Visits to:
      - NTI Gymnasiet, Sweden
      - Tyresö Gymnasium, Sweden
      - Texas A&M University, USA
      - Supareo & Toulouse Universities, France
    - German University delegates visit to NKOCET
    - Internship program at Polytech Nancy University, France
    - Meetings with:
      - Prof. Sama Mbang (Digital Transformation Alliance, Cameroon)
      - Prof. Mikhail Stepanov (Supaero University, France)
    """)
# Future Plans section
    st.subheader("🚀 Future Plans for Study Abroad Cell")
    
    st.markdown("""
    <style>
        .future-plan-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .future-plan-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .plan-item {
            font-size: 1rem;
            margin-bottom: 10px;
            padding-left: 1.5rem;
            text-indent: -1.5rem;
        }
        
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="future-plan-card">
        <div class="plan-item">Organize sessions led by alumni and external agencies</div>
        <div class="plan-item">Target of <strong>at least 10 students per year</strong> to pursue MS abroad</div>
        <div class="plan-item">Host embassy sessions on campus</div>
        <div class="plan-item">Include first-year students through orientation programs</div>
        <div class="plan-item">Facilitate foreign delegate visits for funding and exchange opportunities</div>
        <div class="plan-item">Launch foreign university outreach sessions for 12th-grade students</div>
        <div class="plan-item">Revamp SAC infrastructure, set up a <strong>dedicated library</strong>, and assign student mentors</div>
    </div>
    """, unsafe_allow_html=True)

    # Global Gallery section (keep as before)
    st.divider()
    st.subheader("🌐 Global Gallery")

    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <a href="https://thecampuscoder49.pixieset.com/studyabroad/" target="_blank" style="text-decoration: none;">
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
                ✨ Foreign University Tie-up ➔
            </button>
        </a>
        <p style="color: #e2e8f0; margin-top: 10px; font-size: 14px; font-style: italic;">Click to view our photo gallery in a new window</p>
    </div>
    """, unsafe_allow_html=True)
footer ()