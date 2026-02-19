import streamlit as st
from utils.prompt_builder import build_logo_prompt
from utils.api_client import generate_logo
import base64
import json
import os
from datetime import datetime
from io import BytesIO

st.set_page_config(
    page_title="AI Logo Generator",
    page_icon="🎨",
    layout="wide"
)
# -------------- NAVIGATION BAR (TOP LINKS) --------------
st.markdown("""
    <style>
    .topnav {
        background-color: white;
        overflow: hidden;
        padding: 10px 30px;
        border-radius: 12px;
        margin-top: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .topnav .logo {
        font-weight: 800;
        font-size: 20px;
        color: #4f46e5;
    }

    .topnav a {
        float: left;
        color: #1f2937;
        text-align: center;
        padding: 8px 14px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 600;
    }

    .topnav a:hover {
        color: #7c3aed;
    }
    </style>

    <div class="topnav">
        <div class="logo">AI Logo Generator</div>
        <div>
            <a href="#">Services</a>
            <a href="#">Products</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
            <a href="#">Careers</a>
            <a href="#">Newsroom</a>
            <a href="#">🔍</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = 1
if "generated_images" not in st.session_state:
    st.session_state.generated_images = None
if "selected_logo" not in st.session_state:
    st.session_state.selected_logo = None

# ---------------- HELPER ----------------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ---------------- LOAD IMAGES ----------------
hero_bg = get_base64("assets/hero_bg.png")
bg_page2 = get_base64("assets/bg_page2.png")
bg_page3 = get_base64("assets/bg_page3.png")
bg_page4 = get_base64("assets/bg_page4.png")
bg_page5 = get_base64("assets/bg_page5.png")

# ---------------- PAGE BACKGROUND LOGIC ----------------
page_backgrounds = {
    1: hero_bg,
    2: bg_page2,
    3: bg_page3,
    4: bg_page4,
    5: bg_page5,
}
current_page = st.session_state.page
active_bg = page_backgrounds.get(current_page, hero_bg)

# ---------------- GLOBAL STYLING ----------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(
        rgba(255,255,255,0.10),
        rgba(255,255,255,0.10)
    ),
    url("data:image/png;base64,{active_bg}");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}}

.main-container {{
    background: rgba(255,255,255,0.97);
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    margin-top: 20px;
    text-align: center;
}}

h1, h2, h3 {{
    color: #111827 !important;
    font-weight: 800 !important;
}}

p, label, span {{
    color: #374151 !important;
    font-weight: 500;
}}

.stButton > button {{
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border-radius: 14px;
    font-weight: 600;
    padding: 0.7rem 1.6rem;
    border: none;
}}

.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}}

input, textarea, select {{
    border-radius: 12px !important;
    background: white !important;
}}

.chatbot {{
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border-radius: 50%;
    width: 65px;
    height: 65px;
    text-align: center;
    line-height: 65px;
    font-size: 28px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}}
</style>
""", unsafe_allow_html=True)

# ---------------- STEP HEADER ----------------
steps = ["Home", "Business Type", "Company Info", "Preferences", "Generate"]
path = " > ".join(steps[:current_page])

st.markdown(f"### Step {current_page} / 5")
st.markdown(f"**{path}**")
st.progress(current_page / 5)

# ---------------- UNIFIED WHITE HEADER CARD ----------------
st.markdown("""
<div style="
    background: #fdeff2;
    border-radius:12px;
    padding:10px 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    margin-top:10px;
    margin-bottom:15px;
    text-align:center;
    font-weight:600;
    color:#1f2937;
">
🚀 You Imagine, We Create.<br>
<span style="
    font-size:18px;
    letter-spacing:3px;
    font-weight:800;
    background: linear-gradient(90deg,#7c3aed,#2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
">POKAK TECHNOLOGIES</span><br>
<span style="
    display:block;
    margin-top:10px;
    font-size:15px;
    font-weight:600;
    color:#7c3aed;
">
ADARSH K K - AI_INTERN_LOGO_CREATION_WEBSITE
</span>
</div>
""", unsafe_allow_html=True)

# ---------------- PAGE NAVIGATION ----------------
def next_page():
    if st.session_state.page < 5:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# ---------------- MAIN CONTENT CONTAINER ----------------
#st.markdown('<div class="main-container">', unsafe_allow_html=True)

