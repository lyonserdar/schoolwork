#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Module 7 Homework

__class_section__ = "ECE 3710 - 002"
__project__ = "M07 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "3/5/2021"
__divider__ = "------------------------------------------------------------------------"

# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm, expon, probplot
from sympy import symbols, Eq, solve
from math import e

### 1. Sec 4.5, #4 (15 points)
print(__divider__)
print("1. Sec 4.5, #4 (15 points)")
print(__divider__)
"""
X is a random variable that follows the Normal distribution with mean = 2, and variance
= 9. Compute the following probabilities.Hint: Remember that variance is σ^2. If using
statistical functions, ensure you know if they input variance or standard deviation.
X ∼ N(2, 9)
"""
# Setup
mean = 2
variance = 9
std = np.sqrt(variance)

# a. P(X≥2)
print(1 - norm(mean, std).cdf(2))

# b. P(1≤X<7)
print(norm(mean, std).cdf(7) - norm(mean, std).cdf(1))

# c. P(−2.5<X<−1)
print(norm(mean, std).cdf(-1) - norm(mean, std).cdf(-2.5))

# d. P(−3≤X−2< 3) Hint: X-2 represents a mean shift.
print(abs(norm(mean - 2, std).cdf(-3) - norm(mean - 2, std).cdf(3)))

x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
plt.plot(x, norm.pdf(x, mean, std))
plt.plot(x, norm.cdf(x, mean, std))
plt.show()

### 2. Sec 4.5, #12 (15 points)
print(__divider__)
print("2. Sec 4.5, #12 (15 points)")
print(__divider__)
"""
Specifications for an aircraft bolt require that the ultimate tensile strength be at
least 18 kN. It is known that 10% of the bolts have strengths less than 18.3 kN and that
5% of the bolts have strengths greater than 19.76 kN. It is also known that the
strengths of these bolts are normally distributed. Hint: Use an “inverse” standard
normal probability calculation (or table lookup) to find the “z-score” values for the
percentiles of the two levels of strength given.  Use the z-score formula to write two
simple equations with the known strength values and two unknowns (μ and σ).  Use basic
algebra to solve for the mean (μ) and standard deviation (σ).
"""
# Setup
z1 = norm.ppf(0.10, loc=0, scale=1)
z2 = norm.ppf(0.95, loc=0, scale=1)
mean = 0
std = 0

# a. Find the mean and standard deviation of the strengths.
std = (19.76 - 18.3) / (z2 - z1)
print("std", std)
mean = 19.76 - z2 * std
print("mean", mean)

# b. What proportion of the bolts meet the strength specification?
print(1 - norm(mean, std).cdf(18))

x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
plt.plot(x, norm.pdf(x, mean, std))
plt.plot(x, norm.cdf(x, mean, std))
plt.show()

### 3. Sec 4.5, #16 (15 points)
print(__divider__)
print("3. Sec 4.5, #16 (15 points)")
print(__divider__)
"""
The amount of paint required to paint a surface with an area of 50 m^2 is normally
distributed with mean 6 L and standard deviation 0.3 L.
"""
# Setup
mean = 6
std = 0.3

# a. If 6.2 L of paint are available, what is the probability that the entire surface
#    can be painted?
print(norm(mean, std).cdf(6.2))

# b. How much paint is needed so that the probability is 0.9 that the entire surface can
#    be painted?
z = norm.ppf(0.9, loc=mean, scale=std)
print(z)

# c. What must the standard deviation be so that the probability is 0.9 that 6.2 L of
#    paint will be sufficient to paint the entire surface?
new_std = (6.2 - mean) / z
print(new_std)

x = np.linspace(norm.ppf(0.01, mean, std), norm.ppf(0.99, mean, std), 100)
plt.plot(x, norm.pdf(x, mean, std))
plt.plot(x, norm.cdf(x, mean, std))
plt.show()

### 4. Sec 4.7, #2 (20 points)
print(__divider__)
print("4. Sec 4.7, #2 (20 points)")
print(__divider__)
"""
The time between requests to a web server is exponentially distributed with mean 0.5
seconds.
"""
# Setup
mean = 0.5

# a. What is the value of the parameter λ?
# lambda is a reserved key for python so I cannot use it for a variable name
mu = 1 / 0.5
print(mu)

# b. What is the median time between requests?
print(expon.median(scale=1 / mu))

# c. What is the standard deviation?
print(expon.std(scale=1 / mu))

# d. What is the 80th percentile?
x = symbols("x")
expr = Eq(1 - e ** (-mu * x) - 0.8, 0)
x_80 = solve(expr)
print(x_80[0])

# e. Find the probability that more than one second elapses between requests.
print(1 - expon.cdf(1, scale=1 / mu))

# f. If there have been no requests for the past two seconds, what is the probability
#    that more than one additional second will elapse before the next request?
print(1 - expon.cdf(1, scale=1 / mu))

x = np.linspace(expon.ppf(0.01, scale=1 / mu), expon.ppf(0.99, scale=1 / mu), 100)
plt.plot(x, expon.pdf(x, scale=1 / mu))
plt.plot(x, expon.cdf(x, scale=1 / mu))
plt.show()

### Extra Credit Sec 4.10, #4 (10 points)
print(__divider__)
print("Extra Credit Sec 4.10, #4 (10 points)")
print(__divider__)
"""
Below are the durations (in minutes) of 40 time intervals between eruptions of the
geyser Old Faithful in Yellowstone National Park. 
91 51 79 53 82 51 76 82 84 53 
86 51 85 45 88 51 80 49 82 75 
73 67 68 86 72 75 75 66 84 70 
79 60 86 71 67 81 76 83 76 55 
"""
# Setup
data = [
    91,
    51,
    79,
    53,
    82,
    51,
    76,
    82,
    84,
    53,
    86,
    51,
    85,
    45,
    88,
    51,
    80,
    49,
    82,
    75,
    73,
    67,
    68,
    86,
    72,
    75,
    75,
    66,
    84,
    70,
    79,
    60,
    86,
    71,
    67,
    81,
    76,
    83,
    76,
    55,
]

# a. Construct a normal probability plot for these data.
probplot(data, dist="norm", fit=True, plot=plt)
plt.show()

# b. Do they appear to come from an approximately normal distribution?
# No, the data do not lie close to a straight line at all points. 

### OUTPUT
# ------------------------------------------------------------------------
# 1. Sec 4.5, #4 (15 points)
# ------------------------------------------------------------------------
# 0.5
# 0.5827683075454216
# 0.091848052662599
# 0.6826894921370859
# ------------------------------------------------------------------------
# 2. Sec 4.5, #12 (15 points)
# ------------------------------------------------------------------------
# std 0.4989056210478824
# mean 18.939373279712914
# 0.9701408503200377
# ------------------------------------------------------------------------
# 3. Sec 4.5, #16 (15 points)
# ------------------------------------------------------------------------
# 0.7475074624530773
# 6.38446546966338
# 0.031326036760685176
# ------------------------------------------------------------------------
# 4. Sec 4.7, #2 (20 points)
# ------------------------------------------------------------------------
# 2.0
# 0.34657359027997264
# 0.5
# 0.804718956217049
# 0.1353352832366127
# 0.1353352832366127
# ------------------------------------------------------------------------
# Extra Credit Sec 4.10, #4 (10 points)
# ------------------------------------------------------------------------
# See the plot
# No, the data do not lie close to a straight line at all points. 