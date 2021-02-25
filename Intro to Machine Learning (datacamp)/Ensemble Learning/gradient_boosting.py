# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

# Import models
from sklearn.ensemble import GradientBoostingRegressor

# Set seed for reproducibility
SEED = 1

# Load the dataset
dataset = datasets.load_boston()
X = dataset["data"]
y = dataset["target"]

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=SEED
)

# Instantiate Gradient Boosting Regressor
gbt = GradientBoostingRegressor(n_estimators=300, max_depth=1, random_state=SEED)

# Fit gbt to the training set
gbt.fit(X_train, y_train)

# Predict the test set labels
y_pred = gbt.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred) ** (1 / 2)
print(f"Test set RMSE: {rmse_test:.2f}")
