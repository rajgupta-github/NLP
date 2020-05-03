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

messages = pd.read_csv('../Data/TextFiles/spam.csv', encoding='cp437')
messages = messages[['v1', 'v2']]
messages.columns = ['label', 'message']

lemmatizer = WordNetLemmatizer()

#Data cleaning and preprocessing
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    
    review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)


# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=2500)
X = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(messages.label, drop_first=True).values 


# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Training model using Naive bayes classifier
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(X_train, y_train)

y_pred=spam_detect_model.predict(X_test)

from sklearn.metrics import classification_report
NB_report = classification_report(y_test, y_pred)
print(NB_report)