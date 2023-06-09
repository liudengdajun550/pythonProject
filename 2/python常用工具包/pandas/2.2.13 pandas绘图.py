#解决pandas无法在pycharm中绘图问题：https://blog.csdn.net/weixin_44556353/article/details/125312652
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#随机产生一些数据
s = pd.Series(np.random.randn(10),index=np.arange(0,100,10))
s.plot()
plt.show()

#画2个子图
fig, axes=plt.subplots(2,1)#子图是两行一列
#输入数据
data = pd.DataFrame(np.random.randn(16),index=list('abcdefghijklmnop'))
data.plot(ax=axes[0],kind='bar')#polt是画图，画什么？ax用于指定子图画在什么位置,第一个图画在第一行第一列，形式使用柱状图
data.plot(ax=axes[1],kind='barh')#第二张图画在第二行第一列，形式使用列柱状图横过来
plt.show()

#导入数据，进行绘图
tips = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\tips.csv')
print(tips.head())
#利用获取的数据绘制直方图,50条数据
tips.total_bill.plot(kind='hist',bins=50)
plt.show()
#绘制散点图
macro = pd.read_csv(r'C:\Users\HP\PycharmProjects\pythonProject\data\macrodata.csv')
pd.plotting.scatter_matrix(macro,color='k',alpha=0.3)#指明染色和透明度
plt.show()

print(macro.head())
#选取几列作为散点图
data = macro[['quarter','realgdp']]
pd.plotting.scatter_matrix(data,color='k',alpha=0.3)#指明染色和透明度
plt.show()


# import matplotlib.pyplot as plt
#
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
# plt.style.use('seaborn')
# plt.rcParams['font.sans-serif'] = ['KaiTi'] #引入中文
# fig, ax = plt.subplots()
# # ax.scatter(x_values, y_values, c='green', s=10)
# # ax.scatter(x_values, y_values, c=(0, 0.2, 0), s=10) #RGB配色
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)
# ax.set_title("平方的值", fontsize=24)
# ax.set_xlabel("数据", fontsize=14)
# ax.set_ylabel("数的平方", fontsize=14)
# ax.axis([0, 1100, 0, 1100000])    #坐标范围设置
# plt.show()
#
