#字典结构{}
tang = {}
print(type(tang))
#字典的第二种构造方式，dict()
tang = dict()
print(type(tang))
print(tang)
#字典结构的操作：key->value
deng = {}
deng['frist'] = 'xiao'
print(deng)
#键值不可重复，每次向后新增
deng['second'] = 'fan'
print(deng)
#通过键找到值
print(deng['frist'])
#更新字典值
deng['frist'] = 123
print(deng)
#其他赋值方式,w无先后顺序
deng = {'first':'deng','second':'xiao', 'thrid':'fan'}
print(deng)

#使用list方式作为value
number = [1,2,3]
deng['first'] = number
print(deng)

#字典嵌套字典
father = {}
son = {'中文': 'chinese', '日文': 'japnese'}
daughter = {'level': 3, 'name': 'good'}
father = {'son':son, 'daughter':daughter}
print(father)

#其他写法的字典结构
deng = dict([('xiao',1),('fan',2)])
print(deng)
#直接多键值进行操作
deng['xiao'] += 1
print(deng['xiao'])

#按键拿值
print(deng['xiao'])
print(deng.get('xiao'))
#如果拿的值不存在也可以自定义赋值
print(deng.get('meiyou'))
print(deng.get('meiyou','hahahah'))

print(deng)
#使用pop弹出,需要指定键值
deng.pop('fan')
print(deng)
del deng['xiao']
print(deng)


#字典更新操作，相同键值，新字典值会覆盖旧字典值，新增的内容会被增加到旧字典中
hobbit1 = {'traveller1':'frodo', 'traveller2':'sam'}
hobbit2 = {'traveller3':'gandaofu', 'traveller4':'gollem', 'traveller2':'beard'}
hobbit1.update(hobbit2)
print(hobbit1)

#查看某个键是否在字典中

print('deng' in hobbit1)
print('traveller1' in hobbit1)

#字典中获取全部键值
print(hobbit1.keys())
#字典中获取全部value值
print(hobbit1.values())
#字典中获取全部键值对
print(hobbit1.items())
