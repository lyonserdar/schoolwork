#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Module 11 Homework

__class_section__ = "ECE 3710 - 002"
__project__ = "M11 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "4/22/2021"
__divider__ = "------------------------------------------------------------------------"

# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm, expon, probplot
from sympy import symbols, Eq, solve
from math import e, ceil
from sklearn.linear_model import LinearRegression

### 1. (5 points)
print(__divider__)
print("1. (5 points)")
print(__divider__)
"""
For each of the following three scatterplots (a, b, and c), state whether the
correlation coefficient is an appropriate summary, and explain briefly. Hint: Think
about calculating a correlation coefficient for each data set. Will it properly
represent the data? Or, will there be problems due to curvature or outliers?
"""
# Setup

# a.
print(
    f"a. Yes, it looks like we have a positive corelation, correlation coefficient \n \
    is appropriate in this case."
)

# b.
print(
    f"b. No, we have a nonlinear looking relationship, the r would be close to 0 \n \
    even though there is a relation ship that looks like a bell."
)

# c.
print(
    f"c. Yes and No, we can see a strong relationship but the r will be effected by \n \
    the outliers, however in this case the r will be close to the r without the outliers"
)


### 2. (20 points)
print(__divider__)
print("2. (20 points)")
print(__divider__)
"""
In a study of ground motion caused by earthquakes, the peak velocity (in m/s) and peak
acceleration (in m/s^2) were recorded for five earthquakes. The results are presented in
the following table. 
"""
# Setup
df1 = pd.DataFrame(
    [(1.54, 7.64), (1.60, 8.04), (0.95, 8.04), (1.30, 6.37), (2.92, 3.25)],
    columns=["velocity", "acceleration"],
)

# a. Compute the correlation coefficient between peak velocity and peak acceleration.
r = df1.corr().iloc[0][1]
print(f"a. correlation coefficient, r = {r}")

# b. Construct a scatterplot for these data.
ax1 = df1.plot.scatter(x="velocity", y="acceleration")
print(f"b. Close the plot window to continue")
plt.show()

# c. Is the correlation coefficient an appropriate summary for these data? Explain why
#    or why not.
print(
    f"c. It's hard to tell, the sample size is too small, looks right but in \n \
    reality it could easily be the completely opposite"
)

# d. Someone suggests converting the units from meters to centimeters and from seconds
#    to minutes. What effect would this have on the correlation?
print(f"d. No change in correlation coefficient")


### 3. (10 points)
print(__divider__)
print("3. (10 points)")
print(__divider__)
"""
In a study of the relationship between the Brinell hardness (x) and tensile strength in
ksi (y) of specimens of cold drawn copper, the least-squares line was y= −196.32 + 2.42x.
"""
# Setup

# a. Predict the tensile strength of a specimen whose Brinell hardness is 102.7.
brinell_hardness = 102.7
tensile_strength = -196.32 + 2.42 * brinell_hardness
print(f"a. Tensile strength =  {tensile_strength} ksi")

# b. If two specimens differ in their Brinell hardness by 3, by how much do you predict
#    their tensile strengths to differ?
brinell_hardness = 3
tensile_strength_difference = 2.42 * brinell_hardness
print(f"b. Tensile strength difference =  {tensile_strength_difference} ksi")


### 4. (30 points)
print(__divider__)
print("4. (30 points)")
print(__divider__)
"""
An engineer wants to predict the value for y when x = 4.5, using the following data set. 
z=ln(y)
"""
# Setup
df4 = pd.DataFrame(
    [
        (1, 0.2, -1.61),
        (2, 0.3, -1.20),
        (3, 0.5, -0.69),
        (4, 0.5, -0.69),
        (5, 1.3, 0.26),
        (6, 2.3, 0.83),
        (7, 2.9, 1.06),
        (8, 4.5, 1.50),
        (9, 8.7, 2.16),
        (10, 12.0, 2.48),
    ],
    columns=["x", "y", "z"],
)

# a. Construct a scatterplot of the points (x, y).
ax1 = df4.plot.scatter(x="x", y="y")
print(f"a. Close the plot window to continue")
plt.show()

# b. Should the least-squares line be used to predict the value of y when x = 4.5? If so,
#    compute the least-squares line and the predicted value. If not, explain why not.
print(f"b. No, the data doesn't seem linear. We can't use simple linear reg.")

# c. Construct a scatterplot of the points (x, z), where z = lny.
ax1 = df4.plot.scatter(x="x", y="z")
print(f"c. Close the plot window to continue")
plt.show()

# d. Use the least-squares line to predict the value of z when x = 4.5. Is this an
#    appropriate method of prediction? Explain why or why not.
lr = LinearRegression()
X, y = df4[["x"]], df4[["z"]]
lr.fit(X, y)
prediction = lr.predict([[4.5]])
print(f"d. {prediction[0][0]}")


### OUTPUT
# ------------------------------------------------------------------------
# 1. (5 points)
# ------------------------------------------------------------------------
# a. Yes, it looks like we have a positive corelation, correlation coefficient 
#      is appropriate in this case.
# b. No, we have a nonlinear looking relationship, the r would be close to 0 
#      even though there is a relation ship that looks like a bell.
# c. Yes and No, we can see a strong relationship but the r will be effected by 
#      the outliers, however in this case the r will be close to the r without the outliers
# ------------------------------------------------------------------------
# 2. (20 points)
# ------------------------------------------------------------------------
# a. correlation coefficient, r = -0.884357316254951
# b. Close the plot window to continue
# c. It's hard to tell, the sample size is too small, looks right but in 
#      reality it could easily be the completely opposite
# d. No change in correlation coefficient
# ------------------------------------------------------------------------
# 3. (10 points)
# ------------------------------------------------------------------------
# a. Tensile strength =  52.214 ksi
# b. Tensile strength difference =  7.26 ksi
# ------------------------------------------------------------------------
# 4. (30 points)
# ------------------------------------------------------------------------
# a. Close the plot window to continue
# b. No, the data doesn't seem linear. We can't use simple linear reg.
# c. Close the plot window to continue
# d. -0.05727272727272714