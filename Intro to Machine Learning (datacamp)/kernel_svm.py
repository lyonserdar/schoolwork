from sklearn.svm import SVC

svm = SVC(gamma=1)  # default is kernel="rbf"

# # Instantiate an RBF SVM
# svm = SVC()
# # Instantiate the GridSearchCV object and run the search
# parameters = {'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
# searcher = GridSearchCV(svm, parameters)
# searcher.fit(X , y)
# # Report the best parameters
# print("Best CV params", searcher.best_params_)

# # Instantiate an RBF SVM
# svm = SVC()
# # Instantiate the GridSearchCV object and run the search
# parameters = {'C':[0.1, 1, 10], 'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
# searcher = GridSearchCV(svm, parameters)
# searcher.fit(X_train, y_train)
# # Report the best parameters and the corresponding score
# print("Best CV params", searcher.best_params_)
# print("Best CV accuracy", searcher.best_score_)
# # Report the test accuracy using these best parameters
# print("Test accuracy of best grid search hypers:", searcher.score(X_train, y_train))