# ---------------- PAGE 1 ----------------
if current_page == 1:
    st.title("Create Your Brand Identity")
    st.write("Professional AI-powered logos built in minutes.")
    st.button("Start Building Logos", on_click=next_page)

    st.divider()
    st.subheader("Frequently Asked Questions")

    with st.expander("How does the AI generate logos?"):
        st.write("Structured inputs → prompt → AI image generation.")
    with st.expander("Can I download high-quality files?"):
        st.write("Yes. Instant download supported.")
    with st.expander("Will my data be stored?"):
        st.write("Feedback is stored for model improvement.")

# ---------------- PAGE 2 ----------------
elif current_page == 2:
    st.title("Select Business Type")
    st.session_state.business_type = st.radio(
        "Choose category:",
        ["Services", "Physical Goods", "Tech / Software", "Creator"]
    )
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)

# ---------------- PAGE 3 ----------------
elif current_page == 3:
    st.title("Company Details")
    st.session_state.industry = st.text_input("Industry")
    st.session_state.company_name = st.text_input("Company Name")
    st.session_state.tagline = st.text_input("Tagline")
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)


# ---------------- PAGE 4 ----------------
elif current_page == 4:
    st.title("Brand Preferences")
    st.session_state.style = st.selectbox(
        "Brand Style", ["Modern", "Minimal", "Futuristic", "Friendly", "Professional"]
    )
    st.session_state.colors = st.text_input("Preferred Colors")
    st.session_state.font = st.selectbox(
        "Font Type", ["Sans-serif", "Serif", "Bold", "Handwritten"]
    )
    st.session_state.icon = st.text_input("Icon Preference")
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)



# ---------------- PAGE 5 ----------------
elif current_page == 5:
    st.title("Generate Logo")

    if st.button("Generate Logos"):
        data = {
            "business_type": st.session_state.get("business_type"),
            "industry": st.session_state.get("industry"),
            "company_name": st.session_state.get("company_name"),
            "tagline": st.session_state.get("tagline"),
            "style": st.session_state.get("style"),
            "colors": st.session_state.get("colors"),
            "font": st.session_state.get("font"),
            "icon": st.session_state.get("icon"),
        }

        prompt = build_logo_prompt(data)

        with st.spinner("Generating logos..."):
            st.session_state.generated_images = [
                generate_logo(prompt) for _ in range(1)
            ]

    if st.session_state.generated_images:
        cols = st.columns(2)

        for i, img in enumerate(st.session_state.generated_images):
            with cols[i % 2]:
                if img is not None:
                    st.image(img, width=350)
                else:
                    st.error("Image generation failed.")
                if st.button(f"Rate Logo {i+1} / Provide Feedback", key=f"rate_{i}"):
                    st.session_state.selected_logo = i
                    st.session_state[f"show_hint_{i}"] = True
                else:
                    st.session_state[f"show_hint_{i}"] = False

                if st.session_state.get(f"show_hint_{i}"):
                    st.markdown("""
                    <div style='
                        background-color: rgba(0, 0, 0, 0.65);
                        color: #fff;
                        padding: 10px 16px;
                        border-radius: 8px;
                        margin-top: 10px;
                        font-size: 15px;
                        text-align: center;
                    '>
                    ⬇️ Please scroll down to rate and share feedback. It helps us improve!
                    </div>
                    """, unsafe_allow_html=True)

                if img is not None:
                    buffer = BytesIO()
                    img.save(buffer, format="PNG")
                    buffer.seek(0)
                    st.download_button(
                        label=f"Download Logo {i+1}",
                        data=buffer,
                        file_name=f"logo_{i+1}.png",
                        mime="image/png",
                        key=f"download_{i}"
                    )
                    
                

    # ✅ Feedback Section: Only if a logo was selected
    if st.session_state.selected_logo is not None:
        st.divider()
        st.subheader("Rate Selected Logo")

        rating = st.slider("⭐ Rating", 1, 5, 3)
        feedback = st.text_area("Optional Feedback")

        if st.button("Submit Feedback"):
            feedback_data = {
                "timestamp": str(datetime.now()),
                "industry": st.session_state.get("industry"),
                "style": st.session_state.get("style"),
                "rating": rating,
                "feedback": feedback
            }

            os.makedirs("data", exist_ok=True)
            file_path = "data/feedback.json"

            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            existing.append(feedback_data)

            with open(file_path, "w") as f:
                json.dump(existing, f, indent=4)

            st.toast("✅ Thank you for your feedback!")
            st.success("Feedback saved.")

    st.button("Back", on_click=prev_page)





