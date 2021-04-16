#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Document Clustering
# 1. Clean data before processing (e.g. removing "the")
# 2. Determine the importance of the terms in a document (in TF-IDF matrix)
# 3. Cluster the TF-IDF matrix

# Import libraries
import pandas as pd
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import seaborn as sns
import random
import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

# Import toy dataset
from plots import plots as data
from plots import stop_words

# Import models
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.cluster.vq import kmeans


def remove_noise(text, stop_words=stop_words):
    tokens = word_tokenize(text)
    cleaned_tokens = []
    for token in tokens:
        token = re.sub("[^A-Za-z0-9]+", "", token)
        if len(token) > 1 and token.lower() not in stop_words:
            # Get lowercase
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


tfidf_vectorizer = TfidfVectorizer(
    max_df=0.8, max_features=50, min_df=0.2, tokenizer=remove_noise
)

tfidf_matrix = tfidf_vectorizer.fit_transform(data)

print(tfidf_vectorizer)

num_clusters = 2

cluster_centers, distortion = kmeans(tfidf_matrix.todense(), num_clusters)

terms = tfidf_vectorizer.get_feature_names()

for i in range(num_clusters):
    center_terms = dict(zip(terms, list(cluster_centers[i])))
    sorted_terms = sorted(center_terms, key=center_terms.get, reverse=True)
    print(sorted_terms[:3])