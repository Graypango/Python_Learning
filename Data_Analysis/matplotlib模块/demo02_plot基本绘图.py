'''
    绘制正弦、余弦
'''
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']

x = np.linspace(-np.pi,np.pi,1000)
# 正弦
sin_y = np.sin(x)
# 余弦
cos_y = np.cos(x)/2

# 画图
plt.plot(x,sin_y, linewidth=1.5,linestyle=':',color='red',alpha=0.8, label='sin线')
plt.plot(x,cos_y, linewidth=1.5,linestyle='-',color='green',alpha=0.8, label=r'$\frac{cos}{2}$'+"线")
plt.legend(loc='upper left')
# 刻度
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$'])
plt.yticks([-1,-1/2,0,1/2,1],
           ['-1', r"$-\frac{1}{2}$", '0', r'$\frac{1}{2}$', '1'])

# 坐标轴
pg = plt.gca()
pg.spines['left'].set_position(('data',0))
pg.spines['right'].set_color(None)
pg.spines['top'].set_color(None)
pg.spines['bottom'].set_position(('data',0))

# 特殊点
point_x = np.pi*3/4
point_y = np.cos(point_x)/2
plt.scatter(point_x, point_y,marker='*',s=80,color='red')

# 备注
plt.annotate(
    '卖出点',
    xy=(point_x,point_y),
    textcoords='offset points', # 以当前备注的点为基点
    xytext=(-40,-40), # 设置备注的坐标
    fontsize=13,
    # 设置箭头、连接样式
    arrowprops={
        'arrowstyle': '->',
        'connectionstyle': 'angle3'
    }
)

# 显示
plt.show()