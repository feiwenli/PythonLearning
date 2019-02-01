from inspect import signature
def typeassert(*ty_args, **ty_kargs):
	def decorator(func):	#func ：装饰器传入的参数
		sig = signature(func)
		btypes = sig.bind_partial(*ty_args, **ty_kargs).arguments	#装饰器规定参数的一个字典
		def wrapper(*args, **kargs):
			d = sig.bind(*args, **kargs).arguments	#函数 f 的参数的字典
			for name, obj in d.items():		#name是函数 f 中参数的名字，如a、b，obj是参数的类型
				if name in btypes:
					if not isinstance(obj, btypes[name]):	#如果 f 的参数类型obj不是装饰器中规定的btypes[name]类型的
						raise TypeError('"%s" must be "%s"' %(name, btypes[name]))
			return func(*args, **kargs)
		return wrapper
	return decorator


@typeassert(int, str, list)
def f(a,b,c = 1):
	print(a,b,c)

f(1, 'abc', [1,2,3])
#f(1, 2, [1,2,3])	#TypeError: "b" must be "<class 'str'>"

#获取函数签名
'''
from inspect import signature
def f(a,b,c = 1):
    print(a,b,c)
sig = signature(f)    
a = sig.parameters['a']
print(a.name,a.kind)    #a.kind 参数属于哪种类型，位置参数，或者关键字参数
c = sig.parameters['c']
print(c.default)    #1    默认参数的值
bargs = sig.bind(str,int,int)    #建立映射，做类型检查
bargs.arguments['a']    #builtins.str    一个字典，得到a是一个str类型的
bargs.arguments['a']    #builtins.int    b是一个int类型的
'''