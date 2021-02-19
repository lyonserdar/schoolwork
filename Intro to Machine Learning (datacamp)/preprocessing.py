import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
# import matplotlib.pyplot as plt

# plt.style.use("ggplot")
df = pd.read_csv("gapminder.csv")

# Create dummy variables: df_region
df_region = pd.get_dummies(df)
print(df.columns)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df, drop_first=True)

# Print the new columns of df_region
print(df_region.columns)



X = df_region.drop("life", axis=1).values
y = df_region["life"].values
y = y.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

ridge = Ridge(alpha=0.5, normalize=True)
ridge_cv = cross_val_score(ridge, X_train, y_train, cv=5)
print(ridge_cv)
