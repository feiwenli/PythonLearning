from multiprocessing import Process
from multiprocessing import Pool
import os,time,random
'''
#子进程要执行的代码
def run__proc(name):
	print('Run child progress %s (%s)...'%(name,os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.'%os.getpid())
	p = Process(target = run__proc,args=('test',))
	print('Child progress will start.')
	p.start()	#启动子进程
	p.join()	#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	print('Child progress end.')
'''
#pool
def long_time_task(name):
	print('Run task %s (%s)...' %(name,os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' %(name,(end-start)))

if __name__ == '__main__':
	print('Parent process %s.'%os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task,args = (i,))
	print('Waiting for all subprocresses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
