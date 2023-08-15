import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available)#查看有哪些风格

x=np.linspace(-10,10)
y=np.sin(x)
plt.plot(x,y)#把数据画到面板上
plt.show()#显示图片

plt.style.use('Solarize_Light2')#单风格使用
plt.plot(x,y)
plt.show()

plt.style.use(['Solarize_Light2','bmh'])#组合风格使用
plt.plot(x,y)
plt.show()