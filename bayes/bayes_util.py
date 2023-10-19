import pandas as pd

table = pd.DataFrame(index=['Spam', 'Ham'])

def bayesian_table(table,prior,likelihood):

    #posterior이 table.columns에 있다면 prior를 posterior로 만들어준다.
    if 'posterior' in table.columns :
        table['prior'] = table['posterior']
    else :
        table['prior'] = prior

    table['likelihood'] = likelihood
    table['unnorm'] = table['prior'] * table['likelihood']

    norm_const = table['unnorm'].sum()

    table['posterior'] = table['unnorm'] / norm_const
    return table

prior = 0.5
likelihood = [0.6, 0.2]
table = bayesian_table(table, prior, likelihood)
print(table)

likelihood = [0.4,0.05]
table = bayesian_table(table,prior,likelihood)
print(table)