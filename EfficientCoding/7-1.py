
class IntTuple(tuple):
	def __new__(cls,iterable):	#IntTupule会传入到cls中，其它参数与__init__方法一致
		g = (x for x in iterable if isinstance(x,int) and x > 0)
		return super().__new__(cls, g)
		
	def __int__(self,iterable):
		#before
		super().__int__(iterable)
		#after

t = IntTuple([1,-1,'abc',6,['x','y'],3])
print(t)