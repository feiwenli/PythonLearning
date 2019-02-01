#-*- coding: utf-8 -*-
s1 = int (input("please enter your grade,last year:"))
s2 = int (input("please enter your grade:"))
r = (s2 - s1) / s1 *100
print('%.1d %%' %r)
print(len('中文'))
print(len('中文'.encode('utf-8')))