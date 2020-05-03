#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:14:17 2020

@author: rajkgupta
"""

import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.utils import column_or_1d
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

messages = pd.read_csv('../Data/TextFiles/spam.csv', encoding='cp437')
messages = messages[['v1', 'v2']]
messages.columns = ['label', 'message']

lemmatizer = WordNetLemmatizer()

# Data cleaning and preprocessing
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()

    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)


def call_ml_model(X, y):
    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)
    # Training model using Naive bayes classifier
    spam_detect_model = MultinomialNB().fit(X_train, y_train)
    y_pred = spam_detect_model.predict(X_test)
    # Classification report using bag of words model
    NB_report = classification_report(y_test, y_pred)
    print(NB_report)


# Creating the Bag of Words model
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()
y = pd.get_dummies(messages.label, drop_first=True).values
y = column_or_1d(y, warn=True)
print("Classification report using bag of words model")
call_ml_model(X, y)

# Creating the TF-IDF model
cv = TfidfVectorizer(max_features=5000)
X = cv.fit_transform(corpus).toarray()
print("Classification report using TF-IDF model")
call_ml_model(X, y)
