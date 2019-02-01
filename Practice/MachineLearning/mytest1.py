# -*- coding=utf-8 -*-
import numpy as np
from numpy import *
import matplotlib
from matplotlib import pyplot as plt

# 测试数据集——二维list
dataSet = [[-0.0717613, 14.0423555], [-1.3894893, 4.66343556], [-0.7521344, 6.53454564], [-1.3434556, 7.13445466],
           [0.4343545, 11.4565652], [0.4631454, 7.03584541], [0.6874983, 12.9878699], [-2.5464145, 6.89357295],
           [0.5415663, 9.64154554]]

dataMat = mat(dataSet).T  # 将数据集转换为Numpy矩阵，并转置
plt.scatter([dataMat[0]], [dataMat[1]], c='red', marker='o')  # 绘制数据集散点图

# 绘制直线图形
X = np.linspace(-2, 2, 100)  # 产生直线数据库
# 建立线性方程
Y = 2.8 * X + 9

plt.plot(X, Y)  # 绘制直线图
plt.show()
