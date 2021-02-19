from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df = pd.read_csv("congress.csv")

# X = dataset.drop("diabetes", axis=1).values
# y = dataset["diabetes"].values
# y = y.reshape(-1, 1)

df[df == '?'] = np.nan
print(df.isnull().sum())
print("Shape of original DataFrame:", df.shape)
df = df.dropna()
print("Shape of DataFrame after dropping NaNs", df.shape)

def main():
    pass


if __name__ == "__main__":
    main()
