#!/user/bin/env python3
# -*- coding: utf-8 -*-
print('300+200=', 300 + 200)
# print('please enter your name:')
# name = input()
# print("hello,",name)
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
print('\\\\n\\\\')
# r''表示''里面的字符不转义
print(r'\\\\n\\\\')
print(r'''line1
line2
line3
line4''')
print('''line1
line2
line3
line4''')
# a test
n = 123
print(n)
f = 456.789
print(f)
s1 = 'Hello,world'
print(s1)
s2 = 'Hello,\'Adam\''
print(s2)
s3 = r'Hello,"Bart"'
print(s3)
s4 = r'''Hello,
Lisa!'''
print(s4)

print(ord('A'))
print(chr(25888))
print('\u4e2d\u6587')

print(len('中文'.encode('utf-8')))
