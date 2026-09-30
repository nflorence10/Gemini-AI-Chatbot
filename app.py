# mini chatbot - PY

import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# ---------- Gemini Setup ----------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="✦",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>

    /* ---------- Google Fonts ---------- */
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* ---------- Main Page ---------- */
    .stApp {
        background: #101114;
        color: #e8e9ed;
        font-family: 'DM Sans', sans-serif;
    }

    /* Remove Streamlit top bar */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    /* Main content width */
    .block-container {
        max-width: 760px;
        padding-top: 4rem;
        padding-bottom: 4rem;
    }

    /* ---------- Title ---------- */
    h1 {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 2.7rem !important;
        font-weight: 600 !important;
        color: #f4f4f5 !important;
        text-align: center;
        letter-spacing: -1.5px;
        margin-bottom: 0.3rem !important;
    }

    /* Small accent above title */
    .top-label {
        text-align: center;
        color: #7c9cff;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #858892;
        font-size: 1rem;
        margin-bottom: 2.5rem;
    }

    /* ---------- Input Label ---------- */
    .stTextArea label p {
        color: #d7d8dd !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
    }

    /* ---------- Text Area ---------- */
    .stTextArea textarea {
        background: #18191d !important;
        color: #eeeeef !important;
        border: 1px solid #2a2c32 !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.98rem !important;
        min-height: 150px !important;
        resize: vertical !important;
        transition: border 0.2s ease, box-shadow 0.2s ease;
    }

    .stTextArea textarea::placeholder {
        color: #60636c !important;
    }

    .stTextArea textarea:focus {
        border-color: #617edc !important;
        box-shadow: 0 0 0 1px #617edc !important;
    }

    /* ---------- Generate Button ---------- */
    .stButton {
        margin-top: 0.8rem;
    }

    .stButton > button {
        width: 100% !important;
        height: 48px !important;

        background: #f1f3f8 !important;
        color: #111216 !important;

        border: none !important;
        border-radius: 10px !important;

        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;

        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background: #ffffff !important;
        color: #111216 !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    .stButton > button:focus {
        box-shadow: none !important;
    }

    /* ---------- Success / Warning ---------- */
    [data-testid="stAlert"] {
        background: #18191d !important;
        border: 1px solid #2a2c32 !important;
        border-radius: 10px !important;
        color: #dfe0e5 !important;
    }

    /* ---------- Response Box ---------- */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #18191d !important;
        border: 1px solid #2a2c32 !important;
        border-radius: 14px !important;
        padding: 1.4rem !important;
        margin-top: 0.5rem;
    }

    /* Response text */
    [data-testid="stVerticalBlockBorderWrapper"] p,
    [data-testid="stVerticalBlockBorderWrapper"] li {
        color: #dedfe4 !important;
        line-height: 1.7;
    }

    /* Code inside response */
    [data-testid="stVerticalBlockBorderWrapper"] code {
        background: #24262c !important;
        color: #a9bcff !important;
        border-radius: 5px;
        padding: 0.15rem 0.35rem;
    }

    /* ---------- Spinner ---------- */
    [data-testid="stSpinner"] p {
        color: #858892 !important;
    }

    /* ---------- Mobile ---------- */
    @media (max-width: 600px) {

        .block-container {
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        h1 {
            font-size: 2.1rem !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- UI ----------

st.markdown(
    '<div class="top-label">GEMINI · AI ASSISTANT</div>',
    unsafe_allow_html=True
)

st.title("Gemini AI Chatbot")

st.markdown(
    '<div class="subtitle">Ask a question. Get a clear answer.</div>',
    unsafe_allow_html=True
)

prompt = st.text_area(
    "Your prompt",
    placeholder="e.g. Explain artificial intelligence in simple terms...",
    height=150
)

if st.button("Generate Response"):

    if prompt.strip():

        with st.spinner("Generating response..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("Response generated")

        with st.container(border=True):
            st.markdown(response.text)

    else:
        st.warning("Please enter a prompt.")

