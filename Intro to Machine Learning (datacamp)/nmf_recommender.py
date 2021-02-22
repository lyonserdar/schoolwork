# Apply NMF to the word-frequency array
from sklearn.decomposition import NMF

articles = []
nmf = NMF(n_components=6)
nmf_features = nmf.fit_transform(articles)

from sklearn.preprocessing import normalize

norm_features = normalize(nmf_features)
# if has index 23
current_article = norm_features[23, :]
similarities = norm_features.dot(current_article)
print(similarities)

import pandas as pd

titles = []
norm_features = normalize(nmf_features)
df = pd.DataFrame(norm_features, index=titles)
current_article = df.loc['Dog bites man']
similarities = df.dot(current_article)
print(similarities.nlargest())

### All in one
# # Perform the necessary imports
# from sklearn.decomposition import NMF
# from sklearn.preprocessing import Normalizer, MaxAbsScaler
# from sklearn.pipeline import make_pipeline
# # Create a MaxAbsScaler: scaler
# scaler = MaxAbsScaler()
# # Create an NMF model: nmf
# nmf = NMF(n_components=20)
# # Create a Normalizer: normalizer
# normalizer = Normalizer()
# # Create a pipeline: pipeline
# pipeline = make_pipeline(scaler, nmf, normalizer)
# # Apply fit_transform to artists: norm_features
# norm_features = pipeline.fit_transform(artists)
# # Import pandas
# import pandas as pd
# # Create a DataFrame: df
# df = pd.DataFrame(norm_features, index=artist_names)
# # Select row of 'Bruce Springsteen': artist
# artist = df.loc['Bruce Springsteen']
# # Compute cosine similarities: similarities
# similarities = df.dot(artist)
# # Display those with highest cosine similarity
# print(similarities.nlargest())
