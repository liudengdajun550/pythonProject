import time
#时间戳，1970到现在有多久
print(time.time())
#转为可理解的本地时间
print(time.localtime(time.time()))
#格式化时间
print(time.asctime(time.localtime(time.time())))
#转为指定格式的时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

#获取日历
import calendar
print(calendar.month(2023,5))
#查看函数帮助,不能带括号
print(help(calendar.month))