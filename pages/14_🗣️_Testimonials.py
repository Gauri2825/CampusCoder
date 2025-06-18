import streamlit as st
import base64
from pathlib import Path
from utils.file import footer

# Helper function to encode local image to Base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    except FileNotFoundError:
        # Fallback to a placeholder image if the file is not found
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAABsklEQVR4nO2YTUvDQBCGE90n1/uUfXlHkTxAXkG8gf028QLxBsYDxBN4gYjNl2D7+XbWnK211qDQQqVpkvlgsg+j6wFqK+hR2n1t412hXl+N7bS/h87k1/n/3l1j0vL75wJ0g7d3Y9g2c+lC1l+4c0Bwz4p23+4sYfP79k54v3hQfA4h0+e4P5D20s0v95tS/A4oJ1m350j0M+H4h8zJ8D0s/o669P/v/o9n+yS+J/J0j7lqB8T5A2T9aW1+k5fK8lX6L14n+FJL4n/iQ2Z09pPjP/pC2z9O35oT+I1j+P8L5T3x+tXhPzQ/x+tHhPzR+x+tGhPzR+B+tCxh8Dq9G+D4wz77B99Yp+Bxgf2Q9iB20f9xWq/g8Qx934u2b/g82m+9Hl4/Y/A/c22iW+J/J0j7hY+C1k3V/62t+59w/e4/f7g9a8D+C+9d332v3oAAAAASUVORK5CYII="

st.set_page_config(layout="wide", page_title="Testimonials | College Name", page_icon="🌟")
    
# Base directory for images
IMG_DIR = Path(__file__).parent.parent / "assets"

