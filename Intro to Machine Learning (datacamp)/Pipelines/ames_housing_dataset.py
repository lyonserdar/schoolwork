from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

df_origin = pd.read_csv("ames_housing_dataset.csv")


def main():
    print(df_origin.head())
    print(df_origin.info())
    print(df_origin.describe())


if __name__ == "__main__":
    main()
