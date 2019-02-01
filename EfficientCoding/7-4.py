from math import pi

class Circle(object):
	def __init__(self,radius):
		self.radius = radius

	def getRadius(self):
		return round(self.radius, 2)	#保留小数

	def setRadius(self,value):
		if not isinstance (value,(int,float)):
			raise ValueError('Wrong type.')
		self.radius = float(value)

	def getArea(self):
		return self.radius **2 * pi

	#可以通过属性值直接访问
	R = property(getRadius, setRadius)

c = Circle(3.2)
print(c.R)
c.R = 90
print(c.R)
print(c.getArea())