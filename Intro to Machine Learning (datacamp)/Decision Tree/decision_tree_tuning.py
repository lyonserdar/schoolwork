# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# Import models
from sklearn.tree import DecisionTreeClassifier

# Set seed for reproducibility
SEED = 1

# Load the dataset
dataset = datasets.load_breast_cancer()
X = dataset["data"]
y = dataset["target"]

# Split data into 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=SEED
)

# Instantiate Decision Tree Classifier
dt = DecisionTreeClassifier(random_state=SEED)

# Get dt's hyperparameters
params = dt.get_params()
for param_name, param_value in params.items():
    print(f"{param_name}: {param_value}")

# Define the grid of hyperparameters
params_dt = {
    "max_depth": [3, 4, 5, 6],
    "min_samples_leaf": [0.04, 0.06, 0.08],
    "max_features": [0.2, 0.4, 0.6, 0.8],
}

# Instantiate a 10-fold CV grid search object
grid_dt = GridSearchCV(
    estimator=dt, param_grid=params_dt, scoring="accuracy", cv=10, n_jobs=-1
)

# Fit grid_dt to the training data
grid_dt.fit(X_train, y_train)

# Extract best hyperparameters from grid_dt
best_hyperparams = grid_dt.best_params_
print(f"Best hyperparameters: {best_hyperparams}")

# Extract best CV score from grid_dt
best_CV_score = grid_dt.best_score_
print(f"Best CV accuracy: {best_CV_score}")

# Extract best model from grid_dt
best_model = grid_dt.best_estimator_

# Evaluate test set accuracy
test_acc = best_model.score(X_test, y_test)
print(f"Best model accuracy: {test_acc:.3f}")
