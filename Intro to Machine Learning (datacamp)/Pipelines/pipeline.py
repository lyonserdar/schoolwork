from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("congress.csv", header=None)
df.columns = ['party', '', '', '']

X = df.drop("party", axis=1).values
y = df["party"].values
y = y.reshape(-1, 1)

df[df == '?'] = np.nan
print(df.isnull().sum())
# imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
# clf = SVC()
steps = [('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
        ('SVM', SVC())]
pipeline = Pipeline(steps)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

def main():
    pass


if __name__ == "__main__":
    main()


# # Setup the pipeline steps: steps
# steps = [('imputation', Imputer(missing_values='NaN', strategy="mean", axis=0)),
#          ('scaler', StandardScaler()),
#          ("elasticnet", ElasticNet())]

# # Create the pipeline: pipeline 
# pipeline = Pipeline(steps)

# # Specify the hyperparameter space
# parameters = {'elasticnet__l1_ratio':np.linspace(0,1,30)}

# # Create train and test sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.4, random_state=42
# )

# # Create the GridSearchCV object: gm_cv
# gm_cv = GridSearchCV(pipeline, param_grid=parameters)

# # Fit to the training set
# gm_cv.fit(X_train, y_train)

# # Compute and print the metrics
# r2 = gm_cv.score(X_test, y_test)
# print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
# print("Tuned ElasticNet R squared: {}".format(r2))