#转换数据的形状
import numpy as np
deng_array = np.arange(10) #生成0-10之间的均匀10个数
print(deng_array)
print(deng_array.shape) #查看当前矩阵的形状
#变换列表形状
deng_array.shape = 2, 5 #2行5列，由一维数组变为二维矩阵
print(deng_array)
#换一种变换方式
deng_array = deng_array.reshape(1,10) #注意元素数量是一样的（大小一定要一致）
print(deng_array)
#
deng_array1 = np.arange(10) #生成0-10之间的均匀10个数
print(deng_array1.shape) #查看当前的形状一维数组，当前元素有10个值
#通过维度参数变换形状
deng_array1 = deng_array1[np.newaxis,:]
print(deng_array1.shape) #查看当前矩阵的形状,二维数组，其中第一个元素有10个值
deng_array1 = deng_array1[:,np.newaxis,np.newaxis]
print(deng_array1.shape) #查看当前矩阵的形状,二维数组，其中第一个元素有10个值
print(deng_array1) #查看当前矩阵的形状,二维数组，其中第一个元素有10个值
#使用压缩方式进行存储:把所有空的轴去掉
deng_array2 = np.squeeze(deng_array1)
print(deng_array2)
print(deng_array2.shape)
#对矩阵进行转至
deng_array2.shape = 2,5
print(deng_array2)
deng_array3 = deng_array2.transpose()
print(deng_array3)
print(deng_array3.shape)
#方法名的缩写T
print(deng_array3.T)
print(deng_array3)

#数组的拼接
a = np.array([[123,234,345],[456,567,789]])
b = np.array([[11,22,33],[44,55,66]])
#将两个矩阵以元组形式传到concatenate（(a,b)）才可连接,直接在末尾安维度拼接（默认按第一维度拼接）
c = np.concatenate((a,b))
print(c)
#按照其他维度进行拼接
d= np.concatenate((a,b),axis=1)
print(d)
#其他拼接方法：vstack（axio=0）,hstack(axios=1)
print(np.vstack((a,b)))
print(np.hstack((a,b)))

#将维度拉平为一维
print(a.flatten())
print(a.ravel())
