#大数据量对于内存的压力比较大，所以需要关注数据的量级
import numpy as np
import pandas as pd
g1 = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\game_logs.csv')
print(g1.head())
print(g1.shape)
#查看当前内存的使用量
print(g1.info(memory_usage = 'deep'))
#查看不同类型占用的内存大小
for dtype in ['float64','int64','object']:
    selected_dtype = g1.select_dtypes(include=[dtype])
    mean_usage_b = selected_dtype.memory_usage(deep=True).mean()
    mean_usage_mb = mean_usage_b/1024**2
    print('平均内存占用：',dtype,mean_usage_mb)
#查看不同类型，能表示的最大范围值
int_types = ['uint8','int8','int16','int32','int64']
for it in int_types:
    print(np.iinfo(it))

#内存占用的比较与计算
def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep=True)
    usage_mb = usage_b/1024**2
    return '{:03.2f}MB'.format(usage_mb) #重点关注打印精度
g1_int = g1.select_dtypes(include=['int64'])#重点关注include中的类型
conver_int = g1_int.apply(pd.to_numeric,downcast='unsigned')
print(mem_usage(g1_int))
print(mem_usage(conver_int))
#同理float类型
g1_float = g1.select_dtypes(include=['float64'])#重点关注include中的类型
conver_float = g1_int.apply(pd.to_numeric,downcast='float')
print(mem_usage(g1_float))
print(mem_usage(conver_float))

#查看优化后的内容
optimized_g1 = g1.copy()
optimized_g1[conver_int.columns] = conver_int
optimized_g1[conver_float.columns] = conver_float
print(mem_usage(g1))
print(mem_usage(optimized_g1))

#处理对象类型
g1_object = g1.select_dtypes(include=['object']).copy()
print(g1_object.describe())
#考虑相同值指向同一块内存
dow = g1_object.day_of_week
print(dow.head())
#直接指定类型
dow_cat = dow.astype('category')
print(dow_cat.head())
print(mem_usage(dow))
print(mem_usage(dow_cat))

#对当前大数据进行分析，如果重复量大于50%要分类处理
converted_obj = pd.DataFrame()

for col in g1_object.columns:
    num_unique_values = len(g1_object[col].unique())
    num_total_values = len(g1_object[col])
    if num_unique_values / num_total_values < 0.5:
        converted_obj.loc[:,col] = g1_object[col].astype('category')#超过0.5变为category类型
    else:
        converted_obj.loc[:,col] = g1_object[col]
print(mem_usage(g1))
print(mem_usage(converted_obj))

#日期类型的处理
date = optimized_g1.date
print(date[:5])
print(mem_usage(date))
#优化datetime格式
optimized_g1['date'] = pd.to_datetime(date,format='%Y%m%d')
print(mem_usage(optimized_g1['date']))