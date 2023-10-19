import pandas as pd

#ex1) 공을 하나 꺼냈을 때, 검은색
table1 = pd.DataFrame(index=['X-black', 'Y-black'])

#ex2) 공을 하나 꺼냈을 때, 흰색
table2 = pd.DataFrame(index=['X-white', 'Y-white'])

#ex3) 공을 두 번 뽑았을 때, 검은색, 검은색
table3 = pd.DataFrame(index=['X-black&black', 'Y-black&black'])

#ex4) 공을 두 번 뽑았을 때, 검은색, 흰색
table4 = pd.DataFrame(index=['X-black&white', 'Y-black&white'])


#함수로 작성
def bayesian_table(table,prior,likelihood):

    table['prior'] = prior

    table['likelihood'] = likelihood
    table['unnorm'] = table['prior'] * table['likelihood']

    norm_const = table['unnorm'].sum()

    table['posterior'] = table['unnorm'] / norm_const
    return table

prior = 0.5
likelihood = [0.1, 0.8]
table1 = bayesian_table(table1, prior, likelihood)
print(table1)

prior = 0.5
likelihood = [0.9, 0.2]
table2 = bayesian_table(table2, prior, likelihood)
print(table2)

prior = 0.5**2
likelihood = [0.1**2, 0.8**2]
table3 = bayesian_table(table3, prior, likelihood)
print(table3)

prior = 0.5**2
likelihood = [0.1*0.9, 0.2*0.8]
table4 = bayesian_table(table4, prior, likelihood)
print(table4)