# Import DictVectorizer
from sklearn.feature_extraction import DictVectorizer

# Import DataFrame
from ames_housing_dataset import df_origin

df = df_origin.copy()

# Convert df into a dictionary: df_dict
df_dict = df.to_dict("records")

# Create the DictVectorizer object: dv
dv = DictVectorizer(sparse=False)

# Apply dv on df: df_encoded
df_encoded = dv.fit_transform(df_dict)

# Print the resulting first five rows
print(df_encoded[:5,:])

# Print the vocabulary
print(dv.vocabulary_)