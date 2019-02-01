# coding = utf-8
from functools import reduce
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#将str转化为int
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
	return reduce(fn,map(char2sum,s))
#用lamdba函数简化
def char2num2(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2int2(s):
	return reduce(lambda x,y:x*10+y,map(char2num2,s))
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def name(n):
	return n.title()
print(name("jdfai.flgFJG"))