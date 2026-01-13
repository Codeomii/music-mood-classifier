import os
import streamlit as st
import joblib

# Page setup
st.set_page_config(page_title="Music Mood Classifier", page_icon="🎵")
st.title("🎵 Music Mood Classifier")

# Path to saved model
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.joblib")

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("❌ Model not found. Please run training first: python -m src.train")
        st.stop()
    return joblib.load(MODEL_PATH)

model = load_model()

# Choose input type
mode = st.radio("Choose input type:", ["Lyrics", "Spotify Features"])

# Lyrics-based prediction
if mode == "Lyrics":
    lyrics = st.text_area("Paste song lyrics:", height=200, placeholder="Type or paste lyrics here...")
    if st.button("Predict Mood"):
        if lyrics.strip():
            pred = model.predict([lyrics])[0]
            st.success(f"🎶 Predicted Mood: {pred}")
        else:
            st.warning("⚠️ Please paste some lyrics first.")

# Spotify features-based prediction
else:
    danceability = st.slider("Danceability", 0.0, 1.0, 0.5)
    energy = st.slider("Energy", 0.0, 1.0, 0.5)
    valence = st.slider("Valence", 0.0, 1.0, 0.5)
    tempo = st.slider("Tempo", 50, 200, 120)

    if st.button("Predict Mood"):
        features = [[danceability, energy, valence, tempo]]
        pred = model.predict(features)[0]
        st.success(f"🎶 Predicted Mood: {pred}")