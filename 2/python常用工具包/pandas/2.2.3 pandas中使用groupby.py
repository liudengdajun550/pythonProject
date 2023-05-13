import pandas as pd

df = pd.DataFrame({'key':['a','b','c','a','b','c','a','b','c'],
                   'data':[0,5,10,5,10,15,10,25,20]})
print(df)
for key in ['a','b','c']:
    print(key,df[df['key'] == key].sum())
print(df.groupby('key').sum())
import numpy as np
print(df.groupby('key').aggregate(np.sum))#使用nadarry
titanic = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\titanic.csv')
print(titanic.groupby('sex')['age'].mean())

print(titanic.groupby('sex')['survived'].mean())