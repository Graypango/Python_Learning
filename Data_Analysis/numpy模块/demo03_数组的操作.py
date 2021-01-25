import numpy as np

print('----------1、类型的操作-------------')
'''
     查看类型：dtype
     修改类型：astype
     变量类型：type
'''
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.dtype)
# 1234567890 float 数据溢出
arr = arr.astype('str')
print(arr)

arr2 = np.array([1,2,3], dtype='str')
print(arr2)

print('----------------------------------------')
nums = [1,2,3,4,5]
print(nums[0], type(nums[0]))
print(nums[:1], type(nums[:1]))

print('-----------------2、长度的操作----------------')

data = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [110,120,114]
]
arr2 = np.array(data)
print('长度：',len(arr2))
print('长度：',arr2.size)

print('-----------------3、下标的操作----------------')
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
arr3 = np.array(data)
print('数据：', arr3[1][-1])
print('数据：', arr3[1,-1])
print('最后两个数据：', arr3[-1][1:])
print('最后两个数据：', arr3[-1,[1,2]])