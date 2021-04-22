#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Module 10 Homework

__class_section__ = "ECE 3710 - 002"
__project__ = "M10 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "4/19/2021"
__divider__ = "------------------------------------------------------------------------"

# Import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm, expon, probplot
from sympy import symbols, Eq, solve
from math import e, ceil

### 1. (5 points)
print(__divider__)
print("1. (5 points)")
print(__divider__)
"""
True or false:
"""
# Setup

# a. If we reject H0, then we conclude that H0 is false.
print(f"a. If we reject H0, then we conclude that H0 is false.: True")

# b. If we do not reject H0, then we conclude that H0 is true.
print(f"b. If we do not reject H0, then we conclude that H0 is true.: False")

# c. If we reject H0, then we conclude that H1 is true.
print(f"c. If we reject H0, then we conclude that H1 is true.: True")

# d. If we do not reject H0, then we conclude that H1 is false.
print(f"d. If we do not reject H0, then we conclude that H1 is false.: True")


### 2. (5 points)
print(__divider__)
print("2. (5 points)")
print(__divider__)
"""
Let μ be the radiation level to which a radiation worker is exposed during the course of
a year. The Environmental Protection Agency has set the maximum safe level of exposure
at 5 rem per year. If a hypothesis test is to be performed to determine whether a
workplace is safe, which is the most appropriate null hypothesis: H0: μ ≤ 5, H0: μ ≥ 5,
or H0: μ = 5? Explain.
"""

print(f"H0: μ ≤ 5, We assume that work place is safe and that's our null hypothesis.")


### 3. (5 points)
print(__divider__)
print("3. (5 points)")
print(__divider__)
"""
A machine that fills cereal boxes is supposed to be calibrated so that the mean fill
weight is 12 oz. Let μ denote the true mean fill weight. Assume that in a test of the
hypotheses H0: μ = 12 versus H1: μ ≠ 12, the P-value is 0.30.
"""
# Setup

# a. Should H0 be rejected on the basis of this test? Explain.
print(f"a. P-value is 0.30, we can't reject HO without further information it's more than 0.05")


### 4. (30 points)
print(__divider__)
print("4. (30 points)")
print(__divider__)
"""
A process for a certain type of ore is designed to reduce the concentration of
impurities to less than 2%. It is known that the standard deviation of impurities for
processed ore is 0.6%. Let μ represent the mean impurity level, in percent, for ore
specimens treated by this process. The impurity of 80 ore specimens is measured, and a
test of the hypothesis H0: μ ≥ 2 versus H1: μ < 2 will be performed.
"""
# Setup
mu = 2
std = 0.6
n = 80

# a. If the test is made at the 5% level, what is the rejection region? (hint: ≤
#    critical point)
alpha = 0.05
z = norm.ppf(1 - alpha / 2)
rejection_region = mu - z * (std / (n ** (1 / 2)))
print(f"a. x ≤ {rejection_region} {z}")

# b. If the sample mean impurity level is 1.85, will H0 be rejected at the 5% level?
mean = 1.85
print(f"b. True, since 1.85 ≤ rejection_region")

# c. If the value 1.9 is the critical point, what is the level of the test?
z = (mu - 1.9) / (std / (n ** (1 / 2)))
print(f"c. {100 * (2 * (1 - norm.cdf(z)))}")

### 5. (20 points)
print(__divider__)
print("5. (20 points)")
print(__divider__)
"""
Resistors for use in a certain application are supposed to have a mean resistance μ
greater than 100Ω. Assume that the standard deviation of the resistances is 5Ω.
Resistances will be measured for a sample of resistors, and a test of the hypothesis H0:
μ < 100 versus H1: μ > 100 will be made. Assume that in fact the true mean resistance is
101 Ω.
"""
# Setup
mu = 100
std = 5

# a. If 100 resistors are sampled, what is the power of a test made at the 5% level?
n = 100
alpha = 0.05
z = norm.ppf(1 - alpha / 2)
rejection_region = mu - z * (std / (n ** (1 / 2)))
new_z = (mu - rejection_region) / (std / (n ** (1 / 2)))
print(f"a. {1 - (1 - norm.cdf(new_z))}")

# b. How many resistors must be sampled so that a 5% level test has power 0.95?
z = norm.ppf(0.95)
n = ceil((z / ((mu - rejection_region) / std)) ** 2)
print(f"b. n = {n}")


### OUTPUT
# ------------------------------------------------------------------------
# 1. (5 points)
# ------------------------------------------------------------------------
# a. If we reject H0, then we conclude that H0 is false.: True
# b. If we do not reject H0, then we conclude that H0 is true.: False
# c. If we reject H0, then we conclude that H1 is true.: True
# d. If we do not reject H0, then we conclude that H1 is false.: True
# ------------------------------------------------------------------------
# 2. (5 points)
# ------------------------------------------------------------------------
# H0: μ ≤ 5, We assume that work place is safe and that's our null hypothesis.
# ------------------------------------------------------------------------
# 3. (5 points)
# ------------------------------------------------------------------------
# a. P-value is 0.30, we can't reject HO without further information it's more than 0.05
# ------------------------------------------------------------------------
# 4. (30 points)
# ------------------------------------------------------------------------
# a. x ≤ 1.8685216189135128 1.959963984540054
# b. True, since 1.85 ≤ rejection_region
# c. 13.603712811414326
# ------------------------------------------------------------------------
# 5. (20 points)
# ------------------------------------------------------------------------
# a. 0.975
# b. n = 71
