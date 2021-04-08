#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Module 9 Homework

__class_section__ = "ECE 3710 - 002"
__project__ = "M09 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "4/8/2021"
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
Find the value of z required to create a two-sided confidence interval with the
following confidence levels: Hint: Use a normal inverse function such as norminv(p) in
Matlab. Also remember the interval is two-sided so you need to put half of the area
outside the confidence interval on both sides.
"""
# Setup

# a. 80%
alpha_a = 0.20
z_a = norm.ppf(1 - alpha_a / 2)
print(f"a. z = {z_a:.4f} for 80% CI")

# b. 99%
alpha_b = 0.01
z_b = norm.ppf(1 - alpha_b / 2)
print(f"b. z = {z_b:.4f} for 99% CI")

### 2. (5 points)
print(__divider__)
print("2. (5 points)")
print(__divider__)
"""
Find the level of confidence for a two-sided confidence interval for each of the
following z values: Hint: Use a normal CDF function such as normcdf(z) in Matlab.
Remember the interval is two-sided so you need to account for half of the area outside
the confidence interval on both sides.
"""
# Setup

# a. z = 1.5
z_a = 1.5
confidence_level_a = 100 * (1 - 2 * (1 - norm.cdf(z_a)))
print(f"a. {confidence_level_a:.4f}% CI for z = 1.5")

# b. z = 3
z_b = 3
confidence_level_b = 100 * (1 - 2 * (1 - norm.cdf(z_b)))
print(f"b. {confidence_level_b:.4f}% CI for z = 3")

### 3. (25 points)
print(__divider__)
print("3. (25 points)")
print(__divider__)
"""
In a sample of 60 electric motors, the average, or mean, efficiency (in percent) was 85
and the standard deviation was 2.
"""
# Setup
n = 60
mean = 85
std = 2

# a. Find a 95% confidence interval for the mean efficiency.
alpha_a = 1 - 95 / 100
z_a = norm.ppf(1 - alpha_a / 2)
offset_a = z_a * std / n ** (1 / 2)
print(f"a. {mean}±{offset_a:.4f} ({mean - offset_a:.4f}, {mean + offset_a:.4f})")

# b. Find a 99.5% confidence interval for the mean efficiency.
alpha_b = 1 - 99.5 / 100
z_b = norm.ppf(1 - alpha_b / 2)
offset_b = z_b * std / n ** (1 / 2)
print(f"b. {mean}±{offset_b:.4f} ({mean - offset_b:.4f}, {mean + offset_b:.4f})")

# c. What is the confidence level of the interval (84.63, 85.37)?
z_c = (85.37 - mean) / (std / n ** (1 / 2))
confidence_level_c = 100 * (1 - 2 * (1 - norm.cdf(z_c)))
print(f"c. {confidence_level_c:.4f}% CI for the interval (84.63, 85.37)")

# d. How many motors must be sampled so that a 95% confidence interval specifies the
# mean efficiency to within ± 0.35 percent?
n_d = (z_a * std / 0.35) ** 2
print(f"d. n = {ceil(n_d)} for 95% CI and within ± 0.35")

# e. How many motors must be sampled so that a 99.5% confidence interval specifies the
# mean to within ± 0.35 percent?
n_e = (z_b * std / 0.35) ** 2
print(f"e. n = {ceil(n_e)} for 99.5% CI and within ± 0.35")

### 4. (15 points)
print(__divider__)
print("4. (15 points)")
print(__divider__)
"""
Sixty-four independent measurements were made of the speed of light. They averaged
299,795 km/s and had a standard deviation of 8 km/s.
"""
# Setup
n = 64
mean = 299795
std = 8

# a. A 95% confidence interval for the speed of light is 299,795 ± 1.96 km/s
alpha_a = 1 - 95 / 100
z_a = norm.ppf(1 - alpha_a / 2)
offset_a = z_a * std / n ** (1 / 2)
print(f"a. TRUE: {mean}±{offset_a:.4f} ({mean - offset_a:.4f}, {mean + offset_a:.4f})")

# b. The probability is 95% that the speed of light is in the interval 299,795 ± 1.96
# km/s
print(f"b. FALSE: We are 95% confident that it is in the interval")

# c. If another (65th) measurement is made, the probability is 95% that it would fall in
# the interval 299,795± 1.96 km/s
print(f"b. FALSE")

### Extra Credit (10 points)
print(__divider__)
print("Extra Credit (10 points)")
print(__divider__)
"""
An electrical engineer wishes to compare the mean lifetimes of two types of transistors
in an application involving high-temperature performance. A sample of 60 transistors of
type A were tested and were found to have a mean lifetime of 1827 hours and a standard
deviation of 168 hours. A sample of 180 transistors of type B were tested and were found
to have a mean lifetime of 1658 hours and a standard deviation of 225 hours.
Find a 95% confidence interval for the difference between the mean lifetimes of the two
types of transistors.
"""
# Setup
n_a = 60
mean_a = 1827
std_a = 168
n_b = 180
mean_b = 1658
std_b = 225

alpha = 1 - 95 / 100
mean = mean_b - mean_a
z = norm.ppf(1 - alpha / 2)
offset = z_a * std / (std_b ** 2 / n_b + std_a ** 2 / n_a) ** (1 / 2)
print(f"{mean}±{offset:.4f} ({mean - offset:.4f}, {mean + offset:.4f})")


### OUTPUT
# ------------------------------------------------------------------------
# 1. (5 points)
# ------------------------------------------------------------------------
# a. z = 1.2816 for 80% CI
# b. z = 2.5758 for 99% CI
# ------------------------------------------------------------------------
# 2. (5 points)
# ------------------------------------------------------------------------
# a. 86.6386% CI for z = 1.5
# b. 99.7300% CI for z = 3
# ------------------------------------------------------------------------
# 3. (25 points)
# ------------------------------------------------------------------------
# a. 85±0.5061 (84.4939, 85.5061)
# b. 85±0.7248 (84.2752, 85.7248)
# c. 84.8143% CI for the interval (84.63, 85.37)
# d. n = 126 for 95% CI and within ± 0.35
# e. n = 258 for 99.5% CI and within ± 0.35
# ------------------------------------------------------------------------
# 4. (15 points)
# ------------------------------------------------------------------------
# a. TRUE: 299795±1.9600 (299793.0400, 299796.9600)
# b. FALSE: We are 95% confident that it is in the interval
# b. FALSE
# ------------------------------------------------------------------------
# Extra Credit (10 points)
# ------------------------------------------------------------------------
# -169±0.5719 (-169.5719, -168.4281)
