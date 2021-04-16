##
# TODO: This is a mess, fix it once xgboost is updated to Python 3.8

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
param_grid = {
    "learning_rate": np.arange(0.05, 1.05, 0.05),
    "n_estimators": [200],
    "subsample": np.arange(0.05, 1.05, 0.05),
}

model = xgb.XGBRegressor()
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_grid,
    n_iter=25,
    scoring="neg_mean_squared_error",
    cv=4,
    verbose=1,
)

random_search.fit(X_train, y_train)

print(f"Best parameters found: {random_search.best_params_}")
print(f"Lowest RMSE found: {np.sqrt(np.abs(random_search.best_score_))}")


# # Import necessary modules
# from sklearn.feature_extraction import DictVectorizer
# from sklearn.pipeline import Pipeline

# # Fill LotFrontage missing values with 0
# X.LotFrontage = X.LotFrontage.fillna(0)

# # Setup the pipeline steps: steps
# steps = [("ohe_onestep", DictVectorizer(sparse=False)),
#          ("xgb_model", xgb.XGBRegressor())]

# # Create the pipeline: xgb_pipeline
# xgb_pipeline = Pipeline(steps)

# # Fit the pipeline
# xgb_pipeline.fit(X.to_dict("records"), y)