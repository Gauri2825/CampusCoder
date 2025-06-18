import streamlit as st
from PIL import Image
import base64
import os # Import os to list files in a directory
from utils.file import set_page_config,footer
from streamlit.components.v1 import html
import time

set_page_config()

# --- Load multiple background images for the slider ---
BG_IMAGES_ENCODED = []
IMAGE_DIR = "assets"
IMAGE_PREFIX = "header_" 
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')

try:
    all_assets = os.listdir(IMAGE_DIR)
    slider_images = sorted([f for f in all_assets if f.startswith(IMAGE_PREFIX) and f.endswith(VALID_EXTENSIONS)])

    if not slider_images:
        st.error(f"No slider images found in '{IMAGE_DIR}' starting with '{IMAGE_PREFIX}'.")
    else:
        for img_name in slider_images:
            img_path = os.path.join(IMAGE_DIR, img_name)
            with open(img_path, "rb") as f:
                BG_IMAGES_ENCODED.append(base64.b64encode(f.read()).decode())
except FileNotFoundError:
    st.error(f"Image directory '{IMAGE_DIR}' not found.")
    BG_IMAGES_ENCODED = []
except Exception as e:
    st.error(f"An error occurred while loading images: {e}")
    BG_IMAGES_ENCODED = []


def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")
# Convert your bot icon to base64
chat_icon_base64 = get_base64_image("assets/chat_icon.png")
def set_bg_hack():
    num_images = len(BG_IMAGES_ENCODED)
    if num_images == 0:
        st.markdown(
            """
            <style>
            .stApp {
                padding: 0 !important;
                margin: 0 !important;
            }
            .college-header {
                background-color: #333;
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                color: white;
                text-align: center;
                position: relative;
                width: 100vw;
                height: 100vh;
                margin-left: -50vw;
                left: 50%;
                margin-right: -50vw;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .college-header::before {
                content: "";
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 100%);
                z-index: 1;
            }
            .college-header h1, .college-header h3 {
                position: relative;
                z-index: 2;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        return

    animation_duration_per_image = 3  # seconds per image
    total_animation_duration = num_images * animation_duration_per_image

    keyframes = ""
    for i, img_b64 in enumerate(BG_IMAGES_ENCODED):
        start_percent = (i / num_images) * 100
        end_percent = ((i + 1) / num_images) * 100

        keyframes += f"""
        {start_percent}% {{
            background-image: url(data:image/png;base64,{img_b64});
        }}
        {end_percent}% {{
            background-image: url(data:image/png;base64,{img_b64});
        }}
        """

    st.markdown(
        f"""
        <style>
        .stApp {{
            padding: 0 !important;
            margin: 0 !important;
        }}
        .college-header {{
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            color: white;
            text-align: center;
            position: relative;
            width: 100vw;
            height: 100vh;
            margin-left: -50vw;
            left: 50%;
            margin-right: -50vw;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            animation: imageSlider {total_animation_duration}s infinite;
        }}
        .college-header::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(45deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.2) 100%);
            z-index: 1;
        }}
        .college-header h1 {{
            position: relative;
            z-index: 2;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            animation: move 15s linear infinite;
        }}
        .college-header h3 {{
            position: relative;
            z-index: 2;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
         @keyframes move {{
            0% {{ transform: translateX(100%); }}
            50% {{ transform: translateX(-50%); }}
            100% {{ transform: translateX(-100%); }}
        }}

        @keyframes imageSlider {{
            {keyframes}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Load logo from assets and encode
LOGO_IMAGE_PATH = os.path.join(IMAGE_DIR, "logo.webp")  # Change filename if needed
encoded_logo = ""
if os.path.exists(LOGO_IMAGE_PATH):
    with open(LOGO_IMAGE_PATH, "rb") as logo_file:
        encoded_logo = base64.b64encode(logo_file.read()).decode()
else:
    st.warning("Logo image not found in assets folder.")

def college_header():
    # Paths to images
    logo_path = "assets/logo.webp"
    naac_path = "assets/naac.webp"

    # Encode images
    def encode_image(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception as e:
            st.error(f"Error loading image {path}: {e}")
            return ""

    logo_b64 = encode_image(logo_path)
    naac_b64 = encode_image(naac_path)

    st.markdown(f"""
    <div class="college-header">
        <div class="logo-container left">
            <img src="data:image/webp;base64,{logo_b64}" alt="College Logo">
        </div>
        <div class="logo-container right">
            <img src="data:image/webp;base64,{naac_b64}" alt="NAAC Logo">
        </div>
        <div class="header-text">
            <h3>Pradnya Niketan Education Society Pune's</h3>
            <h1>🎓 Nagesh Karajagi <span style="font-style: italic;">ORCHID</span> College of <br> Engineering & Technology, Solapur 🎓</h1>
            <h3>Autonomous Institution | AICTE Approved | NAAC Accredited A+ Grade (CGPA: 3.32)</h3>
            <div class="location-wrapper">
                <a href="/Location" class="location-link" title="Visit Our Location">
                    <div class="location-tooltip">Find us on map!</div>
                    <div class="location-icon">
                        <i class="fas fa-map-marker-alt"></i>
                        <span class="pulse-effect"></span>
                    </div>
                </a>
            </div>
        </div>
    </div>
    <div class="chatbot-wrapper">
    <a href="https://cdn.botpress.cloud/webchat/v3.0/shareable.html?configUrl=https://files.bpcontent.cloud/2025/06/03/14/20250603145628-8YR0POIO.json" target="_blank">
    <img class="chatbot-icon" src="data:image/png;base64,{chat_icon_base64}" alt="Chatbot">
    </a>
    <div class="chat-tooltip">Ask our Bot!</div>
    </div>
    <style>
        .logo-container {{
            position: absolute;
            top: 10px;
            width: 100px;
        }}

        .logo-container.left {{
            left: 10px;
        }}

        .logo-container.right {{
            right: 10px;
        }}

        .logo-container img {{
            max-width: 100%;
            height: auto;
        }}

        .header-text h1 {{
            font-size: 28px;
            margin: 10px 0;
        }}

        @keyframes bounce {{
            0%, 100% {{ transform: translateX(50%) translateY(0); }}
            50% {{ transform: translateX(50%) translateY(-10px); }}
        }}
       
        .location-wrapper {{
            position: relative;
            display: inline-block;
            margin: 20px auto;
            text-align: center;
            width: 100%;
        }}
        
        .location-link {{
            display: inline-block;
            position: relative;
            text-decoration: none;
            color: inherit;
        }}
        
        .location-icon {{
            position: relative;
            font-size: 5rem;
            color: #e63946;
            transition: all 0.3s ease;
            animation: bounce 2s infinite;
            z-index: 2;
        }}
        
        .location-icon:hover {{
            transform: scale(1.2);
            color: #ff0000;
        }}
        
        .pulse-effect {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: rgba(230, 57, 70, 0.5);
            animation: pulse 2s infinite;
            z-index: 1;
        }}
        
        .location-tooltip {{
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: #333;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 1.1rem;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            white-space: nowrap;
        }}
        
        .location-link:hover .location-tooltip {{
            opacity: 1;
            visibility: visible;
            bottom: 90%;
        }}
        
        @keyframes pulse {{
            0% {{
                transform: scale(0.8);
                opacity: 0.7;
            }}
            70% {{
                transform: scale(1.3);
                opacity: 0;
            }}
            100% {{
                transform: scale(0.8);
                opacity: 0;
            }}
        }}

        #chatbot-button {{
            position: fixed;
            bottom: 20px;
            right: 30px;
            z-index: 10000;
            background-color: transparent;
            border-radius: 50%;
            width: 80px;
            height: 80px;
            border: none;
            cursor: pointer;
            padding: 0;
            overflow: hidden;
        }}
        .chatbot-wrapper {{
            position: fixed;
            bottom: 20px;
            right: 30px;
            width: 80px;
            height: 80px;
            z-index: 10000;
            cursor: pointer;
        }}

        .chatbot-icon {{
            width: 100%;
            height: 100%;
            border-radius: 50%;
        }}

        .chat-tooltip {{
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: #333;
            color: #fff;
            padding: 6px 10px;
            border-radius: 5px;
            font-size: 0.9rem;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            white-space: nowrap;
        }}

        .chatbot-wrapper:hover .chat-tooltip {{
            opacity: 1;
            visibility: visible;
        }}

    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)

def fun_facts():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
        padding: 0 1rem;
        font-family: 'Poppins', sans-serif;
    }

    .stat-box {
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #f0f4ff, #ffffff);
        border-radius: 12px;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }

    .stat-box h2 {
        color: #1e56a0;
        font-size: 2em;
        margin: 0;
    }

    .stat-box p {
        margin: 0.5rem 0 0;
        font-size: 1.1em;
        color: #333;
    }

    @media (max-width: 768px) {
        .stats-container {
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        }
    }

    @media (max-width: 480px) {
        .stats-container {
            grid-template-columns: 1fr;
        }
    }
    </style>

    <div class="stats-container">
        <div class="stat-box">
            <h2>2200+</h2>
            <p>Students 👨‍🎓</p>
        </div>
        <div class="stat-box">
            <h2>450+</h2>
            <p>Placements 💼</p>
        </div>
        <div class="stat-box">
            <h2>110+</h2>
            <p>Faculty 👩‍🏫</p>
        </div>
        <div class="stat-box">
            <h2>30+</h2>
            <p>Labs 🔬</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_admission_popup():
    if "admission_popup_shown" not in st.session_state:
        st.session_state.admission_popup_shown = False

    if not st.session_state.admission_popup_shown:
        popup_placeholder = st.empty()

        with popup_placeholder.container():
            st.markdown(
                """
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
                .admission-card {
                    background-color: #e6f7ff; /* Lighter, more vibrant blue-ish background */
                    border-radius: 15px; /* Slightly more rounded corners */
                    padding: 25px; /* More padding */
                    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); /* Stronger shadow */
                    text-align: center;
                    animation: fadeIn 0.6s ease-out, slideIn 0.6s ease-out; /* Add slideIn animation */
                    margin: 20px auto;
                    max-width: 550px; /* Slightly wider card */
                    border: 2px solid #2e86de; /* Add a subtle border */
                    position: relative; /* Needed for absolute positioning of close button */
                    overflow: hidden; /* Ensures nothing spills out */
                    font-family: 'Poppins', sans-serif;
                }
                .admission-card h3 {
                    color: #0056b3; /* Darker blue for heading */
                    margin-bottom: 12px;
                    font-size: 1.8em; /* Larger heading font */
                    text-transform: uppercase; /* Uppercase heading */
                    letter-spacing: 1px;
                }
                .admission-card p {
                    color: #333;
                    font-size: 1.1em; /* Slightly larger paragraph font */
                    line-height: 1.6;
                    margin-bottom: 15px;
                }
                .admission-card .highlight {
                    color: #e60000; /* Bright red for emphasis */
                    font-weight: bold;
                    font-size: 1.2em;
                }

                @keyframes fadeIn {
                    from { opacity: 0; }
                    to { opacity: 1; }
                }
                @keyframes slideIn {
                    from { transform: translateY(-50px); }
                    to { transform: translateY(0); }
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="admission-card">
                    <h3>📢 Admissions Open! 🎓</h3>
                    <p>Exciting news! Admissions for the upcoming academic year are now open at <strong>Orchid</strong>!</p>
                    <p class="highlight">Join us to experience world-class education, state-of-the-art facilities, and a vibrant campus life.</p>
                    <p>Secure your spot and embark on a transformative educational journey with us.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Wait for 3 seconds
        time.sleep(3)
        # Clear the placeholder to make the popup disappear
        popup_placeholder.empty()
        # Set the flag so it doesn't reappear on subsequent reruns
        st.session_state.admission_popup_shown = True


def about_us_section():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
        .about-container {
            font-family: 'Poppins', sans-serif;
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 3rem;
            color: #1a237e;
            position: relative;
        }
        .section-title:after {
            content: '';
            position: absolute;
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, #1a237e, #3949ab);
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 2px;
        }
        .about-flex-row {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 2rem;
        }
        .about-flex-item {
            flex: 1 1 280px;
            max-width: 320px;
            padding: 2rem 1.5rem;
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            z-index: 1;
        }
        .about-flex-item:before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(90deg, #1a237e, #3949ab);
            transition: height 0.3s ease;
            z-index: -1;
        }
        .about-flex-item:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.12);
        }
        .about-flex-item:hover:before {
            height: 100%;
        }       
        .about-flex-item h3 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
            color: #000;
            position: relative;
            transition: color 0.3s ease;
        }        
        .about-flex-item:hover h3 {
            color: #fff;
        }
        .about-flex-item p {
            font-size: 1rem;
            line-height: 1.7;
            color: #555;
            margin-bottom: 1.2rem;
            transition: color 0.3s ease;
        }
        .about-flex-item:hover p {
            color: rgba(255,255,255,0.9);
        }        
        .about-flex-item:nth-child(1):before {
            background: linear-gradient(90deg, #1976d2, #64b5f6);
        }        
        .about-flex-item:nth-child(2):before {
            background: linear-gradient(90deg, #43a047, #81c784);
        }        
        .about-flex-item:nth-child(3):before {
            background: linear-gradient(90deg, #f9b233, #ffd54f);
        }        
        .about-flex-item:nth-child(4):before {
            background: linear-gradient(90deg, #d32f2f, #e57373);
        }        
        .icon-container {
            width: 60px;
            height: 60px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }        
        .icon {
            font-size: 1.8rem;
            color: white;
        }        
        @media (max-width: 768px) {
            .about-flex-item {
                flex: 1 1 100%;
                max-width: 100%;
            }            
        }
        /* Laptop/Desktop (4 columns) */
        @media (min-width: 1024px) {
            .about-flex-row {
                grid-template-columns: repeat(4, 1fr);
            }
        }
        
        /* Tablets (2 columns) */
        @media (max-width: 1023px) and (min-width: 768px) {
            .about-flex-row {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        
        /* Mobile (1 column) */
        @media (max-width: 767px) {
            .about-flex-row {
                grid-template-columns: 1fr;
            }
            .section-title {
                font-size: 2rem;
                margin-bottom: 2rem;
            }            
            .about-flex-item {
                padding: 1.5rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-container">
        <div class="about-flex-row">
            <div class="about-flex-item">
                <div class="icon-container">
                <span class="icon">🏫</span>
                </div>
                <h3>About Us</h3>
                <p>N.K. Orchid College of Engineering & Technology is a premier institution dedicated to providing quality education and fostering innovation.
                </p>
                <p>We offer undergraduate and postgraduate programs with a focus on practical learning and industry collaboration.
                </p>
            </div>
            <div class="about-flex-item">
                <div class="icon-container">
                <span class="icon">👁</span>
                </div>
                <h3>Our Vision</h3>
                <p>To be a globally recognized institution that nurtures talent and fosters innovation in engineering and technology.
                </p>
                <p>We aim to create an environment that encourages creativity, critical thinking, and lifelong learning.
                </p>
            </div>
            <div class="about-flex-item">
                <div class="icon-container">
                    <span class="icon">🎯</span>
                </div>
                <h3>Our Mission</h3>
                <p>
                    To provide quality education that meets industry and societal needs while fostering research and innovation.
                </p>
                <p>
                    We're committed to creating a diverse and inclusive environment for personal and professional growth.
                </p>
            </div>
            <div class="about-flex-item">
                <div class="icon-container">
                <span class="icon">❤</span>
                </div>
                <h3>Core Values</h3>
                <p>Integrity, Excellence, Innovation, Collaboration, and Social Responsibility guide our institution.
                </p>
                <p>We instill these values to prepare students for future challenges.
                </p>
            </div>
        </div>
    </div>
    
    <script>
    // Animation for cards when they come into view
    document.addEventListener('DOMContentLoaded', function() {
        const cards = document.querySelectorAll('.about-flex-item');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, 150 * index);
                    observer.unobserve(entry.target);
                }
            });
        }, {threshold: 0.1});
        
        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    });
    </script>
    """, unsafe_allow_html=True)


# Rest of your Streamlit app content goes here
# Call the function to show the popup
show_admission_popup()
set_bg_hack() # Applies the overall background and header styling
college_header() # This is the dynamic banner with the image and text animation




st.markdown("<h2 style='text-align: center; margin-bottom: 1.5rem;'>📖 About Us</h2>", unsafe_allow_html=True)
fun_facts()
about_us_section()
# --------------------------- WHY CHOOSE US SECTION ---------------------------
st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>💡 Why Choose NKOCET?</h2>", unsafe_allow_html=True)

st.markdown("""
<style>
    .why-choose {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1.2rem;
        margin: 1.5rem auto;
        max-width: 1100px;
    }
    .why-card {
        flex: 1 1 250px;
        background-color: #f1faff;
        border-left: 5px solid #2e86de;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        font-size: 1rem;
    }
</style>

<div class="why-choose">
    <div class="why-card">🤝 Industry-oriented curriculum with <strong>placement support</strong></div>
    <div class="why-card">🏆 <strong>Top-ranked</strong> institution in the region</div>
    <div class="why-card">🌐 <strong>Global exposure</strong> through study abroad programs</div>
    <div class="why-card">🎓 Strong alumni in <strong>leading companies</strong></div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.cta-container {
    background-color: #fff8e1;
    padding: 25px;
    border-radius: 15px;
    border: 2px dashed #ffca28;
    text-align: center;
    margin-top: 2rem;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.cta-heading {
    color: #ff6f00;
    font-size: 1.8rem;
    margin-bottom: 10px;
}

.cta-container {
    animation: fadeSlide 0.6s ease-out;
}

@keyframes fadeSlide {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)

clicked = st.markdown("""
<div class="cta-container">
    <div class="cta-heading">🚀 Take the First Step Toward Your Future</div>
    <p style="font-size: 1.1rem;">Ready to join a community of innovators, leaders, and achievers?</p>
</div>
""", unsafe_allow_html=True)

# --- Main Page Content ---

# Title
st.markdown("<h2 style='text-align: center;'>🎓 Explore Our College</h2>", unsafe_allow_html=True)
st.write("")  # Spacer
st.markdown(
    """
    <style>
    /* This section might be redundant if set_bg_hack() already sets the main background. */
    /* If you want a different background for the main content area, you'll need
        to scope this CSS more specifically or use Streamlit's container methods. */
    .stApp {
        /* background-image: url('assets/image.jpg'); / / Likely overridden by set_bg_hack */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }
    /* Hide Streamlit's default padding and menu */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    header, footer {visibility: hidden;}
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

pages = [
    ("🏆 Achievements", "1_🏆_Student_Achievements"),
    ("🎓 Admission", "2_🎓_Admission"),
    ("📄 Brochure", "3_📄_Download_Brochure"),
    ("🏫 Departments", "4_🏫_Departments"),
    ("🎉 Events", "5_🎉_Events_Culture"),
    ("📚 Library", "6_📚_Library"),
    ("🗺 Location", "7_🗺_Location"),
    ("🧪 Research & Development", "8_🧪_Research & Development"),
    ("🎗 Infrastructure", "9_🎗_Infrastructure"),
    ("🖼 Photo Gallery", "10_🖼_Photo_Gallery"),
    ("💼 Placements", "11_💼_Placements"),
    ("🌍 Study Abroad", "12_🌍_Study_Abroad"),
    ("⚽ Sports", "13_⚽_Sports"),
    ("🗣️ Testimonials", "14_🗣️_Testimonials"),
    ("🚌Transportation", "15_🚌_Transportation"),
    ("🏠 Hostel", "16_🏠_Hostel"),
    ("🌠 Esteemed Guests", "17_🌠_EsteemedGuests"),
    ("🎮 CampusTeams" , "18_🎮_CampusTeams"),
    ("👩‍💻 Campus Coders 🧑‍💻", "Development_Team"),
    ("🎥 video Moments", "19_🎥_video_Moments"),
]

# Create button grid with styling
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 50px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        background-color: #f8f9fa;
        color: #333;
        font-weight: 500;
        transition: all 0.3s;
        margin: 0 20px;
    }
    .stButton>button:hover {
        background-color: #e9ecef;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

for i in range(0, len(pages), 6):
    cols = st.columns(6)
    for j in range(6):
        if i + j < len(pages):
            name, page = pages[i + j]
            with cols[j]:
                if st.button(name):
                    st.switch_page(f"pages/{page}.py")

st.markdown("<h2 style='text-align: center;'>🎥 NKOCET CAMPUS TOUR 🎥</h2>", unsafe_allow_html=True)

st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <iframe width="900" height="500" src="https://www.youtube.com/embed/F-IujllQ3sI" frameborder="0" allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)

footer()