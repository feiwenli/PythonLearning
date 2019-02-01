# -*-coding=utf-8-*-
# 折线图

import numpy as np
import matplotlib.pyplot as plt
'''
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)	# 横轴
c,s = np.cos(x), np.sin(x)
plt.figure(1)	# 指定第一个图
plt.plot(x,c,color='blue',linewidth=2.0,linestyle='-',label='cos',alpha=0.5) 	# 自变量，因变量  alpha:透明度
plt.plot(x,s,'y+',label='SIN')	# r+,r*,r-
plt.title('cos&sin')
ax = plt.gca() 	# 轴的编辑器
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))	# 把位置设到数据域的0位置

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
	[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])	# 横轴标示的数字和位置
plt.yticks(np.linspace(-1,1,5,endpoint=True))	# -1~1 5个点
for label in ax.get_xticklabels()+ax.get_yticklabels():
	label.set_fontsize(16)
	label.set_bbox(dict(facecolor='white',edgecolor='None',alpha=0.3))	# 数字背景色

plt.legend(loc='upper left')	# 图例
plt.grid()	# 网格线
# plt.axis([-2, 2, -0.5, 1])	# 显示范围

# 填充颜色
plt.fill_between(x,np.abs(x)<0.5,c,c>0.5,color='green',alpha=0.3)
# 注释
t = 1
plt.plot([t,t],[0,np.cos(t)],'r',linewidth=1,linestyle='--')
plt.annotate('cos(1)',xy=(t,np.cos(1)),xycoords='data',xytext=(+10,+30),
	textcoords='offset points',arrowprops=dict(arrowstyle="->",connectionstyle='arc3,rad=.2'))
# textcoords='offset points' 相对位置
plt.show()
'''

# scatter
fig = plt.figure()
fig.add_subplot(3,3,1)
n = 128
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y,X)		# 上色
plt.axes([0.025, 0.025, 0.95, 0.95])	# 范围
plt.scatter(X, Y, s=75, c=T, alpha=.5)	
plt.xlim(-1.5, 1.5), plt.xticks([])
plt.ylim(-1.5, 1.5), plt.yticks([])
plt.axis()
plt.title('scatter')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


