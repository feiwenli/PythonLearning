# -*- coding = utf-8 -*-

import re

def main():
	s =  '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
	ss = ''.join(s.split())
	while True:
		if '(' in ss:
			p = re.search(r'\([^()]+\)',ss)
			if p is not None:
				r = cal(p.group())
				ss = re.sub(r'\([^()]+\)',str(r),ss,1)
		else:
			r = cal(ss)
			print(r)
			break
def add_sub(a):	
	if '--' in a:
		a = a.replace('--','+')
	p = re.findall(r'-?\d+\.?\d*',a)
	list = []
	for i in p:
		list.append(float(i))
	t = sum(list)
	print('add_sub:',t)
	return t
	

def div(d):
	p = re.search(r'-?\d+\.?\d*(\/-?\d+\.?\d*)',d)
	if p is not None:
		pp = re.findall(r'-?\d+\.?\d*',p.group())
		list = []
		for i in pp:
			list.append(float(i))
		division = list[0]/list[1]
		r = re.sub(r'-?\d+\.?\d*(\/-?\d+\.?\d*)',str(division),d,1)
		print('div:',division)
		return r
'''
def mul(m):
	p = re.search(r'-?\d+\.?\d*(\*-?\d+\.?\d*)',m)
	if p is not None:
		pp = re.findall(r'-?\d+\.?\d*',p.group())
		list = []
		for i in pp:
			list.append(float(i))
		multip = list[0]*list[1]
		r = re.sub(r'-?\d+\.?\d*\*-?\d+\.?\d*',str(multip),m,1)	#error
		print('mul:',multip)
		return r
'''
def mul(m):
    p=re.search(r"\d+\.?\d*(\*-?\d+\.?\d*)",m)
    if p is not None:
        p=p.group()
        pp=re.findall(r"-?\d+\.?\d*",p)  #搜索string，以列表形式返回全部能匹配的子串
        list=[]
        for i in pp:
            list.append(float(i))   #将字符串列表转化为数字列表
        multip=list[0]*list[1]
        r=re.sub(r"\d+\.?\d*(\*-?\d+\.?\d*)",str(multip),m,1)
        print('mul:',multip)
        return r

def cal(c):
	while True:
		if '*' in c:
			cc = c.split('*')
			if '/' in cc[0]:
				c = div(c)
			else:
				c = mul(c)
		elif '/' in c:
			c = div(c)
		elif '+' or '-' in c:
			c = add_sub(c)
			return c
		else:
			return c

main()