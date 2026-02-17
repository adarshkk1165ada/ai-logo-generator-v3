import streamlit as st
from utils.prompt_builder import build_logo_prompt
from utils.api_client import generate_logo
import base64
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="AI Logo Generator",
    page_icon="🎨",
    layout="wide"
)

# ---------- Helper ----------
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

hero_base64 = get_base64("assets/hero_bg.png")

# ---------- Styling ----------
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-color: #f4f6f9;
    font-family: 'Segoe UI', sans-serif;
}}

.navbar {{
    display: flex;
    justify-content: space-between;
    padding: 20px 40px;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}}

.nav-links span {{
    margin-right: 25px;
    font-weight: 500;
    cursor: pointer;
}}

.nav-links span:hover {{
    color: #2563eb;
}}

.hero {{
    height: 450px;
    background-image: url("data:image/png;base64,{hero_base64}");
    background-size: cover;
    background-position: center;
    border-radius: 16px;
    position: relative;
    margin-bottom: 40px;
}}

.hero-overlay {{
    position: absolute;
    top:0;
    left:0;
    right:0;
    bottom:0;
    background: rgba(0,0,0,0.45);
    border-radius: 16px;
}}

.hero-content {{
    position: absolute;
    top:50%;
    left:50%;
    transform: translate(-50%, -50%);
    color: white;
    text-align: center;
}}

.hero-content h1 {{
    font-size: 48px;
    font-weight: 700;
}}

.stButton > button {{
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    font-weight: 600;
}}

.stButton > button:hover {{
    background-color: #1e40af;
}}

input, textarea, select {{
    border: 2px solid #cbd5e1 !important;
    border-radius: 8px !important;
}}

/* Floating chatbot */
.chatbot {{
    position: fixed;
    bottom: 30px;
    right: 30px;
    background: #2563eb;
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    text-align: center;
    line-height: 60px;
    font-size: 26px;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}}
</style>
""", unsafe_allow_html=True)

# ---------- Navbar ----------
st.markdown("""
<div class="navbar">
    <div><strong>AI Logo Generator</strong></div>
    <div class="nav-links">
        <span>Services</span>
        <span>Products</span>
        <span>About</span>
        <span>Contact</span>
        <span>Login</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Session ----------
if "page" not in st.session_state:
    st.session_state.page = 1
if "generated_images" not in st.session_state:
    st.session_state.generated_images = None
if "selected_logo" not in st.session_state:
    st.session_state.selected_logo = None

def next_page():
    if st.session_state.page < 5:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# ---------- Progress + Breadcrumb ----------
steps = ["Home", "Business Type", "Company Info", "Preferences", "Generate"]
current_step = st.session_state.page
path = " > ".join(steps[:current_step])

st.markdown(f"### Step {current_step} of 5")
st.progress(current_step / 5)
st.markdown(f"**Path:** {path}")
st.divider()

# ---------- PAGE 1 ----------
if current_step == 1:

    st.markdown("""
    <div class="hero">
        <div class="hero-overlay"></div>
        <div class="hero-content">
            <h1>Create Your Brand Identity</h1>
            <p>Professional AI-powered logos built in minutes.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.button("Start Building Logos", on_click=next_page)

    st.divider()
    st.subheader("Frequently Asked Questions")

    with st.expander("How does the AI generate logos?"):
        st.write("It converts structured inputs into prompts and generates variations.")

    with st.expander("Can I download high-quality files?"):
        st.write("Yes. Logos are downloadable instantly.")

    with st.expander("Will my data be stored?"):
        st.write("Feedback is stored to improve future personalization.")

# ---------- PAGE 2 ----------
elif current_step == 2:
    st.title("Select Business Type")

    st.session_state.business_type = st.radio(
        "Choose category:",
        ["Services", "Physical Goods", "Tech / Software", "Creator"]
    )

    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)

# ---------- PAGE 3 ----------
elif current_step == 3:
    st.title("Company Details")

    st.session_state.industry = st.text_input("Industry")
    st.session_state.company_name = st.text_input("Company Name")
    st.session_state.tagline = st.text_input("Tagline")

    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)

# ---------- PAGE 4 ----------
elif current_step == 4:
    st.title("Brand Preferences")

    st.session_state.style = st.selectbox(
        "Brand Style",
        ["Modern", "Minimal", "Futuristic", "Friendly", "Professional"]
    )

    st.session_state.colors = st.text_input("Preferred Colors")
    st.session_state.font = st.selectbox(
        "Font Type",
        ["Sans-serif", "Serif", "Bold", "Handwritten"]
    )
    st.session_state.icon = st.text_input("Icon Preference")

    col1, col2 = st.columns(2)
    col1.button("Back", on_click=prev_page)
    col2.button("Next", on_click=next_page)

# ---------- PAGE 5 ----------
elif current_step == 5:
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
                generate_logo(prompt) for _ in range(4)
            ]

    if st.session_state.generated_images:

        cols = st.columns(2)

        for i, img in enumerate(st.session_state.generated_images):
            with cols[i % 2]:
                st.image(img, width=350)

                if st.button(f"Select Logo {i+1}", key=f"select_{i}"):
                    st.session_state.selected_logo = i

                st.download_button(
                    label=f"Download Logo {i+1}",
                    data=img,
                    file_name=f"logo_{i+1}.png",
                    mime="image/png",
                    key=f"download_{i}"
                )

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
                st.success("Feedback saved for future model improvement.")

    st.button("Back", on_click=prev_page)

# ---------- Floating Chatbot ----------
st.markdown('<div class="chatbot">💬</div>', unsafe_allow_html=True)





