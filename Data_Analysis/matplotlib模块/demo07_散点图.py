import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']

# 准备数据
weight = np.random.normal(135,10,100)
height = np.random.normal(168,10,100)

plt.figure('散点图', facecolor='pink')
plt.title('亚洲人的身高-体重分布图')
plt.xlabel('体重')
plt.ylabel('身高')
d = (168-height)**2 + (135-weight)**2
plt.scatter(weight,height,cmap='jet',c=d)
plt.colorbar() # 显示颜色板
plt.show()

