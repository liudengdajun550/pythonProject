import numpy as np
array = [1,2,3,4,5]
# array+1 #TypeError: can only concatenate list (not "int") to list
#numpy进行格式转换
array1=np.array(array)
print(type(array1))
print(array1+1)
array2 = array1+1
array3 = array2+array1
print(array3)
array4 = array2*array1
print(array4)
print(array1[0])
print(array1[-2:])
print(array1.shape)
