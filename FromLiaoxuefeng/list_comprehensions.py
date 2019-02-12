# -*- coding: utf-8 -*-
import os

# 列出当前目录下所有的文件名
print([d for d in os.listdir('.')])
# 生成[1*1,2*2,3*3,...,10*10]
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
# 使用两层循环，可以生成全排列
print([m + n for m in 'ABC' for n in 'sdfg'])
# 将list中所有的字符串变成小写
LN = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in LN])
# practice
L = ['Hello', 'World', 18, 'Apple', None]
print([sm.lower() for sm in L if isinstance(sm, str)])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])
