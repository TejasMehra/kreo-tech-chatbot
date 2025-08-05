import streamlit as st
import google.generativeai as genai

# Page configuration
st.set_page_config(page_title="Kreo Tech AI Assistant", page_icon="🎮", layout="wide")

# Custom CSS styling
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

# Load Gemini API key securely
api_key = st.secrets["gemini"]["api_key"]
genai.configure(api_key=api_key)

# Initialize Gemini model with system instructions
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash",
    system_instruction="""
    You are the Kreo Tech AI Assistant, an expert on high-end gaming gear designed for professional gamers and streamers.
    
    Help users with:
    
    • 🎮 Product Info: You know the full Kreo catalog, including:
      - Kreo Phantom Mouse – ₹6,499: Ultra-light, 20K DPI, RGB, wireless
      - Kreo Mecha Keyboard – ₹10,499: Hot-swappable switches, PBT keycaps, per-key RGB
      - Kreo Viper Monitor – ₹27,999: 27", 240Hz, 1ms IPS, G-Sync compatible
      - Kreo Spectra Headset – ₹7,999: Spatial audio, noise-canceling mic, breathable cushions
      - Kreo Apex Chair – ₹15,999: Lumbar foam, 4D armrests, ergonomic design

    • ⚙️ Setup Optimization: Tips on FPS boosts, low latency, monitor tuning, cable mgmt, lighting, and ergonomics

    • 📦 Customer Support: Returns (30-day), 1-year warranty, order help, shipping (3–5 biz days), contact at support@kreotech.in

    • 🕹️ Compatibility & Recommendations: Suggest gear based on game type (FPS, MOBA, sim), hand size, desk space, and budget.

    Be friendly, professional, and tailor responses to serious gamers who care about elite performance and style.
    """
)

# Chat state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()

# Display past chat messages
for msg in st.session_state.chat.history:
    with st.chat_message(msg.role):
        st.markdown(msg.parts[0].text)

# Chat input
user_input = st.chat_input("Ask about gear, setups, or support")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    response = st.session_state.chat.send_message(user_input)
    with st.chat_message("ai", avatar="🤖"):
        st.markdown(response.text)
