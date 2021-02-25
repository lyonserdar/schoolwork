# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import mean_squared_error as MSE
from sklearn.model_selection import train_test_split

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
rf = RandomForestRegressor(n_estimators=400, min_samples_leaf=0.12, random_state=SEED)

# Fit rf to the training set
rf.fit(X_train, y_train)

# Predict the test set
y_pred = rf.predict(X_test)

# Evaluate the test set RMSE
rmse_test = MSE(y_test, y_pred) ** (1 / 2)
print(f"Test set RMSE of rf: {rmse_test}")

# Create a pd.Series of features importance
importances_rf = pd.Series(rf.feature_importances_, index=dataset['feature_names'])

# Sort importances_rf
sorted_importances_rf = importances_rf.sort_values()

# Make a horizontal bar plot
sorted_importances_rf.plot(kind="barh", color="lightgreen")
plt.title('Features Importances')
plt.show()
