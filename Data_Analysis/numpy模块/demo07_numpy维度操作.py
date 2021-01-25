import numpy as np
arr = np.arange(1,13)
print(arr)

print('------------1、视图变维------------')
# reshape
arr2 = arr.reshape((4,3))
print(arr2)
arr[0] = 110
print(arr2)
# ravel
arr3 = arr2.ravel()
print(arr3)
arr[-1] = 120
print(arr3)

print('------------2、复制变维------------')
arr4 = arr2.flatten()
print(arr4)
arr4[1] = 119
print(arr2)

print('------------3、就地变维------------')
data = np.arange(1,17).reshape(4,4)
print(data)
data.shape = (2,8)
print(data)
data.resize(8,2)
print(data)