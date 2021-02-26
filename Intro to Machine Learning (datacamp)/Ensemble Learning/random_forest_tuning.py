# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# Import models
from sklearn.ensemble import RandomForestRegressor

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

# Instantiate a random forest regressor
rf = RandomForestRegressor(random_state=SEED)

# Inspect rf's hyperparameters
params = rf.get_params()
for param_name, param_value in params.items():
    print(f"{param_name}: {param_value}")

# Define the grid of hyperparameters
params_rf = {
    "n_estimators": [300, 400, 500],
    "max_depth": [4, 6, 8],
    "min_samples_leaf": [0.1, 0.2],
    "max_features": ["log2", "sqrt"],
}

# Instantiate a 10-fold CV grid search object
grid_rf = GridSearchCV(
    estimator=rf,
    param_grid=params_rf,
    scoring="neg_mean_squared_error",
    verbose=1,
    cv=3,
    n_jobs=-1,
)

# Fit grid_rf to the training data
grid_rf.fit(X_train, y_train)

# Extract best hyperparameters from grid_rf
best_hyperparams = grid_rf.best_params_
print(f"Best hyperparameters: {best_hyperparams}")

# Extract best model from grid_rf
best_model = grid_rf.best_estimator_

# Predict the test set labels
y_pred = best_model.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred) ** (1 / 2)
print(f"Test set RMSE of rf: {rmse_test:.2f}")
