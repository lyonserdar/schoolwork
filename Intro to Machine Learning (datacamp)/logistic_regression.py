# This is a classification model not regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from dataset_diabetes import X_train, X_test, y_train, y_test
import matplotlib.pyplot as plt

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

y_pred_prob = logreg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

plt.plot([0, 1], [0, 1], "k--")
plt.plot(fpr, tpr, label="Logistic Regression")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.title("Logistic Regression ROC Curve")
plt.show()

# ### digits
# lr = LogisticRegression()
# lr.fit(X,y)
# # Get predicted probabilities
# proba = lr.predict_proba(X)
# # Sort the example indices by their maximum probability
# proba_inds = np.argsort(np.max(proba,axis=1))
# # Show the most confident (least ambiguous) digit
# show_digit(proba_inds[-1], lr)
# # Show the least confident (most ambiguous) digit
# show_digit(proba_inds[0], lr)