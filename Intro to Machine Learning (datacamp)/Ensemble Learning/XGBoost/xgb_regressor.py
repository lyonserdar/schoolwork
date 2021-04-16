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
dataset = datasets.load_boston()
X = dataset["data"]
y = dataset["target"]
# X, y = boston_data.iloc[:, :-1], boston_data.iloc[:, -1]

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=SEED
)

# Instantiate XGBoost
xg_reg = xgb.XGBRegressor(objective="reg:linear", n_estimators=10, seed=SEED)

# Fit xg_clf to the training set
xg_reg.fit(X_train, y_train)

# Predict the test set
y_pred = xg_reg.predict(X_test)

# Evaluate the accuracy of the test set
accuracy = np.sqrt(MSE(y_test, y_pred))
print(f"RMSE: {accuracy}")

# Learning API only
# DM_train = xgb.DMatrix(data=X_train, label=y_train)
# DM_test = xgb.DMatrix(data=X_test, label=y_test)
# params = {"booster": "gblinear", "objective": "reg:linear"}
# xg_reg = xgb.train(params=params, dtrain=DM_train, num_boost_round=10)
# preds = xg_reg.predict(DM_test)
# rmse = np.sqrt(mean_squared_error(y_test, preds))
# print(f"RMSE: {rmse}")
