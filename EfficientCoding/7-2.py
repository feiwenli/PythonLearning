import sys

class Player(object):
	def __init__(self,uid,name,status=0,level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level

class Player2(object):
	__slots__ = ['uid','name','stat','level']	#阻止动态属性绑定
	def __init__(self,uid,name,status=0,level=1):
		self.uid = uid
		self.name = name
		self.stat = status
		self.level = level

p1 = Player('0001','jim')
p2 = Player2('0002','jim')
print( set(dir(p1)) - set(dir(p2)) )
#动态绑定内存
print('p1.__dict__ :',p1.__dict__)
p1.x = 123
print('p1.__dict__ :',p1.__dict__)
p1.__dict__['y'] = 99
del p1.__dict__['x']
print('p1.__dict__ :',p1.__dict__)
#动态绑定的属性是很占用内存的
print(sys.getsizeof(p1.__dict__))