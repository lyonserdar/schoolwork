__class__ = "ECE 3710"
__project__ = "M04 Homework"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "2/11/2021"

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6, 1000)
y = 64 / (x + 2) ** 5
plt.fill_between(x, y, 0, where=(x > 2) & (x < 4), color="lightblue")
plt.xlabel("Lifetime in years")
plt.ylabel("Probability density function")
plt.plot(x, y)
plt.show()
