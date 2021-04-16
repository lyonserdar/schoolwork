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

DM_train = xgb.DMatrix(data=X_train, label=y_train)
DM_test = xgb.DMatrix(data=X_test, label=y_test)
params = {
    "booster": "reg:linear",
    "colsample_bytree": 0.3,
    "learning_rate": 0.1,
    "max_depth": 5,
}
xg_reg_cv_results = xgb.cv(
    params=params,
    dtrain=DM_train,
    nfold=4,
    num_boost_round=200,
    metrics="rmse",
    as_pandas=True,
    seed=SEED,
)

rmse = xg_reg_cv_results["test-rmse-mean"].tail(1)
print(f"RMSE: {rmse}")
