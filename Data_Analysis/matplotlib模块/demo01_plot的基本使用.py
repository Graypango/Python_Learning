import matplotlib.pyplot as plt
import numpy as np

# 准备数据
month = np.arange(1,13)
money = np.random.randint(80,100,12)

# 绘制操作
# step1：设置图表的文字字体
plt.rcParams['font.sans-serif'] = ['FangSong']

# step2：绘制图形
plt.plot(month,money)

# step3：添加相关设置
plt.title('2020年股票走势图')
plt.xlabel('月份')
plt.ylabel('金额')
# 设置范围
# plt.xlim(7,12)
# 设置水平线：均线
plt.hlines(np.mean(money),1,12)

# 总后一步：显示图形
plt.savefig('2020年股票走势图.jpg')
plt.show()