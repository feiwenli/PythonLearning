import logging
from time import localtime,time, strftime, sleep

class CallingInfo(object):
	def __init__(self, name):
		log = logging.getLogger(name)	#获取logger对象，如果不指定name则返回root对象
		log.setLevel(logging.INFO)	
		fh = logging.FileHandler(name + '.log')
		log.addHandler(fh)	
		log.info('Start'.center(50, '-'))
		self.log = log
		self.formatter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'

	def info(self,func):
		def wrapper(*args, **kargs):
			wrapper.ncalls += 1
			lt = localtime()
			start = time()
			res = func(*args, **kargs)
			used = time() - start
			info = {}
			info['func'] = func.__name__
			info['time'] = strftime('%x %X', lt)
			info['used'] = used
			info['ncalls'] = wrapper.ncalls
			msg = self.formatter % info
			self.log.info(msg)
			return res
		wrapper.ncalls = 0
		return wrapper

cinfo1 = CallingInfo('mylog1')
cinfo2 = CallingInfo('mylog2')

@cinfo1.info
def f():
	print ('in f')

@cinfo1.info
def g():
	print ('in g')

@cinfo2.info
def h():
	print ('in h')

from random import choice

for _ in range(50):
	choice([f,g,h])()
	sleep(choice([0.5, 1, 1.5]))