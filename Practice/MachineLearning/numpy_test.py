# -*- coding=utf-8 -*-
import numpy as np
from numpy import *
from numpy.linalg import *

# 3*5的全0矩阵
myZero = np.zeros([3, 5])
print myZero

myOnes = np.ones([3, 5])
print myOnes

# 3行4列的0~1之间的随机数矩阵
myRand = np.random.rand(3, 4)
print myRand
print np.random.rand()	
print np.random.randint(1,10,3)	# 均匀分布

print np.random.randn()	# 标准正态分布
print np.random.randn(2,4)	# 标准正态分布

print np.random.choice([10,20,30])	# 只能从备选选项中选

print np.random.beta(1,10,100)	# beta分布


# 3*3的单位矩阵
# myEye = np.eye(3,5)
myEye = np.eye(3,5)
print myEye

# 加减
print myOnes+myEye
print myOnes-myEye

# 矩阵数乘
mymatrix = mat([[1,2,3],[4,5,6],[7,8,9]])
a = 10
print a*mymatrix

# 矩阵所有元素求和
print sum(mymatrix)

vector = np.array([5,10,15,20])
equal_to_ten = (vector == 10)
print equal_to_ten
print vector[equal_to_ten]
print np.exp(vector)
print np.exp2(vector)
print np.sqrt(vector)
print np.log(vector)
print np.sin(vector)


# 类型转换
vec = np.array(['1','2','3','4'])
print vec.dtype
vec = vec.astype(float)
print vec.dtype
print vec

print '追加'
print np.concatenate((vector,vec),axis=0)
print np.hstack((vec,vector))
print np.vstack((vec,vector)) # 上下追加
print np.split(vector,2)
print np.copy(vector,2)


print vector.min()
matrix = np.array([
	[5,10,15],
	[20,30,35],
	[35,40,45]
	])
print matrix.sum(axis=0)  	# 按列求和	axis 指定维度，axis越大，深入程度越大
print matrix.sum(axis=1)	# 按行求和
print 'inv:' 
print inv(matrix)	# 逆矩阵
print 'transpose:'
print matrix.transpose()	# 转置
print 'Det(行列式)'
print det(matrix)
print '第一个array特征值，第二个array表示特征向量'
evals, evecs = eig(matrix)
print '特征值：',evals,'\n特征向量：',evecs
# 特征值和特征向量，还原原矩阵
sigma = evals*aye(m)
print evecs*sigma*linalg.inv(evecs)


# 解方程
y = np.array([[5.],[7.],[9.]])
print '解方程'
print solve(matrix,y)

print np.arange(1,11).reshape([2,5])
print np.arange(1,11).reshape([2,-1])	# 5缺省成-1

print 'FFT(快速傅氏变换):'
print np.fft.fft(np.array([1,1,1,1,1,1,1,1,1]))
print 'coef(相关系数)：'
print np.corrcoef([1,0,1],[0,2,1])
print 'poly(一元多次函数)：'
print np.poly1d([2,1,3])

a = mat([1,2])
b = mat([[1,3],
		[3,1]])
print a*b