import pandas as pd
#series结构的增删改查，属于ndarray结构
data = [10,11,12]
index = ['a','b','c']
s = pd.Series(data=data,index=index)
#查操作
print(s[0])
mask = [True,False,False]
print(s[mask])
print(s.loc['b'])
print(s.iloc[1])
s1=s.copy()
s1['a']=1
print(s1,s)
#改
#替换某个值为另一个
s1.replace(to_replace=1,value=101,inplace=True)
print(s1)
print(s1.index)
s1.index=['a','b','d']#替换索引
print(s1.index)
s1.rename(index={'a':'A'},inplace=True)#替换某个索引
print(s1.index)
#增
s2 =s1.copy()
s2.append(s1,ignore_index=False)#是否构造新的索引，增加多个值
print(s2)
s2['j'] = 200 #增加一个值
print(s2)
#删除
del s2['A']
print(s2)
s2.drop(['b','j'],inplace=True)#删除并生效
print(s2)
#Dataframe结构的增删改查
data = [[1,2,4],[3,5,6]]
index = ['a','b']
columns = ['A','B','C']
df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)
#通过值查询
print(df.loc['a'])
#通过列查询
print(df.iloc[1])

#dataframe改数据
df.loc['a']['A'] = 5
print(df)
#改索引值
df.index=['f','g']
print(df)
#增操作
data = [[1,2,4],[3,5,6]]
index = ['a','b']
columns = ['A','B','C']
df2 = pd.DataFrame(data=data,index=index,columns=columns)
print(df2)
df3 = pd.concat([df,df2],axis=1)#一定要保证维度是一样的
print(df3)
#增加一行
df2['xiaofan'] = [10,11]
print(df2)
#增加多列
df4 = pd.DataFrame([[10,11],[12,13]],index=['j','k'],columns=['D','E'])
print(df4)
df5 = pd.concat([df2,df4],axis=1)
print(df5)
#删除操作
df5.drop(['j'],axis=0,inplace=True)#按行删除
print(df5)
del df5['D'] #按列删除
print(df5)
#也可以删除多列
df5.drop(['C','xiaofan'],axis=1,inplace=True)
print(df5)




