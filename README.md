# 🎨 ai-logo-generator-v3

An AI-powered multi-step logo generation web application built using Streamlit and Stability AI REST API.

This version integrates real AI-based image generation using Stability AI's official API (SDXL model).

---

## 🚀 Live Demo

Try the app here:

https://ai-logo-generator-v3-nu22cbjyc6gafiyfjhdofu.streamlit.app/

---##

## 🧠 Project Overview

This application allows users to:

- Select business type
- Enter company details
- Define brand preferences
- Generate AI-based logos
- Download generated logos
- Rate and submit feedback

The app uses Stability AI’s image generation API to create high-resolution logo designs based on structured prompts.

---

## 🏗 Architecture Overview

User Input (Streamlit UI)
        ↓
Prompt Builder (Structured Prompt Construction)
        ↓
Stability AI REST API (SDXL Model)
        ↓
Image Processing (Pillow)
        ↓
Display + Download
        ↓
Feedback Stored in JSON

---

## 🛠 Tech Stack

- Python 3.11+
- Streamlit
- Stability AI REST API
- Requests (HTTP communication)
- Pillow (Image handling)
- JSON (Feedback storage)

---

## 📂 Project Structure

```
ai-logo-generator-v3/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│
├── utils/
│   ├── api_client.py
│   └── prompt_builder.py
│
└── data/   (ignored in production)
```

---

## 🔐 API Integration

This project uses Stability AI REST API (SDXL model).

Authentication is handled securely using Streamlit Secrets:

`.streamlit/secrets.toml` (local only, not pushed to GitHub)

Example:

```
STABILITY_API_KEY = "your_api_key_here"
```

In production (Streamlit Cloud), the same key must be added under:

App Settings → Secrets

---

## ⚙ How to Run Locally

1. Clone the repository
2. Create virtual environment
3. Install dependencies:

```
pip install -r requirements.txt
```

4. Add your Stability API key in:

```
.streamlit/secrets.toml
```

5. Run:

```
streamlit run app.py
```

---

## 🧾 Feedback System

User ratings and feedback are stored locally in:

```
data/feedback.json
```

This folder is ignored in Git to prevent pushing runtime data.

For production-scale systems, this should be replaced with a proper database (PostgreSQL, MongoDB, etc.).

---

## 📦 Deployment

The application is deployed using Streamlit Cloud.

Deployment Steps:

- Push code to GitHub
- Connect repository to Streamlit Cloud
- Add Stability API key in Secrets section
- Deploy

---

## ⚠ Security Notes

- API keys are never stored in the code.
- `.streamlit/secrets.toml` is excluded via `.gitignore`.
- Sensitive credentials are handled via environment-based configuration.

---

## 📌 Future Improvements

- Replace JSON feedback storage with database
- Add usage tracking
- Add rate limiting
- Add authentication system
- Improve error handling
- Add async request handling

---

## 👨‍💻 Author

Adarsh K K  
AI Intern – AI Logo Generation System  
Built as part of production-ready AI integration learning.

---

## 🧠 Engineering Focus of This Version

- Clean API abstraction
- Modular prompt builder
- Separation of concerns
- Production-safe secrets management
- Deployment-ready structure

---

> "Systems become powerful when structure replaces chaos."


