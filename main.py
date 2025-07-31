import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Kreo Tech AI Assistant", page_icon="🎮", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #0e0e0e;
        color: white;
    }
    .stApp {
        background: linear-gradient(to bottom right, #121212, #1c1c1c);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput > div > div > input {
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #444;
        border-radius: 10px;
        padding: 8px;
    }
    .stButton > button {
        background-color: #ff004f;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
        font-size: 16px;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ff004f;
    }
    .stChatInputContainer textarea {
        background-color: #1f1f1f;
        color: white;
        border-radius: 10px;
        border: 1px solid #444;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("# 🎮 Kreo Tech – Pro Gamer Assistant")
st.markdown("### Get elite advice on gaming gear and setups")

api_key = st.text_input("Gemini API key", type="password", label_visibility="collapsed", placeholder="Enter Gemini API Key")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="models/gemini-1.5-flash",
        system_instruction="""
        You are the Kreo Tech AI Assistant, an expert on high-end gaming gear designed for professional gamers and streamers. Your job is to assist users with:

        - Product Information: You know Kreo Tech's entire product catalog, including:
          • Kreo Phantom Mouse – $79.99: ultra-lightweight, 20K DPI sensor, customizable RGB, lag-free wireless.
          • Kreo Mecha Keyboard – $129.99: hot-swappable switches, PBT double-shot keycaps, per-key RGB.
          • Kreo Viper Monitor – $349.99: 27", 240Hz, 1ms IPS panel, G-Sync compatible.
          • Kreo Spectra Headset – $99.99: spatial audio, noise-canceling mic, breathable ear cushions.
          • Kreo Apex Chair – $199.99: ergonomic support, lumbar foam, 4D armrests, stain-resistant fabric.

        - Customer Support: Handle questions about orders, returns (30-day window), warranty (1-year standard), shipping times (3–5 business days), and support contact (support@kreotech.gg).

        - Gaming Setup Optimization: Provide advice on improving gaming performance, latency reduction, FPS boosts, monitor settings, ergonomics, cable management, lighting, and peripherals.

        - Compatibility & Recommendations: Help users pick gear for specific games (FPS, MOBA, racing, etc.), hand sizes, playstyles, desk setups, or budget levels.

        Respond with professionalism and clarity, tailored to gamers who want elite-tier performance, aesthetics, and value.
        """
    )
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat()

    for msg in st.session_state.chat.history:
        with st.chat_message(msg.role):
            st.markdown(msg.parts[0].text)

    user_input = st.chat_input("Ask about gear, performance, or setup tips")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        response = st.session_state.chat.send_message(user_input)
        with st.chat_message("ai"):
            st.markdown(response.text)
else:
    st.warning("Please provide a Gemini API key to continue.")
