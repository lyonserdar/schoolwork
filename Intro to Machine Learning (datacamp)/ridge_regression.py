import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from dataset_boston import X_train, X_test, y_train, y_test, X, y, X_rooms


def display_plot(alpha_space, cv_scores, cv_scores_std):
    print(cv_scores)
    print(cv_scores_std)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(
        alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2
    )
    ax.set_ylabel("CV Score +/- Std Error")
    ax.set_xlabel("Alpha")
    ax.axhline(np.max(cv_scores), linestyle="--", color=".5")
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale("log")
    plt.show()


def main():
    alpha_space = np.logspace(-4, 0, 50)
    ridge_scores = []
    ridge_scores_std = []

    # ridge = Ridge(alpha=0.1, normalize=True)
    # ridge.fit(X_train, y_train)
    # ridge_pred = ridge.predict(X_test)
    # print(ridge.score(X_test, y_test))
    # rmse = np.sqrt(mean_squared_error(y_test, ridge_pred))
    # print("Root Mean Squared Error:", rmse)

    ridge = Ridge(normalize=True)

    for alpha in alpha_space:
        ridge.alpha = alpha
        ridge_cv_scores = cross_val_score(ridge, X_train, y_train, cv=10)
        ridge_scores.append(np.mean(ridge_cv_scores))
        ridge_scores_std.append(np.std(ridge_cv_scores))

    display_plot(alpha_space, ridge_scores, ridge_scores_std)


if __name__ == "__main__":
    main()

