import numpy as np
from matplotlib import pyplot as plt

#在一个图中画3条线
deng_array = np.arange(0,5)
plt.plot(deng_array,deng_array,'r--')#第一条线
plt.plot(deng_array,deng_array+1,'bo')#第二条线
plt.plot(deng_array,deng_array**2,'bs')#第三条线
plt.show()

#换种写法，一图中展示多条线
plt.plot(deng_array,deng_array,'r--',deng_array,deng_array+1,'bo',deng_array,deng_array**2,'bs')#多条线展示在一起
plt.show()

#画条线
x=np.linspace(-10,10) #均匀取x轴的值
y=np.sin(x)
plt.plot(x,y,linewidth=2.0)#加入x,y之后，还可以指定线条有多粗linewidth
plt.plot(x,y,linestyle=':')#加入x,y之后，指定线条样式
plt.plot(x,y,linestyle=':',marker='o')#加入x,y之后，指定线条样式,增加关键点
plt.plot(x,y,linestyle=':',marker='o',markerfacecolor='r')#加入x,y之后，指定线条样式,增加关键点，指定关键点的颜色
plt.plot(x,y,linestyle=':',marker='o',markerfacecolor='r',markersize=10)#加入x,y之后，指定线条样式,增加关键点，指定关键点的颜色,指定关键点大小

plt.show()