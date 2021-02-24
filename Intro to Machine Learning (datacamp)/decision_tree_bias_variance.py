from dataset_automobile import X, y
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as MSE
from sklearn.model_selection import cross_val_score

# Set seed for reproducibility
SEED = 123

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=SEED
)

# Instantiate decision tree regressor
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.14, random_state=SEED)

# Evaluate the list of MSE obtained by  10-fold CV
# Set n_jobs to -1 in order to exploit all CPU cores in computation
MSE_CV = -cross_val_score(
    dt, X_train, y_train, cv=10, scoring="neg_mean_squared_error", n_jobs=-1
)

# Fit 'dt' to the training set
dt.fit(X_train, y_train)

# Predict the labels of training set
y_pred_train = dt.predict(X_train)

# Predict the labels of test set
y_pred_test = dt.predict(X_test)

# CV MSE
print(f"CV MSE: {MSE_CV.mean():.2f}")

# Training set MSE
print(f"Train MSE: {MSE(y_train, y_pred_train):.2f}")

# Test set MSE
print(f"Test MSE: {MSE(y_test, y_pred_test):.2f}")
