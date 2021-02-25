__class__ = "ECE 3710"
__project__ = "M06 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/23/2021"
__divider__ = "------------------------------------------------------------------------"

from scipy.stats import binom, poisson
import matplotlib.pyplot as plt
import numpy as np

### 1. Sec 4.2, #4 (15 points)
print(__divider__)
print("1. Sec 4.2, #4 (15 points)")
print(__divider__)
"""
At a certain airport, 75% of the flights arrive on time. A sample of 10 flights is
studied.Hint: Estimate p. Then use a Binomial pmf or CDF function with parameters n=10
and p.
"""
# Setup
p = 0.75
n = 10
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = binom.stats(n, p, moments="mvsk")
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
ax.plot(x, binom.pmf(x, n, p), "bo", ms=8, label="binom pmf")
ax.vlines(x, 0, binom.pmf(x, n, p), colors="b", lw=5, alpha=0.5)

# a. Find the probability that all 10 of the flights were on time.
print(f"P(X=10) = {binom.pmf(10, n, p):.5f}")  # 0.05631

# b. Find the probability that exactly eight of the flights were on time.
print(f"P(X=8) = {binom.pmf(8, n, p):.5f}")  # 0.28157

# c. Find the probability that eight or more of the flights were on time.
print(f"P(X>=8) = {1 - binom.cdf(7, n, p):.5f}")  # 0.52559

plt.show()


### 2. Sec 4.3, #8 (15 points)
print(__divider__)
print("1. Sec 4.3, #8 (15 points)")
print(__divider__)
"""
The number of cars arriving at a given intersection follows a Poisson distribution with
a mean rate of 4 per second.
"""
# Setup
mu = 4
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. What is the probability that 3 cars arrive in a given second (i.e. 1 second
#    interval)?
print(f"P(X=3) = {poisson.pmf(3, mu):.5f}")  # 0.19537

# b. What is the probability that 8 cars arrive in a period of three seconds?Hint: The
#    Poisson parameter will be different based on the time interval of interest. So, 𝜆in
#    1 second, 2𝜆 in 2 seconds, etc.
print(f"P(X=8) = {poisson.pmf(8, mu * 3):.5f}")  # 0.06552

# c. What is the probability that more than 3 cars arrive in a period of two
#    seconds?Hint: Use the fundamental rule that P(A)= 1 - P(A^c)
print(f"P(X>3) = {1 - poisson.cdf(3, mu * 2):.5f}")  # 0.95762

plt.show()

### 3. Sec 4.3, #10 (10 points)
print(__divider__)
print("3. Sec 4.3, #10 (10 points)")
print(__divider__)
"""
A chemist wishes to estimate the concentration of particles in a certain suspension. She
withdraws 3 mL of the suspension and counts 48 particles. 
"""
# Setup
mu = 48 / 3
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# a. Estimate the concentration in particles per mL.
print(f"Estimated particles per mL is {mu}")  # 16 mL

# b. Find the uncertainty in the estimate.
print(f"Uncertainty in the estimate is {(mu/3)**(1/2):.5f}")  # 2.30940

plt.show()

### Extra Credit (10 points)
print(__divider__)
print("Extra Credit (10 points)")
print(__divider__)

# a. Search online for an example of a Poisson process and give the reference. (Hint:
#    Use Google Scholar or similar search tool for academic articles).

# Source: http://www.medicine.mcgill.ca/epidemiology/hanley/bios601/Intensity-Rate/horsekicks_anthrax_poisson.pdf

# b. Describe the experiment or process from your reference and explain what makes it a
#    Poisson process.

# Anthrax(Splenic fever): on average, 10 deaths from anthrax in the years 1875-1894 (presumably in England and Wales).
# There are average of 10 deaths per year from anthrax
# It is a rate of deaths per year, we can use Poisson process to create a probability mass function

# c. Using the Poisson parameters given in the reference, pose your own question and
#    make an appropriate Poisson calculation.

# Setup
mu = 10
fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = poisson.stats(n, p, moments="mvsk")
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
ax.plot(x, poisson.pmf(x, mu), "bo", ms=8, label="poisson pmf")
ax.vlines(x, 0, poisson.pmf(x, mu), colors="b", lw=5, alpha=0.5)

# c. What is the probability that the death from anthrax is more than 10
print(f"P(X>10) = {1 - poisson.cdf(10, mu):.5f}")  # 0.41696

plt.show()

### OUTPUT
# ------------------------------------------------------------------------
# 1. Sec 4.2, #4 (15 points)
# ------------------------------------------------------------------------
# P(X=10) = 0.05631
# P(X=8) = 0.28157
# P(X>=8) = 0.52559
# ------------------------------------------------------------------------
# 1. Sec 4.3, #8 (15 points)
# ------------------------------------------------------------------------
# P(X=3) = 0.19537
# P(X=8) = 0.06552
# P(X>3) = 0.95762
# ------------------------------------------------------------------------
# 3. Sec 4.3, #10 (10 points)
# ------------------------------------------------------------------------
# Estimated particles per mL is 16.0
# Uncertainty in the estimate is 2.30940
# ------------------------------------------------------------------------
# Extra Credit (10 points)
# ------------------------------------------------------------------------
# P(X>10) = 0.41696
