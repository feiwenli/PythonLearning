import re
from collections import Counter
from random import randint
#统计词频
txt = open("E:\core\\test.txt").read()
c = Counter(re.split('\W+',txt))
print(c.most_common(10))
############
data = [randint(0,20) for _ in range(20)]
c2 = Counter(data)
print(c2.most_common(3))
print(c2[4])
#统计序列中元素出现的频率
c3 = dict.fromkeys(data,0)	#以data为key创造一个dict
for x in data:
	c3[x] += 1
print(sorted(c3.items(),key = lambda x : x[1],reverse = True))
