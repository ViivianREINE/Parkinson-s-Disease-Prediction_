import streamlit as st
import pickle
import numpy as np
import base64
import os

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Parkinson's Disease Prediction",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------- MODEL PATHS ----------------------
MODEL_PATH = r"D:\ML Projects\svm_model.pkl"
SCALER_PATH = r"D:\ML Projects\scaler.pkl"
BACKGROUND_PATH = r"D:\ML Projects\fall_bg.jpg"

# ---------------------- LOAD MODEL ----------------------
@st.cache_resource
def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(SCALER_PATH, "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# ---------------------- BACKGROUND IMAGE ----------------------
def add_bg_from_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Background image not found, using plain background.")

add_bg_from_local(BACKGROUND_PATH)

# ---------------------- CUSTOM THEME COLORS ----------------------
st.markdown("""
    <style>
    .main {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        padding: 20px;
    }
    .stButton>button {
        background-color: #8B5E3C; 
        color: white;
        border-radius: 12px;
        font-size: 16px;
        padding: 8px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #A9745C;
        color: #fff;
    }
    .title {
        text-align: center;
        font-size: 38px;
        color: #4E342E; 
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #6D4C41; 
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #4E342E;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<h1 class='title'>🧠 Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-powered diagnostic tool with clinical voice features</p>", unsafe_allow_html=True)

# ---------------------- FEATURES ----------------------
FEATURES = [
    "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)",
    "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP",
    "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer",
    "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5",
    "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
    "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
]

# Realistic default values (from dataset averages)
default_values = [
    119.992, 157.302, 74.997, 0.005, 0.00003, 0.003, 0.004, 0.0002, 0.02,
    0.1, 0.01, 0.02, 0.01, 0.02, 0.02, 21.0, 0.5, 0.7, -5.0, 0.2, 2.0, 0.1,]

st.sidebar.header("📊 Input Voice Features")
if os.path.exists(BACKGROUND_PATH):
    st.sidebar.image(BACKGROUND_PATH, use_container_width=True)

inputs = []
cols = st.sidebar.columns(2)
for i, feat in enumerate(FEATURES):
    with cols[i % 2]:
        val = st.number_input(feat, value=default_values[i], step=0.01, format="%.5f")
        inputs.append(val)

x = np.array(inputs).reshape(1, -1)

# ---------------------- PREDICTION ----------------------
if st.sidebar.button("🔮 Predict Parkinson's"):
    if x.shape[1] != scaler.scale_.shape[0]:
        st.error("Input size does not match the scaler/model. Check FEATURES list!")
    else:
        x_scaled = scaler.transform(x)
        pred = model.predict(x_scaled)[0]
        proba = model.predict_proba(x_scaled)[0][1] if hasattr(model, "predict_proba") else None

        st.markdown("### 🧾 Prediction Result")
        if pred == 1:
            st.error("⚠️ High likelihood of **Parkinson's Disease**")
        else:
            st.success("✅ Low likelihood of Parkinson's Disease")

        if proba is not None:
            st.progress(float(proba))
            st.write(f"**Prediction Confidence:** {proba:.2%}")

# ---------------------- FOOTER ----------------------
st.markdown("<p class='footer'>Made by Priyam Parashar 🍁</p>", unsafe_allow_html=True)
