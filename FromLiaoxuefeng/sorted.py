# -*- coding=utf-8 -*-

lis = [53,661,664,-66,-634]
print(sorted(lis))
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted(lis, key = abs))

name = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(name, key=str.lower))
# 反向排序
print(sorted(name, key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序
L2 = sorted(L, key=lambda x : x[0])
print(L2)

# 按分数排序
L3 = sorted(L, key=lambda x : x[1])
print(L3)
