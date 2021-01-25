import numpy as np

# 文件读取
title,date,money = np.loadtxt(
    'aapl.csv',
    delimiter = ',',
    usecols = [0,1,7],
    unpack=True,
    dtype='U10,U20,float'
)
print(money)
sd = money*3.14/100
print(sd)
xj = money+sd
print(xj)

# 转置
res = np.array([title,date,money,xj]).T

# 保存数据
np.savetxt('aapl1.csv',res,fmt='%s',delimiter=',')
