import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from dataset_boston import X_train, X_test, y_train, y_test, X, y, X_rooms, dataset

lasso = Lasso(alpha=0.1, normalize=True)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
print(lasso.score(X_test, y_test))
rmse = np.sqrt(mean_squared_error(y_test, lasso_pred))
print("Root Mean Squared Error:", rmse)


names = dataset.drop("MEDV", axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X_train, y_train).coef_

plt.plot(range(names.size), lasso_coef)
plt.xticks(range(names.size), names, rotation=60)
plt.ylabel("Coefficients")
plt.margins(0.02)
plt.show()