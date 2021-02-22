import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

samples = [] # TODO: find a dataset that is classification and multi target
country_names = []

mergings = linkage(samples, method='complete')
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
plt.show()

#https://campus.datacamp.com/courses/unsupervised-learning-in-python/visualization-with-hierarchical-clustering-and-t-sne?ex=5

# # Perform the necessary imports
# import pandas as pd
# from scipy.cluster.hierarchy import fcluster

# # Use fcluster to extract labels: labels
# labels = fcluster(mergings, 6, criterion='distance')

# # Create a DataFrame with labels and varieties as columns: df
# df = pd.DataFrame({'labels': labels, 'varieties': varieties})

# # Create crosstab: ct
# ct = pd.crosstab(df['labels'], df['varieties'])

# # Display ct
# print(ct)
