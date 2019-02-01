# -*- coding = utf-8 -*-
#文档测试
def fact(n):
	'''
	>>> fact(1)
	1
	>>> fact(3)
	6
	>>> fact(0)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(-1)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(-100)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(10)
	3628800
	>>> fact('s')
	Traceback (most recent call last):
		...
	TypeError: unorderable types: str() < int()
	>>> fact(100000)
	Traceback (most recent call last):
		...
	RecursionError: maximum recursion depth exceeded in comparison
	'''

	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	return n*fact(n - 1)

if __name__ == '__main__':
	import doctest
	doctest.testmod()