import numpy as np
deng_array = np.array([[1.5,1.3,7.5],
                       [5.6,7.8,1.2]])
print(deng_array)
print(np.sort(deng_array))#排序
print(np.sort(deng_array,axis=0))
print(deng_array)
print(np.argsort(deng_array)) #获取排序前的位置索引
#[0,10]均匀构造10个数
deng_array = np.linspace(0,10,10)
print(deng_array)
#插入数据到deng_array
values = [2.34,4,67]
print(np.searchsorted(deng_array,values))#排序好的数组才能使用该函数，打印插入数据在原数组的位置
#第3个列升序条件下第1个列降序
deng_array1 = [[1,0,6],
               [1,7,0],
               [2,3,1],
               [2,4,0]]
index =np.lexsort([-1*deng_array1[:, 0], deng_array1[:, 2]]) #有问题，待确认
print(index)
deng_array1 = deng_array1[index]
print(deng_array1)