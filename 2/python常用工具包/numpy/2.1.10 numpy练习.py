import numpy
import numpy as np

'''
打印numpy版本号
'''
print(numpy.__version__)
'''
构造全零的矩阵，并打印所占内存大小
'''
zero_size = np.zeros((3,4))
print(zero_size.size * zero_size.itemsize)
'''
打印函数的帮助文档
'''
print(help(numpy.add.__doc__))
print(numpy.add.__doc__)
'''
创建一个10-49的数组，并将其倒叙展示
'''
list=numpy.arange(10,50,1)
print(list[::-1])
'''
找出数组中不为0的索引
'''
list=[0,2,3,4,0,0,0,34,46,9]
print(numpy.nonzero(list))
'''
随机构造一个3*3矩阵，并打印其中的最大值和最小值
'''
list = np.arange(1,10,1)
list = list.reshape(3,3)
print(list)
print(numpy.min(list))
print(numpy.max(list))

list = np.random.random((3,3))
print(list)
print(list.min())
print(list.max())

'''
构造一个5*5矩阵，其中全部填充为1，并在外圈补充一圈0
'''
#numpy中有个pad函数可进行边界填充
list = numpy.ones((5,5))
list = numpy.pad(list,1,constant_values=0)
print(list)

'''
构建一个（6,7,8）的矩阵，并找到第100个元素的索引值
'''
list = numpy.random.random((6,7,8))
#查找元素的索引值函数
index = numpy.unravel_index(100,(6,7,8))
print(index)

'''
对一个5*5矩阵做归一化
'''
list = np.random.random((5,5))
#归一化需要获取最大值和最小值？
min = numpy.min(list)
max = numpy.max(list)
list = (list-min)/(max-min)
print(list)
'''
找到两个数组中相值同的数据
'''

list1 = numpy.random.randint(1,10,10)
list2 = numpy.random.randint(2,20,10)
print(list1)
print(list2)
#获取数组的交集
print(numpy.intersect1d(list1,list2))
'''
获取昨天、今天、明天的日期
'''
yesterday = np.datetime64('today','D') - np.timedelta64(1,'D')
print(yesterday)
today = np.datetime64('today','D')
print(today)
tommorow = np.datetime64('today','D') + np.timedelta64(1,'D')
print(tommorow)

'''
得到一个月的所有天
'''
print(np.arange('2023-07','2023-08',dtype='datetime64[D]'))

'''
得到一个数的整数部分
'''
#指定随机数范围
random_list = np.random.uniform(0,10,10)
print(random_list)
#获取整数部分
print(numpy.floor(random_list))
#向上取整
print(numpy.ceil(random_list))

'''
构建一个数组希望他不会被改变
'''
cannotchange = np.arange(5)
# cannotchange.flags.writeable = False
cannotchange[0] = 1
print(cannotchange)
'''
打印大数据中的部分值和全部值
'''
print_option = np.zeros((15,15))
print(print_option)
np.set_printoptions(threshold=5) #np.nan打印所有数据
print_option2 = np.zeros((15,15))
print(print_option2)

'''
找到最接近一个数的索引
'''
closing_index = np.arange(100) #好寻找的数组
closing_index2 = np.random.uniform(0,100) #随机取一个数
print(closing_index2)
index = (np.abs(closing_index-closing_index2)).argmin()#数组的索引
print(closing_index[index])

'''
将32位的float类型转为32位的int类型
'''
z = np.arange(10, dtype=np.int32)
print(z.dtype)
z = z.astype(dtype=np.float32)
print(z.dtype)
'''
打印数组元素坐标和值,numpy中函数ndenumerate
'''
z = np.arange(9).reshape((3,3))
for index,value in np.ndenumerate(z):
    print("%d:%d"%index%value)
    print(index,value)

'''
数组按照某一维进行排序
'''
z = np.random.randint(1,10,(3,3))
print(z)
print(z[z[:,2].argsort()]) #指定按那一列排序，再将索引回传回去
'''
统计数组值每一个出现的次数
'''
number_count = np.array([1,2,3,4,1,2,6,7,8,9,4,2])
#按值做索引记录每个值的数据
print(np.bincount(number_count))

'''
如何求一个四维数组的最后两维求和
'''
z= np.random.randint(1,100,(2,3,4,5))
print(z)
#后两维求和
res = z.sum(axis=(-2,-1))
print(res)
'''
交换矩阵中两行
'''
z = np.arange(25).reshape((5,5))
print(z)
z[[0,1]] = z[[1,0]]
print(z)
'''
找到数组中最长出现的索引值
'''
index_max_count = np.random.randint(1,10,50)
print(np.bincount(index_max_count).argmax())
'''
快速查找topk
'''
z=np.arange(10000)#生成10000个数据
np.random.shuffle(z)#洗牌顺序
n = 5
print(z[np.argpartition(-z,n)[:n]])

'''
去掉数组中，所有元素相同的值
'''
np.set_printoptions(threshold=10)
del_value = np.random.randint(1,10,(10,3))
print(del_value)
e= np.all(del_value[:,1:]==del_value[:,:-1],axis=1) #所有都一样
print(e)
e= np.any(del_value[:,1:]==del_value[:,:-1],axis=1) #任何一个一样都都一样
print(e)
