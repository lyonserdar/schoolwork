from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import datasets

iris = datasets.load_iris()

X = iris["data"]
y = iris["target"]

# Stratify gives similar ratio of samples as the data set (Classification)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=1
)

dt = DecisionTreeClassifier(max_depth=2, random_state=1)
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"{acc:.2f}")

# Entropy and Gini
# # Import accuracy_score from sklearn.metrics
# from sklearn.metrics import accuracy_score
# # Use dt_entropy to predict test set labels
# y_pred = dt_entropy.predict(X_test)
# # Evaluate accuracy_entropy
# accuracy_entropy = accuracy_score(y_test, y_pred)
# # Print accuracy_entropy
# print('Accuracy achieved by using entropy: ', accuracy_entropy)
# # Print accuracy_gini
# print('Accuracy achieved by using the gini index: ', accuracy_gini)


