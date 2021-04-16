#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * t-SNE

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
# from sklearn.metrics import mean_squared_error as MSE
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction import DictVectorizer

# Import models
from sklearn.manifold import TSNE

data = datasets.load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.head(), df.shape)
df_numeric = df.select_dtypes(["number"])
print(df_numeric.head(), df_numeric.shape)


m = TSNE(learning_rate=50)

tsne_features = m.fit_transform(df_numeric)
print(tsne_features[1:4, :])

df["X"] = tsne_features[:, 0]
df["y"] = tsne_features[:, 1]

sns.scatterplot(x="X", y="y", hue= "proline", data=df)

plt.show()
