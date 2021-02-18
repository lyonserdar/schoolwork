import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from dataset_boston import X_train, X_test, y_train, y_test, X, y, X_rooms

reg = LinearRegression()
reg.fit(X_rooms, y)
prediction_space = np.linspace(min(X_rooms), max(X_rooms)).reshape(-1, 1)

plt.scatter(X_rooms, y, color='blue')
plt.plot(prediction_space, reg.predict(prediction_space), color='red', linewidth=2)
plt.show()

reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
# print(y_pred)
print(reg_all.score(X_test, y_test))
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print("Root Mean Squared Error:", rmse)