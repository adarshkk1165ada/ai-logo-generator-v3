import streamlit as st
from utils.prompt_builder import build_logo_prompt
from utils.api_client import generate_logo

st.set_page_config(
    page_title="AI Logo Generator",
    page_icon="🎨",
    layout="centered"
)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1


# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.title("🎨 AI Logo Generator for Startups & Freelancers")
    st.markdown("Generate professional AI-powered logos using structured inputs.")
    st.divider()

    st.button("Start", on_click=next_page)


# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.title("Select Business Type")
    st.divider()

    business_type = st.radio(
        "Choose your category:",
        ["Services", "Physical Goods", "Tech / Software", "Creator"]
    )

    st.session_state.business_type = business_type

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_page)

    with col2:
        st.button("Next", on_click=next_page)


# ---------- PAGE 3 ----------
elif st.session_state.page == 3:
    st.title("Industry & Company Details")
    st.divider()

    industry = st.text_input("Industry")
    company_name = st.text_input("Company Name")
    tagline = st.text_input("Tagline")

    st.session_state.industry = industry
    st.session_state.company_name = company_name
    st.session_state.tagline = tagline

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_page)

    with col2:
        st.button("Next", on_click=next_page)


# ---------- PAGE 4 ----------
elif st.session_state.page == 4:
    st.title("Brand Preferences")
    st.divider()

    style = st.selectbox(
        "Brand Style",
        ["Modern", "Minimal", "Futuristic", "Friendly", "Professional"]
    )

    colors = st.text_input("Preferred Colors (e.g., blue and black)")

    font = st.selectbox(
        "Font Type",
        ["Sans-serif", "Serif", "Bold", "Handwritten"]
    )

    icon = st.text_input("Icon Preference (e.g., drone, leaf, abstract shape)")

    st.session_state.style = style
    st.session_state.colors = colors
    st.session_state.font = font
    st.session_state.icon = icon

    col1, col2 = st.columns(2)

    with col1:
        st.button("Back", on_click=prev_page)

    with col2:
        st.button("Next", on_click=next_page)


# ---------- PAGE 5 ----------
elif st.session_state.page == 5:
    st.title("Generate Logo")
    st.divider()

    st.markdown("### Review Your Inputs")

    st.write("**Business Type:**", st.session_state.get("business_type", ""))
    st.write("**Industry:**", st.session_state.get("industry", ""))
    st.write("**Company Name:**", st.session_state.get("company_name", ""))
    st.write("**Tagline:**", st.session_state.get("tagline", ""))
    st.write("**Style:**", st.session_state.get("style", ""))
    st.write("**Colors:**", st.session_state.get("colors", ""))
    st.write("**Font:**", st.session_state.get("font", ""))
    st.write("**Icon:**", st.session_state.get("icon", ""))

    st.divider()

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

        st.subheader("Generating Logo...")

        try:
            with st.spinner("Calling HuggingFace API..."):
                image_bytes = generate_logo(prompt)

            st.image(image_bytes, width=400)

            st.download_button(
                label="Download Logo",
                data=image_bytes,
                file_name="logo.png",
                mime="image/png",
            )

        except Exception as e:
            st.error(f"API Error: {e}")

    st.button("Back", on_click=prev_page)
