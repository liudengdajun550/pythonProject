import  numpy as np
path = r'C:\Users\HP\PycharmProjects\pythonProject\data\writeFile.txt'
#正常逻辑读写
data = []
with open(path, 'r') as f:#注意需要在目录前加上r防止识别反斜杠为字符串
    for line in f:
        fields = line.split(' ')
        cur_data = [float(x) for x in fields] #list结构，遍历fields，然后x转换为指定类型
        data.append(cur_data)
#将矩阵转为ndarray结构进行矩阵处理
print(data)

#np有loadtxt()函数直接打开文件并转为ndarray结构,要求行列都是一致的数据
data = np.loadtxt(path)
print(data)
#指定分隔符 delimiter
data = np.loadtxt(path, delimiter=' ')
print(data)

#指定去掉第几行skiprows
data = np.loadtxt(path, delimiter=' ',skiprows=1)
print(data)

#指定使用那些列usecols=(1,2,3)

#写文件
data = np.random.randint(0,10,(4,5))
np.savetxt(path,data)
np.savetxt(path,data,fmt='%d')#指定保存格式
np.savetxt(path,data,fmt='%d',delimiter = ' ')#指定保存格式

#读写中间结果，比如  array结构
data = np.random.randint(0,10,(4,5))
np.save('npsavetemp.npy',data)#保存中间结果
load_data = np.load('npsavetemp.npy')
print(load_data)
data2 = np.array([1,2,3,4,4])
#以字典方式进行存储
np.savez('dic.npz',a=data2,b=data)
load_data_z = np.load('dic.npz')
print(load_data_z.keys())
print(load_data_z['a'])

