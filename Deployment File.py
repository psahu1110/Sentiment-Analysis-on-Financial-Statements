# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:06:18 2023

@author: Pooja
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model and other necessary files
model = joblib.load(r"C:\Users\Pratik\sentiment\rfc.pkl")
vectorizer = joblib.load(r"C:\Users\Pratik\sentiment\tfidf.pkl")
stop_words = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# Define function to clean and preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…]', '', text)
    text = re.sub('\n', '', text)
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if not word in stop_words]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

# Define the Streamlit app
def app():
    st.title('Sentiment Analysis of Financial News')
    st.write('Enter a sentence to predict its sentiment')
    user_input = st.text_input('Enter your sentence:')
    if user_input:
        preprocessed_input = preprocess_text(user_input)
        X_test = vectorizer.transform([preprocessed_input])
        prediction = model.predict(X_test)
        if prediction == 1:
            st.write('Positive')
        elif prediction == -1:
            st.write('Negative')
        else:
            st.write('Neutral')

if __name__ == '__main__':
    app()