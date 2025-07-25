## 📰 Fake News Classification (Fake / Real)

 ##Project Overview

This project classifies news articles as Fake or Real using Natural Language Processing (NLP) and a Logistic Regression model.
We combine two datasets (Fake.csv and True.csv), preprocess the text, vectorize with TF-IDF, and train the Logistic Regression model.

The trained model is deployed using a Streamlit web app for live predictions.




## Folder Structure

FakeNewsClassification/

├── Fake.csv                # Dataset (Fake news)
├── True.csv                # Dataset (True news)
├── news_classification.py  # ML training script
├── app.py                  # Streamlit app (Logistic Regression)
├── fake_news_lr_model.pkl  # Saved Logistic Regression model
├── tfidf_vectorizer.pkl    # Saved TF-IDF vectorizer
├── requirements.txt        # Required Python libraries
└── README.md               # Project guide




## Steps to Run the Project

1. Install Dependencies

   Run this command in your terminal:

   pip install -r requirements.txt



2. Train the Model

   Run the main script to combine datasets, clean data, train, evaluate, and save the model:

   python news_classification.py

   This will create:

   news.csv

   fake_news_lr_model.pkl

   tfidf_vectorizer.pkl




3. Launch the Streamlit Web App

To start the web interface for predictions:

streamlit run app.py




## Usage of Web App

1. Enter any news article text in the text area.


2. Click Predict.


3. The app will display whether the article is Fake ❌ or Real ✅.




## Requirements

Python 3.8+

pandas

numpy

scikit-learn

nltk

seaborn

matplotlib

joblib

streamlit




## Next Improvements

Add support for Naive Bayes or other ML models.

Use deep learning models like LSTMs or BERT.

Explain predictions using SHAP or LIME.

Deploy app online with Streamlit Cloud.




## Author
## Sakshi Dhiman
