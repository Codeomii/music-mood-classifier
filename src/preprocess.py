import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure NLTK resources
def ensure_nltk():
    try:
        stopwords.words('english')
    except LookupError:
        nltk.download('stopwords')
    try:
        WordNetLemmatizer()
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

ensure_nltk()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

label_map = {
    'joy': 'happy', 'sadness': 'sad', 'anger': 'angry', 'fear': 'sad',
    'calm': 'calm', 'energetic': 'energetic',
    'happy': 'happy', 'sad': 'sad', 'angry': 'angry'
}

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = [t for t in text.split() if t not in stop_words and len(t) > 2]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return " ".join(tokens)

def load_and_prepare(path: str, dataset_type="lyrics") -> pd.DataFrame:
    df = pd.read_csv(path)

    if dataset_type == "lyrics":
        lyrics_col = next((c for c in ['lyrics','Lyric','text','song_lyrics'] if c in df.columns), None)
        label_col  = next((c for c in ['emotion','label','mood'] if c in df.columns), None)
        if not lyrics_col or not label_col:
            raise ValueError(f"Missing columns. Found: {list(df.columns)}. Need lyrics + label.")
        df = df.dropna(subset=[lyrics_col, label_col])
        df['clean_lyrics'] = df[lyrics_col].apply(clean_text)
        df['emotion'] = df[label_col].map(lambda x: label_map.get(str(x).lower(), str(x).lower()))

    elif dataset_type == "spotify":
        mood_col = next((c for c in ['mood','target','label','track_genre'] if c in df.columns), None)
        if not mood_col:
            raise ValueError(f"Missing mood/label column. Found: {list(df.columns)}")
        df = df.dropna(subset=[mood_col])
        df['mood'] = df[mood_col].map(lambda x: label_map.get(str(x).lower(), str(x).lower()))
        for col in ['danceability','energy','valence','tempo']:
            if col not in df.columns:
                df[col] = 0
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    return df