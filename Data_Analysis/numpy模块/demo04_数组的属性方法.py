import numpy as np

data = [
    [1+2j,3+4j,5+7j],
    [4+3j,5+9j,6+3j],
    [7+2j,8+2j,9+9j],
]
arr = np.array(data)
print('shape：',arr.shape)
print('dtype：',arr.dtype)
print('size：',arr.size)
print('实部：',arr.real)
print('虚部：',arr.imag)
print('元素字节数：',arr.itemsize)
print('总字节数：',arr.nbytes)
print('转置：',arr.T)
print('维度：',arr.ndim)
