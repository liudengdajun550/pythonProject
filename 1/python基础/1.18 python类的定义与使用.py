#类对象，关键字class,初始化一定会调用的构造函数_init_，self代表当前实例自身
class people:
    '帮助信息:xxx'
    blood = 100 #所有实例都共享的数据
    def __init__(self, name, age): #构造函数，初始化赋值
        self.name = name
        self.age = age
    def display(self):
        print('blood leave:',self.blood)

    def display_name(self):
        print(self.name)

#可通过类名.__doc__查看类的帮助信息
print(people.__doc__)
#构造对象
p1 = people('deng', 28)
p1.display_name()
p1.display()

p2 = people('xiaofan', 28)
p2.display_name()
p2.display()

#查看对象是否有x属性
print(hasattr(p1,'name'))
print(hasattr(p1,'sex'))
#获取属性的值
print(getattr(p1,'name'))
#设置属性值
setattr(p1,'name', 'python')
print(getattr(p1,'name'))
#删除属性
delattr(p1,'name')
# print(getattr(p1,'name'))

#查看类的内置属性
print(people.__doc__)
print(people.__name__)
print(people.__module__)
print(people.__bases__)
print(people.__dict__)

#类的继承，子类默认可调用父类全部方法，child(parent):即可继承
class Parent:
    parent_number = 100
    def __init__(self):
        print('父类构造方法')
    def parentM(self):
        print('父类方法')
    def setAttr(self,attr):
        Parent.attr = attr
    def getAttr(self):
        print(Parent.attr)
    def newM(self):
        print('父类被覆盖方法')
class Children(Parent):
    def __init__(self):
        print('子类构造方法')
    def childrenM(self):
        print('子类方法')
    # 子类重写父类方法
    def newM(self):
        print('子类重写父类方法')
c = Children()
c.parentM()
c.childrenM()
c.setAttr(123)
c.getAttr()
c.newM()
#多继承
class Base1:
    def method1(self):
        print("Base1.method1")

class Base2:
    def method1(self):
        print("Base2.method1")
    def method2(self):
        print("Base2.method1")

class MyClass(Base1, Base2):
    pass

# MyClass now has access to methods from both Base1 and Base2. For example:
# MyClass现在可以访问Base1和Base2的方法。例如：

mc = MyClass()
mc.method1()  # Output: Base1.method1
mc.method2()


