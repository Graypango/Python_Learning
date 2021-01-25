# 假如：已从表格里面读取到数据
data = {
    'title': ['苹果','橘子','香蕉','草莓'],
    'number': ['3','5.1','2.5','4'],
    'price': ['3.6','2','7.5','20.2']
}

# 添加1列：金额
'''
    zip()
'''
money = []
for n,p in zip(data['number'],data['price']):
    money.append(float(n) * float(p))
data['金额'] = money
print(data)

import numpy as np
money2 = np.array(data['number'],dtype='float') * np.array(data['price'],dtype='float')
data['money'] = money2
print(data)






