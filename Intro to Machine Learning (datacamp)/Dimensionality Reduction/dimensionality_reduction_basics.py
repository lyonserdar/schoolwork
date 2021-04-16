#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Dimensionality Reduction Basics

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

# Import models
# import xgboost as xgb

df = pd.read_csv("../Datasets/pokemon.csv")
print(df.head())

print(df.describe())

number_cols = ["HP", "Attack", "Defense"]

non_number_cols = ["Name", "Type 1", "Type 2"]

df_selected = df[number_cols + non_number_cols]
print(df_selected.head())

sns.pairplot(df_selected, hue="Type 1", diag_kind="hist")
plt.show()

# Drop Column/Feature
# df.drop("column name", axis=1)