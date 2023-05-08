import numpy as np
#基本数组生成使用np.array()
print(np.array([1,23,3]))
#常用的数据生成函数
'''
1.arange(10),均匀生成10以内的四个数
'''
print(np.arange(10))
#2-20每两个数+2,从start,到end,步长为2
print(np.arange(2,20,2))
#还可以指定生成的数组类型
print(np.arange(2,20,2,dtype=np.float32))

#从start到end均匀生成x个数(等距分布，包含首尾)：np.linespace
print(np.linspace(0,200,30))
#np.logspace默认10为底，从start到end均匀生成x个数(等距分布，包含首尾)
print(help(np.logspace(1,10))) #帮助文档
print(np.logspace(1,10,5))

#构造坐标
x = np.linspace(-10,10,5) #均匀分布后扩展为x轴
print(x)
y = np.linspace(-10, 10, 5)
print(y)
#依据x,y构造网格(立体索引)
x,y = np.meshgrid(x,y)
print(x)
print(y)

#构造行向量
row = np.r_[1,10,1] #1-10步长为1
col = np.c_[1,10,2]
print(row)
print(col)

#更常用的数组
#np.zeros
print(np.zeros(3)) #一维矩阵3个元素
print(np.zeros((2,3),dtype=float))#

#构造值为1的矩阵
print(np.ones((3,4)))
#构造全是x的矩阵
print(np.ones((3,3))*8)

#构造一个空的矩阵，可以使用np.empty(),生成的矩阵中值随机生成
print(np.empty(5))
rd = np.empty(5)
#可通过随机赋值进行填充
rd.fill(2)
print(rd)

#如果想要构建的矩阵与某一个矩阵形状一致，可以使用np.zero_like()进行初始化
like = np.zeros_like(rd)
print(like)
like = np.ones_like(rd)
print(like)

#生成单位矩阵
print(np.identity(5))



