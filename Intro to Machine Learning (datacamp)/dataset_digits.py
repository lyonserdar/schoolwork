import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

# print(digits.keys())
# print(digits.DESCR)
# print(digits.images.shape)
# print(digits.data.shape)

X = digits["data"]
y = digits["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=10, stratify=y
)


def main():
    plt.imshow(digits["images"][1010], cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    main()
