#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Whiten: rescaling data to a standard deviation of 1
# * x_new = x / std(x)

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Import models
from scipy.cluster.vq import whiten

# Fifa 18 sample data
df = pd.read_csv("../../Datasets/fifa_18_sample_data.csv")
print(df.head())

# Scale wage and value of the players 
df["scaled_wage"] = whiten(df["eur_wage"])  # The wage of a player in Euros
df["scaled_value"] = whiten(df["eur_value"])  # The transfer market value in Euros

# Plot the two columns in a scatter plot
df.plot(x='scaled_wage', y='scaled_value', kind='scatter')
plt.show()

# Check mean and standard deviation of scaled values
print(df[['scaled_wage', 'scaled_value']].describe())