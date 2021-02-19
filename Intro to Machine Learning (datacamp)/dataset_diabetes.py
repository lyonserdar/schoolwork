from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

dataset = pd.read_csv("diabetes.csv")

X = dataset.drop("diabetes", axis=1).values
y = dataset["diabetes"].values
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


def main():
    pass


if __name__ == "__main__":
    main()
