import pandas as pd

print(pd.get_option('display.max_rows'))
print(pd.set_option('display.max_rows',100))#设置打印的最大行数
print(pd.Series(index=range(100)))#生成样本
print(pd.get_option('display.max_columns'))
print(pd.set_option('display.max_columns',100))#设置打印的最大列数
print(pd.DataFrame(columns=range(0,30)))#生成30列
print(pd.Series(index=['A'],data=['t'*70]))
print(pd.set_option('display.max_colwidth',100))#设置打印的字符串长度
print(pd.Series(index=['A'],data=['t'*70]))
print(pd.get_option('display.precision'))#设置精度
data = pd.Series(index=['a'],data=1.2345346312433)
print(pd.set_option('display.precision',20))
print(data)
