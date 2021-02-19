import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
df = pd.read_csv("gapminder.csv")
df.boxplot("life", "Region", rot=60)
plt.show()
