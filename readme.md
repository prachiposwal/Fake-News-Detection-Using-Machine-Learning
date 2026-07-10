## 🚀 Live Demo

🔗 https://fake-news-detection-using-machine-learning-wleefmmw33chul9nvqt.streamlit.app

# 📰 Fake News Detection System

A Machine Learning-based web application that detects whether a news article is **Real** or **Fake** using Natural Language Processing (NLP) and a Linear Support Vector Machine (SVM). The application is deployed using **Streamlit** and provides a simple interface for users to classify news articles.

---
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

- - -

## 📌 Project Overview

Fake news spreads rapidly through digital platforms and social media, making it difficult for users to verify the authenticity of information.

This project uses **Natural Language Processing (NLP)** techniques to preprocess news articles, convert them into numerical features using **TF-IDF Vectorization**, and classify them using Machine Learning algorithms.

## 🌟 Repository Highlights

- ✅ Complete End-to-End Machine Learning Pipeline
- ✅ Natural Language Processing (NLP) using TF-IDF
- ✅ Six Machine Learning Models Compared
- ✅ Linear SVM selected as the Best Model
- ✅ Interactive Streamlit Web Application
- ✅ GitHub Hosted Source Code
- ✅ Real-Time Fake News Prediction

---

## 🎯 Objectives

- Detect fake news using Machine Learning.
- Build an end-to-end NLP pipeline.
- Compare multiple classification algorithms.
- Deploy the best-performing model using Streamlit.
- Create a user-friendly web application.

---

## 📂 Dataset

**Dataset Name:** Fake and Real News Dataset

### Dataset Information

- **Total Records:** 45,752 news articles
- **Classes:** Real News and Fake News
- **Feature Used:** News article text
- **Target Variable:** Label (Real / Fake)

The dataset contains news articles collected from reliable and unreliable sources, making it suitable for supervised text classification tasks.

---

## ⚙️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn

### Natural Language Processing (NLP)
- TF-IDF Vectorization
- CountVectorizer

### Data Analysis
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Plotly

### Model Deployment
- Streamlit

### Model Serialization
- Joblib

---

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Understanding
3. Text Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. TF-IDF Vectorization
7. Model Training
8. Model Evaluation
9. Model Comparison
10. Streamlit Deployment

---

## 🤖 Models Implemented

The following machine learning models were trained and evaluated on the Fake News Detection dataset:

- ✅ Logistic Regression
- ✅ Multinomial Naive Bayes
- ✅ Random Forest Classifier
- ✅ Linear Support Vector Machine (Linear SVM) ⭐ **Best Performing Model**
- ✅ K-Nearest Neighbors (KNN)
- ✅ Multi-Layer Perceptron (Neural Network)

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 97.5% |
| Random Forest | 97.97% |
| Naive Bayes | 92.43% |
| Linear SVM | **98.31%** ✅ |
| K-Nearest Neighbors (KNN) | 87.47% |
| Multi-Layer Perceptron (Neural Network) | 96.39% |

## 🏆 Best Performing Model

Among all the evaluated machine learning models, the **Linear Support Vector Machine (Linear SVM)** achieved the highest accuracy (**98.10%**) along with excellent Precision, Recall, and F1-Score.

Therefore, Linear SVM was selected as the final model and deployed using **Streamlit** for real-time fake news detection.
---

## 📁 Project Structure

```text
News Dataset
      │
      ▼
Data Cleaning & Preprocessing
      │
      ▼
Text Normalization
(Removing Stopwords, Punctuation, Lemmatization)
      │
      ▼
Feature Extraction (TF-IDF)
      │
      ▼
Train-Test Split
      │
      ▼
Machine Learning Models
(Logistic Regression, Naive Bayes,
Random Forest, Linear SVM,
KNN, Neural Network)
      │
      ▼
Model Evaluation
      │
      ▼
Best Model Selection
(Linear SVM)
      │
      ▼
Streamlit Deployment
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/prachiposwal/Fake-News-Detection-Using-Machine-Learning.git
```

### 2. Navigate to the Project Folder

```bash
cd Fake-News-Detection-Using-Machine-Learning
```

### 3. Install the Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 💻 Application Features

- Paste any news article.
- Predict whether it is Real or Fake.
- Simple and interactive Streamlit interface.
- Fast prediction using a trained Machine Learning model.

---


## 📸 Screenshots

### 🏠 Home Page

![Home Page](images/imageshome.png.png)

---

### ❌ Fake News Prediction

![Fake Prediction](images/imagefake_prediction.png.png)

---

### ✅ Real News Prediction

![Real Prediction](images/imagesreal_prediction.png.png)

### Model Accuracy Comparison

![Accuracy Comparison](images/accuracy_comparison.png.png)

### Linear SVM Confusion Matrix

![Confusion Matrix](images/confusion_matrix_svm.png.png)


---

## 🚀 Future Improvements

- Implement Transformer-based models such as BERT and RoBERTa.
- Add Explainable AI techniques using SHAP or LIME.
- Integrate real-time news APIs for live prediction.
- Support multilingual fake news detection.
- Deploy the application using Docker and cloud platforms.
- Build a user feedback mechanism for continuous model improvement.

---

## 👩‍💻 Author

## 👨‍💻 Author

**Prachi Poswal**

- GitHub: https://github.com/prachiposwal

This project was developed for learning, portfolio building, and demonstrating practical applications of Machine Learning and Natural Language Processing.

---

## ⭐ Acknowledgements

This project was developed as part of an end-to-end Machine Learning and Natural Language Processing portfolio.
---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!