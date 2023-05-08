#判断结构关键词：if 变量: 缩进
deng =100
#单条件
if deng >50:
    print('ok')

if deng > 200:
    print('>200')
else:
    print('<200')
#多条件
xiaofan = 200
if xiaofan<50:
    print('>50')
elif xiaofan<100:
    print('>50,<100')
else:
    print('>100')
#只要条件中涉及到判断都可以进行判断
#列表结构
xiaofan = ['23',3]
if 3 in xiaofan:
    print('3 in xiaofan')
#字典结构
xiaofan = {1:'中国', '小凡':"deng"}
if 1 in xiaofan: #判断键是否在
    print('字典中包含对应值')
