import numpy as np

nums = np.random.randint(1,50,20).reshape((4,5))
print(nums)

print('------------获取2、3列数据----------')
print(nums[:,1:3])

print('------------获取1、4、5列数据----------')
print(nums[:,[0,3,4]])
print('----------------------------------------------------------')
data = np.random.randint(1,50,27).reshape((3,3,3))
print(data)

print('获取第2、3页的后两列数据')
print(data[1:,:,1:])

print('每一页每一行第一列的第一个数据')
print(data[:,:,0])





