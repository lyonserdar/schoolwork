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

plt.style.use("ggplot")

SEED = 1  # Set seed for reproducibility
n = 50  # Sample size

# Import data from the csv file
df = pd.read_csv("sample_temperature_data.csv")
# df = pd.read_csv("file.csv")  # Read the temp data from csv file
# print(df.head())  # See first 5 elements of the dataframe
# print(df.shape)  # Size of the dataframe
df = df.reset_index()
X = (df[["index"]] + 1).values
y = df[["TEMP"]].values  # avg temperature
# X_scaled = (X - X.mean()) / X.std() # Z
X_scaled = (X - min(X)) / (max(X) - min(X))  # 0 to 1
y_scaled = (y - y.mean()) / y.std()

# a. Compute the mean and variance of the population.
# print(df.describe())
X_mean = X.mean()
y_mean = y.mean()
X_variance = X.var()
y_variance = y.var()
print(f"Mean and Variance of days(X): {X_mean}, {X_variance}")
print(f"Mean and Variance of temp(y): {y_mean}, {y_variance}")


# b. Use simple random sample (SRS) sampling method and randomly select 50 samples.
# Then, compute the sample mean and sample variance.
df_sample = df.sample(n=n, random_state=SEED)
# print(df_sample.head())
# print(df_sample.describe())
df_sample = df_sample.reset_index()

X_sample = (df_sample[["index"]] + 1).values
y_sample = df_sample[["TEMP"]].values

X_sample_scaled = (X_sample - X_sample.mean()) / X_sample.std()  # Z
y_sample_scaled = (y_sample - y_sample.mean()) / y_sample.std()

X_sample_mean = X_sample.mean()
y_sample_mean = y_sample.mean()

X_sample_scaled_mean = X_sample_scaled.mean()
y_sample_scaled_mean = y_sample_scaled.mean()

X_sample_variance = X_sample.var()
y_sample_variance = y_sample.var()
print(f"Sample mean and Variance of days(X): {X_sample_mean}, {X_sample_variance}")
print(f"Sample mean and Variance of temp(y): {y_sample_mean}, {y_sample_variance}")

# c. Discuss the results obtained in parts (a) and (b).

# d. Plot the histogram of the population (set the length of bins to 10 degrees).
# Discuss what it shows.
plt.hist(y, bins=10)
plt.title("Histogram of Temperature")
plt.xlabel("Temperature in F")
plt.show()

# e. Normalize the histogram data.
plt.hist(y_scaled, bins=10)
plt.title("Histogram of Normalized Temperature")
plt.xlabel("Temperature (Normalized)")
plt.show()

# f. Plot the population (using plot(x,y,’o’)).
# Use appropriate labels for the x- and y-axis
# (x indicatesthe day of the year (eg., 1, 2, ...) and y-axis shows the temperature).
# In the title of this figure, state the starting and ending date of your data.
plt.scatter(X, y)
plt.title("Temp")
plt.xlabel("Day of the year (eg., 1, 2, ...)")
plt.ylabel("Temperature in F")

# g. On the same figure, show the population mean with a red line and the sample mean
# obtained from the SRS method with a blue line.
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

# Scaled
plt.scatter(X_scaled, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()


# h. Make a regression model of your choosing (any order of polynomial) and solve it
# using the least-square error method applied to the sample data.
# Justify your proposed model.
numerator = 0
denominator = 0

for i in range(n):
    numerator += (X_sample[i] - X_sample_mean) * (y_sample[i] - y_sample_mean)
    denominator += (X_sample[i] - X_sample_mean) ** 2

m = numerator / denominator  # slope
c = y_sample_mean - (m * X_sample_mean)  # intercept

print(f"Coefficients: m: {m}, c: {c}")
print(f"Line: {m}x + {c}")

X_pred = np.linspace(np.min(X), np.max(X), 1000)
y_pred = m * X_pred + c

# i. Overlay on the plot in step “f” the predictions of your regression model for each
# day of the year.
plt.scatter(X, y)
plt.plot(X_pred, y_pred, c="g", label="Regression Line")
plt.title("Temp with Regression Line")
plt.xlabel("Day of the year (eg., 1, 2, ...)")
plt.ylabel("Temperature in F")
plt.legend()
plt.show()

plt.scatter(X_scaled, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled ** 2, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year x^2 (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled ** 3, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year x^3 (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled ** 10, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year x^10 (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled, y)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled, y ** 2)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature^2 in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled, y ** 3)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature^3 in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled, y ** 10)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature^10 in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()

plt.scatter(X_scaled ** 2, y ** 2)
plt.title("Temp Scaled")
plt.xlabel("Day of the year (Scaled)")
plt.ylabel("Temperature^2 in F")
plt.axhline(y_mean, color="r", linestyle="--")
plt.axhline(y_sample_mean, color="b", linestyle="--")
plt.show()


# j. Using your regression model, make a prediction for the average temperature
# on June 15, 2021.

