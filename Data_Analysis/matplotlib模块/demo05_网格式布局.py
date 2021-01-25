'''
    北上广深江
'''
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong']
plt.figure('网格式布局', facecolor='yellow')
# 创建GridSpec，对布局进行拆分
gs = plt.GridSpec(3,3)
def bsgsj(dyg,txt):
    plt.subplot(dyg)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5,0.5,txt,va='center',ha='center',size=36)

bsgsj(gs[0,:2], '北京')
bsgsj(gs[:2,-1], '上海')
bsgsj(gs[-1,1:], '广州')
bsgsj(gs[1:,0], '深圳')
bsgsj(gs[1,1], '江苏')
plt.show()