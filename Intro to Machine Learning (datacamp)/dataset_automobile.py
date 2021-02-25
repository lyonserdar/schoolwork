import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('automobile.csv')
# print(df.head())
df_origin = pd.get_dummies(df)
# print(df_origin.head())
df_origin = df_origin.drop('origin_Asia', axis=1)
# print(df_origin.head())

X = df_origin.drop("mpg", axis=1).values
y = df_origin["mpg"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)