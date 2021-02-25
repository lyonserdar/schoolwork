# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Import models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier

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

# Instantiate a classification DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=4, min_samples_leaf=0.16, random_state=SEED)

# Instantiate a BaggingClassifier
bc = BaggingClassifier(base_estimator=dt, n_estimators=300, n_jobs=-1)

# Fit bc to the training set
bc.fit(X_train, y_train)

# Predict test set labels
y_pred = bc.predict(X_test)

# Evaluate the test set accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Bagging Classifier: {accuracy:.3f}")

# Evaluate the test set accuracy
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Accuracy of Decision Tree Classifier: {accuracy_dt:.3f}")

# Instantiate a BaggingClassifier with OOB(Out of Bag Evaluation)
bc_oob = BaggingClassifier(
    base_estimator=dt, n_estimators=300, oob_score=True, n_jobs=-1
)

# Fit bc to the training set
bc_oob.fit(X_train, y_train)

# Predict test set labels
y_pred_oob = bc_oob.predict(X_test)

# Evaluate the test set accuracy
accuracy = accuracy_score(y_test, y_pred_oob)
print(f"Accuracy of Bagging Classifier w/ OOB: {accuracy:.3f}")

# Extract the OOB accuracy from bc_oob
oob_accuracy = bc_oob.oob_score_

# Print OOB accuracy
print(f"OOB accuracy: {oob_accuracy:.3f}")
