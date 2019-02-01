# coding=utf-8
# 后缀表达式求值
# 6 5 2 3 + 8 * + 3 + *

from Stack import Stack

l = '6 5 2 3 + 8 * + 3 + *'
l = l.split()
s = Stack()

for i in l:
	if i.isdigit():
		i = int(i)
		s.push(i)
	else:
		tem1 = s.pop()
		tem2 = s.pop()
		print tem2,tem1
		if i == '+':
			s.push(tem2 + tem1)
		elif i == '-':
			s.push(tem2 - tem1)
		elif i == '*':
			s.push(tem2 * tem1)
		elif i == '/':
			s.push(tem2 / tem1)

result = s.pop()
print result

