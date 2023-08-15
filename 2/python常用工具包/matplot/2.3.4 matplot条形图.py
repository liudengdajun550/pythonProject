import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.arange(5)
# y = np.random.randn(5) #选取5个正数
y = np.random.randint(-5, 5, 5) #[-5,5]之间选取5个整数
fig, axes = plt.subplots(ncols=2) #两列
v_bar = axes[0].bar(x, y, color='red')
h_bar = axes[1].barh(x, y, color='red')
plt.show()