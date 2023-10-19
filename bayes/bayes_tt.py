import pandas as pd

table = pd.DataFrame(index=['Spam','Ham'])

table['prior'] = 0.5
table['likelihood'] = 0.6, 0.2
table['unnorm'] = table['prior'] * table['likelihood']

norm_const = table['unnorm'].sum()

table['posterior'] = table['unnorm'] / norm_const
print(table)

table2 = pd. DataFrame(index=['Spam','Ham'])

table2['prior'] = table['posterior']
table2['likelihood'] = 0.4, 0.05
table2['unnorm'] = table2['prior']*table2['likelihood']

norm_const2 = table2['unnorm'].sum()
table2['posterior'] = table2['unnorm'] / norm_const2
print(table2)
