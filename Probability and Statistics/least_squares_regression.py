#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Least-squares Regression Group Project
# Group Members:
# Ali Serdar Aydogdu
# Brandon Fambrough
# James Hancock
# Romina Owens

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
SEED = 1

# Import data from the csv file
df = pd.read_csv("sample_temperature_data.csv")
# df = pd.read_csv("file.csv")  # Read the temp data from csv file
print(df.head())  # See first 5 elements of the dataframe
print(df.shape)  # Size of the dataframe
# ? x represents date and y temperature
X = df[["DATE"]]  # date # ? Use date or turn that in to day count like 0...450th day
Y = df[["TEMP"]]  # avg temperature

# a. Compute the mean and variance of the population.
print(df.describe())

# b. Use simple random sample (SRS) sampling method and randomly select 50 samples.
# Then, compute the sample mean and sample variance.
n = 50  # Set ut ti 50
df_sample = df.sample(n=n, random_state=SEED)
print(df_sample.head())
print(df_sample.describe())

# c. Discuss the results obtained in parts (a) and (b).

# d. Plot the histogram of the population (set the length of bins to 10 degrees).
# Discuss what it shows.
hist = df.hist(column="TEMP",bins=10)
plt.show()

# e. Normalize the histogram data.

# f. Plot the population (using plot(x,y,’o’)).
# Use appropriate labels for the x- and y-axis
# (x indicatesthe day of the year (eg., 1, 2, ...) and y-axis shows the temperature).
# In the title of this figure, state the starting and ending date of your data.

# g. On the same figure, show the population mean with a red line and the sample mean
# obtained from the SRS method with a blue line.

# h. Make a regression model of your choosing (any order of polynomial) and solve it
# using the least-square error method applied to the sample data.
# Justify your proposed model.

# i. Overlay on the plot in step “f” the predictions of your regression model for each
# day of the year.

# j. Using your regression model, make a prediction for the average temperature
# on June 15, 2021.

