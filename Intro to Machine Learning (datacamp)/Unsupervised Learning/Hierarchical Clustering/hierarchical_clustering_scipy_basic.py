# samples = [] # TODO: find a dataset that is classification and multi target
# country_names = []

# mergings = linkage(samples, method='complete')
# dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
# plt.show()


# # Use fcluster to extract labels: labels
# labels = fcluster(mergings, 6, criterion='distance')

# # Create a DataFrame with labels and varieties as columns: df
# df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# # Create crosstab: ct
# ct = pd.crosstab(df['labels'], df['varieties'])

# # Display ct
# print(ct)


# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Import toy dataset
# from sklearn import datasets

# Import functions to compute accuracy and split data
# from sklearn.metrics import mean_squared_error as MSE
# from sklearn.model_selection import train_test_split

# Import models
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import dendrogram

x_coordinates = [
    80.1,
    93.1,
    86.6,
    98.5,
    86.4,
    9.5,
    15.2,
    3.4,
    10.4,
    20.3,
    44.2,
    56.8,
    49.2,
    62.5,
    44.0,
]
y_coordinates = [
    87.2,
    96.1,
    95.6,
    92.4,
    92.4,
    57.7,
    49.4,
    47.3,
    59.1,
    55.5,
    25.6,
    2.1,
    10.9,
    24.1,
    10.3,
]

df = pd.DataFrame({"x_coordinate": x_coordinates, "y_coordinate": y_coordinates})

Z = linkage(df, method="ward")
df["cluster_labels"] = fcluster(Z, 3, criterion="maxclust")

sns.scatterplot(x="x_coordinate", y="y_coordinate", hue="cluster_labels", data=df)
plt.show()
