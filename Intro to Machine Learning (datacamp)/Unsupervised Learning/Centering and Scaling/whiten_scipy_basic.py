#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Whiten: rescaling data to a standard deviation of 1
# * x_new = x / std(x)

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt

# Import models
from scipy.cluster.vq import whiten

# Data is basic integers
data = [5, 1, 3, 3, 2, 3, 3, 8, 1, 2, 2, 3, 5]
print(data)

scaled_data = whiten(data)
print(scaled_data)

plt.plot(data, label="original")
plt.plot(scaled_data, label="scaled")

plt.legend()
plt.show()

# Data is small fractional numbers
data = [
    0.0025,
    0.001,
    -0.0005,
    -0.001,
    -0.0005,
    0.0025,
    -0.001,
    -0.0015,
    -0.001,
    0.0005,
]

scaled_data = whiten(data)
print(scaled_data)

plt.plot(data, label="original")
plt.plot(scaled_data, label="scaled")

plt.legend()
plt.show()