import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)

print('-------------根据true、false筛选----------')
mask = [True,False,True,True,False,True]
res = arr[mask]
print(res)

print('-------------根据条件筛选：从大数组里面筛选子集----------')
arr1 = np.random.randint(1,100,20)
print(arr1)
print('筛选60分以上的数据：')
res = arr1[arr1>60]
print(res)
print('筛选1-10分或者90分以上的数据：')
res1 = arr1[((arr1>=1)&(arr1<=10))|(arr1>90)]
print(res1)

print('-------------重新排列筛选----------')
arr2 = np.array([110,120,119,911,114,12345])
mask = [1,4,2] # 定义下标
res2 = arr2[mask]
print(res2)




