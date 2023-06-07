import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
# #画一个折线图:全是点
# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# #为每个轴设定名字,字体大小frontSize
# plt.xlabel('x 轴', fontsize = 16)
# plt.ylabel('y 轴',fontsize=16)
# plt.show()
# # pd.Series([4,5,7]).plot()
# # plt.show()
#换其他形状的图或形式，在plot中设置使用的图方式，'--'虚线，":"点线
plt.plot([1,2,3,4,5],[1,4,9,16,25],'--')
#为每个轴设定名字,字体大小frontSize
plt.xlabel('x 轴', fontsize = 16)
plt.ylabel('y 轴',fontsize=16)
plt.show()
#换其他形状的图或形式，在plot中设置使用的图方式，还可以指定颜色
plt.plot([1,2,3,4,5],[1,4,9,16,25],'--',color='r')
#为每个轴设定名字,字体大小frontSize
plt.xlabel('x 轴', fontsize = 16)
plt.ylabel('y 轴',fontsize=16)
plt.show()
#换其他形状的图或形式，在plot中设置使用的图方式，可以把颜色和形状放在一起展示
plt.plot([1,2,3,4,5],[1,4,9,16,25],'bo')
#为每个轴设定名字,字体大小frontSize
plt.xlabel('x 轴', fontsize = 16)
plt.ylabel('y 轴',fontsize=16)
plt.show()