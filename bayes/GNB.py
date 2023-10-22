from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

setosa_df = df[df.target == 0]
versicolor_df = df[df.target == 1]
virginica_df = df[df.target == 2]

setosa_df_sl = setosa_df['sepal length (cm)']
setosa_df_sw = setosa_df['sepal width (cm)']
setosa_df_pl = setosa_df['petal length (cm)']
setosa_df_pw = setosa_df['petal width (cm)']
versicolor_df_sl = versicolor_df['sepal length (cm)']
versicolor_df_sw = versicolor_df['sepal width (cm)']
versicolor_df_pl = versicolor_df['petal length (cm)']
versicolor_df_pw = versicolor_df['petal width (cm)']
virginica_df_sl = virginica_df['sepal length (cm)']
virginica_df_sw = virginica_df['sepal width (cm)']
virginica_df_pl = virginica_df['petal length (cm)']
virginica_df_pw = virginica_df['petal width (cm)']

fig, axes = plt.subplots(4)
min_sl = df['sepal length (cm)'].min()
max_sl = df['sepal length (cm)'].max()
min_sw = df['sepal width (cm)'].min()
max_sw = df['sepal width (cm)'].max()
min_pl = df['petal length (cm)'].min()
max_pl = df['petal length (cm)'].max()
min_pw = df['petal width (cm)'].min()
max_pw = df['petal width (cm)'].max()

x_sl = np.linspace(min_sl, max_sl, 1000)
x_sw = np.linspace(min_sw, max_sw, 1000)
x_pl = np.linspace(min_pl, max_pl, 1000)
x_pw = np.linspace(min_pw, max_pw, 1000)

def JG(df, x, dot, n):
    mu = df.mean()
    sigma = df.std()
    y = (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(x - mu) ** 2 / (2 * sigma ** 2))
    axes[n].scatter(dot, (1 / np.sqrt(2 * np.pi * sigma ** 2)) * np.exp(-(dot - mu) ** 2 / (2 * sigma ** 2)))
    return y

y = JG(setosa_df_sl, x_sl, df['sepal length (cm)'].iloc[0], 0)
axes[0].plot(x_sl, y)
y = JG(setosa_df_sw, x_sw, df['sepal width (cm)'].iloc[0], 1)
axes[1].plot(x_sw, y)
y = JG(setosa_df_pl, x_pl, df['petal length (cm)'].iloc[0], 2)
axes[2].plot(x_pl, y)
y = JG(setosa_df_pw, x_pw, df['petal width (cm)'].iloc[0], 3)
axes[3].plot(x_pw, y)
y = JG(versicolor_df_sl, x_sl, df['sepal length (cm)'].iloc[0], 0)
axes[0].plot(x_sl, y)
y = JG(versicolor_df_sw, x_sw, df['sepal width (cm)'].iloc[0], 1)
axes[1].plot(x_sw, y)
y = JG(versicolor_df_pl, x_pl, df['petal length (cm)'].iloc[0], 2)
axes[2].plot(x_pl, y)
y = JG(versicolor_df_pw, x_pw, df['petal width (cm)'].iloc[0], 3)
axes[3].plot(x_pw, y)
y = JG(virginica_df_sl, x_sl, df['sepal length (cm)'].iloc[0], 0)
axes[0].plot(x_sl, y)
y = JG(virginica_df_sw, x_sw, df['sepal width (cm)'].iloc[0], 1)
axes[1].plot(x_sw, y)
y = JG(virginica_df_pl, x_pl, df['petal length (cm)'].iloc[0], 2)
axes[2].plot(x_pl, y)
y = JG(virginica_df_pw, x_pw, df['petal width (cm)'].iloc[0], 3)
axes[3].plot(x_pw, y)

print(df['sepal length (cm)'].iloc[0])
plt.show()