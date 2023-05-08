deng_v =10

def stride2(deng_list):
    deng_list_sum = 0
    for i in range(len(deng_list)):
        if deng_list[i]%2 != 0:
            deng_list_sum+=deng_list[i]
    return deng_list_sum
deng_list = [1,3,4,2,6,8,234]
print(stride2(deng_list))

# #导入文件
# import main #模块名
#
# #调用模块中方法和变量
# main.print_hi('hai')
# print(main.main_val)
# #对引入进来的变量进行重新赋值
# main.main_val =100
# print(main.main_val)

#对引入的包进行重命名
import main as mm
print(mm.print_hi('hi'))

#直接从模块中导入某些属性或方法
from main import main_val as val, print_hi as hi
print(hi('hi'))
print(val)

#内容较多，将模块内容全部导入
from main import *
print(main_val)

#直接调用操作系统，进行文件操作
import os
# os.remove('shaybushi') #
print(os.path.abspath('../..')) #查看当前文件目录
