# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Import models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.ensemble import VotingClassifier

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

# Instantiate individual classifiers
lr = LogisticRegression(random_state=SEED)
knn = KNN(n_neighbors=27)
dt = DecisionTreeClassifier(min_samples_leaf=0.13, random_state=SEED)

# Define a list of classifiers
classifiers = [
    ("Logistic Regression", lr),
    ("K Nearest Neighbors", knn),
    ("Classification Tree", dt),
]

# Iterate over the defined list of classifier tuples 
for clf_name, clf in classifiers:
    # Fit clf to the training set
    clf.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = clf.predict(X_test)

    # Evaluate the accuracy of clf on the test set
    print(f"{clf_name}: {accuracy_score(y_test, y_pred):.3f}")

# Instantiate a VotingClassifier
vc = VotingClassifier(estimators=classifiers)

# Fit vc to the training set and predict test set labels
vc.fit(X_train, y_train)
y_pred = vc.predict(X_test)

# Evaluate the test-set accuracy of vc
print(f"Voting Classifier: {accuracy_score(y_test, y_pred):.3f}")