import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong']

plt.figure('自由式布局',facecolor='lightgray')
#  x y wight height
plt.axes([0.05,0.05,0.5,0.4])
plt.text(0.5,0.5,'上海',size=36,va='center',ha='center')

plt.axes([0.05,0.5,0.5,0.4])
plt.text(0.5,0.5,'中国',size=36,va='center',ha='center')
plt.show()