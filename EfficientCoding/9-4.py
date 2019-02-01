from functools import wraps
import time
import logging
from random import randint

def warn(timeout):
	def decorator(func):
		def setTimeout(k):
			nonlocal timeout 	#类似与c语言中的全局变量，可随时修改，仅在python3中有
			timeout = k
		def wrapper(*args, **kargs):
			start = time.time()
			res = func(*args, **kargs)
			used = time.time() - start
			if used > timeout:
				msg = '"%s": %s > %s' %(func.__name__,used,timeout)
				logging.warn(msg)
			return res
		wrapper.setTimeout = setTimeout
		return wrapper
	return decorator

@warn(1.5)
def test():
	print('In test')
	while randint(0,1):
		time.sleep(0.5)

for _ in range(30):
	test()

test.setTimeout(1)
for _ in range(30):
	test()