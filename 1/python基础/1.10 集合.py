# 集合：set,用于去除所有重复数据
deng = [123,123,123,]
print(set(deng))
#也可以直接定义集合类型
deng = set([123,123,345,345])
print(deng)
#也可以直接定义{},作为集合，如果写key-value对就是字典，不写就是集合
xiao = {1,2,3,4,1,1}
print(xiao)

#集合操作
a = {1,2,3,4,5}
b = {1,4,5,6,7,7,8}
#集合的并集
print(a.union(b))
print(a|b)
#集合交集
print(a.intersection(b))
print(a&b)
print(b.intersection(a))
#a与b差异,差集
print(a.difference(b)) #a中不在b中的值
print(a-b)
print(b.difference(a))
print(b-a)

#子集
a={1,2,4,5,6,3}
b={2,3}
print(b.issubset(a))
print(b<=a)
print(a.issuperset(b))
print(a>b)
print(b>b)

#增加值
a = {1,2,3}
a.add(4)
print(a)
#更新值
a.update([3,4,5,6])
print(a)
#删除值
a.remove(4)
print(a)

a.pop()
print(a)