from functools import update_wrapper, wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
def mydecorator(func):
	@wraps(func)	#这是一种简便方法
	def wrapper(*args, **kargs):
		'''wrapper function'''
		print('In wrapper')
		func(*args, **kargs)
	#update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__',))	
	#默认参数WRAPPER_ASSIGNMENTS ：('__module__', '__name__', '__qualname__', '__doc__', '__annotations__') 
	#默认参数WRAPPER_UPDATES ：('__dict__',)
	#update_wrapper(wrapper,func)	#传入默认参数WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES
	return wrapper

@mydecorator
def example():
	'''example function'''
	print(' In example')

print( example.__name__)
print( example.__doc__)
print(WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)