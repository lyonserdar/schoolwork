# Standardization: Subtract the mean and divide by variance
# All features are centered around zero and have variance one

# Subtract the minimum and divide by the range
# Normalized data has minimum zero and maximum one

# Normalized data ranges from -1 to 1

import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("diabetes.csv")



X = dataset.drop("diabetes", axis=1).values
y = dataset["diabetes"].values

print(np.mean(X), np.std(X))
X_scaled = scale(X)
print(np.mean(X_scaled), np.std(X_scaled))

steps = [('scaler', StandardScaler()), ('knn', KNeighborsClassifier())]
pipeline = Pipeline(steps)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=21
)

knn_scaled = pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(knn_scaled.score(X_test, y_test))

knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)
print(knn_unscaled.score(X_test, y_test))


# steps = [('scaler', StandardScaler()),
#          ('SVM', SVC())]

# pipeline = Pipeline(steps)

# parameters = {'SVM__C':[1, 10, 100],
#               'SVM__gamma':[0.1, 0.01]}

# cv = GridSearchCV(pipeline, param_grid=parameters)
# cv.fit(X_train, y_train)
# y_pred = cv.predict(X_test)
# print("Accuracy: {}".format(cv.score(X_test, y_test)))
# print(classification_report(y_test, y_pred))
# print("Tuned Model Parameters: {}".format(cv.best_params_))