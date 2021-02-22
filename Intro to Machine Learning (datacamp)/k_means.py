from sklearn.cluster import KMeans
from dataset_iris import X_train, X_test, y_train, y_test, X
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("ggplot")

model = KMeans(n_clusters=3)
model.fit(X_train)
labels = model.predict(X_train)
print(labels)
print(y_train)

labels_new = model.predict(X_test)
print(labels_new)
print(y_test)

xs = X_train[:, 0]
ys = X_train[:, 2]

plt.scatter(xs, ys, c=labels)
plt.show()

xs = X_test[:, 0]
ys = X_test[:, 1]

plt.scatter(xs, ys, c=labels_new, alpha=0.5)
centroids = model.cluster_centers_
centroids_x = centroids[:, 0]
centroids_y = centroids[:, 1]
plt.scatter(centroids_x, centroids_y, marker="D", s=50)
plt.show()

print(labels)
print(y_train)
df = pd.DataFrame({'labels': labels, 'species': [['setosa', 'versicolor', 'virginica'][i] for i in y_train]})
print(df)
cross_tabulation = pd.crosstab(df['labels'], df['species'])
print(cross_tabulation)

print(model.inertia_)

ks = range(1, 6)
inertias = []

for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(X_train)
    inertias.append(model.inertia_)

plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()

# labels = model.fit_predict(X_train)
# scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
# scaler.fit(X)
# X_scaled = scaler.transform(X)
scaler = StandardScaler()
kmeans = KMeans(n_clusters=3)
pipeline = make_pipeline(scaler, kmeans)
pipeline.fit(X_train)
labels = pipeline.predict(X_train)
# print(labels)

df = pd.DataFrame({'labels': labels, 'species': [['setosa', 'versicolor', 'virginica'][i] for i in y_train]})
print(df)
cross_tabulation = pd.crosstab(df['labels'], df['species'])
print(cross_tabulation)
# In this dataset standardization made the clustering worse.
# from sklearn.preprocessing import MaxAbsScaler, Normalizer
