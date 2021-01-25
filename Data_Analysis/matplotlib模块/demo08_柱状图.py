import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']

# 橘子、苹果的销售
month = np.arange(1,13)
apples = np.random.randint(20,40,12)
oranges = np.random.randint(10,30,12)

plt.figure('柱状图', facecolor='yellow')
plt.title('橘子-苹果销售走势图')
plt.xlabel('月份')
plt.ylabel('销量')
# 第一种解决方案：设置偏移
# 第二种解决方案：+ -
plt.xticks(month,["%s月"%x for x in range(1,13)])
plt.bar(month-0.25, apples, color='green',width=0.4, label='苹果')
plt.bar(month+0.25, oranges,color='orangered',width=0.4,label='橘子')
# plt.bar(month+0.25, -oranges,color='orangered',width=0.4,label='橘子')
plt.legend()

plt.show()

