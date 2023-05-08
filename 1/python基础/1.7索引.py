tang = 'tang yu di'
#数组索引从0开始，倒数第一个索引-1开始
print(tang[0])
print(tang[5])
print(tang[-1])
#切片,左闭右开[)
#【0：4】从0到3
print(tang[0:4])
#从当前位置到最后
print(tang[5:])
#到倒数最后一位
print(tang[:-1])
#那边不写那边通杀，都不写全选
print(tang[:])
#从后面开始算
print(tang[-3:])
#每隔几个去一个值
print(tang[::2])