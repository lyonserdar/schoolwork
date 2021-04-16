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

# Instantiate XGBoost
xg_clf = xgb.XGBClassifier(objective="binary:logistic", n_estimators=10, seed=SEED)

# Fit xg_clf to the training set
xg_clf.fit(X_train, y_train)

# Predict the test set
y_pred = xg_clf.predict(X_test)

# Evaluate the accuracy of the test set
accuracy = float(np.sum(y_pred == y_test)) / y_test.shape[0]
print(f"Accuracy: {accuracy}")
