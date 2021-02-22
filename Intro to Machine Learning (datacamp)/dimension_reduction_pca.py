from sklearn.decomposition import PCA
from dataset_iris import X_train, X_test, y_train, y_test
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
pca.fit(X_train)

transformed = pca.transform(X_train)
print(transformed.shape)

xs = transformed[:, 0]
ys = transformed[:, 1]

plt.scatter(xs, ys, c=y_train)
plt.show()

# # TruncatedSVD and csr_matrix
# from sklearn.decomposition import TruncatedSVD
# model = TruncatedSVD(n_components=3)
# model.fit(documents) # csr_matrix
# TruncatedSVD(algorithm='randomized')
# transformed = model.transform(documents)

# # tf-idf word-frequency array
# # Import TfidfVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# # Create a TfidfVectorizer: tfidf
# tfidf = TfidfVectorizer(documents)
# # Apply fit_transform to document: csr_mat
# csr_mat = tfidf.fit_transform(documents)
# # Print result of toarray() method
# print(csr_mat.toarray())
# # Get the words: words
# words = tfidf.get_feature_names()
# # Print words
# print(words)


# Perform the necessary imports
# from sklearn.decomposition import TruncatedSVD
# from sklearn.cluster import KMeans
# from sklearn.pipeline import make_pipeline
# # Create a TruncatedSVD instance: svd
# svd = TruncatedSVD(n_components=50)
# # Create a KMeans instance: kmeans
# kmeans = KMeans(n_clusters=6)
# # Create a pipeline: pipeline
# pipeline = make_pipeline(svd, kmeans)
# # Import pandas
# import pandas as pd
# # Fit the pipeline to articles
# pipeline.fit(articles)
# # Calculate the cluster labels: labels
# labels = pipeline.predict(articles)
# # Create a DataFrame aligning labels and titles: df
# df = pd.DataFrame({'label': labels, 'article': titles})
# # Display df sorted by cluster label
# print(df.sort_values('label'))