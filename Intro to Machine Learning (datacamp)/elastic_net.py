from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from dataset_diabetes import X_train, X_test, y_train, y_test

l1_space = np.linspace(0, 1, 30)
param_grid = {"l1_ratio": l1_space}

elastic_net = ElasticNet()

gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)

gm_cv.fit(X_train, y_train)

y_pred = gm_cv.predict(X_test)
r2 = gm_cv.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print("Tuned ElasticNet l1 ratio:", gm_cv.best_params_)
print("Tuned ElasticNet R squared:", r2)
print("Tuned ElasticNet MSE:", mse)
