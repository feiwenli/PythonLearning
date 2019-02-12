# -*- coding: utf-8 -*-
from collections import Iterable

print('\'abc\'', isinstance('abc', Iterable))
print('[1,2,3]', isinstance([1, 2, 3], Iterable))
print('123', isinstance(123, Iterable))
# 下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print('\n')
L = [2, 3, 4, 'g', 'h']
for i, value in enumerate(L):
    print(i, value)
# dict 迭代value
d = {'Micheal': 98, 'Bob': 58, 'Tracy': 99}
print('the grade of Micheal:', d['Micheal'])
for value in d.values():
    print(value)
# dict 同时迭代key和value
for k, v in d.items():
    print(k, v)
# dict 默认迭代key
for k in d:
    print(k)
