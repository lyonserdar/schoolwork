from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

dataset = pd.read_csv("boston.csv")

X = dataset.drop("MEDV", axis=1).values
y = dataset["MEDV"].values

# Single Feature
X_rooms = X[:, 5]
X_rooms = X_rooms.reshape(-1, 1)

y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


def main():
    plt.scatter(X_rooms, y)
    plt.ylabel("Value of house / 1000 ($)")
    plt.xlabel("Number of rooms")
    plt.show()


if __name__ == "__main__":
    main()
