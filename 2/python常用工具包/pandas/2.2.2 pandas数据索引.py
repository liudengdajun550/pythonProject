import pandas as pd
titanic = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\titanic.csv')
print(titanic)
print(titanic['age'][:5])
print(titanic[['fare','age']][:5])#两列传值的时候要作为一个整体传值
#loc:使用label进行定位
#iloc:用position定位
print(titanic.iloc[0:5])
print(titanic.iloc[0:5,1:3])
print(titanic.head(5))
df = titanic.set_index('embark_town')
print(df.loc['Southampton','fare'])#按值定位
df.loc['Southampton','fare'] = 1000#赋值
print(df.loc['Southampton','fare'])#按值定位

#bool类型的索引
print(df['fare']>40)#索引
print(df[df['fare']>40])#用bool类型做索引
print(df.loc[df['sex'] == 'male','age'].mean())