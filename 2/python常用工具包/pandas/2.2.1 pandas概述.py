import pandas as pd

#读取csv文件
df = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\pandas_read_file.csv')
print(df)
print(df.values)
print(df.info)
#pandas使用dataframe数据结构
#构建一个dataframe
data = {'country':['china','japan','korea'],
        'population':['13','1','0.5']}
data = pd.DataFrame(data)
print(data)
print(data.info)
#获取某一列,被称作series,也就是dataframe中的一部分
print(data['country'])
print(data.head(2))
#设定某一列作为索引
data = data.set_index('country')
print(data['population'])
data1 = {'country':['china','japan','korea'],
        'population':[13,1,0.5]}
data1 = pd.DataFrame(data1)
print('data1')
print(data1)
country = data1['country']
print(data1['population'])
population = data1['population']+1
print(population*2)
print(population.mean())
print(population.min())
print(population.max())
print(population.describe())#统计值