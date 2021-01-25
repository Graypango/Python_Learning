import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
# 绘制2019、2020的股票分析图
month = np.arange(1,13)
money_2020 = np.random.randint(100,150,12)
money_2019 = np.random.randint(200,250,12)

# 创建figure窗口对象
plt.figure('股票分析走势图', facecolor='yellow')
plt.subplot(2,1,1)
# 基本设置
plt.title('2019年股票走势图')
plt.xlabel('月份')
plt.ylabel('金额')
plt.tick_params(labelsize=8) # 设置刻度文本大小
plt.plot(month,money_2019,label='2019年')
plt.legend()
plt.grid(linestyle=':', alpha=0.6, color='red')  # 网格线

plt.subplot(2,1,2)
plt.title('2020年股票走势图')
plt.xlabel('月份')
plt.ylabel('金额')
plt.tick_params(labelsize=8) # 设置刻度文本大小
plt.plot(month,money_2020,label='2020年')
plt.legend()
plt.grid(linestyle=':', alpha=0.6, color='red')  # 网格线

plt.tight_layout() # 紧凑布局
plt.show()