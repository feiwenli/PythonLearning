# coding = -utf-8
import functools
def log(fn):	
	#判断是否是一个函数
	if not callable(fn):
		def decorator(func):
			@functools.wraps(func)
			#用来把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
			def wrapper(*args,**kw):
				print('begin:')
				print('%s %s():'%(fn,func.__name__))
				func(*args,**kw)
				print('end.')  
			return wrapper
		return decorator
	else:
		@functools.wraps(fn)
			#用来把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错
		def wrapper(*args,**kw):
			print('call %s():'%fn.__name__)
			#func(*args,**kw)
			return fn(*args,**kw)  #感觉没差
		return wrapper

@log('fa')  #相当于now = log('execute')(now)
def now():
	print('2017-8-23')
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
#于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
print(now.__name__)
now()
