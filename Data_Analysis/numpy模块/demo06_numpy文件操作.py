import numpy as np

# 加载数据：拆包
title,date,money = np.loadtxt(
    'aapl.csv',
    delimiter = ',',
    usecols=[0,1,7],
    # dtype='U10,U20,float'
    dtype={'names':['title','date','money'],
           'formats': ['U10','U20','float']
           },
    unpack=True
)
# 访问数据

print('成交量：',money)

print('------------------------------------------------------')
# 数据处理
# 处理函数的参数默认代表该列数据
def str_date(dmt):
    dmt = str(dmt, encoding='utf-8') # 字节转字符串
    day,month,year = dmt.split("-")
    newdmt = '%s-%s-%s'%(year,month,day)
    return newdmt
# 加载数据：不拆包
result = np.loadtxt(
    'aapl.csv',
    delimiter = ',',
    usecols=[0,1,7],
    # dtype='U10,U20,float'
    dtype={'names':['title','date','money'],
           'formats': ['U10','U20','float']
           },
    # 处理列数据
    converters = {1: str_date}
)
# 访问数据
print('成交量：',result['money'])
print(result['date'])
