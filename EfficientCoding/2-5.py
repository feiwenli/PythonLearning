#如何快速找到多个字典的公共键
from random import randint,sample
from functools import reduce
sample('jfjagprwe',randint(3,6))
s1 = {x: randint(1,4) for x in sample('hfjagprwe',randint(3,6))}
s2 = {x: randint(1,4) for x in sample('hfjagprwe',randint(3,6))}
s3 = {x: randint(1,4) for x in sample('hfjagprwe',randint(3,6))}
print(s1)
print(s2)
print(s3)
#法1:罗嗦，效率不高
res = []
for k in s1:
	if k in s2 and k in s3:
		res.append(k)
print(res)
#法2
print(reduce(lambda a,b : a&b ,map(dict.keys,[s1,s2,s3])))