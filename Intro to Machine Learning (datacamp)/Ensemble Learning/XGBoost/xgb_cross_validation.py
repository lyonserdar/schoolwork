# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

# Import models
import xgboost as xgb  # XGBoost requires < Python 3.8, Install it later!


# Set seed for reproducibility
SEED = 1

# Load the dataset
dataset = datasets.load_breast_cancer()
X = dataset["data"]
y = dataset["target"]

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=SEED
)

dmatrix = xgb.DMatrix(data=X_train, label=y_train)

params = {"objective": "binary:logistic", "max_depth": 4}

# Instantiate XGBoost CV
cv_results = xgb.cv(
    dtrain=dmatrix,
    params=params,
    nfold=4,
    num_boost_round=10,
    metrics="error",
    as_pandas=True,
)

# Evaluate the accuracy
accuracy = 1 - cv_results["test-error-mean"].iloc[-1]
print(f"Accuracy: {accuracy}")
