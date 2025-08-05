import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Kreo Tech AI Assistant", page_icon="🎮", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to bottom right, #0e0e0e, #1a1a1a);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput > div > div > input,
    .stChatInputContainer textarea {
        background-color: #1f1f1f;
        color: white;
        border: 1px solid #444;
        border-radius: 10px;
    }
    .stButton > button {
        background-color: #ff004f;
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #ff004f;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🎮 Kreo Tech – Pro Gamer Assistant")
st.markdown("### Get expert guidance on gaming gear, performance setups, and support")

# Secure API key from secrets
if "gemini" in st.secrets and "api_key" in st.secrets["gemini"]:
    api_key = st.secrets["gemini"]["api_key"]
    genai.configure(api_key=api_key)
else:
    st.error("❌ Gemini API key not found in secrets.")
    st.stop()

# Initialize model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction="""
    You are the Kreo Tech AI Assistant, an expert in professional gaming peripherals.
    
    You help with:
    🎮 Product Info:
    - Kreo Phantom Mouse – ₹6,499: Ultra-light, 20K DPI, RGB, wireless
    - Kreo Mecha Keyboard – ₹10,499: Hot-swappable switches, PBT keycaps, per-key RGB
    - Kreo Viper Monitor – ₹27,999: 27", 240Hz, 1ms IPS, G-Sync compatible
    - Kreo Spectra Headset – ₹7,999: Spatial audio, noise-canceling mic, breathable cushions
    - Kreo Apex Chair – ₹15,999: Lumbar foam, 4D armrests, ergonomic design

    ⚙️ Setup Optimization:
    FPS improvement, low latency tips, monitor tuning, cable management, lighting, ergonomics

    📦 Support:
    30-day returns, 1-year warranty, orders, shipping (3–5 days), support@kreotech.in

    🕹️ Compatibility:
    Recommend gear based on games (FPS, MOBA, sim), hand size, desk space, and budget.

    Be helpful, professional, and tailored to gamers who value performance and aesthetics.
    """
)

# Session state chat setup
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()

# Replay previous messages with proper avatars
for msg in st.session_state.chat.history:
    role = msg.role
    avatar = "🧑‍💻" if role == "user" else "🎮"
    with st.chat_message(role, avatar=avatar):
        st.markdown(msg.parts[0].text)

# Chat input
user_input = st.chat_input("Ask about gear, setups, or support")

if user_input:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_input)
    
    try:
        response = st.session_state.chat.send_message(user_input)
        with st.chat_message("ai", avatar="🎮"):
            st.markdown(response.text)
    except Exception as e:
        st.error("⚠️ Assistant is currently unavailable. You may have hit API limits or encountered a server issue.")
