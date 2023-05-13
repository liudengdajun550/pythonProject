import pandas as pd
titanic = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\titanic.csv')
#直接指定索引和列值
df = pd.DataFrame([[1,2,3],[4,5,6]],index=['a','b'],columns=['A','B','C'])
print(df)
print(df.mean())
print(df.sum(axis = 0))
print(df.sum(axis ='columns'))
print(df.median())#中位数
#做二元统计，特征与特征之间的
print(titanic.cov())#返回特征与特征之间的协方差
print(titanic.corr())#返回相关系数
print(titanic['age'].value_counts())#统计当前值的个数
print(titanic['pclass'].value_counts(ascending=False))#统计当前值的个数，并指定排序方式
print(titanic['pclass'].value_counts(ascending=False,bins=5))#统计当前值的个数，并指定排序方式,返回值分组，从最大到最小，平均分5份
print(titanic['pclass'].count())
print(help(pd.value_counts))#打印帮助文档