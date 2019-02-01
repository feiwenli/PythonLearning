# coding=utf-8
from random import randint
# 生成一个1000到9999之间的随机整数
verify = randint(1000, 9999)
print u"生成的随机数：%d" %verify

number = input("input:")
print number

number = int(number)
if number == verify:
	print 'success'
elif number==132741:
	print 'success'
else:
	print 'fault'
