from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import numpy as np
from scipy.stats import randint
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from dataset_diabetes import X_train, X_test, y_train, y_test

param_grid = {"n_neighbors": np.arange(1, 50)}

knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X_train, y_train.ravel())
print(knn_cv.best_params_)
print(knn_cv.best_score_)


c_space = np.logspace(-5, 8, 15)
param_grid = {"C": c_space}

logreg = LogisticRegression()

logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

logreg_cv.fit(X_train, y_train.ravel())

print(logreg_cv.best_params_)
print(logreg_cv.best_score_)

param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 9),
    "min_samples_leaf": randint(1, 9),
    "criterion": ["gini", "entropy"],
}

tree = DecisionTreeClassifier()
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)
tree_cv.fit(X_train, y_train.ravel())

print(tree_cv.best_params_)
print(tree_cv.best_score_)
