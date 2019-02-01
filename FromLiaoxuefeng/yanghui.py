# -*- coding: utf-8 -*-
from collections import Iterable

# 杨辉三角
def triangles(n):
	list = [1]
	while n>0:
		yield list
		list = [1]+[x+y for x,y in zip(list[:],list[1:])]+[1]
		n -=1
	return
for x in triangles(6):
	print(x)
# test = [1]
# t = zip(test[:],test[1:])
# x = [1, 2, 3]
# y = [4, 5, 6, 7]
# xy = zip(x, y)
# print xy

def triangles2(num):
	L = [1]
	while num >0:
		yield L
		L = [1] + [L[n] + L[n + 1] for n in range(len(L) - 1)] + [1]
		num -= 1

for x in triangles2(6):
	print(x)

print(isinstance(triangles2, Iterable))

