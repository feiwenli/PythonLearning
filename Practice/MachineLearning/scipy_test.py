# encoding=utf-8
# 
import numpy as np

class main():
	# 积分
	from scipy.integrate import quad,dblquad,nquad	# 一维，二维，n维积分
	print quad(lambda x: np.exp(-x), 0, np.inf)	# np.inf 无穷大
	print dblquad(lambda t,x:np.exp(-x*t)/t**3,0, np.inf, lambda x:1, lambda x:np.inf) 
	def f(x,y):
		return x*y
	def bound_y():
		return [0,0.5]
	def bound_x(y):
		return [0,1-2*y]
	print nquad(f,[bound_x,bound_y])

	# 最小值
	from scipy.optimize import minimize
	def rosen(x):
		return sum(100*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
	x0 = np.array([1.3,0.7,0.8,1.9,1.2])
	res = minimize(rosen,x0,method='nelder-mead',options={'xtol':1e-8,'disp':True})
	print 'Rose mini:',res.x


if __name__=='__main__':
	main()