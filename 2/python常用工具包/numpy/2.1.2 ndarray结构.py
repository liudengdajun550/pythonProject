import numpy as np

# 对于ndarry来说列表中元素必须是同一类型，如果不是就向下兼容
deng_list = [1, 2, 3, 4, 5]
deng_list = np.array(deng_list)
print(deng_list)
print(type(deng_list))
# ndarry属性
print(deng_list.dtype)  # 当前列表中值的数据类型
print(deng_list.itemsize)  # 查看当前类型占用了多少字节
print(deng_list.shape)
print(deng_list.size)
print(deng_list.ndim)  # 查看数组维度
# 填充操作
deng_list.fill(0)
print(deng_list)

# ndarry的索引和切片，注意不要越界,与python都一样
print(deng_list[-2:])
# 矩阵格式
deng_list1 = [[1, 2, 3],
              [2, 3, 4],
              [7, 8, 9]]
print(deng_list1)
deng_list1 = np.array(deng_list1)
deng_list1.fill(0)
print(deng_list1)
print(deng_list1.ndim)
print(deng_list1.size)
# 矩阵取值，按维度的索引取值
deng_list2 = [[1, 2, 3],
              [2, 3, 4],
              [7, 8, 9]]
print(deng_list2)
deng_list2 = np.array(deng_list2)
print(deng_list2[1, 1])  # 第二行第二列3,第一维的第2个元素，第二维的第二个元素
print(deng_list2[1])
print(deng_list2[:, 1])  # 第一维全部元素，第二维的全部元素[x,1]
print(deng_list2[:, 0:2])
print(deng_list2[0, 0:2])
deng_list2[1][1] = 100
print(deng_list2)

# ndarry拷贝
deng_list3 = deng_list2  # 内存引用，操作3会影响2
deng_list3[1][1] = 20
print(deng_list3)
print(deng_list2)
deng_list4 = deng_list2.copy()  # 深拷贝
deng_list4[1][1] = 30
print(deng_list4)
print(deng_list2)

# nadrray等差数组[)
deng_list = np.arange(1, 10, 2)
print(deng_list)

# 指定ndarray中数据类型
mask = np.array([-1, 0.5, 4, 1, 0], dtype=bool)
print(mask)
# 利用bool类型作为数据筛选方式，为true的值被挑选出来，取不取值
print(deng_list[mask])

# 随机产生数
random_val = np.random.rand(5)  # 随机产生10个（0，1）的数
print(random_val)
mask = random_val > 0.5  # 通过随机数构造bool类型结果
print(mask)
print(deng_list[mask])

# 获取值>30的值的索引
print(deng_list > 3)
print(np.where(deng_list > 3))
print(type(np.where(deng_list > 3)))  # tuple也可以转为ndarry
print(np.array(np.where(deng_list > 3)))

#指定array数据类型
deng_list5 = np.array([1,2,3,4,5],dtype=np.float32)
print(deng_list5.dtype) #类型
print(deng_list5.nbytes)#每个元素所占字节数
#如果array中各种类型数据都有
deng_list5 = np.array([1,2.2,"zhonwen"],dtype=np.object)
print(deng_list5)
print(deng_list5*2)

#重新构造
deng_list5 = np.array([1,2,3,4,5])
deng_list6 = np.asarray(deng_list5,dtype=np.float32)
print(deng_list6)
print(deng_list6.astype(np.int))
print(deng_list5)



