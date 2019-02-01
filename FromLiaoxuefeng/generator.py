#!/usr/bin/pythonb
# -*- coding: utf-8 -*-
g = (x*x for x in range(10))
# 一个一个打印
#print(next(g))
#print(next(g))
#正确方法
for n in g:
	print(n)
#斐波拉契数列（Fibonacci），除第一个和第二个数外，
#任意一个数都可由前两个数相加得到
def fib(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		a,b = b, a+b
		n = n + 1
	return 'done'
print(fib(6))
#将fib变成generator
def fibcp(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b, a+b
		n = n + 1
	return 'done'
for x in fibcp(6):
	print(x)    #拿不到返回值‘done’
#要想拿到返回值
g = fibcp(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break

class name(object):
	"""docstring for name"""
	def __init__(self, arg):
		super(name, self).__init__()
		self.arg = arg
		