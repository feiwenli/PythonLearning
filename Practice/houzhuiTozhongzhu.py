# coding=utf-8
# 后缀表达式转中缀表达式
from Stack import Stack

l = '6 5 2 3 + 8 * + 3 + *'
l = l.split()
s = Stack()
result = ''

t = 0
for i in l:
	if i.isdigit():
		s.push(i)
	else:
		t = t + 1
		if t == 1:
			tem1 = s.pop()
			tem2 = s.pop()
			print tem2,tem1
		else:
			tem2 = s.pop()
		if i == '+' or i == '-':
			if t == 1:
				result = tem2+i+tem1
			else:
				result = tem2+i+result
			print result
		elif i == '*' or i =='/':
			result = tem2+i+'('+result+')'
			print result

result = eval(result)
print result
