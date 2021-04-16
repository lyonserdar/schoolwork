#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Correlation

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.feature_selection import VarianceThreshold

# Import models
# from sklearn.manifold import TSNE

data = datasets.load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
print(df.head(), df.shape)
df_numeric = df.select_dtypes(["number"])
print(df_numeric.head(), df_numeric.shape)

corr = df_numeric.corr()
print(corr)

mask = np.triu(np.ones_like(corr, dtype=bool))

cmap = sns.diverging_palette(h_neg=10, h_pos=240, as_cmap=True)
sns.heatmap(
    df_numeric.corr(),
    mask=mask,
    center=0,
    cmap=cmap,
    linewidths=1,
    annot=True,
    fmt=".2f",
)
plt.show()


# * Removing highly correlated features
# Create positive correlation matrix
corr_df = df.corr().abs()
# Create and apply mask
mask = np.triu(np.ones_like(corr_df, dtype=bool))
tri_df = corr.mask(mask)
print(tri_df)
# Find columns that meet treshold
to_drop = [c for c in tri_df.columns if any(tri_df[c] > 0.95)]
print(to_drop)
# Drop these columns
reduced_df = df.drop(to_drop, axis=1)
