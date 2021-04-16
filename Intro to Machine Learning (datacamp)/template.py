#!/usr/bin/env python
# -*- coding: utf-8 -*-

# * Template File

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

# Import models
import xgboost as xgb

