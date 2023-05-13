import pandas as pd
example = pd.DataFrame({'Month':['Jan','jan','jan','jan',
                                    'fre','fre','fre','fre',
                                    'mar','mar','mar','mar'],
                           'Category':['Transport','Grocery','household','Entertainment',
                                       'Transport','Grocery','household','Entertainment',
                                       'Transport','Grocery','household','Entertainment'],
                           'Amout':[74,235,123,121,100,123,234,56,23,34,78,79]})
print(example)
#考虑多个变量之间的
example_pivot=example.pivot(index='Category',columns='Month',values='Amout') #按category维度统计指标Month的值Amount
print(example_pivot)
print(example_pivot.sum(axis=1))
print(example_pivot.sum(axis=0))

df = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\titanic.csv')
print(df)
print(df.pivot_table(index='sex',columns='pclass',values='fare'))#默认求平均值
print(df.pivot_table(index='sex',columns='pclass',values='fare',aggfunc=max))#默认求最大值
print(df.pivot_table(index='sex',columns='pclass',values='fare',aggfunc=min))#默认求最大值
print(df.pivot_table(index='sex',columns='pclass',values='fare',aggfunc='count'))#默认求数量
#计数：crosstab
print(pd.crosstab(index=df['sex'],columns=df['pclass']))
#
print(df.pivot_table(index='pclass',columns='sex',values='survived',aggfunc='mean'))#默认求最大值
df['underaged'] = df['age']<=18
print(df.pivot_table(index='underaged',values='survived',aggfunc='count'))#默认求最大值
