from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.style.use("ggplot")
iris = datasets.load_iris()
print(type(iris))
print(iris.keys())
print(iris.target_names)

X = iris['data']
y = iris['target']

df = pd.DataFrame(X, columns=iris['feature_names'])

print(df.head())
print(df.info())
print(df.describe())

pd.plotting.scatter_matrix(df, c=y, figsize=[8,8], s=150, marker='D')
plt.show()

# If dataset is binary Seaborn's countplot is more useful.
# plt.figure()
# sns.countplot(x='education', hue='party', data=df, palette='RdBu')
# plt.xticks([0,1], ['No', 'Yes'])
# plt.show()