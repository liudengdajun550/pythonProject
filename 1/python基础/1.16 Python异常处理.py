import math

#捕获值异常后处理
for i in range(10):
    try:
        input_number = input('please input a number:')
        if input_number == 'q':
            break
        result = math.log(float(input_number))
        print(result)
    except ValueError:
        print('输入值必须>0')
        break
#各种不同的异常情况，使用通用异常
for i in range(2):
    try:
        input_number = input('please input a number:')
        if input_number == 'q':
            break
        result = 1/math.log(float(input_number))
        print(result)
    except Exception:
        print('所有异常都被捕获')
        break
#根据不同异常情况进行不同处理
for i in range(2):
    try:
        input_number = input('please input a number:')
        if input_number == 'q':
            break
        result = 1/math.log(float(input_number))
        print(result)
    except ValueError:
        print('ValueError')
        break
    except ZeroDivisionError:
        print('ZeroDivisionError:log value must >0')
        break
    except Exception:
        print('unknown error')
        break
    finally:
        print('我是异常的最后一步，一定会执行')

#自定义异常类：raise
class DengError(ValueError): #继承异常ValueError
    pass #先不写实现
cur_list = ['deng','xiao','fan']
while True:
    input_str = input('请输入字符串：')
    if input_str not in cur_list:
        raise DengError('Invalid number %s' %input_str) #抛出异常
