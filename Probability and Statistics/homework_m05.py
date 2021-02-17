__class__ = "ECE 3710"
__project__ = "M05 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/17/2021"
__divider__ = "------------------------------------------------------------------------"

import numpy as np
from scipy import integrate
from math import sqrt

### 1. Sec 2.5, #4 (5 points)
print(__divider__)
print("1. Sec 2.5, #4 (5 points)")
print(__divider__)
"""
Two batteries, with voltages V1 and V2, are connected in series. The total voltage V is
given by V = V1 + V2. Assume that V1 has mean 12V and standard deviation 1V, and that V2
has mean 6V and standard deviation 0.5V.
"""
# Setup
v1_mean = 12.0
v1_std = 1.0
v2_mean = 6.0
v2_std = 0.5

# a. Find μV.
v_mean = v1_mean + v2_mean
print("v_mean:", v_mean)  # 18 V

# b. Assuming V1 and V2 to be independent, find σV.
v_std = sqrt(v1_std ** 2 + v2_std ** 2)
print("v_std:", v_std)  # 1.1180 V

### 2. Sec 2.5, #8 (15 points)
print(__divider__)
print("2. Sec 2.5, #8 (15 points)")
print(__divider__)
"""
A machine that fills bottles with a beverage has a fill volume whose mean is 20.01
ounces, with a standard deviation of 0.02 ounces. A case consists of 24 bottles randomly
sampled from the output of the machine.
"""
# Setup
fill_volume_mean = 20.01
fill_volume_std = 0.02
n_samples = 24

# a. Find the mean of the total volume of the beverage in the case.
total_volume_mean = n_samples * fill_volume_mean
print("total_volume_mean:", total_volume_mean)  # 480.24 ounces

# b. Find the standard deviation of the total volume of the beverage in the case.
total_volume_std = n_samples * fill_volume_std
print("total_volume_std:", total_volume_std)  # 0.48 ounces

# c. Find the mean of the average volume per bottle of the beverage in the case.
volume_per_bottle_mean = fill_volume_mean
print("volume_per_bottle_mean:", volume_per_bottle_mean)  # 20.01 ounces

# d. Find the standard deviation of the volume per bottle of the beverage in the case.
volume_per_bottle_std = fill_volume_std / sqrt(n_samples)
print("volume_per_bottle_std:", volume_per_bottle_std)  # .0041 ounces

# e. How many bottles must be included in a case for the standard deviation of the
#    average volume per bottle to be 0.0025 ounces?
n_samples_new = (fill_volume_std / 0.0025) ** 2
print("n_samples_new:", n_samples_new)  # 64 bottles

### 3. Sec 2.5, #14 (10 points)
print(__divider__)
print("3. Sec 2.5, #14 (10 points)")
print(__divider__)
"""
The oxygen equivalence number of a weld is a number that can be used to predict
properties such as hardness, strength, and ductility. The article “Advances in Oxygen
Equivalence Equations for Predicting the Properties of Titanium Welds” (D. Harwig, W.
Ittiwattana, and H. Castner,The Welding Journal, 2001:126s-136s) presents several
equations for computing the oxygen equivalence number of a weld. One equation, designed
to predict the hardness of a weld, is X = O + 2N + (2/3)C, where X is the oxygen
equivalence, and O, N, and C are the amounts of oxygen, nitrogen, and carbon,
respectively, in weight percent, in the weld. Suppose that for welds of a certain
type,μ0 = 0.1668,μN = 0.0255,μC = 0.0247,σ0 = 0.0340,σN = 0.0194, and σC = 0.0131.
"""
# Setup
oxygen_mean = 0.1668
nitrogen_mean = 0.0255
carbon_mean = 0.0247
oxygen_std = 0.0340
nitrogen_std = 0.0194
carbon_std = 0.0131

# a. Find μX.
oxygen_equivalence_mean = oxygen_mean + 2 * nitrogen_mean + (2 / 3) * carbon_mean
print("oxygen_equivalence_mean:", oxygen_equivalence_mean)  # 0.2343

# b. Suppose the weight percents of O, N, and C are independent. Find σX.
oxygen_equivalence_std = sqrt(
    oxygen_std ** 2 + 2 ** 2 * nitrogen_std ** 2 + (2 / 3) ** 2 * carbon_std ** 2
)
print("oxygen_equivalence_std:", oxygen_equivalence_std)  # 0.05232

