###
# TODO: Work In Progress - OneHotEncoder categorical_features is deprecated


# Import OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

# Import DataFrame
from ames_housing_dataset import df_origin

df = df_origin.copy()

# Fill missing values with 0
df.LotFrontage = df["LotFrontage"].fillna(0)

# Create a boolean mask for categorical columns
categorical_mask = df.dtypes == object

# Get list of categorical column names
categorical_columns = df.columns[categorical_mask].tolist()
print(df[categorical_columns].head())
print(df.columns)

# Create OneHotEncoder
# ohe = OneHotEncoder(categorical_features=categorical_columns, sparse=False)
ohe = OneHotEncoder()

# Apply OneHotEncoder to categorical columns
# (output is no longer a dataframe)
df_encoded = ohe.fit_transform(df)

# Print first 5 rows of the resulting dataset
print(df_encoded[:5, :])

# Print the shape of the original DataFrame
print(df.shape)

# Print the shape of the transformed array
print(df_encoded.shape)


# # Get list of categorical column names
# categorical_columns = df.columns[categorical_mask].tolist()

# # Print the head of the categorical columns
# print(df[categorical_columns].head())

# # Create LabelEncoder object: le
# le = LabelEncoder()

# # Apply LabelEncoder to categorical columns
# df[categorical_columns] = df[categorical_columns].apply(lambda x: le.fit_transform(x))

# # Print the head of the LabelEncoded categorical columns
# print(df[categorical_columns].head())
