#反向迭代
class FloatRange:
	def __init__(self,start,end,step = 0.2):
		self.start = start
		self.end = end
		self.step = step

	def __iter__(self):
		t = self.start
		while t <= s.end:
			yield t
			t += self.step

	def __reversed__(self):
		t = self.end
		while t >= self.start:
			yield t
			t -= self.step

for x in reversed(FloatRange(1.0,5.0,0.1)):
	print(x)