#create histogram
import numpy as np
import matplotlib.pyplot as plt

n_data = 100

x_data = np.random.normal(loc=5, scale=5, size=(n_data,))

plt.hist(x_data)
plt.show()