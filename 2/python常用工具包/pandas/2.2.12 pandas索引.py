import pandas as pd
import numpy as np
s = pd.Series(np.arange(5),index=np.arange(5)[::-1],dtype='int64')
print(s)
#获取索引
print(s.isin([1,2,3]))
#利用索引回传
print(s[s.isin([1,2,3])])
#制作多重索引
s2 = pd.Series(np.arange(6),index=pd.MultiIndex.from_product([[1,2],['a','b','c']]))
print(s2)
#定位索引
print(s2.iloc[s2.index.isin([(1,'a'),[2,'b']])])
#pandas索引中的where操作
print(s[s>2])
dates = pd.date_range('20230528',periods=8)
df = pd.DataFrame(np.random.randn(8,4),index=dates,columns=['A','B','C','D'])
print(df)
print(df.where(df<0))#不满足要求的会置为nan
#不小于0，那置为负值
print(df.where(df<0),-df)#不满足要求的会置为-value
#其他查询条件
print(df.query('(A<B)'))#直接进行列操作
print(df.query('(A<B)&(C>D)'))#多条件列操作


#选取某一列
print(df.select(lambda x:x=='A',axis='columns'))
