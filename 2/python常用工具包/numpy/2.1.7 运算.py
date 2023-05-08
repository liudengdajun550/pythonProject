#numpy中的基础运算
import numpy as np
x = np.array([4, 6])
y = np.array([2, 3])

#对应位置相乘
print(np.multiply(x,y))
#矩阵相乘
print(np.dot(x,y))#一定要注意，能够进行点乘一定是维度一致的
print(x.shape)
print(y.shape)
x.shape = 2,1 #此时与Y相乘是会报错的
print(np.dot(y,x))
# y.shape = 2,1
# print(np.dot(x,y))
#星乘会按照维度做一个自动转换
x = np.array([1,2,3])
y = np.array([[1,2,3],[4,5,6]])
print(x*y)

#双等号判断值是否相等,维度不一样会报错
x = np.array([1,2,3])
y = np.array([1,2,3])
print(x==y)
#使用np中的逻辑与,如果位置都是真返回真，非0为真
x = np.array([1,2,3])
y = np.array([0,1,3])
print(np.logical_and(x,y))
print(np.logical_or(x,y))
print(np.logical_not(x,y))
