# -*- coding=utf-8 -*-
# 标准化欧式距离
# 
import numpy as np
from numpy import *
from numpy.linalg import *

vectormat = mat([[1,2,3],[4,5,6]])
v12 = vectormat[0]-vectormat[1]
print sqrt(v12*v12.T)
# norm
varmat = std(vectormat.T, axis=0)	# 计算全局标准差 
print varmat
normvmat = (vectormat-mean(vectormat))/varmat.T
# numpy.mean(a, axis=None, dtype=None, out=None, keepdims=False)
# 返回的数组元素的平均值。平均取默认扁平阵列flatten(array)上 
print normvmat
normv12 = normvmat[0]-normvmat[1]
print sqrt(normv12*normv12.T)


