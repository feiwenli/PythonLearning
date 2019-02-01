# -*- coding: utf-8 -*-
L = list(range(100))
print(L[-2:0])
print(L[-2:0:-1])
print(L[-2:])
#前十个数，每两个取一
print(L[:10:2])
#取前19个数
print(L[:19])
#所有的数，每5个取一个
print(L[::5])
#原样复制一个list
print(L[:])
