import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.stylable_container import stylable_container


def set_page_config():
    st.set_page_config(
        page_title="N.K. Orchid College - Home",
        layout="wide",
        page_icon="🎓",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'https://www.nkorchid.edu.in',
            'Report a bug': "mailto:support@nkorchid.edu.in",
            'About': "### N.K. Orchid College of Engineering & Technology"
        }
    )

def footer():
    st.markdown("""
    <!-- Font Awesome CDN -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

    <style>
    .custom-footer {
        background-color: #0c3c78;
        color: white;
        padding: 2rem 5%;
        font-family: 'Segoe UI', sans-serif;
        border-top: 5px solid #f9b233;
        margin-top: 2rem;
    }
    .custom-footer h4 {
        color: white;
        border-bottom: 2px solid #f9b233;
        padding-bottom: 0.3rem;
        font-size: 1.2rem;
        margin-bottom: 0.8rem;
    }
    .custom-footer p, .custom-footer a {
        font-size: 0.95rem;
        line-height: 1.5;
        color: white;
        text-decoration: none;
    }
    .custom-footer a:hover {
        color: #f9b233;
        text-decoration: underline;
    }
    .custom-footer input {
        width: 100%;
        padding: 0.5rem;
        margin-top: 0.5rem;
        border-radius: 5px;
        border: none;
    }
    .custom-footer button {
        background-color: #f9b233;
        color: #000;
        border: none;
        padding: 0.5rem 1rem;
        margin-top: 0.7rem;
        border-radius: 5px;
        cursor: pointer;
    }
    .custom-footer button:hover {
        background-color: #e2a429;
    }
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 2rem;
        text-align: left;
    }
    .social-icons a {
        color: white;
        font-size: 1.3rem;
        margin-right: 15px;
        display: inline-block;
    }
    .social-icons a:hover {
        color: #f9b233;
    }
    .bottom-bar {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #ccc;
        color: #ccc;
        font-size: 0.85rem;
    }
    </style>

    <div class="custom-footer">
        <div class="footer-grid">
            <div>
                <h4>🎓 N.K. Orchid College</h4>
                <p>Empowering minds, building futures. Join our community of innovators and leaders.</p>
                <div class="social-icons">
                    <a href="https://www.instagram.com/invites/contact/?i=1ds7dudm9450w&utm_content=1wflhmu" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.facebook.com/NKORCHIDENGG" target="_blank"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://twitter.com/nk_orchid?t=k7XMCi2mspNr3DP8weqkLA&s=08" target="_blank"><i class="fab fa-twitter"></i></a>
                    <a href="https://www.linkedin.com/in/nkorchidcollege" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
            <div>
                <h4>Contact Info</h4>
                <p>📍 Gat No. 16, Solapur-Tuljapur Road,<br> Tale-Hipparaga, Solapur - 413002</p>
                <p>📞 +91 2172990051</p>
                <p>✉ admission@orchidengg.ac.in</p>
            </div>
        </div>
        <div class="bottom-bar">
            © 2024 N.K. Orchid College of Engineering & Technology. All Rights Reserved |
            <a href="#">Privacy Policy</a> |
            <a href="#">Terms of Service</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
