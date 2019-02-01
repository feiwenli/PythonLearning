import re

def mySplit(s,ds):
	res = [s]

	for d in ds:
		t = []
		list(map( lambda x : t.extend(x.split(d)) , res))
		res = t

	return [x for x in res if x]	#去掉空的字符串

s = 'abc,def;ghi|jk|lmn\opq;rs\ttuvw,xyz'
print(mySplit(s,',;\|\t'))

print("-"*80)

res = s.split(';')
print(res)
w =[]
w = map( lambda x : x.split(',') , res)
print(list(w))
t = []
list(map( lambda x : t.extend(x.split(',')) , res))
print(t)
print('-'*50)
print(re.split(r'[,;\\|\t]',s))