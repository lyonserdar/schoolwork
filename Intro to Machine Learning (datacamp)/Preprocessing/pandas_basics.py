#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Pandas Basics

# Import libraries
import pandas as pd

# import numpy as np
# import matplotlib.pyplot as plt

# Import toy dataset
# from sklearn import datasets

# Import functions to compute accuracy and split data
# from sklearn.metrics import mean_squared_error as MSE
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction import DictVectorizer

# Import models
# import xgboost as xgb

# Read JSON file
df = pd.read_json("../Datasets/hiking.json")


# Pandas basics

# Get the first 5 rows of the dataset
print(df.head())
# Get the columns of the dataset
print(df.columns)
# Get the data type of columns
print(df.dtypes)
# Get the basic stats of the dataset
print(df.describe())
# Remove rows with missing data
print(df.dropna())
# Remove rows with index
print(df.drop([1, 2, 3]))
# Remove column with name
print(df.drop("Name", axis=1))  # "axis=1" drops a column
# Filtering data
print(df[df["Accessible"] == "Y"])
# Get all null values
print(df["Difficulty"].isnull().sum())
# Filter null values
print(df[df["Difficulty"].notnull()])
# Converting column types
df["Difficulty"] = df["Difficulty"].astype("object")
# Get value counts
print(df["Difficulty"].value_counts())