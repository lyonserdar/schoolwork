# Import toy dataset
from sklearn import datasets

# Import functions to compute accuracy and split data
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

# Import models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

# Set seed for reproducibility
SEED = 1

# Load the dataset
dataset = datasets.load_breast_cancer()
X = dataset["data"]
y = dataset["target"]

# Split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, stratify=y, random_state=SEED
)

# Instantiate a classification tree
dt = DecisionTreeClassifier(max_depth=1, random_state=SEED)

# Instantiate an AdaBoost classifier
adb_clf = AdaBoostClassifier(base_estimator=dt, n_estimators=100)

# Fit 'adb_clf' to the training set
adb_clf.fit(X_train, y_train)

# Predict the test set probabilities of positive cases
y_pred_proba = adb_clf.predict_proba(X_test)[:, 1]

# Evaluate test set roc_auc_score
adb_clf_roc_auc_score = roc_auc_score(y_test, y_pred_proba)
print(f"ROC AUC score: {adb_clf_roc_auc_score:.2f}")
