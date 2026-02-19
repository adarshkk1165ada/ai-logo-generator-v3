import requests
import streamlit as st
from io import BytesIO
from PIL import Image

API_URL = "https://api.stability.ai/v2beta/stable-image/generate/core"

def generate_logo(prompt):
    headers = {
        "Authorization": f"Bearer {st.secrets['STABILITY_API_KEY']}",
        "Accept": "image/*"
    }

    files = {
        "prompt": (None, prompt),
        "output_format": (None, "png")
    }

    response = requests.post(API_URL, headers=headers, files=files)

    if response.status_code != 200:
        print("Generation failed:", response.text)
        return None

    return Image.open(BytesIO(response.content))




    


