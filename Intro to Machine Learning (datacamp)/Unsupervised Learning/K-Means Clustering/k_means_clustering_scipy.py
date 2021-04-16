#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * K-means clustering

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import random

# Import models
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq

# kmeans(obs, k_or_guess, iter=20, thresh=1e-05, check_finite=True)
# Generates cluster centers
# obs: standardized observations
# k_or_guess: number of clusters
# iter: number of iterations
# thres: threshold
# check_finite: whether to check if observations contain only finite numbers
# Returns two objects: cluster centers, distortion

# vq(obs, code_book, check_finite=True)
# Generates cluster labels
# obs: standardized observations
# code_book: cluster centers
# check_finite: whether to check if observations contain only finite numbers
# Returns two objects: a list of cluster labels, a list of distorions

from scipy.cluster.vq import whiten


# Fifa 18 sample data
df = pd.read_csv("../../Datasets/fifa_18_sample_data.csv")
print(df.head())

df["scaled_sliding_tackle"] = whiten(df["sliding_tackle"])
df["scaled_aggression"] = whiten(df["aggression"])

cluster_centers, _ = kmeans(df[["scaled_sliding_tackle", "scaled_aggression"]], 3)
df["cluster_labels"], _ = vq(
    df[["scaled_sliding_tackle", "scaled_aggression"]], cluster_centers
)

sns.scatterplot(
    x="scaled_sliding_tackle", y="scaled_aggression", hue="cluster_labels", data=df
)
plt.show()
