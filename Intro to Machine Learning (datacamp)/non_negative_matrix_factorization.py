from sklearn.decomposition import NMF

samples = []
model = NMF(n_components=2)
model.fit(samples)
nfl_features = model.transform(samples)
print(nmf_features.round(2))

# # Import pandas
# import pandas as pd
# # Create a pandas DataFrame: df
# df = pd.DataFrame(nmf_features, index=titles)
# # Print the row for 'Anne Hathaway'
# print(df.loc['Anne Hathaway'])
# # Print the row for 'Denzel Washington'
# print(df.loc['Denzel Washington'])

# Import pandas
# import pandas as pd
# # Create a DataFrame: components_df
# components_df = pd.DataFrame(model.components_, columns=words)
# # Print the shape of the DataFrame
# print(components_df.shape)
# # Select row 3: component
# component = components_df.iloc[3]
# # Print result of nlargest
# print(component.nlargest())


# def show_as_image(sample):
#     bitmap = sample.reshape((13, 8))
#     plt.figure()
#     plt.imshow(bitmap, cmap='gray', interpolation='nearest')
#     plt.colorbar()
#     plt.show()

### Led digits dataset
# Import pyplot
# from matplotlib import pyplot as plt
# # Select the 0th row: digit
# digit = samples[0,:]
# # Print digit
# print(digit)
# # Reshape digit to a 13x8 array: bitmap
# bitmap = digit.reshape(13, 8)
# # Print bitmap
# print(bitmap)
# # Use plt.imshow to display bitmap
# plt.imshow(bitmap, cmap='gray', interpolation='nearest')
# plt.colorbar()
# plt.show()
# Import NMF
# from sklearn.decomposition import NMF
# # Create an NMF model: model
# model = NMF(n_components=7)
# # Apply fit_transform to samples: features
# features = model.fit_transform(samples)
# # Call show_as_image on each component
# for component in model.components_:
#     show_as_image(component)
# # Assign the 0th row of features: digit_features
# digit_features = features[0, :]
# # Print digit_features
# print(digit_features)

# Import PCA
# from sklearn.decomposition import PCA
# # Create a PCA instance: model
# model = PCA(n_components=7)
# # Apply fit_transform to samples: features
# features = model.fit_transform(samples)
# # Call show_as_image on each component
# for component in model.components_:
#     show_as_image(component)
    