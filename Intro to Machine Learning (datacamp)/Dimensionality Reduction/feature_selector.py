#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Feature Selector

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


sel = VarianceThreshold(threshold=0.1)
sel.fit(df / df.mean())

mask = sel.get_support()
print(mask)
print(df.shape)
reduced_df = df.loc[:, mask]
print(reduced_df.shape)

# Fewer than 30% missing values = True value
mask = df.isna().sum() / len(df) < 0.3
print(mask)
reduced_df = df.loc[:, mask]
