from PIL import Image, ImageDraw
import io
import random


def generate_logo(prompt: str):
    """
    Mock logo generator (offline, unlimited, safe).
    """

    colors = ["#ffffff", "#f0f4f8", "#e8f0ff", "#f9f9f9"]
    bg_color = random.choice(colors)

    img = Image.new("RGB", (1024, 1024), color=bg_color)
    draw = ImageDraw.Draw(img)

    text = "AI LOGO"
    draw.text((380, 480), text, fill="black")

    byte_arr = io.BytesIO()
    img.save(byte_arr, format="PNG")

    return byte_arr.getvalue()


