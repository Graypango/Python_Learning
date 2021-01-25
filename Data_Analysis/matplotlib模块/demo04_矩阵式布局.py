import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure('矩阵式布局-九宫格',facecolor='green')

chs = "".join([chr(x) for x in range(97,123)])
print(chs)

for i in range(1,10):
    plt.subplot(3,3,i)
    plt.xticks([])
    plt.yticks([])
    # 文本显示
    plt.text(
        0.5,0.5,chs[(i-1)*3:i*3],
        size=36,
        va='center',
        ha='center'
    )

plt.show()