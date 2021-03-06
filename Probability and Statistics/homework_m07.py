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
from scipy.stats import binom, poisson

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
p = 0.75
n = 10
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = binom.stats(n, p, moments="mvsk")
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), "bo", ms=8, label="binom pmf")
ax.vlines(x, 0, binom.pmf(x, n, p), colors="b", lw=5, alpha=0.5)

# a. P(X≥2)

# b. P(1≤X<7)

# c. P(−2.5<X<−1)

# d. P(−3≤X−2< 3) Hint: X-2 represents a mean shift.

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
mu = 4
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. Find the mean and standard deviation of the strengths.

# b. What proportion of the bolts meet the strength specification?

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
mu = 48 / 3
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. If 6.2 L of paint are available, what is the probability that the entire surface
#    can be painted?

# b. How much paint is needed so that the probability is 0.9 that the entire surface can
#    be painted?

# c. What must the standard deviation be so that the probability is 0.9 that 6.2 L of
#    paint will be sufficient to paint the entire surface?

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
mu = 48 / 3
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. What is the value of the parameter λ?

# b. What is the median time between requests?

# c. What is the standard deviation?

# d. What is the 80th percentile?

# e. Find the probability that more than one second elapses between requests.

# f. If there have been no requests for the past two seconds, what is the probability
#    that more than one additional second will elapse before the next request?

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
mu = 10
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. Construct a normal probability plot for these data. 

# b. Do they appear to come from an approximately normal distribution?

plt.show()

### OUTPUT
