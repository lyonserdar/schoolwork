from sklearn import datasets, neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X = iris["data"]
y = iris["target"]

# knn = KNeighborsClassifier(n_neighbors=6)
# knn.fit(X, y)
# X_new = np.array([[5.6, 2.8, 3.9, 1.1], [5.7, 2.6, 3.8, 1.3], [4.7, 3.2, 1.3, 0.2]])
# prediction = knn.predict(X_new)
# print("Prediction:", prediction)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=12, stratify=y
)

neighbors = np.arange(1, 11)
print(neighbors)
train_accuracy = np.empty(neighbors.size)
test_accuracy = np.empty(neighbors.size)

for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    train_accuracy[i] = knn.score(X_train, y_train)
    test_accuracy[i] = knn.score(X_test, y_test)

plt.title("k-NN: Varying Number of Neighbors")
plt.plot(neighbors, test_accuracy, label="Testing Accuracy")
plt.plot(neighbors, train_accuracy, label="Training Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
plt.show()
