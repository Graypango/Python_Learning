'''
    可以自定义复合类型
'''
import numpy as np

data = [
    ('路飞',[55,60,30],18),
    ('索隆',[70,80,50],25),
    ('娜美',[88,90,95],17)
]
arr = np.array(data)
print(arr)
print(arr[0,1])
print(arr[[0,1,2],0])
'''
    定义类型的好处：
        指定类型：指定列的数据类型
        快速访问：通过列名访问该列数据
'''
print('------------1、字符串---------------')
arr1 = np.array(data,dtype='U10,3int,int')
print(arr1)
# 字符串定义类型，指定列名:f0，f1，f2
print(arr1['f0'])
print(np.sum(arr1['f1'],axis=1))
print('平均分：',np.mean(arr1['f1'],axis=0))
print('语文的平均分：',np.mean(arr1['f1'],axis=0)[0])

print('------------2、列表---------------')
dt = [
    ('name','U10'),
    ('scores','3int'),
    ('age','int')
]
arr2 = np.array(data, dtype=dt)
print(arr2)
print('草帽团的平均年龄：',np.mean(arr2['age']))

print('------------3、字典---------------')
dt = {
    'names': ['姓名','成绩','年龄'],
    'formats': ['U10','3int','int']
}
arr3 = np.array(data, dtype=dt)
print(arr3)
print('总成绩：',np.sum(arr3['成绩']))

print('==============================日期类型===============================')
'''
    日期：xxxx-xx-xx  2021-01-01
'''
birthday = '1989-08-01'
today = '2021-01-17'
dates = np.array([birthday,today])
dates = dates.astype('M8[D]')
print(dates)
lifedays = dates[1]-dates[0]
print(lifedays/12)