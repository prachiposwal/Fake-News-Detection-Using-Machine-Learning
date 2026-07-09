import streamlit as st
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# -------------------------------------------------
# Download NLTK Resources (only if not available)
# -------------------------------------------------

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="centered"
)

# -------------------------------------------------
# Text Cleaning Function
# -------------------------------------------------

def clean_text(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r"http\S+|www\S+", "", text)

    text = re.sub(r"<.*?>", "", text)

    text = text.translate(str.maketrans("", "", string.punctuation))

    text = re.sub(r"\d+", "", text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

# -------------------------------------------------
# Load Model
# -------------------------------------------------

@st.cache_resource
def load_model():

    model = joblib.load("models/final_fake_news_model.pkl")

    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

    return model, vectorizer


try:
    model, vectorizer = load_model()
except Exception as e:
    st.error("❌ Error loading model or vectorizer.")
    st.exception(e)
    st.stop()

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

st.sidebar.title("📌 About")

st.sidebar.info(
"""
This application detects whether a news article is **Real** or **Fake** using Machine Learning.

### Model
Linear SVM

### Feature Extraction
TF-IDF Vectorization

### Developed Using

- Python
- Scikit-learn
- Streamlit
"""
)

# -------------------------------------------------
# Main Title
# -------------------------------------------------

st.title("📰 Fake News Detection System")

st.write(
"""
Paste a complete news article below and click **Predict News**.
"""
)

# -------------------------------------------------
# Input Box
# -------------------------------------------------

news = st.text_area(
    "Paste News Article",
    height=250,
    placeholder="Paste complete news article here..."
)

# -------------------------------------------------
# Prediction
# -------------------------------------------------

if st.button("🔍 Predict News"):

    if news.strip() == "":
        st.warning("Please enter a news article.")

    else:

        cleaned_news = clean_text(news)

        transformed_news = vectorizer.transform([cleaned_news])

        prediction = model.predict(transformed_news)[0]

        st.divider()

        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "Developed by Prachi | Fake News Detection using Machine Learning"
)