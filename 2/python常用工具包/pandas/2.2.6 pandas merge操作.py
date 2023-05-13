import pandas as pd
left = pd.DataFrame({'key':['k0','k1','k2','k3'],
                     'A0':['A0','A1','A2','A3'],
                     'B1':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['k0','k1','k2','k3'],
                     'C0':['C0','C1','C2','C3'],
                     'D1':['D0','D1','D2','D3']})
print(pd.merge(left,right,on='key'))
print(pd.merge(left,right))
left = pd.DataFrame({'key1':['k0','k1','k2','k5'],
                     'key2':['k0','k1','k2','k3'],
                     'A0':['A0','A1','A2','A3'],
                     'B1':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['k0','k1','k2','k4'],
                      'key2':['k0','k1','k2','k3'],
                     'C0':['C0','C1','C2','C3'],
                     'D1':['D0','D1','D2','D3']})

print(pd.merge(left,right,on=['key1','key2']))
print(pd.merge(left,right,on='key1'))
print(pd.merge(left,right,on=['key1','key2'],how='outer'))#并集
print(pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True))#打印连接方式
print(pd.merge(left,right,on=['key1','key2'],how='outer',left_index=True))#打印连接方式-左连接
print(pd.merge(left,right,on=['key1','key2'],how='outer',right_index=True))#打印连接方式-右连接

