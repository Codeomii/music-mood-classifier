# 🎵 Music Mood Classifier

A machine learning project that predicts the **mood of a song** using either:
- **Lyrics dataset (`dataset.csv`)** → Text classification with Naive Bayes
- **Spotify dataset (`spotify_millsongdata.csv`)** → Audio features classification with RandomForest

This project demonstrates end‑to‑end ML workflow: preprocessing, training, evaluation, and deployment via a Streamlit app.

---

## 🚀 Features
- Preprocessing of lyrics (cleaning, lemmatization, stopword removal)
- Training pipelines for both text and numeric features
- Interactive Streamlit app for mood prediction
- Supports **two datasets** (lyrics + Spotify features)
- Easy to extend with hybrid models (lyrics + audio features together)

---

## 📂 Project Structure
music-mood-classifier/
├─ data/
│  ├─ dataset.csv                # lyrics dataset
│  ├─ spotify_millsongdata.csv   # spotify dataset
├─ src/
│  ├─ __init__.py
│  ├─ preprocess.py              # preprocessing functions
│  └─ train.py                   # training scripts
├─ app.py                        # Streamlit app
├─ requirements.txt              # dependencies
├─ README.md                     # project documentation

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-Codeomii>/music-mood-classifier.git
   cd music-mood-classifier
