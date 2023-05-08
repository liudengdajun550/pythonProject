#while
deng = 0
while deng<10:
    print(deng)
    deng+=1

xiaofan = set(['deng','xiao','fan'])
while xiaofan:
    deng = xiaofan.pop()
    print(deng)

#遍历-for 变量名 in 集合：
xiaofan = set(['deng','xiao','fan'])

for name in xiaofan:
    print(name)
#for i in range(范围),范围[0，范围）
for i in range(3):
    print(i)
xiaofan = ['deng','xiao','fan']
#set不支持index,所以主要用于列表类型
#常与len(计数)一同使用
for i in range(len(xiaofan)):
    print(xiaofan[i])

#使用continue进行跳过
deng = [1,2,3,4,5,6]
for i in deng:
    if i%2 == 0:
        print(i)
    else:
        continue
    print(i)

#使用break进行跳出
deng = [1,2,3,4,5,6]
for i in deng:
    if i%2 == 0:
        print(i)
    else:
        break
    print(i)