st.markdown(f"""
    <style>
        :root {{
            --primary-color: #3498db;
            --secondary-color: #2c3e50;
            --accent-color: #e74c3c;
            --light-color: #ecf0f1;
            --dark-color: #2c3e50;
        }}
        
        .testimonial-header {{
            font-size: 3rem !important;
            font-weight: 800;
            color: var(--secondary-color);
            text-align: center;
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #3498db, #e74c3c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}
        
        .testimonial-subheader {{
            font-size: 1.4rem !important;
            color: #7f8c8d;
            text-align: center;
            margin-bottom: 2rem;
            font-weight: 300;
        }}
        
        /* Main wrapper for the entire slider component */
        .testimonial-slider-wrapper {{
            width: 80%;
            max-width: 800px;
            margin: 0 auto 1.5rem auto;
            border-radius: 20px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
            background: white;
            position: relative;
            min-height: 380px;
            height: fit-content;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            box-sizing: border-box;
        }}

        /* Styling for an individual testimonial card */
        .testimonial-card {{
            padding: 2rem;
            box-sizing: border-box;
            width: 100%;
            position: relative;
            text-align: center;
            transition: transform 0.5s ease, opacity 0.5s ease;
        }}
        
        .testimonial-quote {{
            font-size: 1.3rem;
            line-height: 1.8;
            color: var(--dark-color);
            font-style: italic;
            margin-bottom: 2rem;
            position: relative;
            padding: 0 1.5rem;
        }}
        
        .testimonial-quote:before {{
            content: '"';
            font-size: 5rem;
            position: absolute;
            left: -1.5rem;
            top: -1.5rem;
            color: rgba(52, 152, 219, 0.2);
            font-family: serif;
        }}
        
        .testimonial-author {{
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 1.8rem;
            flex-wrap: wrap;
        }}
        
        .author-image-container {{
            margin: 0 1.5rem 1rem 1.5rem;
            min-width: 80px;
        }}
        
        .author-image {{
            width: 80px;
            height: 80px;
            border-radius: 15%;
            object-fit: cover;
            border: 4px solid var(--primary-color);
            transition: transform 0.3s ease;
            display: block;
            margin: 0 auto;
        }}
        
        .author-image:hover {{
            transform: scale(1.05);
        }}
        
        .author-info {{
            display: flex;
            flex-direction: column;
            text-align: center;
            padding: 0 1rem;
            min-width: 200px;
            margin: 0 auto;
        }}
        
        .author-name {{
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--secondary-color);
            margin-bottom: 0.2rem;
        }}
        
        .author-title {{
            font-size: 1rem;
            color: #7f8c8d;
            font-weight: 400;
        }}

        .section-divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, #3498db, transparent);
            margin: 3rem 0;
            border: none;
        }}
        
    .stats-container {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin: 3rem auto;
        max-width: 1200px;
        padding: 0 20px;
        width: 90%;
    }}
    
    .stat-item {{
        text-align: center;
        padding: 1.5rem;
        background: white;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 0;
    }}
        
        .stat-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}
        
        .stat-number {{
            font-size: 3rem;
            font-weight: 700;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            background: linear-gradient(90deg, #3498db, #e74c3c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .stat-label {{
            font-size: 1.1rem;
            color: var(--dark-color);
            font-weight: 500;
        }}

        /* Animation for testimonial cards */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .testimonial-card {{
            animation: fadeIn 0.8s ease-out;
        }}

        /* Alumni Cards Section */
        .alumni-cards-container {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin: 3rem auto;
            max-width: 1200px;
            padding: 0 20px;
        }}

        .alumni-card {{
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.15);
            padding: 2rem;
            text-align: center;
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            flex: 1 1 calc(33.333% - 20px);
            min-width: 300px;
            min-height: 250px;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            position: relative;
            overflow: hidden;
            color: white;
            box-sizing: border-box;
        }}

        .alumni-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }}

        .alumni-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.3) 50%);
            z-index: 1;
        }}

        .alumni-card h3, .alumni-card p {{
            position: relative;
            z-index: 2;
            color: white;
        }}

        .alumni-card h3 {{
            font-size: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 700;
        }}

        .alumni-card p {{
            font-size: 1rem;
            line-height: 1.5;
            margin-bottom: 0;
        }}

        /* Department Cards Section */
        .dept-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin: 2rem 0;
        }}
        
        .dept-card {{
            flex: 1 1 calc(33.333% - 20px);
            min-width: 300px;
            height: 250px;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
        }}
        
        .dept-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.3) 80%);
            z-index: 1;
            border-radius: 10px;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }}
        
        .dept-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        }}
        
        .dept-card:hover::before {{
            background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.4) 80%);
        }}
        
        .dept-content {{
            position: relative;
            z-index: 2;
            color: white;
             padding: 15px;
        background: linear-gradient(to top, rgba(0,0,0,0.6) 0%, rgba(0,0,0,0.3) 60%, transparent 80%);
        border-radius: 0 0 12px 12px;
        margin: -20px;
        margin-top: 20px;
        }}
        
        .dept-title {{
           font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 
        0 1px 3px rgba(0,0,0,0.8),
        0 2px 6px rgba(0,0,0,0.5);
        transition: all 0.3s ease;
        letter-spacing: 0.5px;
        line-height: 1.3;
        }}
        
        .dept-desc {{
             font-size: 0.95rem;
    line-height: 1.5;
    margin-bottom: 1.2rem;
    text-shadow: 
        0 2px 3px rgba(0,0,0,0.9),
        0 3px 6px rgba(0,0,0,0.7);
    opacity: 0.99;
    transition: all 0.3s ease;
    font-weight: 600;
    padding-right: 10px;
        }}
            
        .dept-card::before {{
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        to top, 
        rgba(0,0,0,0.7) 0%, 
        rgba(0,0,0,0.4) 50%
    );
    z-index: 1;
    border-radius: 10px;
    transition: all 0.3s ease;
    }}
        
    .dept-card:hover::before {{
    background: linear-gradient(
        to top, 
        rgba(0,0,0,0.8) 0%, 
        rgba(0,0,0,0.5) 50%
    );
    }}
        /* Hover state enhancements */
.dept-card:hover .dept-title {{
    transform: translateY(-3px);
    text-shadow: 
        0 2px 4px rgba(0,0,0,0.9),
        0 4px 8px rgba(0,0,0,0.6);
    }}

.dept-card:hover .dept-desc {{
    opacity: 1;
    text-shadow: 
        0 2px 3px rgba(0,0,0,0.10),
        0 3px 6px rgba(0,0,0,0.8);
    }}
            
        .dept-btn {{
            display: inline-block;
            padding: 8px 20px;
            background-color: #0d6efd;
            color: white !important;
            text-decoration: none;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            border: 2px solid rgba(255,255,255,0.2);
            text-align: center;
            width: fit-content;
            position: relative;
            overflow: hidden;
            z-index: 2;
        }}
        
        .dept-btn::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: all 0.5s ease;
            z-index: -1;
        }}
        
        .dept-btn:hover {{
            background-color: #0b5ed7;
            transform: translateY(-2px);
            box-shadow: 0 5px 12px rgba(0,0,0,0.3);
            border-color: rgba(255,255,255,0.3);
        }}
        
        .dept-btn:hover::before {{
            left: 100%;
        }}
        
        /* Responsive adjustments */
        @media (max-width: 992px) {{
            .dept-card {{
                flex: 1 1 calc(50% - 20px);
            }}
        }}
        
        @media (max-width: 768px) {{
            .dept-card {{
                flex: 1 1 100%;
            }}
        }}

        /* Specific background images for each alumni card */
        .alumni-cs-card {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/jpeg;base64,{get_image_base64(str(IMG_DIR / "cs_alumni_bg.jpg"))}');
            background-size: cover;
            background-position: center;
        }}
        .alumni-civil-card {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/jpeg;base64,{get_image_base64(str(IMG_DIR / "civil_alumni_bg.jpg"))}');
            background-size: cover;
            background-position: center;
        }}
        .alumni-mech-card {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/jpeg;base64,{get_image_base64(str(IMG_DIR / "mech_alumni_bg.jpg"))}');
            background-size: cover;
            background-position: center;
        }}
        .alumni-entc-card {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/jpeg;base64,{get_image_base64(str(IMG_DIR / "entc_alumni_bg.jpg"))}');
            background-size: cover;
            background-position: center;
        }}
        .alumni-electrical-card {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('data:image/jpeg;base64,{get_image_base64(str(IMG_DIR / "electrical_alumni_bg.jpg"))}');
            background-size: cover;
            background-position: center;
        }}

        /* Responsive adjustments */
        @media (max-width: 768px) {{
            .testimonial-slider-wrapper {{
                width: 90%;
                padding: 15px;
            }}
            
            .testimonial-card {{
                padding: 1.5rem;
            }}
            
            .testimonial-quote {{
                font-size: 1.1rem;
                padding: 0 1rem;
            }}
            
            .testimonial-author {{
                flex-direction: column;
            }}
            
            .author-image-container {{
                margin: 0 auto 1rem auto;
            }}
            
            .author-info {{
                text-align: center;
                padding: 0;
            }}
            
            .stats-container {{
                flex-direction: column;
                align-items: center;
            }}
            
            .stat-item {{
                width: 80%;
                max-width: 300px;
                margin-bottom: 1rem;
            }}

            .alumni-card {{
                flex: 1 1 100%;
                min-width: 100%;
            }}

            .dept-cards-container {{
                grid-template-columns: 1fr;
            }}
        }}

        /* Ensure proper spacing and image display */
        .stImage > img {{
            object-fit: cover !important;
            margin: 0 auto !important;
            display: block !important;
        }}
        
        /* Prevent content from touching edges */
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}
        
         @media (max-width: 768px) {{
        .stats-container {{
            grid-template-columns: 1fr 1fr;
            width: 95%;
        }}
        }}
    
    @media (max-width: 480px) {{
        .stats-container {{
            grid-template-columns: 1fr;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown('<div class="testimonial-header">Voices of Innovation</div>', unsafe_allow_html=True)
st.markdown('<div class="testimonial-subheader">Hear what our bright minds say about their engineering journey</div>', unsafe_allow_html=True)
    
# Testimonial data with corrected image paths for an Engineering College and LinkedIn links
testimonials = [
    {
        "quote": "The rigorous training and support I received during my engineering years played a vital role in shaping my problem-solving mindset. That foundation helped me reach where I am today.",
        "name": "Ramanand Mohare",
        "title": "Software Engineer, Apple",
        "image_path": str(IMG_DIR / "Ramanand_Mohare.jpeg"),
        "linkedin_url": "https://www.linkedin.com/in/ramanand-mohare-47ba091aa/"
    },
    {
        "quote": "My four years at NKOCET, as part of the first graduating batch, have been truly enriching. The dedicated faculty, strong academic and personal support, industry exposure, and well-rounded learning environment prepared me well for my career. With excellent facilities and placement opportunities, NKOCET has set a high standard of education that I will always cherish.",
        "name": "Mr.Arun Panigrahi",
        "title": "INDIAN ARMY,DESIGNATION:MAJOR",
        "image_path": str(IMG_DIR / "Mr.Arun Panigrahi.jpg"),
        "linkedin_url": " "
    },
    {
        "quote": "The strong foundation in mechanical engineering principles, combined with research exposure and industry-focused projects, honed both my technical and managerial capabilities. These experiences continue to guide my decisions every day at KSB.",
        "name": "Madhurima Neel",
        "title": "Assistant Manager KSB LTD, Pune",
        "image_path": str(IMG_DIR / "Madhurima Neel.jpg"),
        "linkedin_url": "https://www.linkedin.com/in/madhurima-neel-a37877ba/"
    },
    {
        "quote": "Engineering not only shaped my technical skills but also ignited my passion for sustainable energy solutions. Qualifying the MPSC (Civil) exam with 5th rank in Maharashtra — and 1st among women — has been a proud milestone in my journey.",
        "name": "Vaishanvi Gaikwad",
        "title": "Qualified Engg. MPSC( Civil) exam with 5th Rank in Maharashtra and 1st Rank from Women's Category in entire Maharashtra",
        "image_path": str(IMG_DIR / "Vaishanvi Gaikwad.jpg"),
        "linkedin_url": " "
    },
    {
        "quote": "Engineering gave me the discipline and clarity needed to pursue civil services with confidence. Securing 2nd rank in the MPSC (Civil) exam across Maharashtra is a testament to that journey.",
        "name": "Mr. Paris Gaikwad",
        "title": "Qualifying Engg. MPSC( Civil) exam with 2nd Rank in the entire Maharashtra",
        "image_path": str(IMG_DIR / "Mr. Paris Gaikwad.jpg"),
        "linkedin_url": " "
    },
    {
        "quote":"Being part of the first ENTC batch at NKOCET was a memorable journey. The faculty’s support and guidance equipped us with the tools to succeed, helping me build a career in the semiconductor field. It's been rewarding to see the department grow into one of the city's top engineering institutes.",
        "name": "Mr.Onkar Shinde",
        "title": "AMD, DESIGNATION:SILICON DESIGN ENGINEER",
        "image_path": str(IMG_DIR / "Mr.Onkar Shinde.jpg"),
        "linkedin_url": " "
    },
    {
        "quote":"As a first-generation student at NKOCET, I truly reinvented myself here. The college became my second home, where academics, sports, and extracurriculars thrived together. The dedicated mechanical branch staff went the extra mile, especially supporting backlog students like me, strengthening both practical and theoretical knowledge. NKOCET is a lighthouse, radiating knowledge and wisdom. I’m grateful for this incredible journey.",
        "name": "Mr. Paresh P Gavasane",
        "title": "RTO INSPECTOR: CLASS 1 OFFICEE",
        "image_path": str(IMG_DIR / "Mr. Paresh P Gavasane.jpg"),
        "linkedin_url": " "
    }

]
    
# Encode images to Base64
for testimonial in testimonials:
    testimonial["image_encoded"] = get_image_base64(testimonial['image_path'])
    
# Prepare testimonials data for JavaScript
testimonials_js = []
for t in testimonials:
    testimonials_js.append({
        "quote": t["quote"],
        "name": t["name"],
        "title": t["title"],
        "image": f"data:image/jpeg;base64,{t['image_encoded']}",
        "linkedin_url": t["linkedin_url"]
    })
    
# JavaScript for auto-sliding testimonials
js_code = f"""
<script>
    var testimonials = {testimonials_js};
    var currentIdx = 0;
    var testimonialContainer = parent.document.getElementById('testimonial-container');
    var dotElements = parent.document.querySelectorAll('.testimonial-dot');
    
    function updateTestimonial() {{
        if (testimonialContainer) {{
            currentIdx = (currentIdx + 1) % testimonials.length;
            var testimonial = testimonials[currentIdx];
            
            testimonialContainer.innerHTML = `
                <div class="testimonial-card">
                    <div class="testimonial-quote">${{testimonial.quote}}</div>
                    <div class="testimonial-author">
                        <div class="author-image-container">
                            <a href="${{testimonial.linkedin_url}}" target="_blank">
                                <img src="${{testimonial.image}}" class="author-image" alt="${{testimonial.name}}">
                            </a>
                        </div>
                        <div class="author-info">
                            <div class="author-name">${{testimonial.name}}</div>
                            <div class="author-title">${{testimonial.title}}</div>
                        </div>
                    </div>
                </div>
            `;
            
            // Update active dot (if dots were implemented)
            dotElements.forEach((dot, index) => {{
                dot.classList.toggle('active', index === currentIdx);
            }});
        }}
    }}
    
    // Initial display
    if (testimonialContainer && testimonials.length > 0) {{
        var initialTestimonial = testimonials[0];
        testimonialContainer.innerHTML = `
            <div class="testimonial-card">
                <div class="testimonial-quote">${{initialTestimonial.quote}}</div>
                <div class="testimonial-author">
                    <div class="author-image-container">
                        <a href="${{initialTestimonial.linkedin_url}}" target="_blank">
                            <img src="${{initialTestimonial.image}}" class="author-image" alt="${{initialTestimonial.name}}">
                        </a>
                    </div>
                    <div class="author-info">
                        <div class="author-name">${{initialTestimonial.name}}</div>
                        <div class="author-title">${{initialTestimonial.title}}</div>
                    </div>
                </div>
            </div>
        `;
    }}
    
    // Set interval for auto-sliding (every 3 seconds)
    if (testimonials.length > 1) {{
        setInterval(updateTestimonial, 3000);
    }}
</script>
"""
    
# Display the testimonial slider
with st.container():
    st.markdown("""
    <div class="testimonial-slider-wrapper">
        <div id="testimonial-container"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Inject JavaScript for auto-sliding
    st.components.v1.html(js_code, height=0, width=0)

# Stats Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: var(--secondary-color); margin-bottom: 2rem;">Our Engineering Impact in Numbers</h2>', unsafe_allow_html=True)
    
st.markdown('''
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">95%</div>
        <div class="stat-label">Placement Rate</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">10+</div>
        <div class="stat-label">Accredited Programs</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">500+</div>
        <div class="stat-label">Research Publications</div>
    </div>
</div>
''', unsafe_allow_html=True)
            
st.markdown("---")

# Engineering Departments Section
st.markdown('<h2 style="text-align: center; color: var(--secondary-color); margin-bottom: 1.5rem;">Explore Our Engineering Departments</h2>', unsafe_allow_html=True)

# Department cards data
departments = [
    {
        "name": "Computer Engineering",
        "description": "Cutting-edge curriculum in AI, ML, and software development with industry-aligned projects.",
        "image": "https://images.squarespace-cdn.com/content/v1/5fce63270356d927d7eecdbd/033e9988-2ac8-4cb9-8b9f-5bf05fb22dcb/gff.jpg",
        "url": "https://campuscoders.pixieset.com/computerscienceandengg/"
    },
    {
        "name": "Civil Engineering",
        "description": "Comprehensive program covering structural design, construction tech, and sustainable infrastructure.",
        "image": "https://pinnacleiit.com/wp-content/uploads/2024/09/XXL.webp",
        "url": "https://campuscoders.pixieset.com/civilengg/"
    },
    {
        "name": "Mechanical Engineering",
        "description": "Hands-on training in design, thermal systems, and advanced manufacturing technologies.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/2/2b/Mechanical_components.png",
        "url": "https://campuscoders.pixieset.com/mechanical/"
    },
    {
        "name": "ENTC Engineering",
        "description": "Focus on electronics, telecommunications, embedded systems, and signal processing.",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcHW46m8It2wf1v24m4YI7OynT9ooKfT7qaA&s",
        "url": "https://campuscoders.pixieset.com/electronicsandtelecommunication/"
    },
    {
        "name": "Electrical Engineering",
        "description": "Comprehensive training in power systems, control engineering, and renewable energy.",
        "image": "https://cache.careers360.mobi/media/article_images/2023/2/13/18-online-courses-for-electrical-engineering.jpg",
        "url": "https://campuscoders.pixieset.com/electrical/"
    }
]

# Display department cards in columns (3 per row)
st.markdown('<div class="dept-container">', unsafe_allow_html=True)

# Split departments into chunks of 3 for proper row layout
for i in range(0, len(departments), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(departments):
            dept = departments[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="dept-card" style="background-image: url('{dept["image"]}')">
                    <div class="dept-content">
                        <h3 class="dept-title">{dept["name"]}</h3>
                        <p class="dept-desc">{dept["description"]}</p>
                        <a href="{dept["url"]}" target="_blank" class="dept-btn">Explore Department Aluminis</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("---")
footer()