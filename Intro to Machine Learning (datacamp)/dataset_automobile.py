import pandas as pd

df = pd.read_csv('automobile.csv')
print(df.head())
df_origin = pd.get_dummies(df)
print(df_origin.head())
df_origin = df_origin.drop('origin_Asia', axis=1)
print(df_origin.head())

X = df.drop("origin", axis=1).values
y = df["MEDV"].values

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.3, random_state=42
# )