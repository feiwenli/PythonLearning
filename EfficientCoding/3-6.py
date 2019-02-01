#如何在一个for语句中迭代多个可迭代对象
from random import randint
from itertools import chain
#并行
chinese = [randint(50,100) for _ in range(20)]
math = [randint(50,100) for _ in range(20)]
english = [randint(50,100) for _ in range(20)]

total = []

for c,m,e in zip(chinese,math,english):
	total.append(c + m +e)

print(total)

#串行
e1 = [randint(40,100) for _ in range(18)]
e2 = [randint(40,100) for _ in range(14)]
e3 = [randint(40,100) for _ in range(25)]
e4 = [randint(40,100) for _ in range(15)]

count = 0

for x in chain(e1,e2,e3,e4):
	if x >90:
		count += 1

print(count)