### 4. Sec 2.5, #16 (20 points)
print(__divider__)
print("4. Sec 2.5, #16 (20 points)")
print(__divider__)
"""
The thicknessX of a wooden shim (in mm) has probability density function
f(x) = (3/4) - 3 * (x - 5) ** 2 / 4 , where 4 <= x <= 6, 0 otherwise
"""
# Setup
pdf = lambda x: (3 / 4) - 3 * (x - 5) ** 2 / 4

# a. Find μX.
f = lambda x: x * pdf(x)
mean = integrate.quad(f, 4, 6)[0]
print("mean:", mean)  # 5.0 mm

# b. Find σX ** 2.
f = lambda x: (x - mean) ** 2 * pdf(x)
variance = integrate.quad(f, 4, 6)[0]
print("variance:", variance)  # 0.2 mm ** 2

# c. Let Y denote the thickness of a shim in inches (1 mm = 0.0394 inches). Find μY and
#    σY ** 2.
mean_in_inches = (0.0394) * mean
print("mean_in_inches:", mean_in_inches)  # 0.197 inches
variance_in_inches = (0.0394) ** 2 * variance
print("variance_in_inches:", variance_in_inches)  # 0.000310472 inches ** 2

# d. If three shims are selected independently and stacked one atop another, find the
#    mean and variance of the total thickness.
total_thickness_mean = 3 * mean
print("total_thickness_mean:", total_thickness_mean)  # 15 mm
total_thickness_variance = 3 ** 2 * variance
print("total_thickness_variance:", total_thickness_variance)  # 1.8 mm ** 2

### Extra Credit (5 points)
print(__divider__)
print("Extra Credit (5 points)")
print(__divider__)
"""
The number of bytes downloaded per second on an information channel has mean 10^5 and
standard deviation 10^4. Among the factors influencing the rate is congestion, which
produces alternating periods of faster and slower transmission. Let X represent the
number of bytes downloaded in a randomly chosen five-second period.
"""
# Setup
bytes_per_second_mean = 10 ** 5
bytes_per_second_std = 10 ** 4

# a. s it reasonable to assume that μX = 5 × 10**5? Explain.
total_bytes_mean = 5 * bytes_per_second_mean
print("total_bytes_mean:", total_bytes_mean)  # 500000 bytes
print("test_mean:", 5 * 10 ** 5)  # 500000 bytes
# Yes, it should take around 5 times downloaded bytes per second

# b. Is it reasonable to assume that σX = sqrt(5) x 10 ** 4? Explain.
total_bytes_std = 5 * bytes_per_second_std
print("total_bytes_std:", total_bytes_std)  # 50000 bytes
print("test_mean:", sqrt(5) * 10 ** 4)  # 22360 bytes
# No, standard deviation is multiplied by the absolute value of the constant
# not the square root of the constant.
# In this case the standard deviation is around half of what it should have been


### OUTPUT
# ------------------------------------------------------------------------
# 1. Sec 2.5, #4 (5 points)
# ------------------------------------------------------------------------
# v_mean: 18.0
# v_std: 1.118033988749895
# ------------------------------------------------------------------------
# 2. Sec 2.5, #8 (15 points)
# ------------------------------------------------------------------------
# total_volume_mean: 480.24
# total_volume_std: 0.48
# volume_per_bottle_mean: 20.01
# volume_per_bottle_std: 0.004082482904638631
# n_samples_new: 64.0
# ------------------------------------------------------------------------
# 3. Sec 2.5, #14 (10 points)
# ------------------------------------------------------------------------
# oxygen_equivalence_mean: 0.23426666666666665
# oxygen_equivalence_std: 0.05232314125806201
# ------------------------------------------------------------------------
# 4. Sec 2.5, #16 (20 points)
# ------------------------------------------------------------------------
# mean: 5.0
# variance: 0.2
# mean_in_inches: 0.19699999999999998
# variance_in_inches: 0.000310472
# total_thickness_mean: 15.0
# total_thickness_variance: 1.8
# ------------------------------------------------------------------------
# Extra Credit (5 points)
# ------------------------------------------------------------------------
# total_bytes_mean: 500000
# test_mean: 500000
# total_bytes_std: 50000
# test_mean: 22360.679774997898
