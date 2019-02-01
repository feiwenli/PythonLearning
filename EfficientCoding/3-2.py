#如何实现可迭代对象和迭代器对象
#从网络上抓取各个城市气温信息并依次显示
from collections import Iterable,Iterator
import requests

class WeatherIterator(Iterator):
	def __init__(self,cities):
		self.cities = cities
		self.index = 0

	def getWeather(self,city):
		r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city='+city)
		data = r.json()['data']['forecast'][0]
		return '%s:%s,%s' %(city,data["low"],data["high"])

	def __next__(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

class WeatherIterable(Iterable):
	def __init__(self,cities):
		self.cities = cities

	def __iter__(self):
		return WeatherIterator(self.cities)

for x in WeatherIterable([u'杭州',u'广州',u'上海',u'北京',u'长春',u'乌鲁木齐']):
	print (x)