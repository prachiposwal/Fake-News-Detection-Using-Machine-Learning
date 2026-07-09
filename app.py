import streamlit as st
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# ---------------------------------------
# Download NLTK Resources
# ---------------------------------------

nltk.download("stopwords")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# ---------------------------------------
# Text Preprocessing Function
# ---------------------------------------

def clean_text(text):

    text = str(text)

    # lowercase
    text = text.lower()

    # remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # remove numbers
    text = re.sub(r"\d+", "", text)

    # tokenize
    words = text.split()

    # remove stopwords + lemmatize
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="centered"
)

# ---------------------------------------
# Load Model
# ---------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("models/final_fake_news_model.pkl")
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.title("📌 About")

st.sidebar.info(
"""
This project detects whether a news article is **Real** or **Fake** using Machine Learning.

### Model
Linear Support Vector Machine (SVM)

### Feature Extraction
TF-IDF Vectorization

### Developed Using
- Python
- Scikit-Learn
- Streamlit
"""
)

# ---------------------------------------
# Main Title
# ---------------------------------------

st.title("📰 Fake News Detection System")

st.markdown("""
Welcome!

Paste any news article below and the trained Machine Learning model will predict whether the article is **Real** or **Fake**.
""")

# ---------------------------------------
# User Input
# ---------------------------------------

news = st.text_area(
    "Paste News Article",
    height=250,
    placeholder="Paste complete news article here..."
)

# ---------------------------------------
# Prediction
# ---------------------------------------

if st.button("🔍 Predict News"):

    if news.strip() == "":
        st.warning("⚠ Please enter a news article.")

    else:

        # Clean the text first
        cleaned_news = clean_text(news)

        # Convert into TF-IDF features
        transformed = vectorizer.transform([cleaned_news])

        # Predict
        prediction = model.predict(transformed)[0]

        st.divider()
        st.subheader("Prediction")

        if prediction == 1:
            st.success("✅ REAL NEWS")
        else:
            st.error("❌ FAKE NEWS")

# ---------------------------------------
# Footer
# ---------------------------------------

st.divider()

st.caption(
"Developed by Prachi | Fake News Detection using Machine Learning"
)