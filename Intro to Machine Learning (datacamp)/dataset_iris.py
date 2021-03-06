from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris["data"]
y = iris["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10, stratify=y
)


def main():
    print(iris.DESCR)
    print(iris.keys())
    print(iris.data.shape)
    print(iris.target_names)


if __name__ == "__main__":
    main()
