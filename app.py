import streamlit as st
import joblib

# Load trained model and vectorizer
model = joblib.load("fake_news_lr_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

st.title("📰 Fake News Detection")
st.write("Enter a news article text below to classify it as Fake or Real.")

user_input = st.text_area("News article text:")

if st.button("Predict"):
    if user_input.strip():
        transformed_input = tfidf.transform([user_input])
        prediction = model.predict(transformed_input)
        label = "Real News ✅" if prediction[0] == 1 else "Fake News ❌"
        st.subheader(f"Prediction: {label}")
    else:
        st.warning("Please enter some text.")