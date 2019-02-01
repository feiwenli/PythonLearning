# 如何让字典保持有序
from collections import OrderedDict
from random import randint
from time import time,sleep

players = list("ABCDEFGH")
start = time()
d = OrderedDict()
print('start')
for i in range(8):
	sleep(2)
	p = players.pop(randint(0,7-i))
	end = time()
	print(p,i+1,end-start,)
	d[p] = (i+1,end-start)

print('-'*20)
for k in d:
	print(k,d[k])

