from sklearn.decomposition import PCA

samples = []
model = PCA(copy=True)
model.fit(samples)
transformed = model.transform(samples)
print(transformed)


### Before PCA ###

# # Perform the necessary imports
# import matplotlib.pyplot as plt
# from scipy.stats import pearsonr

# # Assign the 0th column of grains: width
# width = grains[:, 0]

# # Assign the 1st column of grains: length
# length = grains[:, 1]

# # Scatter plot width vs length
# plt.scatter(width, length)
# plt.axis('equal')
# plt.show()

# # Calculate the Pearson correlation
# correlation, pvalue = pearsonr(width, length)

# # Display the correlation
# print(correlation)

### After PCA ###

# # Import PCA
# from sklearn.decomposition import PCA

# # Create PCA instance: model
# model = PCA()

# # Apply the fit_transform method of model to grains: pca_features
# pca_features = model.fit_transform(grains)

# # Assign 0th column of pca_features: xs
# xs = pca_features[:,0]

# # Assign 1st column of pca_features: ys
# ys = pca_features[:,1]

# # Scatter plot xs vs ys
# plt.scatter(xs, ys)
# plt.axis('equal')
# plt.show()

# # Calculate the Pearson correlation of xs and ys
# correlation, pvalue = pearsonr(xs, ys)

# # Display the correlation
# print(correlation)
