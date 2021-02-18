from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from dataset_boston import X_train, X_test, y_train, y_test, X, y, X_rooms
import numpy as np

reg = LinearRegression()

cv_results = cross_val_score(reg, X, y, cv=5)
print(cv_results)
print(np.mean(cv_results))

cv_results = cross_val_score(reg, X, y, cv=10)
print(cv_results)
print(np.mean(cv_results))