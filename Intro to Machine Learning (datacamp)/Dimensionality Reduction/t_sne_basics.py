from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

iris = datasets.load_iris()

X = iris["data"]
y = iris["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

print(X_train)
print(y_train)

model = TSNE(learning_rate=100)
transformed = model.fit_transform(X_train)
xs = transformed[:, 0]
ys = transformed[:, 1]
plt.scatter(xs, ys, c=y_train)
plt.show()


def main():
    pass
    # print(iris.DESCR)
    # print(iris.keys())
    # print(iris.data.shape)
    # print(iris.target_names)


if __name__ == "__main__":
    main()


# # Scatter plot
# plt.scatter(xs, ys, alpha=0.5)
# # Annotate the points
# for x, y, company in zip(xs, ys, companies):
#     plt.annotate(company, (x, y), fontsize=5, alpha=0.75)
# plt.show()