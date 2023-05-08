#简单函数
def print_value():
    print("a=", 10)
print_value() #调用函数

#带参数的函数
def add_ab(a,b):
    print(a+b)
add_ab(1,2)
add_ab(3,5)

#有返回值的函数
def add_ab(a,b):
    return a+b
deng = add_ab(1,2)
print(deng)

#有默认值的返回值的函数
def add_ab(a=3,b=4):
    return a+b
deng = add_ab()
print(deng)
deng = add_ab(2)
print(deng)
deng = add_ab(b=9)
print(deng)
deng = add_ab(1,2)
print(deng)

#不清楚参数数量，使用*args用于接受不定参数个数的参数
def add_numbers(a=3,*args):
    for i in args:
        a+=i
    return a
print(add_numbers(1,2,3,4,5,6))

#不清楚参数数量，使用**kwargs用于接受不定参数,并限制只能是键值对(字典)方式
def add_numbers2(a=3,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
    return a
add_numbers2(y=9,x=0)

#函数返回值也可以有多个
def add_numbers(a=3,*args):
    b=0
    for i in args:
        a+=i
        b+=a
    return a,b
a,b =add_numbers(1,2,3,4,5,6)
print(a,b)
