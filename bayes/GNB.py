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
for i in range(len(df_case)*len(df)):
    df_list.append(df_case[i % len(df_case)][df.target == (i // len(df_case))])

minmaxs = list()
for i in range(len(df_case)):
    minmaxs.append(df_case[i % len(df_case)].min())
    minmaxs.append(df_case[i % len(df_case)].max())

spaces = list()
for i in range(len(df_case)):
    spaces.append(np.linspace(minmaxs[2*i], minmaxs[2*i+1], 1000))

fig, axes = plt.subplots(len(df_case))

def normallization(df, x, dot, n):
    mu = df.mean()
    sigma = df.std()
    y = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    axes[n].scatter(dot, (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(dot - mu) ** 2 / (2 * sigma ** 2)))
    return y

for i in range(len(df_case)*len(df)):
    y = normallization(df_list[i], spaces[i % len(df_case)], df_case[i % len(df_case)].iloc[0], i % len(df_case))
    axes[i % len(df_case)].plot(spaces[i % len(df_case)], y)

plt.show()