# -*- coding: utf-8 -*-
#解一元二次方程
import math
def quadratic(a,b,c):
	#数据类型检查
	for x in (a,b,c):
		if not isinstance(x,(int,float)):
			raise TypeError('bad operand type')
	if a == 0:
		return 'a不能为0'
	elif b**2-4*a*c >= 0:
		x = (-b+math.sqrt(b**2-4*a*c))/2/a
		y = (-b-math.sqrt(b**2-4*a*c))/2/a
		return x,y
	elif b**2-4*a*c < 0:
		return '无解'
#test
#print(quadratic(2,3,1))
#print(quadratic(1,2,-4))
#print(quadratic(0,3,9))
while(input('是否继续输入（yes/no）?')=='yes'):
	a = float(input('a = '))
	b = float(input('b = '))
	c = float(input('c = '))
	print(quadratic(a,b,c))