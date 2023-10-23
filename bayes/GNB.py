from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

df_case = list()
df_case.append(df['sepal length (cm)'])
df_case.append(df['sepal width (cm)'])
df_case.append(df['petal length (cm)'])
df_case.append(df['petal width (cm)'])

df_list = list()
for i in range(12):
    df_list.append(df_case[i % 4][df.target == (i // 4)])

minmaxs = list()
for i in range(4):
    minmaxs.append(df_case[i % 4].min())
    minmaxs.append(df_case[i % 4].max())

spaces = list()
for i in range(4):
    spaces.append(np.linspace(minmaxs[2*i], minmaxs[2*i+1], 1000))

fig, axes = plt.subplots(4)

def JG(df, x, dot, n):
    mu = df.mean()
    sigma = df.std()
    y = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    axes[n].scatter(dot, (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(dot - mu) ** 2 / (2 * sigma ** 2)))
    return y

for i in range(12):
    y = JG(df_list[i], spaces[i % 4], df_case[i % 4].iloc[0], i % 4)
    axes[i % 4].plot(spaces[i % 4], y)

plt.show()