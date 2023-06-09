import pandas as pd
data = pd.DataFrame({'group':['a','a','a','b','b','b','c','c','c'],
                     'data':[1,2,32,4,5,6,7,8,9]})
print(data)
#升序和降序：按照某些方式进行排序
print(data.sort_values(by=['data','group'],ascending=[True,False],inplace=True))
data = pd.DataFrame({'k1':['one']*3+['two']*3,
                     'k2':[2,2,4,1,2,3]})
print(data)
#按单键值排序
print(data.sort_values(by='k2'))
#去重
print(data.drop_duplicates())
#按照某一维度去重
print(data.drop_duplicates(subset='k1'))

element = pd.DataFrame({'food':['A1','A2','B1','B2','C1','C2'],'data':[1,2,3,1,2,3]})
print(element)
#接下来我们使用函数方式进行参数处理
def food_map(series):
    if series['food'] == 'A1':
        return 'A'
    elif series['food'] == 'A2':
        return 'A'
    elif series['food'] == 'B1':
        return 'B'
    elif series['food'] == 'B2':
        return 'B'
    elif series['food'] == 'C1':
        return 'C'
    elif series['food'] == 'C2':
        return 'C'
#对数据集应用函数
element['food_map'] = element.apply(food_map,axis='columns') #自动判断列
print(element)
#使用map方式获取数据集，需要定义为字典结构
element_upper = {
    'A1':'A',
    'A2':'A',
    'B1':'B',
    'B2': 'B',
    'C1':'C',
    'C2':'C'
}
element['upper'] = element['food'].map(element_upper)
print(element)

#快速构造数据
import numpy as np
data = pd.DataFrame({'data1':np.random.randn(5),
                    'data2':np.random.randn(5)})
print(data)
#设置特征进行处理:增加一列，进行计算
data = data.assign(ration=data['data1']/data['data2'])
print(data)
data.drop('ration',axis='columns',inplace=True)
print(data)
#在列和行上替换一些值,多个值就list方式替换
element = element.replace('A1','D2')
print(element)
#对我的连续值做离散化
ages = [12,11,2,3,4,5,6,2,3,4]
#离散化的区间
bins = [1,5,10,20]
#获取值是在那个区间的
bins_cut = pd.cut(ages,bins)
print(bins_cut)
#统计各区间的值有多少
print(pd.value_counts(bins_cut))
#按照区间分组
group_names = ['young','middle','old']
bin_res = pd.cut(ages,[1,5,10,20],labels=group_names)
print(bin_res)
print(pd.value_counts(bin_res))
#数据中有缺失值要如何查找？
df = pd.DataFrame([range(3),[0,np.nan,0],[0,0,np.nan],range(3)])
print(df)
print(df.isnull().any())#按列查看
print(df.isnull().any(axis=1))#按行查看
#如果有缺失值，使用什么进行填充
print(df.fillna(5))
#定位缺失值
print(df[df.isnull().any(axis=1)])


