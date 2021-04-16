#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Limitations of hierarchical clustering

# Import libraries
import pandas as pd
import random
from timeit import timeit

# Import models
from scipy.cluster.hierarchy import linkage

START = 0
END = 100
COUNT = 100
df = pd.DataFrame(
    {
        "x": random.sample(range(START, END), COUNT),
        "y": random.sample(range(START, END), COUNT),
    }
)


def func_linkage():
    linkage(df[["x", "y"]], method="ward", metric="euclidean")

print(timeit("func_linkage()", number=1000, globals=globals()))

