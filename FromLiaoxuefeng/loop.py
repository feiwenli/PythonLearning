# -*- coding: utf-8 -*-
L = ['bart', 'lisa', 'adam']
for x in L:
    print('Hello,' + x + '!')
num = len(L)
while num >= 0:
    print('Hello,' + L[num - 1] + '!')
    num = num - 1
