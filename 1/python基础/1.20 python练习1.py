'输入一行字符串，统计其中空格、英文字符、数字、和其他字符的个数'
space = 0
letters = 0
digital = 0
others = 0
s = input('please input a string:')
for c in s:
    if c.isalpha():
        letters+=1
    elif c.isdigit():
        digital+=1
    elif c.isspace():
        space+=1
    else:
        others+=1
print(letters,digital,space,others)
print("letters=%d,digital=%d,space=%d,others=%d"%(letters,digital,space,others))

'暂停一秒输出标准时间，使用time的sleep'
import time

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

'将一个列表元素复制到另外一个列表中'
origin = [100,60,40,20,10,0]
target = origin #shallow copy
print(id(origin),id(target))
target = origin[:] #deep copy
print(id(origin),id(target))


'1.四个数字：1，2，3，4组成互不相同且无重复数据的3位数'
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) and (i != k) and (j != k):
                print(i,j,k)
'2.企业发奖金：'
'1-小于10w，发10%，'
'2-高于10w小于20w发7.5%，低于10w部分发10%'
'3-高于20小于40发5%，低于20高于10发7.5%，低于10w部分发10%'
'4-高于40低于60发3%，高于20小于40发5%，低于20高于10发7.5%，低于10w部分发10%'
'5-高于100发1%，高于60低于100发1.5%，高于40低于60发3%，高于20小于40发5%，低于20高于10发7.5%，低于10w部分发10%'
level = [100,60,40,20,10,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]

income = float(input('请输入利润金额：'))
#计算奖金
result = 0
for idx in range(0,6):
    if income > level[idx]:
        result += (income - level[idx]) * rate[idx]
        income = level[idx]
print(result)

'输入3个数x,y,z,按照由小到大输出'
my_list=[]
for i in range(3):
    x = int(input('input an integer'))
    my_list.append(x)
my_list.sort(reverse=True)
print(my_list)