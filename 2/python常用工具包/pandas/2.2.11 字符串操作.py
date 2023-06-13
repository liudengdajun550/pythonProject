import pandas as pd
import numpy as np
s=pd.Series(['A','b','B','grae','GAEs',np.nan])
print(s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
#去除空格
str_space_remove=pd.Index(['tang  ','  yu','di'])
print(str_space_remove.str.strip())
print(str_space_remove.str.lstrip())#左边空格
#更换列名
df = pd.DataFrame(np.random.randn(3,2),columns=['A a','B b'],index=range(3))
print(df)
print(df.columns.str.replace(' ','_'))
print(df)
#字符串切分
s=pd.Series(['a_c_s','s_w_e'])
print(s)
print(s.str.split('_'))
print(s.str.split('_',expand=True))
#限制切分几次
print(s.str.split('_',expand=True,n=1))
#判断是否包含某些元素
print(s.str.contains('a'))

s=pd.Series(['a','A|B','c|d'])
print(s)
print(s.str.get_dummies(sep='|'))


