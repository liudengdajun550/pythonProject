#列表结构，通过[]创建列表结构，放任何类型数据都可以，没有长度要求
tang = []
print(type(tang))
tang = [1,2,3,4]
print(tang)
#列表中无类型与长度要求
tang = [1,2,1.2,"dsa"]
print(tang)
#列表的第二种创建方式
tang=list()
print(type(tang))
tang1 = list([1,2,3])
print(tang1)
#list操作
print(len(tang1) )#数据长度
tang2 = ['abc', 'def']
print(tang1+tang2) #进行字符串拼接，直接使用+
#乘法,复制listn遍
print(tang1*3)
#列表的索引也可以做
print(tang1[-1])

tang1[0] = 234
print(tang1[0])
#全部值进行替换
tang2[:] = ['deng','xiaofan']
print(tang2)
#元素删除 - del
del tang2[0]
print(tang2)
del tang1[3:]
print(tang1)

#判断元素是否在列表中 - in
print(1 in tang1)
print(1 not in tang1)
print('xiaofan' in tang2)
print('xiao' in tang2)

#链表中嵌入链表
xiaofan = [1,2, [3,4]]
print(xiaofan)
#定位链表中链表的元素
print(xiaofan[2][1])
#不是list结构，采用list方式会报错
#print(xiaofan[0][1])

xiaofan = ['xaingjiao','1','pingguo','xingjiao']
#列表中统计次数
print(xiaofan.count('pingguo'))
#通过value获取index，获取到第一个匹配的index
print(xiaofan.index('1'))

#列表尾部添加元素,每次只能添加一个元素
xiaofan.append("nume")
print(xiaofan)
#在某个位置添加一个元素
xiaofan.insert(2,'chinese')
print(xiaofan)
#删除某个元素
xiaofan.remove('chinese')
print(xiaofan)
#弹出元素并删除
xiaofan.pop(1)
print(xiaofan)
#元素排序
xiaofan1 = [631,12,3,45,67]
print(xiaofan1.sort())
print(sorted(xiaofan1))
#掉序列
print(xiaofan1.reverse())

