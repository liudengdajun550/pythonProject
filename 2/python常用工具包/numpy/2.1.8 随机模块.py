#随机数的值范围都在[0,1)之间,每次返回的值都不一致
import numpy as np
#random构建3行2列的浮点数
print(np.random.rand(3,2))
#[0,10]之间的正数值，shape可以自己指定
print(np.random.randint(0,10,(4,5)))
print(np.random.randint(10,size = (4,5)))
#返回一个数
print(np.random.rand())
#其他方法
print(np.random.random_sample())
#start-end之间选择x个数
print(np.random.randint(1,10,3))

#获取高斯分布下的3个数：需要均值和方差
mu,sigma = 0,0.1
print(np.random.normal(0,0.1,3))

#np中支持设置随机数精度
np.set_printoptions(precision=3)
mu,sigma = 0,0.1
print(np.random.normal(0,0.1,3))

#洗牌：将数据打乱顺序shuffle
deng_list = np.array([1,2,3,4,5,6,7])
np.random.shuffle(deng_list)
print(deng_list)

#随机种子:当我们设置一个种子后，随机产生的数据逻辑都是一样的，不会每次运行都是不一样的数据，用于调参数的时候限制其他参数不变的定量变化
np.random.seed(0)
mu,sigma = 0,0.1
print(np.random.normal(0,0.1,3))


