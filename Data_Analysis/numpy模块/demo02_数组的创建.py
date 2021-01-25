import numpy as np

print('-------------1、array------------')
data = (110,120,119,911,114)
arr = np.array(data)
print(arr)
data1 = [1,2,3,4,5]
arr1 = np.array(data1)
print(arr1)

print('-------------2、arange------------')
arr2 = np.arange(1,100001)
print(arr2)

arr3 = np.arange(1,100,2)
print(arr3)

'''
    1对夫妻，有2个小孩，其中1个是男孩，另一也是男孩的几率是多大？
    男 男
    男 女
    女 男
    女 女
'''
print('-------------3、ones------------')
oss = np.ones((4,5))
print(oss)
oss1 = np.ones(4)
print(oss1)

print('-------------4、zeros------------')
zs = np.zeros((4,4))
print(zs)

print('-------------5、random------------')
# randint：start，end，number
ages = np.random.randint(20,50,100)
print(ages)

print('-------------6、linespace------------')
'''
    start
    end
    多少份
'''
nums = np.linspace(1,10,5)
print(nums)

print('-------------7、normal------------')
# 随机出正态分布的数据
'''
    正态分布normal：170 10 100
    定值、标准差、数量
'''
nm = np.random.normal(170,10,100)
print(nm)
