import pandas as pd

df = pd.read_csv("PlayTennis.csv")
table = pd.DataFrame(index=['Spam', 'Ham'])
print(df)
print(df['Play Tennis'].count())
print(df['Play Tennis'].value_counts())

def bayesian_table(table,prior,likelihood):
    table['prior'] = prior

    table['likelihood'] = likelihood
    table['unnorm'] = table['prior'] * table['likelihood']

    norm_const = table['unnorm'].sum()

    table['posterior'] = table['unnorm'] / norm_const
    return table

prior = 0.5
likelihood = [0.6, 0.2]
table = bayesian_table(table, prior, likelihood)