# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Import models
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.vq import whiten


# Fifa 18 sample data
df = pd.read_csv("../../Datasets/fifa_18_sample_data.csv")
print(df.head())

df["scaled_sliding_tackle"] = whiten(df["sliding_tackle"])
df["scaled_aggression"] = whiten(df["aggression"])

# linkage(observations, method="single", metric="euclidean", optimal_ordering=False)
# method: how to calculate the proximity of clusters
# metric: distance metric
# optimal_ordering: order data points
# method="single": based on two closest objects
# method="complete": based on two farthest objects
# method="average": based on the arithmetic mean of all objects
# method="centroid": based on the geometric mean of all objects
# method="median": based on the median of all objects
# method="ward": based on the sum of squares

# fcluster(Z, t, criterion='inconsistent', depth=2, R=None, monocrit=None)
# Z(distance_matrix): output of linkage() method
# t(num_clusters): number of clusters
# criterion: how to decide thresholds of form clusters

Z = linkage(
    df[["scaled_sliding_tackle", "scaled_aggression"]],
    method="ward",
    metric="euclidean",
)
# dn = dendrogram(Z)
# dn = dendrogram(Z, labels=df[["name"]].values)
# plt.show()
df["cluster_labels"] = fcluster(Z, 3, criterion="maxclust")

# Display cluster centers of each cluster
print(
    df[["scaled_sliding_tackle", "scaled_aggression", "cluster_labels"]]
    .groupby("cluster_labels")
    .mean()
)

sns.scatterplot(
    x="scaled_sliding_tackle", y="scaled_aggression", hue="cluster_labels", data=df
)
plt.show()
