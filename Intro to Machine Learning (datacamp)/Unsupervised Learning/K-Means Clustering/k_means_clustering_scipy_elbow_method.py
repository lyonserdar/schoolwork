#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * K-means clustering elbow method
# Other methods are average silhouette and gap statistic

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import random

# Import models
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq
from scipy.cluster.vq import whiten


# Fifa 18 sample data
df = pd.read_csv("../../Datasets/fifa_18_sample_data.csv")
print(df.head())

df["scaled_sliding_tackle"] = whiten(df["sliding_tackle"])
df["scaled_aggression"] = whiten(df["aggression"])

distortions = []
num_clusters = range(2, 7)

for i in num_clusters:
    centroids, distortion = kmeans(
        df[["scaled_sliding_tackle", "scaled_aggression"]], i
    )
    distortions.append(distortion)

elbow_plot_data = pd.DataFrame(
    {"num_clusters": num_clusters, "distortions": distortions}
)

sns.lineplot(x="num_clusters", y="distortions", data=elbow_plot_data)
plt.xticks(num_clusters)
plt.show()

# Ideal num_clusters is 3