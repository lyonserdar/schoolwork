# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Import models
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.vq import whiten

df = pd.DataFrame(
    {"x": [2, 3, 5, 6, 2], "y": [1, 1, 5, 5, 2], "labels": ["A", "A", "B", "B", "A"]}
)

# Visualize clusters with matplotlib
colors = {"A": "red", "B": "blue"}
df.plot.scatter(x="x", y="y", c=df["labels"].apply(lambda x: colors[x]))
plt.show()

# Visualize clusters with seaborn
sns.scatterplot(x='x', y='y', hue='labels', data=df)
plt.show()