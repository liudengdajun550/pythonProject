# numpy 数组的数值计算
import numpy as np
deng_array = np.array([[4,7,3],
                       [4,5,6]])
print(deng_array)
print(np.sum(deng_array))
#指定沿着哪个方向（轴或者维度）进行加和
print(np.sum(deng_array,axis=0))
#看一下有几个轴
print(deng_array.ndim)
#按轴求和
print(np.sum(deng_array, axis=1))
print(np.sum(deng_array, axis=-1))
print(deng_array.sum(axis=1))
print(deng_array.sum(axis=0))
print(deng_array.sum())

#按轴求积
print(deng_array.prod())
print(deng_array.prod(axis=1))
print(deng_array.prod(axis=0))

#求最大值最小值
print(deng_array.min())
print(deng_array.min(axis=1))#获取每一行的最小值
print(deng_array.min(axis=0))#获取每一列的最小值
print(deng_array.max())
print(deng_array.max(axis=1))#获取每一行的最大值
print(deng_array.max(axis=0))#获取每一列的最大值
#获取最大值所在位置
print(deng_array.argmax())
print(deng_array.argmin())
print(deng_array.argmax(axis=1))

#计算均值
print(deng_array.mean())
print(deng_array.mean(axis=0)) #列均值

#标准差
print(deng_array.std())
print(deng_array.std(axis=0))

#方差
print(deng_array.var())
print(deng_array.var(axis=0))

#数值限制clip(a,b),小于a的值都会变为a,大于b的值都会变为b,为什么没效果嘞
print(deng_array)
deng_array.clip(3, 3)
print(deng_array)

#四舍五入
deng_array1 = np.array([1,2,4.28,3.56])
print(deng_array1.round())
#指定四舍五入的精度
print(deng_array1.round(decimals=1))

